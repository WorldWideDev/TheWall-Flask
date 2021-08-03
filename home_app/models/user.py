from home_app.config.mysqlconnection import connectToMySQL
from home_app import app
from flask_bcrypt import Bcrypt
from flask import flash
import re

bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from home_app import app
class User:
    db_name = "the_wall"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]

    @classmethod
    def authenticate(cls, email, password):
        print(email, password)
        user = cls.get_one_by_email(email)
        should_authenticate = True
        if not user:
            should_authenticate = False
        else:
            should_authenticate = bcrypt.check_password_hash(user.password, password)
        if not should_authenticate:
            flash("Invalid login credentials", "login")
            return 0
        return user.id

    @classmethod
    def validate(cls, data):
        errors = []
        if cls.get_one_by_email(data["email"]):
            errors.append("Email already exists")
        if len(data["first_name"]) < 1:
            errors.append("First Name field is required")
        if len(data["last_name"]) < 1:
            errors.append("Last Name field is required")
        if not EMAIL_REGEX.match(data["email"]):
            errors.append("Invalid email address")
        if len(data["password"]) < 8:
            errors.append("Password must be at least 8 characters")
        if data["password"] != data["confirm_pw"]:
            errors.append("Passwords do not match")

        if errors:
            for error in errors:
                flash(error, "register")
            return False
        return True
        

    @classmethod
    def get_all(cls):
        results = connectToMySQL(cls.db_name).query_db("SELECT * FROM users;")
        return [ cls(x) for x in results ]

    @classmethod
    def get_one_by_email(cls, email):
        results = connectToMySQL(cls.db_name).query_db("SELECT * FROM users WHERE email= %(email)s;", { "email": email })
        return cls(results[0]) if results else None

    @classmethod
    def get_one(cls, id):
        results = connectToMySQL(cls.db_name).query_db("SELECT * FROM users WHERE id = %(id)s;", { "id": id })
        return cls(results[0]) if results else None

    @classmethod
    def save(cls, data):
        data = dict(data)
        data["password"] = bcrypt.generate_password_hash(data["password"])
        query = "INSERT INTO users (first_name, last_name, email, password) \
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        result_id = connectToMySQL(cls.db_name).query_db(query, data)
        return result_id
