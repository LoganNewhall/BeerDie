from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DATE_REGEX = re.compile(r'^\d{4}-\d{2}-\d{2}$')

class User:
    db = 'beer_die'
    def __init__(self, data):
        self.id = data['id']
        self.f_name = data['f_name']
        self.l_name = data['l_name']
        self.age = data['age']
        self.email = data['email']
        self.username = data['username']
        self.password = data['password']
        self.profile_pic = data['profile_pic']
        self.rules =data['rules']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO users (f_name, l_name, age, email, username, password) VALUES (%(f_name)s, %(l_name)s, %(age)s, %(email)s, %(username)s, %(password)s);'
        user_id = connectToMySQL(cls.db).query_db(query, data)
        return user_id

    @classmethod 
    def get_by_username(cls,data):
        query = 'SELECT * FROM users WHERE username = %(username)s;'
        username_in_db = connectToMySQL(cls.db).query_db(query, data)
        if len(username_in_db) == 1:
            return username_in_db[0]
        else:
            return None
        
    @classmethod
    def get_user(cls, data):
        query = 'SELECT * FROM users WHERE id = %(user_id)s'
        user = connectToMySQL(cls.db).query_db(query, data)
        print(user)
        return user[0]

    @classmethod
    def update_user(cls, data):
        query = 'UPDATE users SET f_name = %(f_name)s, l_name = %(l_name)s, email = %(email)s, username = %(username)s, rules = %(rules)s WHERE id = %(user_id)s;'
        user = connectToMySQL(cls.db).query_db(query, data)
        return user

    @staticmethod
    def validate_user(user):
        is_valid = True
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        email_result = connectToMySQL(User.db).query_db(query, user)
        query = 'SELECT * FROM users WHERE username = %(username)s;'
        username_result = connectToMySQL(User.db).query_db(query, user)
        if len(user['f_name']) < 2:
            flash('First name must be at least 2 characters.', 'register')
            is_valid = False
        if len(user['l_name']) < 2:
            flash('Last name must be at least 2 characters.', 'register')
            is_valid = False
        if len(email_result) >= 1:
            flash('Email is already in use.', 'register')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid email address.', 'register')
            is_valid = False
        if len(username_result) >= 1:
            flash('Username is taken.', 'register')
            is_valid = False
        if not DATE_REGEX.match(user['age']):
            flash('Must enter valid birthday.', 'register')
            is_valid = False
        elif (datetime.now() - datetime.strptime(user['age'], '%Y-%m-%d')).days < 7665:
            flash("Must be at least 21 to register.", 'register')
            is_valid = False
        if len(user['password']) < 8:
            flash('Password must have at least 8 characters', 'register')
            is_valid = False
        if user['password'] != user['password_confirm']:
            flash('Passwords do not match', 'register')
            is_valid = False
        return is_valid 