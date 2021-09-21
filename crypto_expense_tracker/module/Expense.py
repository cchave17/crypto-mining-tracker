
class Expense:
    def __init__(self, item, expense):
        self.Item = item
        self.expense = expense

    def get_expense(self):
        expense = {
            "item": self.Item.name,
            "expense": self.expense
        }
        return expense
