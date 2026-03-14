def create_fire() -> None:
    try:
        from alchemy.elements import create_fire
        fire = create_fire()
        print(f"alchemy.elements.create_fire(): {fire}")

    except BaseException:
        print("alchemy.create_fire(): AttributeError - not exposed")


def create_water() -> None:
    try:
        from alchemy.elements import create_water
        fire = create_water()
        print(f"alchemy.elements.create_water(): {fire}")

    except BaseException:
        print("alchemy.create_water(): AttributeError - not exposed")


def create_earth() -> None:
    try:
        from alchemy.elements import create_earth
        fire = create_earth()
        print(f"alchemy.elements.create_earth(): {fire}")

    except BaseException:
        print("alchemy.create_earth(): AttributeError - not exposed")


def create_air() -> None:
    try:
        from alchemy.elements import create_air
        fire = create_air()
        print(f"alchemy.elements.create_air(): {fire}")

    except Exception:
        print(f"alchemy.create_air(): AttributeError - not exposed")


def test_all() -> None:
    import alchemy
    print("\nTesting package-level access (controlled by __init__.py):")
    try:
        print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    except BaseException:
        print("alchemy.create_fire(): AttributeError - not exposed")
    try:
        print(f"alchemy.create_water(): {alchemy.create_water()}")
    except BaseException:
        print("alchemy.create_water(): AttributeError - not exposed")
    try:
        print(f"alchemy.create_earth(): {alchemy.create_earth()}")
    except BaseException:
        print("alchemy.create_earth(): AttributeError - not exposed")
    try:
        print(f"alchemy.create_air(): {alchemy.create_air()}")
    except BaseException:
        print("alchemy.create_air(): AttributeError - not exposed")
    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


def main() -> None:
    print("\n=== Sacred Scroll Mastery ===\n")
    create_fire()
    create_water()
    create_earth()
    create_air()
    test_all()


if __name__ == '__main__':
    main()
