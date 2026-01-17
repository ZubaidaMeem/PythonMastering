class User:
    def __init__(self, user_id): self.id = user_id
    def __eq__(self, other): return self.id == other.id

print(User(1) == User(1))
print(User(1) == User(2))