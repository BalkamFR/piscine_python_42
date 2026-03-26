from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def test_game_simulation() -> None:
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    print("Configuring Game Engine...")
    engine.configure_engine(factory, strategy)

    print(f"Initial Status: {engine.get_engine_status()}")

    print("\nSimulating 3 turns of aggressive play:")
    for i in range(3):
        print(f"\n--- Turn {i+1} ---")
        result = engine.simulate_turn()
        print(f"Strategy: {result['strategy']}")
        print(f"Cards played: {result['cards_played']}")
        print(f"Damage dealt: {result['damage_dealt']}")

    print("\nFinal Engine Status:")
    status = engine.get_engine_status()
    for key, value in status.items():
        print(f"{key}: {value}")


def main() -> None:
    print("\n=== DataDeck Game Simulation ===\n")
    test_game_simulation()
    print("\nGame simulation with Factory and Strategy patterns successful!")


if __name__ == '__main__':
    main()
