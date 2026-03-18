def record_spell(spell_name: str, ingredients: str) -> str:
    from alchemy.grimoire import validate_ingredients
    test_valid = ingredients.split(" ")
    for data in test_valid:
        if data == "fire" or data == "water" or "earth" or "air":
            return f"Spell recorded: {spell_name} "
            f"({validate_ingredients(ingredients)})"
    return f"Spell recorded: {spell_name}"
    f" ({validate_ingredients(ingredients)})"
