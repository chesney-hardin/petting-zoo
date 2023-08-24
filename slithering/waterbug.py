from datetime import date

class WaterBug:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

dancer = WaterBug("Dancer", "water bug")

print(dancer)

