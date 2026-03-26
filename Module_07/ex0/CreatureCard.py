from typing import Any
from ex0.Card import Card, Rarity


class CreatureCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: Rarity,
        attack: int,
        health: int
    ):
        super().__init__(name, cost, rarity)
        self.type: str = "Creature"
        if attack < 0 or health < 0:
            print("Negative value is forbidden for attack ")
            self.attack: int = 0
        else:
            self.attack = attack

        if health < 0:
            print("Negative value is forbidden for health ")
            self.health: int = 0
        else:
            self.health = health

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"{self.type} summoned to battlefield"
        }

    def get_card_info(self) -> dict[str, Any]:
        infos: dict[str, Any] = {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity.value,
            'type':  self.type,
            'attack': self.attack,
            'health': self.health
        }
        return infos

    def get_cost(self) -> int:
        return self.cost

    def attack_target(self, target: "CreatureCard") -> dict[str, Any]:
        result_combat: bool
        if self.attack >= target.health:
            result_combat = True
        else:
            result_combat = False

        attack_result: dict[str, Any] = {
            'attacker': self.name,
            'target': target.name,
            'damage_dealt': self.attack,
            'combat_resolved': result_combat
        }
        return attack_result
