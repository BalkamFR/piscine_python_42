def check_temperature(temp_str: int | str) -> None:
    print()
    print(f"Testing temperature: {temp_str}")
    try:
        a = int(temp_str)
        if a >= 0 and a <= 40:
            print(f"Temperature {a}°C is perfect for plants!")
        elif (a < 0):
            print(f"Error: -{a}°C is too cold for plants (min 0°C)")
        elif (a > 40):
            print(f"Error: {a}°C is too hot for plants (max 40°C)")

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    check_temperature(25)
    check_temperature("abc")
    check_temperature(100)
    check_temperature(-50)
    print("\nAll tests completed - program didn't crash!")


if __name__ == '__main__':
    test_temperature_input()
