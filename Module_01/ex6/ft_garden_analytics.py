class Plant:

    def __init__(
            self,
            name_plant: str,
            starting_height_plant: int) -> None:

        self.__name_plant: str = name_plant
        self.__nbr_type_plant: int = + 1
        res = self.set_height(starting_height_plant)
        if (res == 0):
            self.__plant_create: int = 1
        else:
            self.__plant_create = 0

    def get_plant_create(self) -> int:
        return (self.__plant_create)

    def set_height(self, height_update: int) -> int:

        if (height_update < 0):
            self.__starting_height_plant: int = -1
            print(
                f"Invalid operation ({self.__name_plant})"
                f"attempted: height {height_update}cm")
            print("Security: Negative height [REJECTED]")
            return (1)
        else:
            self.__starting_height_plant = height_update
            return (0)

    def get_height(self) -> int:
        return (self.__starting_height_plant)

    def grow_plant(self, size_grow: int) -> None:

        self.__starting_height_plant = self.__starting_height_plant + size_grow

    def get_name(self) -> str:
        return (self.__name_plant)

    def print_data_plant(self) -> None:
        print(f" - {self.get_name()}: {self.__starting_height_plant}cm")

    def get_type_and_nbr_plant(self) -> str:
        return (f"{self.__nbr_type_plant} regular")


class FloweringPlant(Plant):

    def __init__(
            self,
            name_plant: str,
            starting_height_plant: int,
            color_plant: str,
            blooming_plant: str) -> None:

        super().__init__(name_plant, starting_height_plant)
        self.__color_plant: str = color_plant
        self.__blooming_plant: str = blooming_plant
        self.__nbr_type_plant: int = + 1

    def get_color_plant(self) -> str:
        return (self.__color_plant)

    def get_blooming_plant(self) -> str:
        return (self.__blooming_plant)

    def print_data_plant(self) -> None:
        print(f" - {self.get_name()}: {self.get_height()}cm "
              f"{self.get_color_plant()} ({self.get_blooming_plant()})")

    def get_type_and_nbr_plant(self) -> str:
        return (f"{self.__nbr_type_plant} flowering")


class PrizeFlower(FloweringPlant):

    def __init__(
            self,
            name_plant: str,
            starting_height_plant: int,
            color_plant: str,
            blooming_plant: str,
            prize_plant: int) -> None:
        super().__init__(
            name_plant,
            starting_height_plant,
            color_plant,
            blooming_plant)
        if prize_plant < 0:
            self.__prize_plant: int = 0
        else:
            self.__prize_plant = prize_plant
        self.__nbr_type_plant: int = + 1

    def print_data_plant(self) -> None:
        print(f" - {self.get_name()}: {self.get_height()}cm "
              f"{self.get_color_plant()} flowers "
              f"({self.get_blooming_plant()}),  "
              f"Prize points: {self.__prize_plant}")

    def get_type_and_nbr_plant(self) -> str:
        return (f"{self.__nbr_type_plant} prize flowers")


class GardenManager:
    all_plant_bad: list[Plant] = []

    def __init__(self, name_garden_add: str) -> None:

        self.name_garden: str = name_garden_add
        self.__score_garden: int = 0
        self.all_plants: list[Plant] = []
        self.total_grow: int = 0
        self.GardenStats.all_garden.append(self)

    def add_plants_garden(self, name_plant: Plant) -> None:

        if name_plant.get_plant_create() == 1:
            self.all_plants.append(name_plant)
        else:
            self.all_plant_bad.append(name_plant)
        self.__score_garden += 10
        if name_plant.get_plant_create() == 1:
            print(
                f"Added {name_plant.get_name()} to {self.name_garden} garden")

    def grow_all_plant(self, size_grow: int) -> None:

        print(f"\n{self.name_garden} is helping all plants grow...")
        for plant in self.all_plants:
            print(f"{plant.get_name()} grew {size_grow}cm")
            self.total_grow = size_grow + self.total_grow
            plant.grow_plant(size_grow)

    def getname(self) -> str:
        return (self.name_garden)

    def getscore(self) -> int:
        return (self.__score_garden)

    def getnamegarden(self) -> str:
        return (self.name_garden)

    def print_all(self) -> None:
        print()
        print(f"=== {self.name_garden} Garden Report ===")
        print("Plants in garden:")
        self.print_all_plants()
        print()
        self.print_stats()
        print("\n")

    @classmethod
    def validation_test(cls) -> None:
        if len(cls.all_plant_bad) == 0:
            print("Height validation test: True")
        else:
            print("Height validation test: False")

    @staticmethod
    def print_text_demo() -> None:
        print("\n=== Garden Management System Demo ===\n")

    def print_stats(self) -> None:
        print(
            f"Plants added: {len(self.all_plants)}, "
            f"Total growth: {self.total_grow}cm")
        print("Plant types: ", end='')
        for plant in self.all_plants:
            print(plant.get_type_and_nbr_plant(), end=', ')

    def print_all_plants(self) -> None:
        for plant in self.all_plants:
            plant.print_data_plant()

    def print_report(self) -> None:
        print()
        print(f"=== {self.name_garden} Garden Report ===")
        print("Plants in garden:")
        self.print_all_plants()
        print()
        self.print_stats()
        print("\n")

    class GardenStats():
        all_garden: list = []

        @classmethod
        def garden_scores(cls) -> None:
            print("Garden scores - ", end='')
            for user in cls.all_garden:
                print(f"{user.getname()}: {user.getscore()}", end=', ')
            print()

        @classmethod
        def total_gardens(cls) -> None:
            print(f"Total gardens managed: {len(cls.all_garden)}")


if __name__ == '__main__':
    oak: Plant = Plant("Oak tree", 100)
    rose: FloweringPlant = FloweringPlant("Rose", 25, "red", "blooming")
    Sunflower: PrizeFlower = PrizeFlower(
        "Sunflower", 50, "yellow", "blooming", 10)
    GardenManager.print_text_demo()
    alice: GardenManager = GardenManager("Alice")
    bob: GardenManager = GardenManager("bob")
    alice.add_plants_garden(oak)
    alice.add_plants_garden(rose)
    alice.add_plants_garden(Sunflower)
    bob.add_plants_garden(Sunflower)
    alice.grow_all_plant(1)
    alice.print_all()
    GardenManager.validation_test()
    GardenManager.GardenStats.garden_scores()
    GardenManager.GardenStats.total_gardens()
