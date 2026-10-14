
from flask import Blueprint, render_template

rutas = Blueprint("rutas", __name__)


@rutas.route("/")
def inicio():
    return render_template("index.html")
