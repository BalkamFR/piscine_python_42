from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        targets_order = []
        for target in available_targets:
            if target == "Enemy Player":
                targets_order.insert(0, target)
            else:
                targets_order.append(target)
        return targets_order

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        combat_cards = []
        for card in hand:
            if card.type in ["Creature", "Elite", "Spell"]:
                combat_cards.append(card)

        combat_cards.sort(key=lambda card_obj: card_obj.cost)

        played_cards = []
        mana_spent = 0
        turn_damage = 0

        for card in combat_cards:
            played_cards.append(card.name)
            mana_spent += card.cost
            if card.type == "Spell":
                turn_damage += card.cost

        for unit in battlefield:
            if hasattr(unit, "attack"):
                turn_damage += unit.attack
            elif hasattr(unit, "attack_power"):
                turn_damage += unit.attack_power

        available_targets = ["Enemy Player", "Enemy Creature"]
        priorities = self.prioritize_targets(available_targets)

        return {
            "strategy": self.get_strategy_name(),
            "cards_played": played_cards,
            "mana_used": mana_spent,
            "targets_attacked": [priorities[0]],
            "damage_dealt": turn_damage
        }