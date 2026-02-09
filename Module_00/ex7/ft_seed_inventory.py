def ft_seed_inventory(name_vegetable, number: int, type_name):
	if type_name == "packets":
		print(f"{name_vegetable} seeds: {number} {type_name} available")
	if type_name == "grams":
		print(f"{name_vegetable} seeds: {number} {type_name} total")
	if type_name == "area":
		print(f"{name_vegetable} seeds: covers {number} square meters")


ft_seed_inventory("Tomato", 15, "packets")
ft_seed_inventory("Carrot", 8, "grams")
ft_seed_inventory("Lettuce", 12, "area")
