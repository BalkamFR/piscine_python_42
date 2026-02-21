class Plant:

    def __init__(
            self,
            name_plant: str,
            height_plant: int,
            age_plant: int) -> None:

        self.name_plant: str = name_plant
        self.height_plant: int = height_plant
        self.age_plant: int = age_plant
        self.day_plant: int = 1

    def age(self) -> None:
        self.age_plant += 1
        self.day_plant += 1

    def grow(self) -> None:
        self.height_plant += 1

    def get_info(self) -> str:
        return (f"{self.name_plant}: {self.height_plant}cm, {self.age_plant} "
                "days old")

    def print_days(self) -> None:
        print(f"=== Day {self.day_plant} ===")

    def print_data_plant(self) -> None:
        print(f"{self.name_plant}: {self.height_plant}cm, {self.age_plant} "
              "days old")

    def simulator_age(self, age_more: int) -> None:

        self.print_days()
        self.print_data_plant()
        i = 0
        while (i < age_more):
            self.age()
            self.grow()
            i += 1
        self.print_days()
        self.print_data_plant()
        print(f"Growth this week: +{age_more}cm")


if __name__ == '__main__':
    rose: Plant = Plant("rose", 25, 30)
    rose.simulator_age(6)
