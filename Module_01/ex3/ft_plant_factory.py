class Plant:

    def __init__(
            self,
            name_plant: str,
            starting_height_plant: int,
            starting_age_plant: int) -> None:

        self.name_plant: str = name_plant
        self.starting_height_plant: int = starting_height_plant
        self.starting_age_plant: int = starting_age_plant
        self.day_plant: int = 1
        print(
            f"Created: {name_plant} ({starting_height_plant}cm,"
            f"{starting_age_plant}"
            " days)")

    def age(self) -> None:
        self.starting_age_plant += 1
        self.day_plant += 1

    def grow(self) -> None:
        self.starting_height_plant += 1

    def get_info(self) -> str:
        return (f"{self.name_plant}: {self.starting_height_plant}cm,"
                f"{self.starting_age_plant} days old")

    def print_data_plant(self) -> None:
        print(f"{self.name_plant}: {self.starting_height_plant}cm, "
              f"{self.starting_age_plant} days old")


if __name__ == '__main__':
    print("=== Plant Factory Output ===")
    plants_list = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    plant_obj_list = []
    for data in plants_list:
        plant_obj_list.append(Plant(*data))

    print(f"\nTotal plants created: {len(plant_obj_list)}")
