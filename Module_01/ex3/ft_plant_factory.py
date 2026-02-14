class Garden_Data_Organizer:

    def __init__(
            self,
            name_plant: str,
            starting_height_plant: int,
            starting_age_plant: int):
        self.name_plant: str = name_plant
        self.starting_height_plant: int = starting_height_plant + 0.0
        self.starting_age_plant: int = starting_age_plant
        self.day_plant: int = 1

    def age(self) -> None:
        self.starting_age_plant += 1
        self.day_plant += 1

    def grow(self) -> None:
        self.starting_height_plant += 1

    def get_info(self):
        return (f"{self.name_plant}: {self.starting_height_plant}cm,"
                "{self.starting_age_plant} days old")

    def print_data_plant(self):
        print(f"{self.name_plant}: {self.starting_height_plant}cm, "
              "{self.starting_age_plant} days old")


def add_plant_tab_plants(
        all_plants: list,
        name_plant_add: str,
        height_plant_add: int,
        age_plant_add):
    plant = Garden_Data_Organizer(
        name_plant_add, height_plant_add, age_plant_add)
    print(f"Created: {name_plant_add} ({height_plant_add}cm, {age_plant_add},"
          "days)")
    all_plants.append(plant)


def print_all_plants(all_plants: list):

    i: int = 0
    for plant in all_plants:
        plant.print_data_plant()
        i = +1
    print(f"\n Total plants created: {i}")


if __name__ == '__main__':
    all_plants: list = []
    print("=== Plant Factory Output ===")
    add_plant_tab_plants(all_plants, "Rose", 25, 30)
    add_plant_tab_plants(all_plants, "Oak", 200, 365)
    add_plant_tab_plants(all_plants, "Cactus", 5, 90)
    add_plant_tab_plants(all_plants, "Sunflowe", 80, 45)
    add_plant_tab_plants(all_plants, "Fern", 15, 120)

    print(f"\nTotal plants created: {len(all_plants)}")
    # print_all_plants(all_plants)
