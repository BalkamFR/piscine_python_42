from abc import ABC, abstractmethod
from enum import Enum
from typing import Any


class Rarity(str, Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: Rarity):
        self.name: str = name
        self.cost: int = cost
        self.rarity: Rarity = rarity
        self.type: str = "card"

    @abstractmethod
    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        pass

    def get_card_info(self) -> dict[str, Any]:
        infos: dict[str, Any] = {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity.value,
            'type': self.type
        }
        return infos

    def is_playable(self, available_mana: int) -> bool:
        if available_mana >= self.cost:
            return True
        return False
