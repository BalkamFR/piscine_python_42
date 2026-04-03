from collections.abc import Callable

def mage_counter() -> Callable:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total: int = initial_power

    def accumulator(add) -> int:
        nonlocal total
        total = total + add
        return total
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(target: str) -> str:
        return f"{enchantment_type} {target}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    storage: dict[str, any] = {}

    def store_value(key: str, value: any) -> None:
        print(f"Store '{key}' = {value}")
        storage[key] = value

    def recall_value(key: str) -> None:
        if key in storage:
            print(f"Recall '{key}': {storage[key]}")
        else:
            print(f"Recall '{key}': Memory not found")
    return {"store": store_value, "retrieve": recall_value}


def main() -> None:
    counter_a = mage_counter()
    counter_b = mage_counter()
    print("Testing mage counter...")
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_a call 1: {counter_b()}")

    base_100 = spell_accumulator(100)
    print("\nTesting spell accumulator...")
    print(f"Base 100, add 20: {base_100(20)}")
    print(f"Base 100, add 30: {base_100(30)}")

    fire = enchantment_factory("Fire")
    ice = enchantment_factory("Ice")
    print("\nTesting enchantment factory...")
    print(f"Result: {fire('Sword')}")
    print(f"Result: {ice('Shield')}")

    print("\nTesting memory vault...")
    all_key = memory_vault()
    all_key["store"]("secret", 42)
    all_key["retrieve"]("secret")
    all_key["retrieve"]("unknown")


if __name__ == '__main__':
    main()
