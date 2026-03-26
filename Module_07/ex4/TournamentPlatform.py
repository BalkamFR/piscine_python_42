from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.registered_cards = {}
        self.match_history = []

    def register_card(self, card: TournamentCard) -> str:
        card_name_small = card.name.lower()
        name_with_underscores = card_name_small.replace(" ", "_")
        
        number_of_cards = len(self.registered_cards) + 1
        card_id = f"{name_with_underscores}_{number_of_cards:03d}"
        
        self.registered_cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self.registered_cards:
            return {"error": "Card 1 not found"}
        if card2_id not in self.registered_cards:
            return {"error": "Card 2 not found"}

        card1 = self.registered_cards[card1_id]
        card2 = self.registered_cards[card2_id]

        power1 = card1.attack_pwr + card1.defense_pwr
        power2 = card2.attack_pwr + card2.defense_pwr

        if power1 >= power2:
            winner = card1
            winner_id = card1_id
            loser = card2
            loser_id = card2_id
        else:
            winner = card2
            winner_id = card2_id
            loser = card1
            loser_id = card1_id

        winner.update_wins(1)
        loser.update_losses(1)

        match_result = {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }
        
        self.match_history.append(match_result)
        return match_result

    def get_leaderboard(self) -> list:
        all_cards = list(self.registered_cards.values())
        
        def get_score(card_obj):
            return card_obj.calculate_rating()
            
        sorted_cards = sorted(all_cards, key=get_score, reverse=True)
        
        leaderboard_list = []
        for position, card in enumerate(sorted_cards, 1):
            info = f"{position}. {card.name} (Rating: {card.calculate_rating()})"
            leaderboard_list.append(info)
            
        return leaderboard_list

    def generate_tournament_report(self) -> dict:
        total_cards_count = len(self.registered_cards)
        total_matches_count = len(self.match_history)
        
        sum_of_ratings = 0
        for card in self.registered_cards.values():
            sum_of_ratings += card.calculate_rating()
        
        average_rating = 0
        if total_cards_count > 0:
            average_rating = sum_of_ratings / total_cards_count

        return {
            "total_cards": total_cards_count,
            "matches_played": total_matches_count,
            "avg_rating": average_rating,
            "platform_status": "active"
        }