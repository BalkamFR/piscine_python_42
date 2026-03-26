from typing import Any
from ex0.Card import Card, Rarity


class ArtifactCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: Rarity,
        durability: int,
        effect: str
    ):
        super().__init__(name, cost, rarity)
        self.durability: int = durability
        self.effect_description: str = effect
        self.type: str = "Artifact"

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        result: dict[str, Any] = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect_description}"
        }
        return result

    def activate_ability(self) -> dict[str, Any]:
        return {
            "artifact": self.name,
            "action": "Ability activated",
            "durability_remaining": self.durability
        }
