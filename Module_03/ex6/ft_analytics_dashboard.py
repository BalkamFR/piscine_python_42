class PlayersAnalytics:
    all_players_list: set = set()

    def __init__(
            self,
            name_user: str,
            region_user: str,
            score_player: int,
            active_player: bool,
            achievement: list):
        self.name_user = name_user
        self.regions_players = region_user
        self.score_player = score_player
        self.active_player = active_player
        self.achievement: list = achievement
        PlayersAnalytics.all_players_list.add(self)

    def __repr__(self):
        return (f"{self.name_user}")

    def get_name(self):
        return (f"{self.name_user}")

    def get_score(self):
        return (self.score_player)

    def get_active(self):
        return (self.active_player)
    
    def get_region(self):
        return (self.regions_players)

    def get_achievement(self):
        return (self.achievement)

    @classmethod
    def list_comprehension(cls):
        print("=== List Comprehension Examples ===")
        high_scorers: List = [players.get_name(
        ) for players in cls.all_players_list if players.get_score() >= 2000]
        scores_doubled: List = [
            players.get_score() *
            2 for players in cls.all_players_list]
        active_player: List = [players.get_name(
        ) for players in cls.all_players_list if players.get_active()]
        print(f"High scorers (>2000): {high_scorers}")
        print(f"Scores doubled: {scores_doubled}")
        print(f"Active players: {active_player}")

    @classmethod
    def dict_comprehension(cls):
        print("\n=== Dict Comprehension Examples ===")
        players_score: dict = {players.get_name(): players.get_score(
        ) for players in cls.all_players_list if players.get_active()}
        score_category_high: list = {players.get_score(
        ) for players in cls.all_players_list if players.get_score() >= 2000}
        score_category_medium: list = {players.get_score(
        ) for players in cls.all_players_list if players.get_score() >= 1900 and players.get_score() <= 2200}
        score_category_low: list = {players.get_score(
        ) for players in cls.all_players_list if players.get_score() < 1900}
        all_score: dict = {"high": len(score_category_high), "medium": len(score_category_medium), "low": len(score_category_low)}
        achievement_count:dict = {
            players.get_name(): len(players.get_achievement()) for players in cls.all_players_list if players.get_active()
        }
        print(f"Player scores: {players_score}")
        print(f"Score categories: {all_score}")
        print(f"Achievement counts: {achievement_count}")
    
    @classmethod
    def set_comprehension(cls):
        print("\n=== Set Comprehension Examples ===")
        unique_players:set = {
            unique_players.get_name() for unique_players in cls.all_players_list
        }
        all_achievements:list = [
            achievements for achievements in cls.all_players_list for achievements in achievements.get_achievement()
        ]
        all_achievements_unique:set = {
            achievements for achievements in all_achievements if count_achievements(achievements, all_achievements) == 1
        }
        all_active_region: set = {
            player.get_region() for player in cls.all_players_list if player.get_active()
        }
        print(f"Unique players: {unique_players}")
        print(f"Unique achievements: {all_achievements_unique}")
        print(f"Active regions: {all_active_region}")
    
    @classmethod
    def combined_analysis(cls):
        print("\n=== Combined Analysis ===")
        all_achievements:set = {
            achievements for achievements in cls.all_players_list for achievements in achievements.get_achievement()
        }
        total:float = 0
        for player in cls.all_players_list:
            total = player.get_score() + total
        top_players:PlayersAnalytics
        max_score:int = 0
        
        scores: List = [
            players.get_score() for players in cls.all_players_list]
        
        for players in cls.all_players_list:
            if max(scores) == players.get_score():
                top_players = players
        
        print(f"Total players: {len(cls.all_players_list)}")
        print(f"Total unique achievements: {len(all_achievements)}")
        print(f"Average score: {total / len(cls.all_players_list)}")
        print(f"Top performer: {top_players.get_name()} ({top_players.get_score()} points, {len(top_players.get_achievement())} achievements)")



def count_achievements(name_achi:str, all_achievements:list) -> int:
    i:int = 0
    for data in all_achievements:
        if data == name_achi:
            i += 1
    return i

def all_games() -> None:
    PlayersAnalytics(
        "bob", "east", 1800, True, [
            "first_kill", "found treasure", "found shield"])
    PlayersAnalytics(
        "alice", "north", 2300, True, [
            "found map", "found shield", "boss_slayer", "gold", "badge"])
    PlayersAnalytics(
        "diana", "north", 2050, False, [
            "killed monster", "found bow", "leveled up", "level_10", "trophy", "gold"])
    PlayersAnalytics("charlie",
                     "central",
                     2150,
                     True,
                     ["killed monster",
                      "found treasure",
                      "leveled up",
                      "trophy",
                      "badge",
                      "found bow",
                      "found map"])

    PlayersAnalytics.list_comprehension()
    PlayersAnalytics.dict_comprehension()
    PlayersAnalytics.set_comprehension()
    PlayersAnalytics.combined_analysis()

if __name__ == '__main__':
    print("=== Game Analytics Dashboard ===\n")
    all_games()
