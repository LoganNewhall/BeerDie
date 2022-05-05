from flask_app.config.mysqlconnection import connectToMySQL

class Friend_Request:
    db = 'beer_die'
    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sending_user_id = data['sending_user_id']
        self.receiving_user_id = data['receiving_user_id']