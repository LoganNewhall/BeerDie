from flask_app.config.mysqlconnection import connectToMySQL

class Game_Event:
    db = 'beer_die'
    def __init__(self, data):
        self.game_id = data['game_id']
        self.user_id = data['user_id']
        self.sink = data['sink']
        self.self_sink = data['self_sink']
        self.cup_hit = data['cup_hit']
        self.fifa = data['fifa']
        self.point = data['point']

    @classmethod
    def events(cls, data):
        query = 'INSERT INTO game_events (sink, self_sink, cup_hit, fifa, point) VALUES (%(sink)s, %(self_sink)s, %(cup_hit)s, %(fifa)s, %(point)s) WHERE user_id = %(user_id)s ON DUPLICATE UPDATE sink ;'
        game_events = connectToMySQL(cls.db).query_db(query, data)
        return game_events