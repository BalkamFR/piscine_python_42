class Garden_Data_Organizer:

	def __init__(self, name_plant:str, height_plant:float, age_plant:int):
		self.name_plant:str = name_plant
		self.height_plant:float = height_plant + 0.0
		self.age_plant:int = age_plant
		self.day_plant:int = 1

	def age(self)->None:
		self.age_plant += 1
		self.height_plant += 1
		self.day_plant += 1

	def grow(self)->None:
		if(self.height_plant % 1 != 0):
			self.age_plant += 1
			self.day_plant += 1
		self.height_plant += 0.5

	def get_info(self):
		return (f"{self.name_plant}: {self.height_plant}cm, {self.age_plant} days old")
	
	def print_days(self):
		print(f"=== Day {self.day_plant} ===")

	def print_data_plant(self):
		print(f"{self.name_plant}: {self.height_plant}cm, {self.age_plant} days old")

	def simulator_age(self, age_more:int):
		self.print_days()
		self.print_data_plant()
		i = 0
		while(i < age_more):
			self.age()
			i+=1
		self.print_days()
		self.print_data_plant()
		print(f"Growth this week: +{age_more}cm")

if __name__ == '__main__':
	rose = Garden_Data_Organizer("rose", 25, 30)
	rose.simulator_age(6)
