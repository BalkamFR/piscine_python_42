from abc import ABC, abstractmethod
from enum import Enum

class Rarity(str,Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"

class Card(ABC):
	def __init__(self, name: str, cost: int, rarity: str):
		self.name:str = name
		self.cost:str = cost
		self.rarity:str = rarity
		self.type = "card"

	@abstractmethod
	def play(self, game_state: dict) -> dict:
		pass
	def get_card_info(self) -> dict:
		infos:dict = {
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
