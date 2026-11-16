from flask import Flask, render_template, redirect, url_for


def crear_app():
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
    )

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

    return app