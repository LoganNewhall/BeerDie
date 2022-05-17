from flask_app.config.mysqlconnection import connectToMySQL

class Game_has_User:
    db = 'beer_die'
    def __init__(self, data):
        self.game_id = data['game_id']
        self.team1_player1_id = data['team1_player1_id']
        self.team1_player2_id = data['team1_player2_id']
        self.team2_player1_id = data['team2_player1_id']
        self.team2_player2_id = data['team2_player2_id']
        
    
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO games_has_users (game_id, team1_player1_id, team1_player2_id, team2_player1_id, team2_player2_id) VALUES (%(game_id)s, %(user1_id)s, %(user2_id)s, %(user3_id)s, %(user4_id)s);'
        players = connectToMySQL(cls.db).query_db(query, data)
        return players