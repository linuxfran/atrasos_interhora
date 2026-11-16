import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "local-development-key-change-in-production")
    DATABASE_PATH = os.environ.get("DATABASE_PATH")
