from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.friend_request import Friend_Request
from flask_app.models.friend import Friend
from flask_app.models.game import Game
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('login_register.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    data = {
        'f_name' : request.form['f_name'],
        'l_name' : request.form['l_name'],
        'age' : request.form['age'],
        'email' : request.form['email'],
        'username' : request.form['username'],
        'password' : bcrypt.generate_password_hash(request.form['password'])
    }
    session['user_id'] = User.save(data)
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    data = {
        'username' : request.form['username'],
        'password' : request.form['password']
    }
    user_in_db = User.get_by_username(data)
    if not user_in_db:
        flash('Invalid Username', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db['password'], data['password']):
        flash('Invalid Password', 'login')
        return redirect('/')
    session['user_id'] = user_in_db['id']
    return redirect('/dashboard')

@app.route('/update', methods=['POST'])
def update():
    data = {
        'f_name' : request.form['f_name'],
        'l_name' : request.form['l_name'],
        'email' : request.form['email'],
        'username' : request.form['username'],
        'rules' : request.form['rules'],
        'user_id' : session['user_id']
    }
    User.update_user(data)
    return redirect('/profile')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'user_id' : session['user_id']
    }
    return render_template('dashboard.html', user = User.get_user(data), requests = Friend_Request.get_requests(data), friends = Friend.get_friends(data))

@app.route('/rules')
def rules():
    return render_template('rules.html')

@app.route('/edit')
def edit():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'user_id' : session['user_id']
    }
    return render_template('edit.html', user = User.get_user(data))

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'user_id' : session['user_id']
    }
    
    return render_template('profile.html', user = User.get_user(data), game_details = Game.game_details(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')