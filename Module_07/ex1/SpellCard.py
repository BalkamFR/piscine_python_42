from typing import Any
from ex0.Card import Card, Rarity


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type
        self.type: str = "Spell"

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Deal {self.cost} damage to target"
        }

    def resolve_effect(self, targets: list[Any]) -> dict[str, Any]:
        target_names: list[str] = []
        for target in targets:
            target_names.append(target.name)
        return {
            "spell": self.name,
            "type": self.effect_type,
            "targets": target_names,
            "resolved": True
        }
