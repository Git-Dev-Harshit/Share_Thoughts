from flask import Blueprint, render_template, redirect, request, flash, url_for, session, make_response, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user_models import User, db
from functools import wraps
from datetime import timedelta

auth = Blueprint('auth', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'uid' not in session:
            flash("You need to log in to access this page.", "danger")
            return redirect(url_for('auth.login'))
        
        response = make_response(f(*args, **kwargs))
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
    return decorated_function

@auth.route('/login', methods=['POST', 'GET'])
def login():
    if 'uid' in session:
        return redirect(url_for('blogs.home'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        
        if not user or not check_password_hash(user.password, password):
            flash("Invalid email or password", "danger")
            return redirect(url_for('auth.login'))
        
        session['uid'] = user.id
        session['email'] = user.email
        session['name'] = user.name
        session.permanent = True
        current_app.permanent_session_lifetime = timedelta(days=1)

        return redirect(url_for('blogs.home'))

    return render_template('login.html')

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
        session.permanent = True
        current_app.permanent_session_lifetime = timedelta(days=7)
        return redirect(url_for('blogs.home'))
    
    return render_template('signup.html')

@auth.route('/logout')
@login_required
def logout():
    session.clear()
    response = make_response(redirect(url_for('auth.login')))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

@auth.route('/edit_user', methods=['POST', 'GET'])
@login_required
def edit_user():
    return render_template('edit_user.html')
