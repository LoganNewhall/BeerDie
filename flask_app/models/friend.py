from flask_app.config.mysqlconnection import connectToMySQL

class Friend:
    db = 'beer_die'
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.friend_id = data['friend_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def accept_friend(cls, data):
        query = 'INSERT INTO friends (user_id, friend_id) VALUES (%(user_id)s, %(friend_id)s), (%(friend_id)s, %(user_id)s);'
        friends = connectToMySQL(cls.db).query_db(query, data)
        return friends

    @classmethod
    def get_friends(cls, data):
        query = 'SELECT * FROM friends LEFT JOIN users ON friends.friend_id = users.id WHERE user_id = %(user_id)s;'
        all_friends = connectToMySQL(cls.db).query_db(query, data)
        return all_friends

