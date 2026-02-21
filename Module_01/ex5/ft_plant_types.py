class Plant:

    def __init__(
            self,
            name_plant: str,
            starting_height_plant: int,
            starting_age_plant: int) -> None:

        res: int = self.set_height(starting_height_plant)
        if (res == 1):
            return
        res = self.set_age(starting_age_plant)
        if (res == 1):
            return
        self.__name_plant: str = name_plant
        self.__type_plant: str = "Not define"

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

    def __repr__(self) -> str:
        return (f"{self.__name_plant} ({self.__class__.__name__}): "
                f"{self.__starting_height_plant}cm,"
                f" {self.__starting_age_plant} day")


class Flower(Plant):

    def __init__(
            self,
            name_plant: str,
            starting_height_plant: int,
            starting_age_plant: int,
            color_plant: str) -> None:

        super().__init__(name_plant, starting_height_plant, starting_age_plant)
        self.bloom("beautifully")
        self.__color: str = color_plant

    def bloom(self, bloom_flower: str) -> None:
        self.__bloom_flower: str = bloom_flower

    def __repr__(self) -> str:
        return (f"{self.get_name()} ({self.__class__.__name__}): "
                f"{self.get_height()}cm,"
                f" {self.get_age()} days,"
                f" {self.__color} color"
                f"\n{self.get_name()} is blooming {self.__bloom_flower}")


class Tree(Plant):

    def __init__(
            self,
            name_plant: str,
            starting_height_plant: int,
            starting_age_plant: int) -> None:
        super().__init__(name_plant, starting_height_plant, starting_age_plant)
        self.__trunk_diameter: float = starting_height_plant / 10
        self.produce_shade(self.__trunk_diameter * 1.55)

    def produce_shade(self, shade_tree: float) -> None:
        self.__produce_shade: str = '%.0f' % shade_tree

    def __repr__(self) -> str:
        return (
            f"{self.get_name()} ({self.__class__.__name__}): "
            f"{self.get_height()}cm, "
            f"{self.get_age()} days, "
            f"{self.__trunk_diameter}cm diameter"
            f"\n{self.get_name()} provide {self.__produce_shade}"
            " square meters of shade")


class Vegetable(Plant):
    def __init__(
            self,
            name_plant: str,
            starting_height_plant: int,
            starting_age_plant: int,
            harves_plant: str,
            nutritional_plant: str) -> None:
        super().__init__(name_plant, starting_height_plant, starting_age_plant)
        self.__harvest_season: str = harves_plant
        self.__nutritional_value: str = nutritional_plant

    def __repr__(self) -> str:
        return (f"{self.get_name()} ({self.__class__.__name__}): "
                f"{self.get_height()}cm,"
                f" {self.get_age()} days,"
                f" {self.__harvest_season} harvest"
                f"\n{self.get_name()} is rich {self.__nutritional_value}")


if __name__ == '__main__':
    print("=== Garden Plant Types ===")
    Rose: Flower = Flower("Rose", 25, 30, "red")
    Tomato: Vegetable = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    Oak: Tree = Tree("Oak", 500, 1825)
    print("")
    print(Rose)
    print("")
    print(Oak)
    print("")
    print(Tomato)
