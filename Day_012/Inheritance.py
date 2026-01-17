class User:
    def __init__(self, username):
        self.username = username

class Admin(User):
    def delete_db(self):
        print("Database deleted!")

admin = Admin("Admin")
admin.delete_db()