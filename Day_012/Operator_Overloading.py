class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Wallet(self.amount + other.amount)

w1 = Wallet(100)
w2 = Wallet(50)
w3 = w1 + w2
print(w3.amount)  