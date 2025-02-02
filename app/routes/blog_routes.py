from flask import Blueprint, render_template
from app.routes.auth_routes import login_required

blogs = Blueprint('blogs', __name__)

# Route to show all blogs
@login_required
@blogs.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('home.html')

# Route to create new blog  
@login_required
@blogs.route('/create_blog', methods=['POST'])
def create_blog():
    return render_template('create_blog.html')

# Route to edit existing blog
@login_required
@blogs.route('/edit_blog', methods=['PUT'])
def edit_blog():
    return render_template('edit_blog.html')

# Route to delete existing blog
@login_required
@blogs.route('/delete_blog', methods=['POST'])
def delete_blog():
    return render_template('delete_blog.html')
