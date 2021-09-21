import pandas as pd

file = "D:\Personal Projects\Mining-Tracker\crypto-mining-tracker\Sept_20_2021_Expense_Tracker.xlsx"


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


def get_all_names(cols):
    investors = []
    for col in cols:
        if col == "Hardware" or col == "Item_Total":
            continue
        investors.append(col)
    return investors


def get_all_items(file):
    df = pd.read_excel(file)
    cols = df.columns
    names = get_all_names(cols)
    tracker = {}
    for row in range(len(df.index)):
        cur_row = df.iloc[row]
        for name in names:
            item_cost = cur_row[name]
            item_name = cur_row["Hardware"]
            cur_expense = {item_name: item_cost}
            cur_person = Person(name, cur_expense).get_person
            tracker[name] = cur_person

    print(tracker)


get_all_items(file)
