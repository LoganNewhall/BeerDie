from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL


class Game:
    db = 'beer_die'
    def __init__(self, data):
        self.id = data['id']
        self.team_1_score = data['team_1_score']
        self.team_2_score = data['team_2_score']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO games (team_1_score, team_2_score) VALUES (%(team_1_score)s, %(team_2_score)s);'
        game = connectToMySQL(cls.db).query_db(query, data)
        return game
    
    @classmethod
    def final_score(cls, data):
        query = 'UPDATE games SET team_1_score = %(team_1_score)s, team_2_score = %(team_2_score)s WHERE id = %(game_id)s;'
        final_score = connectToMySQL(cls.db).query_db(query, data)
        return final_score

    @classmethod
    def get_game(cls, data):
        query = 'SELECT * FROM games WHERE id = %(id)s'
        game = connectToMySQL(cls.db).query_db(query, data)
        print(game)
        return game[0]

    @classmethod
    def game_details(cls, data):
        query = 'SELECT * FROM games LEFT JOIN games_has_users ON games.id = games_has_users.game_id LEFT JOIN users u1 ON games_has_users.team1_player1_id = u1.id LEFT JOIN users u2 ON games_has_users.team1_player2_id = u2.id LEFT JOIN users u3 ON games_has_users.team2_player1_id = u3.id LEFT JOIN users u4 ON games_has_users.team2_player2_id = u4.id WHERE %(user_id)s IN (games_has_users.team1_player1_id, games_has_users.team1_player2_id, games_has_users.team2_player1_id, games_has_users.team2_player2_id ) ORDER BY games.id DESC;'
        details = connectToMySQL(cls.db).query_db(query, data)
        return details

    @classmethod
    def current_game(cls, data):
        query = 'SELECT * FROM games LEFT JOIN games_has_users ON games.id = games_has_users.game_id LEFT JOIN users u1 ON games_has_users.team1_player1_id = u1.id LEFT JOIN users u2 ON games_has_users.team1_player2_id = u2.id LEFT JOIN users u3 ON games_has_users.team2_player1_id = u3.id LEFT JOIN users u4 ON games_has_users.team2_player2_id = u4.id WHERE %(user_id)s IN (games_has_users.team1_player1_id, games_has_users.team1_player2_id, games_has_users.team2_player1_id, games_has_users.team2_player2_id ) AND games_has_users.game_id = %(game_id)s;'
        details = connectToMySQL(cls.db).query_db(query, data)
        return details[0]

    @staticmethod
    def validate_players(users):
        is_valid = True
        query = 'SELECT * FROM users WHERE username = %(username_1)s;'
        player1 = connectToMySQL(Game.db).query_db(query, users)
        query = 'SELECT * FROM users WHERE username = %(username_2)s;'
        player2 = connectToMySQL(Game.db).query_db(query, users)
        query = 'SELECT * FROM users WHERE username = %(username_3)s;'
        player3 = connectToMySQL(Game.db).query_db(query, users)
        if len(player1) != 1:
            flash('Team one player 2 has invalid username', 'players')
            is_valid = False
        if len(player2) != 1:
            flash('Team two player 1 has invalid username', 'players')
            is_valid = False
        if len(player3) != 1:
            flash('Team two player 2 has invalid username', 'players')
            is_valid = False
        return is_valid