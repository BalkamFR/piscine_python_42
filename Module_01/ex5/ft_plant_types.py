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
        print(f"Plant created: {self.__name_plant}")

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


class Flower(Plant):

    def __init__(
            self,
            name_plant: str,
            starting_height_plant: int,
            starting_age_plant: int,
            color_plant: str) -> None:
        super().__init__(name_plant, starting_height_plant, starting_age_plant)
        self.set_type_plant("Flower")
        self.bloom("Fad")
        self.__color = color_plant

    def bloom(self, bloom_flower: str) -> None:
        self.__bloom_flower = bloom_flower

    def print_data_plant(self) -> None:
        super().print_data_plant()
        print(f"{self.__color} color")
        print(f"{self.get_name()} is blooming {self.__bloom_flower}!")


class Tree(Plant):

    def __init__(
            self,
            name_plant: str,
            starting_height_plant: int,
            starting_age_plant: int) -> None:
        super().__init__(name_plant, starting_height_plant, starting_age_plant)
        self.set_type_plant("Tree")
        self.__trunk_diameter: int = starting_height_plant / 10
        self.produce_shade(self.__trunk_diameter * 1.56)

    def produce_shade(self, shade_tree: int) -> None:
        self.__produce_shade: int = shade_tree

    def print_data_plant(self) -> None:
        super().print_data_plant()
        print(f"{self.__trunk_diameter}cm diameter")
        print(
            f"{self.get_name()} provides {self.__produce_shade} square meters"
            " of shade")


class Vegetable(Plant):
    def __init__(
            self,
            name_plant: str,
            starting_height_plant: int,
            starting_age_plant: int,
            harves_plant: str,
            nutritional_plant: str) -> None:
        super().__init__(name_plant, starting_height_plant, starting_age_plant)
        self.set_type_plant("Vegetable")
        self.__harvest_season: str = harves_plant
        self.__nutritional_value: str = nutritional_plant

    def print_data_plant(self) -> None:
        super().print_data_plant()
        print(f"{self.__harvest_season} harvest")
        print(f"{self.get_name()} is rich in {self.__nutritional_value}")


if __name__ == '__main__':
    print("=== Garden Plant Types ===")
    Rose = Flower("Rose", 25, 30, "red")
    Tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    Oak = Tree("Oak", 500, 1825)
    print("\n")
    Rose.print_data_plant()
    print("\n")
    Oak.print_data_plant()
    print("\n")
    Tomato.print_data_plant()
