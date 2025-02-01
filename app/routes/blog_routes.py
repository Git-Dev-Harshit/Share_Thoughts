from flask import Blueprint, render_template

blogs = Blueprint('blogs', __name__)

# Route to show all blogs
@blogs.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('home.html')

# Route to create new blog  
@blogs.route('/create_blog', methods=['POST'])
def create_blog():
    return render_template('create_blog.html')

# Route to edit existing blog
@blogs.route('/edit_blog', methods=['PUT'])
def edit_blog():
    return render_template('edit_blog.html')

# Route to delete existing blog
@blogs.route('/delete_blog', methods=['POST'])
def delete_blog():
    return render_template('delete_blog.html')
