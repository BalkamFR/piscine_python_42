class Plant:

    def __init__(
            self,
            name_plant: str,
            starting_height_plant: int,
            starting_age_plant: int):

        res = self.set_height(starting_height_plant)
        if (res == 1):
            return
        res = self.set_age(starting_age_plant)
        if (res == 1):
            return
        self.__name_plant: str = name_plant
        self.__type_plant: str = "Not define"

    def set_type_plant(self, type_plant: str):
        self.__type_plant = type_plant

    def set_height(self, height_update: int) -> int:

        if (height_update < 0):
            self.__starting_height_plant = -1
            print(f"Invalid operation attempted: height {height_update}cm"
                  "[REJECTED]")
            print("Security: Negative height rejected")
            return (1)
        else:
            self.__starting_height_plant = height_update
            return (0)

    def set_age(self, age_update: int) -> int:

        if (age_update < 0):
            self.__starting_age_plant = -1
            print(
                f"Invalid operation attempted: age {age_update}cm [REJECTED]")
            print("Security: Negative age rejected")
            return (1)
        else:
            self.__starting_age_plant = age_update
            return (0)

    def get_height(self) -> int:
        return (self.__starting_height_plant)

    def get_age(self) -> int:
        return (self.__starting_age_plant)

    def get_name(self) -> str:
        return (self.__name_plant)

    def get_info(self) -> str:
        return (f"{self.__name_plant} ({self.__type_plant}): "
                "{self.__starting_height_plant}cm,"
                " {self.__starting_age_plant} day")

    def print_data_plant(self) -> None:
        if (self.__starting_height_plant == -
                1 or self.__starting_age_plant == -1):
            print("Plant is not define")
            return
        else:
            print(self.get_info(), end=' ')


class FloweringPlant(Plant):
    def __init__(self,
            name_plant: str,
            starting_height_plant: int,
            starting_age_plant: int, 
            color_plant: str,
            blooming_plant: str,
            ):
        super().__init__(name_plant, starting_height_plant, starting_age_plant)




class PrizeFlower(FloweringPlant):
    ""

class GardenManager:

    __all_garden:list = []

    def __init__(self, name_garden_add:str):
        self.__name_garden = name_garden_add
        self.__score_garden = 0
        self.__all_plants = []
        self.__all_garden.append(self)

    def add_plants_garden(self, name_plant:list):
        self.__all_plants.append(name_plant)
        print(f"Added {name_plant.get_name()} to {self.__name_garden} garden")


    def getname(self):
        return(self.__name_garden)

    def getscore(self):
        return(self.__score_garden)

    def print_all_plants(self):
        for plant in self.__all_plants:
            print(plant.get_name())

    @classmethod
    def garden_scores(cls):
        print("Garden scores - ", end = '')
        for user in cls.__all_garden:
            print(f"{user.getname()}: {user.getscore()}", end= ', ')
        print()

    @classmethod        
    def total_gardens(cls):
        print(f"Total gardens managed: {len(cls.__all_garden)}")


if __name__ == '__main__':
    oak = Plant("oak", 10, 20)
    rose = Plant("rose", 10, 20)


    alice = GardenManager("alice")
    bob = GardenManager("bob")
    alice.add_plants_garden(rose)
    alice.add_plants_garden(oak)
    alice.print_all_plants()

    GardenManager.garden_scores()
    GardenManager.total_gardens()
