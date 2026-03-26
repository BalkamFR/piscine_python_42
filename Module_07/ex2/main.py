from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard


def get_attribut_class(cls: type) -> list[str]:
    return [
        attribut
        for attribut in cls.__dict__
        if not attribut.startswith("_")
    ]


def test_ability_system() -> None:
    warrior = EliteCard("Arcane Warrior", 6, Rarity.EPIC, 5, 10, 3, 7)

    print("EliteCard capabilities:")
    print(f"Card: {get_attribut_class(Card)}")
    print(f"Combatable: {get_attribut_class(Combatable)}")
    print(f"Magical: {get_attribut_class(Magical)}")

    print(f"\nPlaying {warrior.name} (Elite Card):")

    print("\nCombat phase:")
    print(warrior.attack('Enemy'))
    print(warrior.defend(5))

    print("\nMagic phase:")
    print(
        f"Spell cast: {warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}"
    )
    print(f"Mana channel: {warrior.channel_mana(3)}")


def main() -> None:
    print("\n=== DataDeck Ability System ===\n")
    test_ability_system()
    print("\nMultiple interface implementation successful!")


if __name__ == '__main__':
    main()
