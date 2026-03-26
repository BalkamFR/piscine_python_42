from typing import Any
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card


class GameEngine:
    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.turns_simulated: int = 0
        self.total_damage_dealt: int = 0
        self.total_cards_created: int = 0

    def configure_engine(
        self,
        factory: CardFactory,
        strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict[str, Any]:
        if self.factory is None or self.strategy is None:
            return {"error": "Engine not configured"}

        deck_data: dict[str, Any] = self.factory.create_themed_deck(3)
        hand: list[Card] = deck_data["cards"]
        self.total_cards_created += len(hand)

        battlefield: list[Card] = [self.factory.create_creature()]

        turn_result: dict[str, Any] = self.strategy.execute_turn(
            hand, battlefield
        )

        self.turns_simulated += 1
        self.total_damage_dealt += int(turn_result["damage_dealt"])

        return turn_result

    def get_engine_status(self) -> dict[str, Any]:
        strategy_name: str = "None"
        if self.strategy is not None:
            strategy_name = self.strategy.get_strategy_name()

        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self.total_damage_dealt,
            "cards_created": self.total_cards_created
        }
