from datetime import date
from functools import wraps

from flask import Blueprint, flash, jsonify, redirect, render_template, request, session, url_for

from app.models import (
    autenticar_usuario,
    crear_atraso,
    crear_usuario,
    hay_usuarios,
    listar_atrasos,
    obtener_estadisticas,
)

rutas = Blueprint("rutas", __name__)


@rutas.get("/healthz")
def healthcheck():
    return jsonify(status="ok"), 200


def requiere_sesion(vista):
    @wraps(vista)
    def protegida(*args, **kwargs):
        if "usuario_id" not in session:
            return redirect(url_for("rutas.login"))
        return vista(*args, **kwargs)

    return protegida


@rutas.route("/login", methods=["GET", "POST"])
def login():
    if not hay_usuarios():
        return redirect(url_for("rutas.configurar"))
    if "usuario_id" in session:
        return redirect(url_for("rutas.inicio"))

    if request.method == "POST":
        nombre_usuario = request.form.get("usuario", "").strip()
        password = request.form.get("password", "")
        usuario = autenticar_usuario(nombre_usuario, password)
        if usuario:
            session.clear()
            session["usuario_id"] = usuario["id"]
            session["nombre_usuario"] = usuario["nombre_usuario"]
            return redirect(url_for("rutas.inicio"))
        flash("Usuario o contraseña incorrectos.", "error")

    return render_template("login.html")


@rutas.route("/configurar", methods=["GET", "POST"])
def configurar():
    if hay_usuarios():
        return redirect(url_for("rutas.login"))

    if request.method == "POST":
        nombre_usuario = request.form.get("usuario", "").strip()
        password = request.form.get("password", "")
        confirmacion = request.form.get("confirmacion", "")

        if len(nombre_usuario) < 3 or len(nombre_usuario) > 40:
            flash("El usuario debe tener entre 3 y 40 caracteres.", "error")
        elif len(password) < 10:
            flash("La contraseña debe tener al menos 10 caracteres.", "error")
        elif password != confirmacion:
            flash("Las contraseñas no coinciden.", "error")
        elif crear_usuario(nombre_usuario, password):
            flash("Cuenta administradora creada. Ya puedes iniciar sesión.", "success")
            return redirect(url_for("rutas.login"))
        else:
            flash("La cuenta inicial ya fue creada. Inicia sesión.", "error")
            return redirect(url_for("rutas.login"))

    return render_template("setup.html")


@rutas.route("/salir", methods=["POST"])
@requiere_sesion
def salir():
    session.clear()
    return redirect(url_for("rutas.login"))


@rutas.route("/")
@requiere_sesion
def inicio():
    return render_template(
        "index.html",
        atrasos=listar_atrasos(),
        **obtener_estadisticas(),
    )


@rutas.route("/registrar", methods=["POST"])
@requiere_sesion
def registrar():
    nombre = request.form.get("nombre", "").strip()
    curso = request.form.get("curso", "").strip()
    fecha = request.form.get("fecha", "").strip()
    minutos = request.form.get("minutos", type=int)

    try:
        date.fromisoformat(fecha)
        fecha_valida = True
    except ValueError:
        fecha_valida = False

    if not nombre or not curso or not fecha_valida or minutos is None or minutos < 0:
        flash("Completa todos los campos con datos válidos.", "error")
    else:
        crear_atraso(nombre, curso, fecha, minutos)
        flash("Atraso registrado correctamente.", "success")

    return redirect(url_for("rutas.inicio"))
