
from flask_app import app
from flask import render_template, redirect, request, session
from flask import jsonify
from flask_app.models.game import Game
from flask_app.models.user import User
from flask_app.models.game_has_user import Game_has_User

@app.route('/startgame')
def start_game() :
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'user_id' : session['user_id']
        
    }
    return render_template('start_game.html', user = User.get_user(data))

@app.route('/creategame', methods=['POST'])
def create_game():
    data = {
        'username_1' : request.form['team1_player2'],
        'username_2' : request.form['team2_player1'],
        'username_3' : request.form['team2_player2']
    }
    if not Game.validate_players(data):
        return redirect('/startgame')
    game_data = {
        'team_1_score' : 0,
        'team_2_score' : 0
    }
    session['game_id'] = Game.save(game_data)
    player_data = {
        'game_id' : session['game_id'],
        'user1_id' : session['user_id'],
        'user2_id' : User.get_by_username({'username' : request.form['team1_player2']})['id'],
        'user3_id' : User.get_by_username({'username' : request.form['team2_player1']})['id'],
        'user4_id' : User.get_by_username({'username' : request.form['team2_player2']})['id']
    }
    Game_has_User.save(player_data)
    return redirect('/game')

@app.route('/game')
def live_game():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('live_game.html')

@app.route('/end', methods=['POST'])
def get_post_json():    
    data = request.get_json()
    data['game_id'] = session['game_id']
    Game.final_score(data)
    session['game_id'] = None
    return jsonify(status="success")
