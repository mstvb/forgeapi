from src.game.item import Item


class Player:
    """
    This Class using as Player Instance

    Attributes:
        self.location (dict): Location Data
        self.inventory (dict): Inventory Data

    Parameters:
        pos_x (int): Position of X Axis
        pos_y (int): Postion of Y Axis

    Methods:
        get_location() - Get Location from Player
        add_item(item: Item) - Add Item to Inventory of Player
        remove_item(item: Item) - Remove Item from Inventory from Player
        has_item(item: Item) - Return True when Item in Player Innventory
    """
    __slots__ = ['location', 'inventory', 'xp']

    def __init__(self, pos_x: int, pos_y: int):
        self.location = {'X': pos_x, 'Y': pos_y}
        self.inventory = {}

    def get_location(self):
        return self.location

    def add_item(self, item: Item):
        self.inventory[item.item_name] = Item

    def remove_item(self, item: Item):
        del self.inventory[item.item_name]

    def has_item(self, item: Item):
        return True if self.inventory[item.item_name] else False

    def add_experience(self, param):
        pass
