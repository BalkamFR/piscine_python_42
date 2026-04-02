def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_dict: list[dict] = sorted(
        artifacts,
        key=lambda artifacts: artifacts["power"],
        reverse=True)
    return sorted_dict

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filter_dict: list[dict] = list(
        filter(lambda mages: mages["power"] >= min_power, mages))
    return filter_dict

def spell_transformer(spells: list[str]) -> list[str]:
    transformed_spells: list[str] = list(
        map(lambda x: "* " + x + " *", spells))
    return transformed_spells

def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda mages: mages["power"])
    max_power_int: int = max_power["power"]
    min_power = min(mages, key=lambda mages: mages["power"])
    min_power_int: int = min_power["power"]
    all_score = list(map(lambda x: x["power"], mages))
    all_score_total: int = sum(all_score)
    all_score_len: int = len(all_score)
    avg_power = round(all_score_total / all_score_len, 2)
    return {
        "max_power": max_power_int,
        "min_power": min_power_int,
        "avg_power": avg_power}

def main() -> None:
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Stone Shield', 'power': 45, 'type': 'defense'}
    ]
    mages = [
        {'name': 'Alex', 'power': 85, 'element': 'fire'},
        {'name': 'Jordan', 'power': 95, 'element': 'water'},
        {'name': 'Riley', 'power': 70, 'element': 'earth'},
        {'name': 'Morgan', 'power': 60, 'element': 'air'}
    ]
    spells = ['fireball', 'heal', 'shield']
    print("\nTesting artifact sorter..")
    sorted_arts = artifact_sorter(artifacts)
    print(f"{sorted_arts[0]['name']} ({sorted_arts[0]['power']} power) "
          f"comes before {sorted_arts[1]['name']} "
          f"({sorted_arts[1]['power']} power)")
    print("\nTesting power filter (80)")
    print(power_filter(mages, 80))
    print("\nTesting spell transformer....")
    for spell in spell_transformer(spells):
        print(spell, end=' ')
    print("\n\nTesting mage stats...")
    print(mage_stats(mages))

if __name__ == '__main__':
    main()
