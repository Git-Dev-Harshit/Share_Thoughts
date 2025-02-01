from flask import Blueprint, render_template, redirect, request, flash, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user_models import User, db

auth = Blueprint('auth', __name__)

# Route to login
@auth.route('/login', methods=['POST', 'GET'])
def login():
    if 'uid' in session:
        return redirect(url_for('blogs.home'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        
        if not user:
            flash("Incorrect Email address", "danger")
            return redirect(url_for('auth.login'))
        
        if not check_password_hash(user.password, password):
            flash("Wrong password please try again", "danger")
            return redirect(url_for('auth.login'))
        
        session['uid'] = user.id
        session['email'] = user.email
        session['name'] = user.name

        return redirect(url_for('blogs.home'))


    return render_template('login.html')

# Route to signup
@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    if 'uid' in session:
        return redirect(url_for('blogs.home'))

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists!", "danger")
            return redirect(url_for('auth.signup'))
        
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        session['uid'] = new_user.id
        session['email'] = new_user.email
        session['name'] = new_user.name

        return redirect(url_for('blogs.home'))
    
    return render_template('signup.html')
    
# Route to logout
@auth.route('/logout', methods=['POST', 'GET'])
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

# Route to edit user details
@auth.route('/edit_user', methods=['POST', 'GET'])
def edit_user():
    return render_template('edit_user.html')

