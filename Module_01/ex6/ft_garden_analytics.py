class Plant:

    def __init__(
            self,
            name_plant: str,
            starting_height_plant: int,
            starting_age_plant: int):
        self.__name_plant: str = name_plant
        self.__nbr_type_plant:int =+ 1
        res = self.set_height(starting_height_plant)
        res1 = self.set_age(starting_age_plant)
        if(res == 0 and res1 == 0):
            print(f"{self.__name_plant} created")
            self.__plant_create = 1
        else:
            self.__plant_create = 0

    def get_plant_create(self):
        return(self.__plant_create)

    def set_height(self, height_update: int) -> int:

        if (height_update < 0):
            self.__starting_height_plant = -1
            print(f"Invalid operation ({self.__name_plant}) attempted: height {height_update}cm")
            print("Security: Negative height [REJECTED]")
            return (1)
        else:
            self.__starting_height_plant = height_update
            return (0)

    def set_age(self, age_update: int) -> int:

        if (age_update < 0):
            self.__starting_age_plant = -1
            print(
                f"Invalid operation ({self.__name_plant})  attempted: age {age_update}cm ")
            print("Security: Negative age [REJECTED]")
            return (1)
        else:
            self.__starting_age_plant = age_update
            return (0)

    def get_height(self) -> int:
        return (self.__starting_height_plant)

    def grow_plant(self, size_grow:int):
        self.__starting_height_plant = self.__starting_height_plant + size_grow

    def get_age(self) -> int:
        return (self.__starting_age_plant)

    def get_name(self) -> str:
        return (self.__name_plant)

    def print_data_plant(self) -> None:
        print (f" - {self.get_name()}: {self.__starting_height_plant}cm")

    def get_type_and_nbr_plant(self):
        return(f"{self.__nbr_type_plant} regular")

class FloweringPlant(Plant):
    def __init__(
            self,
            name_plant: str,
            starting_height_plant: int,
            starting_age_plant:int, 
            color_plant: str, 
            blooming_plant: str):
        super().__init__(name_plant, starting_height_plant, starting_age_plant)
        self.__color_plant = color_plant
        self.__blooming_plant = blooming_plant
        self.__nbr_type_plant:int =+ 1

    def get_color_plant(self) -> str:
        return(self.__color_plant)
    
    def get_blooming_plant(self) -> str:
        return(self.__blooming_plant)

    def print_data_plant(self) -> str:
        print (f" - {self.get_name()}: {self.get_height()}cm {self.get_color_plant()} ({self.get_blooming_plant()})")
    
    def get_type_and_nbr_plant(self):
        return(f"{self.__nbr_type_plant} flowering")


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name_plant: str,
        starting_height_plant: int,
        starting_age_plant:int, 
        color_plant: str, 
        blooming_plant: str, 
        prize_plant:int):
        super().__init__(name_plant, starting_height_plant, starting_age_plant, color_plant, blooming_plant)
        self.__prize_plant = prize_plant
        self.__nbr_type_plant:int =+ 1
    
    def print_data_plant(self) -> str:
        print (f" - {self.get_name()}: {self.get_height()}cm {self.get_color_plant()} ({self.get_blooming_plant()}),  Prize points: {self.__prize_plant}")

    def get_type_and_nbr_plant(self):
        return(f"{self.__nbr_type_plant} prize flowers")
            

class GardenManager:

    __all_garden:list = []
    __all_plant_bad:list = []


    def __init__(self, name_garden_add:str):
        self.__name_garden = name_garden_add
        self.__score_garden = 0
        self.__all_plants = []
        self.__total_grow = 0
        self.__all_garden.append(self)

    def add_plants_garden(self, name_plant:list):
        if name_plant.get_plant_create() == 1:
            self.__all_plants.append(name_plant)
        else:
            self.__all_plant_bad.append(name_plant)
        self.__score_garden += 10
        if name_plant.get_plant_create() == 1:
            print(f"Added {name_plant.get_name()} to {self.__name_garden} garden")


    def grow_all_plant(self, size_grow:int):
        print(f"\n{self.__name_garden} is helping all plants grow...")
        for plant in self.__all_plants:
                print(f"{plant.get_name()} grew {size_grow}cm")
                self.__total_grow = size_grow + self.__total_grow
                plant.grow_plant(size_grow)

    def getname(self):
        return(self.__name_garden)

    def getscore(self):
        return(self.__score_garden)

    def print_all_plants(self):
        for plant in self.__all_plants:
            plant.print_data_plant()

    def print_stats(self):
        print(f"Plants added: {len(self.__all_plants)}, Total growth: {self.__total_grow}cm")
        print(f"Plant types: ", end= '')
        for plant in self.__all_plants:
            print(plant.get_type_and_nbr_plant(), end=', ')

    def print_report(self):
        print()
        print(f"=== {self.__name_garden} Garden Report ===")
        print(f"Plants in garden:")
        self.print_all_plants()
        print()
        self.print_stats()
        print("\n")

    @classmethod
    def garden_scores(cls):
        print("Garden scores - ", end = '')
        for user in cls.__all_garden:
            print(f"{user.getname()}: {user.getscore()}", end= ', ')
        print()

    @classmethod
    def total_gardens(cls):
        print(f"Total gardens managed: {len(cls.__all_garden)}")
    
    @classmethod
    def validation_test(cls):
        if len(cls.__all_plant_bad) == 0:
            print("Height validation test: True")
        else:
            print("Height validation test: False")


if __name__ == '__main__':
    print("=== Garden Create Plants ===\n")
    oak = FloweringPlant("oak", 10, 20, "red", "blooming")
    rose = Plant("rose", 10, 20)
    Sunflower = PrizeFlower("Sunflower", 51, 10 ,"red", "blooming", 10)
    print("\n=== Garden Management System Demo ===\n")
    alice = GardenManager("Alice")
    bob = GardenManager("bob")
    alice.add_plants_garden(rose)
    alice.add_plants_garden(Sunflower)    
    alice.add_plants_garden(oak)
    bob.add_plants_garden(Sunflower)
    # alice.grow_all_plant(2)
    bob.print_report()
    # print(f"\nalice\n {alice.verif_height()}")
    GardenManager.validation_test()
    GardenManager.garden_scores()
    GardenManager.total_gardens()
