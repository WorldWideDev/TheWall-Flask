from home_app.config.mysqlconnection import connectToMySQL
from home_app.models import user
class Post:
    db_name = "the_wall"

    def __init__(self, data):
        self.title = data["title"]
        self.content = data["content"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.user = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts JOIN users on users.id = posts.user_id;"
        results = connectToMySQL(cls.db_name).query_db(query)
        posts = []
        for i in range(len(results)):
            post = cls(results[i])
            post.user = user.User(results[i])
            posts.append(post)
        return posts



