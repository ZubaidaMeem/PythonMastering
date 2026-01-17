class User:
    def __init__(self, username):
        self.username = username

class Admin(User):
    def __init__(self, username, department):
        super().__init__(username)  
        self.department = department