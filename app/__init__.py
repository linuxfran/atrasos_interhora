import os

from flask import Flask

from app.config import Config
from app.database import close_db, init_db


def crear_app():
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
    )
    app.config.from_object(Config)
    if app.config["DATABASE_PATH"] is None:
        app.config["DATABASE_PATH"] = os.path.join(app.instance_path, "atrasos.sqlite3")
    os.makedirs(app.instance_path, exist_ok=True)

    from app.routes import rutas

    app.register_blueprint(rutas)
    app.teardown_appcontext(close_db)

    with app.app_context():
        init_db()

    return app
