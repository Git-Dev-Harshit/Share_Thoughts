from flask import Blueprint, render_template
from app.routes.auth_routes import login_required

blogs = Blueprint('blogs', __name__)

@blogs.route('/home', methods=['GET'])
@login_required
def home():
    return render_template('home.html')

@blogs.route('/create_blog', methods=['POST', 'GET'])
@login_required
def create_blog():
    return render_template('create_blog.html')

@blogs.route('/edit_blog', methods=['PUT', 'GET'])
@login_required
def edit_blog():
    return render_template('edit_blog.html')

@blogs.route('/delete_blog', methods=['POST', 'GET'])
@login_required
def delete_blog():
    return render_template('delete_blog.html')