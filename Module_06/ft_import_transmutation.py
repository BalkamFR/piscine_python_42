
def methode1() -> None:
    import alchemy.elements
    print("\nMethod 1 - Full module import:")
    print("alchemy.elements.create_fire(): "
          f"{alchemy.elements.create_fire()}")


def methode2() -> None:
    from alchemy import create_water
    print("\nMethod 2 - Specific function import:")
    print(f"create_water(): {create_water()}")


def methode3() -> None:
    from alchemy.potions import healing_potion as heal
    print("\nMethod 3 - Aliased import:")
    print(f"heal(): {heal()}")


def methode4() -> None:
    from alchemy.elements import create_fire, create_water
    from alchemy.potions import strength_potion
    print("\nMethod 4 - Multiple imports:")
    print(f"create_earth(): {create_water()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")


def main() -> None:
    print("\n=== Import Transmutation Mastery ===")
    methode1()
    methode2()
    methode3()
    methode4()
    print("\nAll import transmutation methods mastered!")


if __name__ == '__main__':
    main()
