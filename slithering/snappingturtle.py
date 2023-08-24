from datetime import date

class SnappingTurtle:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

gotcha = SnappingTurtle("Gotcha", "snapping turtle")

print(gotcha)


