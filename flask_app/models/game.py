from flask_app.config.mysqlconnection import connectToMySQL

class Game:
    db = 'beer_die'
    def __init__(self, data):
        self.id = data['id']
        self.team_1_score = data['team_1_score']
        self.team_2_score = data['team_2_score']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']