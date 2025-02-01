from flask import Blueprint, render_template, redirect

auth = Blueprint(__name__)

# Route to login
@auth.route('/login', method=['POST'])
def login():
    return render_template('login.html')

# Route to signup
@auth.route('/signup', method=['POST'])
def signup():
    return render_template('signup.html')

# Route to logout
@auth.route('/logout', method=['POST'])
def logout():
    return redirect(login)

# Route to edit user details
@auth.route('/edit_user', method=['POST'])
def edit_user():
    return render_template('edit_user.html')

