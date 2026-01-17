class Human:
    species = "Human"
    def __init__(self, name): self.name = name

person = Human("A")
print(f"Name: {person.name}, Species: {person.species}")

Human.species = "Homo Sapiens"
print(f"Name: {person.name}, Species: {person.species}")
