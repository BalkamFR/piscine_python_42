def artifact_sorter(artifacts: list[dict]) -> list[dict]:
	sorted_dict = sorted(artifacts, key=lambda artifact: artifact["power"], reverse=True)
	return sorted_dict

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
	pass

def spell_transformer(spells: list[str]) -> list[str]:
	pass

def mage_stats(mages: list[dict]) -> dict:
	pass

def main() -> None:
	artifacts = [
		{'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
		{'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
		{'name': 'Stone Shield', 'power': 45, 'type': 'defense'}
	]

	print("Testing artifact sorter..")
	
	sorted_artifacts = artifact_sorter(artifacts)
	print(artifacts)
	print(sorted_artifacts)

if __name__ == '__main__':
	main()