from flask_app import app
from flask_app.controllers import users, games, game_has_users, friends, friend_requests

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)