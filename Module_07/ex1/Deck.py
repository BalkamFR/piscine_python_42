from typing import Any
from ex0.Card import Card
import random


class Deck:
    def __init__(self) -> None:
        self.all_card: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.all_card.append(card)

    def remove_card(self, card_name: str) -> bool:
        i = 0
        for card in self.all_card:
            if card.name == card_name:
                self.all_card.pop(i)
                return True
            i += 1
        return False

    def shuffle(self) -> None:
        random.shuffle(self.all_card)

    def draw_card(self) -> Card | None:
        if len(self.all_card) == 0:
            print("The card deck is empty")
            return None
        card: Card = self.all_card[0]
        self.remove_card(card.name)
        return card

    def get_deck_stats(self) -> dict[str, Any]:
        creatures = [card for card in self.all_card if card.type == "Creature"]
        spell = [card for card in self.all_card if card.type == "Spell"]
        artifact = [card for card in self.all_card if card.type == "Artifact"]
        avg_cost = (
            sum(card.cost for card in self.all_card) / len(self.all_card)
            if self.all_card else 0.0
        )
        return {
            'total_cards': len(self.all_card),
            'creatures': len(creatures),
            'spell': len(spell),
            'artifact': len(artifact),
            'avg_cost': avg_cost
        }
