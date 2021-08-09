from home_app.config.mysqlconnection import connectToMySQL
from home_app.models import user
from home_app.models import comment
from flask import flash
class Post:
    db_name = "the_wall"

    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.content = data["content"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.user = None

    @staticmethod
    def validate(data):
        errors = []
        if len(data["title"]) < 1 or len(data["content"]) < 1:
            errors.append("All fields are required")
        elif len(data["content"]) < 5:
            errors.append("Post must contain at least 5 characters")
        if errors:
            for error in errors:
                flash(error)
            return False
        return True

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts JOIN users on users.id = posts.user_id ORDER BY created_at DESC;"
        results = connectToMySQL(cls.db_name).query_db(query)
        posts = []
        for i in range(len(results)):
            post = cls(results[i])
            post.user = user.User(results[i])
            posts.append(post)
        return posts

    @classmethod
    def get_all_with_comments(cls):
        query = "SELECT * FROM posts JOIN users on users.id = posts.user_id ORDER BY posts.created_at DESC;"
        results = connectToMySQL(cls.db_name).query_db(query)
        posts = []
        for i in range(len(results)):
            post = cls(results[i])
            post.user = user.User(results[i])
            post.comments = comment.Comment.post_comments(results[i]["id"])
            posts.append(post)
        return posts

    @classmethod
    def save(cls, data):
        query = "INSERT INTO posts (title, content, user_id) VALUES (%(title)s, %(content)s, %(user_id)s);"
        connectToMySQL(cls.db_name).query_db(query, data)



