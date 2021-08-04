from home_app.config.mysqlconnection import connectToMySQL

class Post:
    db_name = "the_wall"

    def __init__(self, data):
        self.title = data["title"]
        self.content = data["content"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.user = None