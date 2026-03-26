from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    print("=== DataDeck Game Engine ===\n")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    print("Configuring Fantasy Card Game...")
    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}\n")

    print("Simulating aggressive turn...")
    turn_report = engine.simulate_turn()

    print(f"Turn execution:")
    print(f"Strategy: {turn_report['strategy']}")
    print(f"Actions: {{'cards_played': {turn_report['cards_played']}, "
          f"'mana_used': {turn_report['mana_used']}, "
          f"'targets_attacked': {turn_report['targets_attacked']}, "
          f"'damage_dealt': {turn_report['damage_dealt']}}}\n")

    print("Game Report:")
    print(engine.get_engine_status())

    print("\nAbstract Factory & Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()