# Python Libary Imports
from dataclasses import dataclass

# Third-Party Imports
from fastenum import Enum

# Project Package Imports
from src.game.player import Player

class RewardType(Enum):
    """
    Rewards Enum Class

    EP -> 'EP' give Player Experience Points

    ITEM -> 'ITEM' give Player a Item in Inventory
    
    """
    EP = 'EP'
    ITEM = 'ITEM'


class RequirementType(Enum):
    """
    Requirements Enum Class

    LOCATION -> 'LOCATION' to check if Player on a Location

    ITEM -> 'ITEM' to check if Player has Item in Inventory
    
    """
    LOCATION = 'LOCATION'
    ITEM = 'ITEM'


@dataclass
class Achievement:
    """
    Achievment Class 

    Arguments:
        name: [str] -> Name of Achievment
        finished: [bool] -> When Achievment is finished is True else False
        rewards: [list] -> List of Rewards
        requirements: [list] -> List of Requirements
        displayed: [dict] -> With Title / Subtitle

    Methods:
        add_rewards: (name: str, reward_type: RewardType, data: dict) -> Add Reward to Rewards from Achievment
        set_display: (title: str, subtitle: str) -> Set Display [Title, Subtitle] for Achievment
        add_requirement: (name: str, requirement_type: RequirementType, data: dict) -> Add Requirement to Requirements from Achievment
        run: (player: Player) -> Execute this Achievment with Player as Target
        
    """
    name = name
    finished = False
    rewards = []
    requirements = []
    displayed = {'title': self.name.upper(), 'subtitle': subtitle}

    def add_reward(self, name: str, reward_type: RewardType, data: dict):
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
            return 0

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
            return 0

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
