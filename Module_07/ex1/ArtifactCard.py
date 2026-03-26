from ex0.Card import Card, Rarity

class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect_description = effect
        self.type = "Artifact"

    def play(self, game_state: dict) -> dict:
        result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect_description}"
        }
        return result

    def activate_ability(self) -> dict:
        return {
            "artifact": self.name,
            "action": "Ability activated",
            "durability_remaining": self.durability
        }