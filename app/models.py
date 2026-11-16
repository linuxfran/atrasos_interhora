from werkzeug.security import check_password_hash, generate_password_hash

from app.database import get_db


def hay_usuarios():
    return get_db().execute("SELECT 1 FROM usuarios LIMIT 1").fetchone() is not None


def buscar_usuario(nombre_usuario):
    fila = get_db().execute(
        "SELECT id, nombre_usuario, password_hash FROM usuarios WHERE nombre_usuario = ?",
        (nombre_usuario,),
    ).fetchone()
    return dict(fila) if fila else None


def autenticar_usuario(nombre_usuario, password):
    usuario = buscar_usuario(nombre_usuario)
    if usuario and check_password_hash(usuario["password_hash"], password):
        return usuario
    return None


def crear_usuario(nombre_usuario, password):
    db = get_db()
    try:
        db.execute("BEGIN IMMEDIATE")
        if db.execute("SELECT 1 FROM usuarios LIMIT 1").fetchone():
            db.rollback()
            return False
        db.execute(
            "INSERT INTO usuarios (nombre_usuario, password_hash) VALUES (?, ?)",
            (nombre_usuario, generate_password_hash(password)),
        )
        db.commit()
        return True
    except Exception:
        db.rollback()
        raise


def listar_atrasos(limite=20):
    filas = get_db().execute(
        "SELECT nombre, curso, fecha, minutos FROM atrasos "
        "ORDER BY fecha DESC, id DESC LIMIT ?",
        (limite,),
    ).fetchall()
    return [dict(fila) for fila in filas]


def obtener_estadisticas():
    fila = get_db().execute(
        """
        SELECT COUNT(*) AS total_atrasos,
               COALESCE(SUM(minutos), 0) AS total_minutos
        FROM atrasos
        """
    ).fetchone()
    recurrentes = get_db().execute(
        """
        SELECT COUNT(*) FROM (
            SELECT nombre, curso
            FROM atrasos
            GROUP BY lower(nombre), lower(curso)
            HAVING COUNT(*) >= 3
        )
        """
    ).fetchone()[0]
    return {
        "total_atrasos": fila["total_atrasos"],
        "total_minutos": fila["total_minutos"],
        "estudiantes_recurrentes": recurrentes,
    }


def crear_atraso(nombre, curso, fecha, minutos):
    db = get_db()
    db.execute(
        "INSERT INTO atrasos (nombre, curso, fecha, minutos) VALUES (?, ?, ?, ?)",
        (nombre, curso, fecha, minutos),
    )
    db.commit()
