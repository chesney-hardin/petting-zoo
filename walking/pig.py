from datetime import date

class Pig:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

wilbur = Pig("Wilbur", "pot-bellied pig")

print(wilbur)
