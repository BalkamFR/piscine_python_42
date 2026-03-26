from ex0.Card import Rarity
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def show_card_details(card: TournamentCard, card_id: str) -> None:
    print(f"{card.name} (ID: {card_id}):")
    print(f"- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {card.rating}")
    print(f"- Record: {card.wins}-{card.losses}")


def main() -> None:
    print("=== DataDeck Tournament Platform ===\n")
    platform = TournamentPlatform()

    dragon = TournamentCard("Fire Dragon", 5, Rarity.LEGENDARY, 8, 5, 15, 1200)
    wizard = TournamentCard("Ice Wizard", 4, Rarity.RARE, 6, 4, 10, 1150)

    print("Registering Tournament Cards...")
    id1 = platform.register_card(dragon)
    show_card_details(dragon, id1)
    print()
    id2 = platform.register_card(wizard)
    show_card_details(wizard, id2)

    print("\nCreating tournament match...")
    match = platform.create_match(id1, id2)
    print(f"Match result: {match}\n")

    print("Tournament Leaderboard:")
    print(f"1. {dragon.name} - Rating: {dragon.calculate_rating()} "
          f"({dragon.wins}-{dragon.losses})")
    print(f"2. {wizard.name} - Rating: {wizard.calculate_rating()} "
          f"({wizard.wins}-{wizard.losses})")

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()