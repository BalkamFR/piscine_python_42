import random
from typing import Any
from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.creature_catalog: dict[str, dict[str, Any]] = {
            "dragon": {
                "name": "Fire Dragon", "cost": 5, "rarity": Rarity.LEGENDARY,
                "attack": 7, "health": 5
            },
            "goblin": {
                "name": "Goblin Warrior", "cost": 2, "rarity": Rarity.COMMON,
                "attack": 2, "health": 1
            }
        }
        self.spell_catalog: dict[str, dict[str, Any]] = {
            "fireball": {
                "name": "Fireball", "cost": 4, "rarity": Rarity.RARE,
                "type": "damage"
            }
        }
        self.artifact_catalog: dict[str, dict[str, Any]] = {
            "mana_ring": {
                "name": "Mana Ring", "cost": 3, "rarity": Rarity.RARE,
                "durability": 5, "effect": "Passive: +1 mana"
            }
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        stats: dict[str, Any] | None = None

        if isinstance(name_or_power, str):
            stats = self.creature_catalog.get(name_or_power)
        elif isinstance(name_or_power, int):
            for creature_data in self.creature_catalog.values():
                if creature_data["attack"] == name_or_power:
                    stats = creature_data
                    break

        if stats is None:
            random_key = random.choice(list(self.creature_catalog.keys()))
            stats = self.creature_catalog[random_key]

        return CreatureCard(
            str(stats["name"]),
            int(stats["cost"]),
            stats["rarity"],
            int(stats["attack"]),
            int(stats["health"])
        )

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        stats: dict[str, Any] | None = None

        if isinstance(name_or_power, str):
            stats = self.spell_catalog.get(name_or_power)
        elif isinstance(name_or_power, int):
            for spell_data in self.spell_catalog.values():
                if spell_data["cost"] == name_or_power:
                    stats = spell_data
                    break

        if stats is None:
            random_key = random.choice(list(self.spell_catalog.keys()))
            stats = self.spell_catalog[random_key]

        return SpellCard(
            str(stats["name"]),
            int(stats["cost"]),
            stats["rarity"],
            str(stats["type"])
        )

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        stats: dict[str, Any] | None = None

        if isinstance(name_or_power, str):
            stats = self.artifact_catalog.get(name_or_power)
        elif isinstance(name_or_power, int):
            for artifact_data in self.artifact_catalog.values():
                if artifact_data["durability"] == name_or_power:
                    stats = artifact_data
                    break

        if stats is None:
            random_key = random.choice(list(self.artifact_catalog.keys()))
            stats = self.artifact_catalog[random_key]

        return ArtifactCard(
            str(stats["name"]),
            int(stats["cost"]),
            stats["rarity"],
            int(stats["durability"]),
            str(stats["effect"])
        )

    def create_themed_deck(self, size: int) -> dict[str, Any]:
        deck_list: list[Card] = []
        for _ in range(size):
            card_type = random.choice(["creature", "spell", "artifact"])
            if card_type == "creature":
                deck_list.append(self.create_creature())
            elif card_type == "spell":
                deck_list.append(self.create_spell())
            else:
                deck_list.append(self.create_artifact())

        return {
            "deck_name": "Fantasy Deck",
            "total_cards": len(deck_list),
            "cards": deck_list
        }

    def get_supported_types(self) -> dict[str, Any]:
        return {
            "creatures": list(self.creature_catalog.keys()),
            "spells": list(self.spell_catalog.keys()),
            "artifacts": list(self.artifact_catalog.keys())
        }
