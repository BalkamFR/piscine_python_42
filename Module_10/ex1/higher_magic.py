from collections.abc import Callable

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power: (spell1(target, power), spell2(target, power))

def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda target, power: base_spell(target, power * multiplier)

def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda target, power: (
        spell(target, power)
        if condition(target, power)
        else "Spell fizzled"
    )

def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda target, power: [s(target, power) for s in spells]

def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"

def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def is_strong(target: str, power: int) -> bool:
    if power > 100:
        return True
    return False

def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    res_c = combined("Dragon", 50)
    print(f"Combined spell result: {res_c[0]}, {res_c[1]}")

    print("\nTesting power amplifier...")
    amplified = power_amplifier(fireball, 3)
    print(f"Original: 10, Amplified result: {amplified('Dragon', 10)}")

    print("\nTesting conditional caster...")
    caster = conditional_caster(is_strong, fireball)
    print(f"Power 50: {caster('Troll', 50)}")
    print(f"Power 150: {caster('Troll', 150)}")

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, fireball])
    results = sequence("Orc", 20)
    for r in results:
        print(f"- {r}")


if __name__ == "__main__":
    main()
