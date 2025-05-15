from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import login_manager, LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "dujsdujsddfsdbfjksfjhksdhjkfjh"
    app.config['SQLALCHEMY_DATABASE_URI']  = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    craete_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.welcome'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def craete_database(app):
    if not path.exists('instance/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Created Database!')