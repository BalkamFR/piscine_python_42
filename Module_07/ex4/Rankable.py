from abc import ABC, abstractmethod

class Rankable(ABC):
	def calculate_rating(self) -> int:
		pass
	def update_wins(self, wins: int) -> None:
		pass
	def update_losses(self, losses: int) -> None:
		pass
	def get_rank_info(self) -> dict:
		pass
	