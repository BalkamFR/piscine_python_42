from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage_dealt = 0
        self.total_cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        if self.factory is None or self.strategy is None:
            return {"error": "Engine not configured"}

        deck_data = self.factory.create_themed_deck(3)
        hand = deck_data["cards"]
        self.total_cards_created += len(hand)

        battlefield = [self.factory.create_creature()]

        turn_result = self.strategy.execute_turn(hand, battlefield)

        self.turns_simulated += 1
        self.total_damage_dealt += turn_result["damage_dealt"]

        return turn_result

    def get_engine_status(self) -> dict:
        strategy_name = "None"
        if self.strategy is not None:
            strategy_name = self.strategy.get_strategy_name()

        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self.total_damage_dealt,
            "cards_created": self.total_cards_created
        }