""""
Class for each individual owner
"""


class Person:
    def __init__(self, name, expenses):
        self.name = name
        self.expenses = expenses

    def get_person(self):
        person = {
            self.name: {
                "Expenses": self.expenses
            }
        }
        return person
