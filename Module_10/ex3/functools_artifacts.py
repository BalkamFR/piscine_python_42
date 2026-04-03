from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if spells is None or len(spells) == 0:
        return 0
    if operation == "add":
        add = reduce(lambda x, y: x + y, spells)
        return add
    if operation == "multiply":
        mul = reduce(lambda x, y: x * y, spells)
        return mul
    if operation == "max":
        max_value = max(spells)
        return max_value
    if operation == "min":
        min_value = min(spells)
        return min_value
    print(f"Please add good operation ({operation} is not good)")
    return 0


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"Power {power}, Element: {element}, Target: {target}"


def partial_enchanter(base_func: Callable) -> dict[str, Callable]:
    return {
        "Fire": partial(base_func, power=50, element="Fire"),
        "Ice": partial(base_func, power=50, element="Ice"),
        "Lightning": partial(base_func, power=50, element="Lightning")
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatcher(arg: Any) -> str:
        return "Unknown magic type"

    @dispatcher.register(int)
    def _(arg: int) -> str:
        return (f"Damage spell: {arg} damage")

    @dispatcher.register(str)
    def _(arg: str) -> str:
        return (f"Enchantment: {arg}")

    @dispatcher.register(list)
    def _(arg: list) -> str:
        return (f"Multi-cast: {len(arg)} spells")
    return dispatcher


def main() -> None:
    list_nbr: list[int] = [2, 6, 10, 2000, -2, 212, 312]
    print("Testing spell reducer...")
    print(f"list nbr is {list_nbr}")
    print("min =", spell_reducer(list_nbr, "min"))
    print("max =", spell_reducer(list_nbr, "max"))
    print("add =", spell_reducer(list_nbr, "add"))
    print("multiply =", spell_reducer(list_nbr, "multiply"))

    print("\nTesting partial enchanter...")
    factory = partial_enchanter(base_enchantment)
    print(factory["Fire"](target="Orc"))
    print(factory["Ice"](target="Goblin"))

    print("\nMemoized Fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(55): {memoized_fibonacci(55)}")
    print(f"Fib(610): {memoized_fibonacci(610)}")

    print("\nTesting spell dispatcher...")
    spell = spell_dispatcher()
    print(spell(42))
    print(spell("fireball"))
    print(spell(["fireball", "waterball", "fireball"]))
    print(spell({"test": "s"}))


if __name__ == '__main__':
    main()
