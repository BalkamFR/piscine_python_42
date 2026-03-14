def validate_ingredients(ingredients: str) -> str:
	test_valid = ingredients.split()
	for data in test_valid:
		if data == "fire" or data == "water" or "earth" or "air":
			return f"{ingredients} - VALID"
	return f"{ingredients} - INVALID"
 
def record_spell(spell_name: str, ingredients: str) -> str: 
	