from flask_app.config.mysqlconnection import connectToMySQL

class Friend_Request:
    db = 'beer_die'
    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sending_user_id = data['sending_user_id']
        self.receiving_user_id = data['receiving_user_id']


    @classmethod
    def send_request(cls, data):
        query = 'INSERT INTO friend_requests (sending_user_id, receiving_user_id) VALUES (%(sending_user_id)s, %(receiving_user_id)s);'
        sent_request = connectToMySQL(cls.db).query_db(query, data)
        return sent_request

    @classmethod
    def get_requests(cls, data):
        query = 'SELECT * FROM friend_requests LEFT JOIN users ON friend_requests.sending_user_id = users.id WHERE receiving_user_id = %(user_id)s;'
        received_requests = connectToMySQL(cls.db).query_db(query, data)
        return received_requests

    @classmethod
    def delete_request(cls, data):
        query = 'DELETE FROM friend_requests WHERE sending_user_id = %(sending_user_id)s AND receiving_user_id = %(receiving_user_id)s;'
        deleted_request = connectToMySQL(cls.db).query_db(query, data)
        return deleted_request

    @staticmethod
    def validate_request(user):
        is_valid = False
        query = 'SELECT * FROM users WHERE username = %(username)s;'
        user_result = connectToMySQL(Friend_Request.db).query_db(query, user)
        if len(user_result) == 1:
            is_valid = True
        return is_valid