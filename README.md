# Smart Attendance

Aplicación Flask para registrar y consultar atrasos de estudiantes. Los datos se guardan en SQLite.

## Ejecutar localmente

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

La aplicación queda disponible en `http://127.0.0.1:5000`. Por defecto, SQLite crea `instance/atrasos.sqlite3`.

## Desplegar en Railway

Railway detecta `requirements.txt` y usa Railpack. `railway.json` define Gunicorn como servidor, enlazado al puerto `PORT` que Railway asigna.

Para conservar los registros entre despliegues, añade un Railway Volume montado en `/data` y define la variable `DATABASE_PATH=/data/atrasos.sqlite3`. También define `SECRET_KEY` con un valor aleatorio propio desde las variables del servicio.

La primera vez que abras la aplicación, crea la cuenta administradora en `/configurar`. Esa pantalla se bloquea automáticamente después de crear la cuenta. Luego inicia sesión en `/login`.

## Rutas

- `GET /login`: inicio de sesión.
- `GET /configurar`: creación de la primera cuenta administradora; solo está disponible mientras no exista una cuenta.
- `GET /`: panel protegido, estadísticas y últimos 20 atrasos.
- `POST /registrar`: valida y guarda un atraso; requiere sesión.
- `POST /salir`: cierra la sesión.

Un estudiante se considera recurrente al acumular tres o más registros en el mismo curso.
