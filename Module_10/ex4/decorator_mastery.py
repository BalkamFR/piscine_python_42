from collections.abc import Callable
from functools import wraps
from time import time

def spell_timer(func: Callable) -> Callable:
	@wraps(func)
	def wrapper(*args, **kwargs):
		print(f"Casting {func.__name__}...")
		start:float = time()
		spell_res = func(*args, **kwargs)
		end:float = time()
		print(f"Spell completed in {end - start:.3f} seconds")
		return spell_res
	return wrapper

def power_validator(min_power: int) -> Callable:
	def decorator(spells) -> Callable:
		@wraps(spells)
		def wrapper(*args, **kwargs) -> str:
			power = args[1]
			target = args[0]
			if power >= min_power:
				return spells(target, power)
			else:
				return f"Insufficient power for this spell"
		return wrapper
	return decorator

def retry_spell(max_attempts: int) -> Callable:
	pass

class MageGuild:
	@staticmethod
	def validate_mage_name(name: str) -> bool:
		pass
	def cast_spell(self, spell_name: str, power: int) -> str:
		pass

def fireball(target: str, power: int) -> str:
	return f"Fireball hits {target} for {power} damage"

@power_validator(40)
def watter(target: str, power: int) -> str:
	return f"watter hits {target} for {power} damage"

def main() -> None:
	function_fireball = spell_timer(fireball)
	print("Testing spell timer...")
	res = function_fireball("goblin", 20)
	print(f"Result: {res} cast!")
	print("\nTesting retrying spell...")
	print(watter("goblin", 100))

if __name__ == '__main__':
	main()