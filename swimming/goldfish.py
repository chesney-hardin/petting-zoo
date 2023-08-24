from datetime import date

class GoldFish:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

bling = GoldFish("Flipper", "gold fish")

print(bling)

