class PlantError(Exception):

    @staticmethod
    def plant_valid_name(plant: str | None) -> None:
        if type(plant) is not str:
            raise PlantError("Error: Plant name cannot be empty!")
        else:
            print(f"Plant '{plant}' is healthy!")

    @staticmethod
    def plant_valid_water(water: int) -> None:
        if water > 10:
            raise PlantError(
                f"Error: Water level {water} is too high (max 10)")
        else:
            print(f"Plant water level {water}!")

    @staticmethod
    def plant_valid_sunlight(hours: int) -> None:
        if hours < 2:
            raise PlantError(
                f"Error: Sunlight hours {hours} is too low (min 2)")
        else:
            print(f"Sunlight hours is {hours}")


def print_name_plants(plant: str | None) -> None:
    try:
        PlantError.plant_valid_name(plant)
    except PlantError as e:
        print(e)


def water_plant(water: int) -> None:
    try:
        PlantError.plant_valid_water(water)
    except PlantError as e:
        print(e)


def sunlight_plant(sunlight: int) -> None:
    try:
        PlantError.plant_valid_sunlight(sunlight)
    except PlantError as e:
        print(e)


def testing_error() -> None:
    print("Testing good values...")
    print_name_plants("rose")
    print("\nTesting empty plant name...")
    bad_value = None
    print_name_plants(bad_value)
    print("\nTesting bad water level...")
    water_plant(15)
    print("\nTesting bad water level...")
    sunlight_plant(0)


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    testing_error()
    print("\nAll error raising tests completed!")
