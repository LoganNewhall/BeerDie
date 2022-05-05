from flask_app.config.mysqlconnection import connectToMySQL

class Friend:
    db = 'beer_die'
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.friend_id = data['friend_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']