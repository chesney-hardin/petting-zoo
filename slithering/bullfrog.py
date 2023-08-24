from datetime import date

class BullFrog:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

croak = BullFrog("Croak", "bull frog")

print(croak)

