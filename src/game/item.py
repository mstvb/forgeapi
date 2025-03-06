# Python Libary Imports
from dataclasses import dataclass

# Third-Party Imports
from fastenum import Enum

class ItemFlags(Enum):
    """
    ItemFlags Enum Class

    HIDDEN_ATTRIBUTES -> 'HIDDEN_ATTRIBUTES' hide Attributes from Item

    HIDDEN_UNBREAKABLE -> 'HIDDEN_UNBREAKABLE' hide Unbreakable Attribute from Item

    HIDDEN_ENCHANTMENTS -> 'HIDDEN_ENCHANTMENTS' hide Enchantments from Item
    
    """
    HIDDEN_ATTRIBUTES = 'HIDDEN_ATTRIBUTES'
    HIDDEN_UNBREAKABLE = 'HIDDEN_UNBREAKABLE'
    HIDDEN_ENCHANTMENTS = 'HIDDEN_ENCHANTMENTS'


@dataclass
class Item:
    """
    Item Class

    Arguments:
        item_name: [str] -> Name of Item
        amount: [int] -> Amount of Item
        res: [None] -> Ressource
        description: [list] -> Item Description as List
        item_flags: [list] -> ItemFlags as List
        max_stacksize: [int] -> Max Amount of a Item per Stack
        stackable: [bool] -> Is Item Stackable or Not

    Methods:
        set_amount: (amount: int) -> Set Amount of Item
        set_max_stacksize: (amount: int) -> Set Max Amount of Item per Stack
        set_stackable: (stackable: bool) -> Set Item is Stackable as Boolean
        add_itemflag: (itemflag: ItemFlag) -> Add Itemflag to ItemFlags from Item
        add_line: (line: str) -> Add Description Line to Item
        set_line: (i: int, line: str) -> Set Description Line to Item with Index
        build: () -> Build Item
    """
        item_name: str
        amount: int
        res = None
        description = []
        item_flags = []
        max_stacksize = 64
        stackable = True

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
