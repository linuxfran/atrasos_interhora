<<<<<<< HEAD
from flask import Flask, render_template, redirect, url_for
=======
from flask import Flask
>>>>>>> 46452180217b1e9d5761da862ba3bf9ff4ffff11


def crear_app():
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
    )

<<<<<<< HEAD
    @app.route("/")
    def inicio():
        return render_template(
            "index.html",
            total_atrasos=0,
            total_minutos=0,
            estudiantes_recurrentes=0,
            atrasos=[]
        )

    @app.route("/registrar", methods=["POST"])
    def registrar():
        return redirect(url_for("inicio"))
=======
    from app.routes import rutas
    app.register_blueprint(rutas)
>>>>>>> 46452180217b1e9d5761da862ba3bf9ff4ffff11

    return app