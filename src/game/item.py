from fastenum import Enum

class ItemFlags(Enum):
    HIDDEN_ATTRIBUTES = 'HIDDEN_ATTRIBUTES'
    HIDDEN_UNBREAKABLE = 'HIDDEN_UNBREAKABLE'
    HIDDEN_ENCHANTMENTS = 'HIDDEN_ENCHANTMENTS'


class Item:
    __slots__ = ['item_name', 'amount',
                 'res', 'description',
                 'item_flags', 'max_stacksize',
                 'stackable']

    def __init__(self, item_name: str, amount: int):
        self.item_name: str = item_name
        self.amount: int = amount
        self.res = None
        self.description = []
        self.item_flags = []
        self.max_stacksize: int = 64
        self.stackable = True

    def set_amount(self, amount: int):
        self.amount = amount

    def set_max_stacksize(self, amount: int):
        self.max_stacksize = amount

    def set_stackable(self, stackable: bool):
        self.stackable = stackable

    def add_itemflag(self, itemflag: ItemFlags):
        self.item_flags.append(itemflag)

    def remove_itemflag(self, itemflag: ItemFlags):
        self.item_flags.remove(itemflag)

    def add_line(self, description: str):
        self.description.append(description)

    def set_line(self, i: int, description: str):
        self.description.insert(i, description)

    def build(self):
        return self