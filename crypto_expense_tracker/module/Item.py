
class Item:
    """
    Class for hardware info
    """

    def __init__(self, row):
        self.name = row.name
        self.total_cost = row.total_cost

    def get_item(self):
        item = {
            "name": self.name,
            "total_cost": self.total_cost
        }
        return item


