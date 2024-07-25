from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from config import Config

db = SQLAlchemy()
csrf = CSRFProtect()
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()

    return app
