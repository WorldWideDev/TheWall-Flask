from home_app.config.mysqlconnection import connectToMySQL
from home_app.models import user
from home_app.models import post
from flask import flash

class Comment:
    db_name = "the_wall"

    def __init__(self, data):
        self.content = data["content"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.post_id = data["post_id"]
        self.user = None
        self.post = None

    @staticmethod
    def validate(data):
        errors = []
        if len(data["content"]) < 5:
            errors.append("Post must contain at least 5 characters")
        if errors:
            for error in errors:
                flash(error)
            return False
        return True

    @classmethod
    def post_comments(cls, post_id):
        query = " SELECT * FROM comments JOIN posts ON posts.id = comments.post_id JOIN users on users.id = comments.user_id WHERE posts.id = %(post_id)s ORDER BY comments.created_at DESC;"
        results = connectToMySQL(cls.db_name).query_db(query, { "post_id": post_id })
        comments = []
        if not results:
            return comments

        for i in range(len(results)):
            comment = cls(results[i])
            post_data = {
                "title": results[i]["title"],
                "content": results[i]["posts.content"],
                "user_id": results[i]["posts.user_id"],
                "created_at": results[i]["posts.created_at"],
                "updated_at": results[i]["posts.updated_at"],
            }
            comment.user = user.User(results[i])
            comments.append(comment)
        return comments

    @classmethod
    def save(cls, data):
        query = "INSERT INTO comments (content, user_id, post_id) VALUES (%(content)s, %(user_id)s, %(post_id)s);"
        connectToMySQL(cls.db_name).query_db(query, data)



