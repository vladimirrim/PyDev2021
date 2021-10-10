from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config["SQLALCHEMY_BINDS"] = {'users': 'sqlite:///users_db.sqlite',
                                      'library': 'sqlite:///library_db.sqlite',
                                      'books': 'sqlite:///books_db.sqlite',
                                      'reviews': 'sqlite:///reviews_db.sqlite'}
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app


app = create_app()
login_manager = LoginManager()
login_manager.init_app(app)
