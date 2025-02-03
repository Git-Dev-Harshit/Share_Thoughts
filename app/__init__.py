from flask import Flask
from flask_migrate import Migrate
from app.routes.auth_routes import auth
from app.routes.blog_routes import blogs
from app.config.db_config import Config
from app.models import db
import os
from dotenv import load_dotenv

load_dotenv()

migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth)
    app.register_blueprint(blogs)

    return app