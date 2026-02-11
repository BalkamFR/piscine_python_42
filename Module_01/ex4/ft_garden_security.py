class Garden_Security:

	def __init__(self, name_plant:str, starting_height_plant:int, starting_age_plant:int):
		if (starting_height_plant < 0):
			print(f"Invalid operation attempted: height {starting_height_plant}cm [REJECTED]")
			print("Security: Negative height rejected")
			return
		if (starting_age_plant < 0):
			print(f"Invalid operation attempted: age {starting_age_plant}old [REJECTED]")
			print("Security: Negative age rejected")
			return
		if (starting_height_plant >= 0 & starting_age_plant >= 0):	
			self.name_plant:str = name_plant
			self.starting_height_plant:int = starting_height_plant + 0.0
			self.starting_age_plant:int = starting_age_plant
			self.day_plant:int = 1
			print(f"Plant created: {self.name_plant}")
	def age(self)->None:
		self.starting_age_plant += 1
		self.day_plant += 1

	def grow(self)->None:
		self.starting_height_plant += 1

	def get_info(self):
		return (f"{self.name_plant}: {self.starting_height_plant}cm, {self.starting_age_plant} days old")
	
	def print_data_plant(self):
		print(f"Current plant: {self.name_plant} ({self.starting_height_plant}cm, {self.starting_age_plant} days)")


def add_plant_tab_plants(all_plants:list, name_plant_add:str, height_plant_add:int, age_plant_add):
	plant = Garden_Security(name_plant_add, height_plant_add, age_plant_add)
	print(f"Plant created: {name_plant_add}")
	all_plants.append(plant)

if __name__ == '__main__':
	print("=== Garden Security System ===")
	rose = Garden_Security("Rose", 0, 0)
	rose.print_data_plant()
