from flask_app import app
from flask import render_template, redirect, request, session
from flask import jsonify
from flask_app.models.game import Game
from flask_app.models.user import User
from flask_app.models.game_has_user import Game_has_User
from flask_app.models.game_event import Game_Event

@app.route('/event', methods=['POST'])
def get_post_json():    
    data = request.get_json()
    Game_Event.events(data)
    return redirect('/game')
    