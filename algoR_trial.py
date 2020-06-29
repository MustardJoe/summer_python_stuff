introMsg = "Hello World!"
print(introMsg)

class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    def is_worth_it(self):
        ourCalc = ((self.draft - (1.5 * self.crew)) >= 20)
        print(ourCalc)
        return ourCalc

boat = Ship(15, 10)

boat.is_worth_it()






