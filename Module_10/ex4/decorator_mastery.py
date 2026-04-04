from collections.abc import Callable
from functools import wraps
from time import time
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start: float = time()
        spell_res = func(*args, **kwargs)
        end: float = time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return spell_res
    return wrapper


def power_validator(
        min_power: int) -> Callable[[Callable[..., str]], Callable[..., str]]:
    def decorator(spells: Callable[..., str]) -> Callable[..., str]:
        @wraps(spells)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            power = kwargs.get('power', args[-1] if args else 0)
            if power >= min_power:
                return spells(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(
        max_attempts: int) -> Callable[[Callable[..., str]],
                                       Callable[..., str]]:
    def decorator(spells: Callable[..., str]) -> Callable[..., str]:
        @wraps(spells)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            for i in range(max_attempts):
                try:
                    return spells(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... (attempt {
                            i + 1}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not isinstance(name, str) or len(name) < 3:
            return False
        return all(char.isalpha() or char.isspace() for char in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


@power_validator(40)
def watter(target: str, power: int) -> str:
    return f"watter hits {target} for {power} damage"


@retry_spell(max_attempts=3)
def unstable_portal(destination: str) -> str:
    if 0 < 0.7:
        raise RuntimeError("Waaaaaaagh spelled !")
    return f"Portal open in {destination} !"


@retry_spell(max_attempts=3)
def stable_portal(destination: str) -> str:
    return f"Portal open in {destination} !"


def main() -> None:
    function_fireball = spell_timer(fireball)
    print("Testing spell timer...")
    print(function_fireball("goblin", 20))

    print("\nTesting power validator...")
    print(watter("goblin", 100))
    print(watter("orc", 20))

    print("\nTesting retry spell...")
    print(unstable_portal("nether"))
    print(stable_portal("land"))

    print("\nTesting Mage Guild...")
    guild = MageGuild()
    print(
        f"Is 'Mage Gandalf' valid? {
            MageGuild.validate_mage_name('Mage Gandalf')}")
    print(f"Is 'S1' valid? {MageGuild.validate_mage_name('S1')}")
    print(guild.cast_spell("Blizzard", 80))
    print(guild.cast_spell("Spark", 5))


if __name__ == '__main__':
    main()
