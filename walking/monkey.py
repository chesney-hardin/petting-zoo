from datetime import date

class Monkey:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True

george = Monkey()
george.name = "George"
george.species = "Howler Monkey"

print(george)

