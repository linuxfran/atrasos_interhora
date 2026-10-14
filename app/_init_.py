
from flask import Flask


def crear_app():
    app = Flask(
        __name__,
        template_folder="../templates/pages",
        static_folder="../static"
    )

    from app.routes import rutas
    app.register_blueprint(rutas)

    return app
