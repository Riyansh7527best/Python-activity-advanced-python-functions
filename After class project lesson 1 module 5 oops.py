class Labrador():
    species = "DOG"
    def __init__(self,Name,Age):
        self.name = Name
        self.age = Age

Max = Labrador("Max",24)
Elliana = Labrador("Elliana",19)
print(f"{Max.name} is {Max.age} years old and his species is {Max.species}")
print(f"{Elliana.name} is {Elliana.age} years old and his species is {Elliana.species}")