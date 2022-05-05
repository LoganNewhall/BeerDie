from flask_app.config.mysqlconnection import connectToMySQL

class Game_has_User:
    db = 'beer_die'
    def __init__(self, data):
        self.game_id = data['game_id']
        self.user_id = data['user_id']
        