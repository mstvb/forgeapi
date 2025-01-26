from fastenum import Enum
from src.game.player import Player


class RewardType(Enum):
    EP = 'EP'
    ITEM = 'ITEM'


class RequirementType(Enum):
    LOCATION = 'LOCATION'
    ITEM = 'ITEM'


class Achievement:
    __slots__ = ['name', 'finished', 'rewards', 'requirements', 'displayed']

    def __init__(self, name: str, subtitle: str):
        self.name: str = name
        self.finished: bool = False
        self.rewards: list = []
        self.requirements: list = []
        self.displayed: dict = {'title': self.name.upper(), 'subtitle': subtitle}

    def add_rewards(self, name: str, reward_type: RewardType, data: dict):
        if data.get('item'):
            self.rewards.append(
                {'name': name, 'type': reward_type,
                 'item': data.get('item')})
        elif data.get('ep'):
            self.rewards.append(
                {'name': name, 'type': reward_type,
                 'item': data.get('ep')}
            )
        else:
            return

    def set_display(self, title: str, subtitle: str):
        self.displayed = {'title': title.upper(), 'subtitle': subtitle}

    def add_requirement(self, name: str,
                        requirement_type: RequirementType,
                        data: dict):
        if data.get('loc'):
            self.requirements.append(
                {'name': name, 'type': requirement_type,
                 'loc': data.get('loc')})
        elif data.get('item'):
            self.requirements.append(
                {'name': name, 'type': requirement_type,
                 'item': data.get('item')})
        else:
            return

    def run(self, player: Player):
        for requirement in self.requirements:

            if requirement['type'] is RequirementType.ITEM:

                if player.has_item(requirement['item']):
                    player.remove_item(requirement['item'])
                    self.requirements.remove(requirement)

            elif requirement['type'] is RequirementType.LOCATION:

                if player.get_location() is requirement['loc']:
                    self.requirements.remove(requirement)

        if not self.requirements:
            for reward in self.rewards:

                if reward['type'] is RewardType.ITEM:
                    player.add_item(reward['item'])

                elif reward['type'] is RewardType.EP:
                    player.add_experience(reward['ep'])

        self.finished = True