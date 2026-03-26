from typing import Any
from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard


def combat_card() -> None:
    dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)
    goblin = CreatureCard("Goblin Warrior", 3, Rarity.COMMON, 2, 3)
    mana: int = 6
    print("CreatureCard Info:")
    print(dragon.get_card_info())
    game_state: dict[str, Any] = {}
    game_state = dragon.play(game_state)
    print(f"\nPlaying Fire Dragon with {mana} mana available:")
    print(f"Playable: {dragon.is_playable(mana)}")
    print(f"Play result: {game_state}")
    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {dragon.attack_target(goblin)}")
    mana = 3
    print(f"\nTesting insufficient mana ({mana} available):")
    print(f"Playable: {dragon.is_playable(mana)}")


def main() -> None:
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")
    combat_card()
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == '__main__':
    main()
