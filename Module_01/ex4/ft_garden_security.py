class Garden_Security:

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
        print(f"Plant created: {self.__name_plant}")

    def set_height(self, height_update: int) -> int:

        if (height_update < 0):
            self.__starting_height_plant = -1
            print(f"Invalid operation attempted: height {height_update}"
                  "cm [REJECTED]")
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

    def get_height(self):
        return (self.__starting_height_plant)

    def get_age(self):
        return (self.__starting_age_plant)

    def get_info(self):
        return (f"Current plant: {self.__name_plant} ({self.get_height()}cm, "
                "{self.get_age()} days)")

    def print_data_plant(self):
        if (self.__starting_height_plant == -
                1 or self.__starting_age_plant == -1):
            print("Plant is not define")
            return
        else:
            print(self.get_info())


if __name__ == '__main__':
    print("=== Garden Security System ===")
    rose = Garden_Security("Rose", 0, -10)
    rose.print_data_plant()

    tulipe = Garden_Security("tulipe", 29, 20)
    tulipe.print_data_plant()
