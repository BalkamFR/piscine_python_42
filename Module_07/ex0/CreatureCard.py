from Card import Card

class CreatureCard(Card):
	def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
		super().__init__(name, cost, rarity)
		self.type = "Creature"
		if attack < 0 or health < 0:
			print("Negative value is forbidden for attack ")
			self.attack:int = 0
		else:
			self.attack:int = attack
		if health < 0:
			print("Negative value is forbidden for health ")
			self.health:int = 0
		else:
			self.health:int = health
	def play(self, game_state: dict) -> dict:
		game_state.update({
		"card_played": self.name,
		"mana_used": self.cost,
		"effect": f"{self.type} summoned to battlefield"
		})
		return game_state
	def get_card_info(self):
		infos:dict = {
			'name': self.name,
			'cost': self.cost,
			'rarity': self.rarity,
			'type':  self.type,
			'attack': self.attack,
			'health': self.health
			}
		return infos
	def get_cost(self) -> int:
		return self.cost
	def attack_target(self, target) -> dict:
		if self.attack >= target.health:
			result_combat:bool = True
		else:
			result_combat:bool = False
		attack_result:dict = {
			'attacker': self.name,
			'target': target.name,
			'damage_dealt': self.attack,
			'combat_resolved': result_combat
		}
		return attack_result