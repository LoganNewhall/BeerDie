from flask_app.models.user import User
from flask_app import app
from flask import render_template, session, redirect
from flask_app.models.game import Game

@app.route('/<friend_id>/profile')
def friend_profile(friend_id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'user_id' : friend_id
    }
    return render_template('/friend_profile.html', friend = User.get_user(data), game_details = Game.game_details(data))