class PlayersAchievements:
    all_players_list: set["PlayersAchievements"] = set()

    def __init__(self, name_user: str) -> None:
        self.name_user = name_user
        self.achievement: set[str] = set()
        self.first_kill: bool = False
        PlayersAchievements.all_players_list.add(self)

    def __repr__(self) -> str:
        return (f"Player {self.name_user} achievements: {self.achievement}")

    def get_name(self) -> str:
        return (self.name_user)

    def add_achievement(self, achievement_add: str) -> None:
        if achievement_add == "first_kill":
            if not self.first_kill:
                self.achievement.add(achievement_add)
                self.first_kill = True
        else:
            self.achievement.add(achievement_add)

    def all_achi(self) -> set[str]:
        return self.achievement

    def add_multi_achievement(self, achievement_add: list[str]) -> None:
        for data in achievement_add:
            self.add_achievement(data)

    @classmethod
    def print_all_players_stats(cls) -> None:
        print("=== Achievement Tracker System ===\n")
        for players in cls.all_players_list:
            print(players)

    @classmethod
    def unique_achievements(cls) -> None:
        print("\n=== Achievement Analytics ===\n")
        result: set[str] = set()
        for players in cls.all_players_list:
            result = result.union(players.achievement)
        print(f"All unique achievements: {result}")
        print(f"Total unique achievements: {len(result)}")

    @classmethod
    def common_achievements(cls) -> None:
        print()
        i: int = 0
        result: set[str] = set()
        for player in cls.all_players_list:
            if i == 0:
                temp = player.all_achi()
            else:
                result = temp.intersection(player.all_achi())
                temp = result
            i += 1
        print(f"Common to all players: {result}")

    @classmethod
    def rare_achievements(cls) -> None:
        result_dict: dict[str, int] = {}
        for player in cls.all_players_list:
            for achievement in player.all_achi():
                if result_dict.get(achievement) is not None:
                    res: int = result_dict[achievement] + 1
                    result_dict.update({achievement: res})
                else:
                    result_dict.update({achievement: 1})
        rare_items: set[str] = set()
        for key, val in result_dict.items():
            if val == 1:
                rare_items.add(key)
        print(f"Rare achievements (1 player): {rare_items}\n")

    @staticmethod
    def dif_2_players(
        players_1: "PlayersAchievements",
        players_2: "PlayersAchievements"
    ) -> None:
        difference_2_players_1 = players_1.all_achi(
        ).difference(players_2.all_achi())
        difference_2_players_2 = players_2.all_achi(
        ).difference(players_1.all_achi())
        common = players_2.all_achi().intersection(players_1.all_achi())
        print(f"{players_1.get_name()} vs"
              f"{players_2.get_name()} common: {common}")
        print(f"{players_1.get_name()} unique: {difference_2_players_1}")
        print(f"{players_2.get_name()} unique: {difference_2_players_2}")


def all_games() -> None:
    bob = PlayersAchievements("bob")
    bob.add_multi_achievement(
        list({"first_kill", "level_10", "boss_slayer", "collector"}))
    charlie = PlayersAchievements("charlie")
    charlie.add_multi_achievement(list({"level_10", "treasure_hunter",
                                        "boss_slayer", "speed_demon",
                                        "perfectionist"}))
    alice = PlayersAchievements("alice")
    alice.add_multi_achievement(
        list({"first_kill", "level_10", "treasure_hunter", "speed_demon"}))
    PlayersAchievements.print_all_players_stats()
    PlayersAchievements.unique_achievements()
    PlayersAchievements.common_achievements()
    PlayersAchievements.rare_achievements()
    PlayersAchievements.dif_2_players(alice, bob)


if __name__ == '__main__':
    all_games()
