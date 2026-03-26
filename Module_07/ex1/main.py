from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def test_deck_builder() -> None:
    deck = Deck()

    lightning = SpellCard("Lightning Bolt", 3, Rarity.UNCOMMON, "damage")
    crystal = ArtifactCard(
        "Mana Crystal", 4, Rarity.RARE, 3, "+1 mana per turn"
    )
    dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)

    print("Building deck with different card types...")
    deck.add_card(lightning)
    deck.add_card(crystal)
    deck.add_card(dragon)

    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:")
    for _ in range(3):
        card = deck.draw_card()
        if card:
            print(f"\nDrew: {card.name} ({card.type})")
            result = card.play({})
            print(f"Play result: {result}")


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")
    test_deck_builder()
    print("\nPolymorphism in action: Same interface, different behaviors!")


if __name__ == '__main__':
    main()
