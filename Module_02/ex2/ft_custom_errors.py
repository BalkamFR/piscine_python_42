
class GardenError(Exception):
    pass


class PlantError(GardenError):
    @staticmethod
    def verif_plant_age(age: int, name_plant: str) -> None:
        if (age >= 15):
            raise PlantError(f"Caught PlantError: The "
                            f"{name_plant} plant is wilting!")
        else:
            print("Plant is good")



class WaterError(GardenError):
   @staticmethod
   def verif_plant_water(water: int, name_plant: str) -> None:
    if water == 1:
        raise WaterError("Caught WaterError: Not enough water in the tank!")
    else:
        print("Water is good")


def testing_planterror() -> None:
    try:
        PlantError.verif_plant_age(16, "tomato")
    except PlantError as e:
        print(e)



def testing_watererror() -> None:
    try:
        WaterError.verif_plant_water(1, "tomato")
    except WaterError as e:
        print(e)


def catching_all() -> None:
    testing_planterror()
    testing_watererror()


def test_error_types() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    testing_planterror()
    print("\nTesting WaterError...")
    testing_watererror()
    print("\nTesting catching all garden errors...")
    catching_all()
    print("\nAll custom error types work correctly!")

if __name__ == '__main__':
    test_error_types()
