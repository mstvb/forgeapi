from src.game.achievement import Achievement, RequirementType, RewardType
from src.game.item import Item, ItemFlags
from src.game.player import Player
from src.game.display import Display, DisplayMode

if __name__ == '__main__':

    # Achievement
    a = Achievement('testing', 'a new Achievement')
    a.add_requirement('require_test', RequirementType.ITEM, {'item': Item('Sword', 1)})
    a.add_rewards('reward_test', RewardType.ITEM, {'item': Item('Chest', 1)})

    # Player
    p = Player(0, 0)
    p.add_item(Item('Sword', 1))
    a.run(p)