from datetime import date

class Salamander:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

sparkle = Salamander("Sparkle", "salamander")

print(sparkle)


