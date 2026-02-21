def plant_valid(plant: str):
    if type(plant) is not str:
        raise ValueError(f"Error: Cannot water {plant} - invalid plant!")
    else:
        print(f"Watering {plant}")


def water_plants(plant_list):
    print("watering system")
    print("Opening watering system")
    try:
        for plant in plant_list:
            plant_valid(plant)
    except ValueError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")


def testing_error():
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!\n")
    print("Testing with error...")
    water_plants(["tomato", None, "carrots"])
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    testing_error()
