class User:
    def __init__(self, birth_year):
        self.birth_year = birth_year
    @property
    def age(self): return 2026 - self.birth_year

user = User(2002)
user_age = user.age
print(f"User is {user_age} years old")