introMsg = "Hello World!"
print(introMsg)

class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    def is_worth_it(self):
        print(self.draft - (1.5 * self.crew))

boat = Ship(15, 10)

boat.is_worth_it()






