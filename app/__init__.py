import os
from dotenv import load_dotenv
from flask import Flask
from routes.auth_routes import auth
from routes.blog_routes import blogs

load_dotenv()

def create_app():
    app = Flask(__name__, template_folder=os.getenv('TEMPLATE_FOLDER_PATH'), static_folder=os.getenv('STATIC_FOLDER_PATH'))

    app.register_blueprint(auth)
    app.register_blueprint(blogs)

    return app