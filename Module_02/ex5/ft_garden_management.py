class GardenError(Exception):
   
    @staticmethod
    def plant_valid_name(plant:str):
        if type(plant) is not str:
            raise GardenError(f"Error: Plant name cannot be empty!")
        else:
            print(f"Added {plant} successfully")
   
    @staticmethod
    def plant_valid_water(water:int):
        if water > 10:
            raise GardenError(f"Water level {water} is too high (max 10)")

    @staticmethod
    def plant_valid_sunlight(hours:int):
        if hours < 2:
            raise GardenError(f"Sunlight hours {hours} is too low (min 2)")

    @staticmethod
    def check_min_water(water:int):
        if water < 10:
            raise GardenError(f"Not enough water in tank")

class GardenManager():
    def __init__(self, name:str):
        try:
            GardenError.plant_valid_name(name)
            self.name_plant:str = name
            self.watter:int = 0
            self.sun:int = 0
        except GardenError as e:
            print(e)

    def sun_plant(self, level_sun:int):
        self.sun =+ level_sun
    
    def watter_plant(self, level:int):
        print(f"Watering {self.name_plant} - success")
        self.watter =+ level
    
    def check_plant_good(self):
        try:
            GardenError.plant_valid_water(self.watter)
            GardenError.plant_valid_sunlight(self.sun)
            print(f"{self.name_plant}: healthy (water: {self.watter}, sun: {self.sun})")
        except GardenError as e:
            print(f"Error checking lettuce: {e}")
    
    def check_watter_min_good(self):
        try:
            GardenError.check_min_water(self.watter)
            print("Watter is good")
        except GardenError as e:
            print(f"Caught GardenError: {e}")

def test_garden_management():
    tomato:GardenManager = GardenManager("tomato")
    lettus:GardenManager = GardenManager("lettus")
    GardenManager(None)
    print("\nWatering plants...")
    print("Opening watering system")
    tomato.watter_plant(5)
    tomato.sun_plant(8)
    lettus.watter_plant(15)
    lettus.sun_plant(8)
    print("Closing watering system (cleanup)")
    print("\nChecking plant health...")
    tomato.check_plant_good()
    lettus.check_plant_good()
    print("\nTesting error recovery...")
    tomato.check_watter_min_good()
    print("System recovered and continuing...")


if __name__ == '__main__':
    print("=== Garden Management System ===\n")
    test_garden_management()
    print("\nGarden management system test complete!")
