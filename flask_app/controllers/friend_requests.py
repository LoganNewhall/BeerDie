from multiprocessing import reduction
from flask_app import app
from flask import redirect, request, session, flash
from flask_app.models.friend_request import Friend_Request
from flask_app.models.user import User
from flask_app.models.friend import Friend

@app.route('/addfriend', methods=['POST'])
def add_friend():
    data = {
        'username' : request.form['addfriend']
    }
    if not Friend_Request.validate_request(data):
        flash('No user found', 'addfriend')
        return redirect('/dashboard')
    
    friend_request_data = {
        'receiving_user_id' : User.get_by_username(data)['id'],
        'sending_user_id' : session['user_id']
    }
    friend_request = Friend_Request.send_request(friend_request_data)
    return redirect('/dashboard')

@app.route('/accept/<sending_user_id>')
def accept(sending_user_id):
    data ={
        'sending_user_id' : sending_user_id,
        'receiving_user_id' : session['user_id']
    }
    accept_data = {
        'friend_id' : sending_user_id,
        'user_id' : session['user_id']
    }
    friends = Friend.accept_friend(accept_data)
    Friend_Request.delete_request(data)
    return redirect('/dashboard')

@app.route('/delete/<sending_user_id>')
def delete(sending_user_id):
    data = {
        'sending_user_id' : sending_user_id,
        'receiving_user_id' : session['user_id']
    }
    delete_request = Friend_Request.delete_request(data)
    return redirect('/dashboard')
