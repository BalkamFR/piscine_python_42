from alchemy.grimoire import validate_ingredients, record_spell


def ingredient_validation() -> None:
    print("Testing ingredient validation:")
    print(
        "validate_ingredients(\"fire air\"): "
        f"{validate_ingredients('fire air')}")
    print(
        "validate_ingredients(\"dragon scales\"): "
        f"{validate_ingredients('dragon scales')}")


def spell_recording() -> None:
    print("\nTesting spell recording with validation:")
    print(
        "record_spell(\"Fireball\", \"fire air\"): "
        f"{record_spell('Fireball', 'fire air')}")
    print(
        "record_spell(\"Dark Magic\", \"shadow\"):"
        f" {record_spell('Dark Magic', 'shadow')}")


def late_import() -> None:
    print("\nTesting spell recording with validation:")
    print(
        "record_spell(\"Lightning\", \"air\"): "
        f"{record_spell('Lightning', 'air')}")


def main() -> None:
    print("\n=== Circular Curse Breaking ===\n")
    ingredient_validation()
    spell_recording()
    late_import()
    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
