def validate_ingredients(ingredients: str) -> str:
    test_valid = ingredients.split(" ")
    for data in test_valid:
        if (data == "fire" or data == "water"
                or data == "earth" or data == "air"):
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
