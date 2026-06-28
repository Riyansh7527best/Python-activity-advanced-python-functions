class parrot:
    species = "Bird"
    def __init__(self,Name,Age):
        self.Name = Name
        self.Age = Age

Rocky = parrot("Rocky",12)
Stella = parrot("Stella",17)

print(f"{Rocky.Name} is {Rocky.Age} years old Rocky's species is {Rocky.species} \n {Stella.Name} is {Stella.Age} years old Rocky's species is {Stella.species}")