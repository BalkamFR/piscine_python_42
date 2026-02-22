def garden_operations(value_select: str) -> None:
    if value_select == "ValueError":
        try:
            int("abc")
        except BaseException:
            print("Caught ValueError: invalid literal for int()")
    if value_select == "ZeroDivisionError":
        try:
            0 % 0
        except BaseException:
            print("Caught ZeroDivisionError: division by zero")
    if value_select == "FileNotFoundError":
        try:
            f = open("missing.txt", "r")
            print(f.read())
            f.close()
        except BaseException:
            print("Caught FileNotFoundError: No such file 'missing.txt'")
    if value_select == "KeyError":
        try:
            plant = {
                "rose": "red",
            }
            print(plant["oak"])
        except BaseException:
            print("Caught KeyError: 'missing_plant'")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    print("\nTesting ValueError...")
    garden_operations("ValueError")
    print("\nTesting ZeroDivisionError...")
    garden_operations("ZeroDivisionError")
    print("\nTesting FileNotFoundError...")
    garden_operations("FileNotFoundError")
    print("\nTesting KeyError...")
    garden_operations("KeyError")
    print("\nTesting multiple errors together..."
          " \nCaught an error, but program continues !")
    print("\nAll error types tested successfully!")

if __name__ == '__main__':
    test_error_types()
