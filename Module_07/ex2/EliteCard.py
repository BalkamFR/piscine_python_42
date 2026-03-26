from typing import Any, Union
from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: Rarity,
        attack: int,
        health: int,
        defense: int,
        mana: int,
        combat_type: str = "melee",
        spell_cost: int = 4
    ):
        super().__init__(name, cost, rarity)
        self.type: str = "Elite"
        self.combat_type: str = combat_type
        self.spell_cost: int = spell_cost

        self.attack_power: int
        if attack < 0:
            print("Negative value is forbidden for attack")
            self.attack_power = 0
        else:
            self.attack_power = attack

        self.health: int
        if health < 0:
            print("Negative value is forbidden for health")
            self.health = 0
        else:
            self.health = health

        self.defense_value: int
        if defense < 0:
            print("Negative value is forbidden for defense")
            self.defense_value = 0
        else:
            self.defense_value = defense

        self.mana_pool: int
        if mana < 0:
            print("Negative value is forbidden for mana")
            self.mana_pool = 0
        else:
            self.mana_pool = mana

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"{self.type} card enters the battlefield"
        }

    def attack(self, target: Union[str, Card]) -> dict[str, Any]:
        target_name: str
        if isinstance(target, str):
            target_name = target
        else:
            target_name = target.name
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": self.combat_type
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        blocked: int
        if incoming_damage < self.defense_value:
            blocked = incoming_damage
        else:
            blocked = self.defense_value
        taken: int = incoming_damage - blocked
        self.health -= taken
        alive: bool
        if self.health > 0:
            alive = True
        else:
            alive = False
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": alive
        }

    def cast_spell(
        self,
        spell_name: str,
        targets: list[Any]
    ) -> dict[str, Any]:
        self.mana_pool -= self.spell_cost
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.spell_cost
        }

    def channel_mana(self, amount: int) -> dict[str, Any]:
        self.mana_pool += amount
        return {
            "channeled": amount,
            "total_mana": self.mana_pool
        }

    def get_combat_stats(self) -> dict[str, Any]:
        return {
            "attack": self.attack_power,
            "defense": self.defense_value,
            "health": self.health
        }

    def get_magic_stats(self) -> dict[str, Any]:
        return {
            "mana_pool": self.mana_pool
        }
