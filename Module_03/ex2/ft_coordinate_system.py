import math


class CreatePlayers():
    def __init__(self, name_players: str, pos_players: tuple) -> None:
        self.name_players: str = name_players
        self.pos_players: tuple = pos_players
        print(f"Position created: {pos_players}")

    def split_arg_distance(self, brut: str, position_base: tuple) -> tuple:
        try:
            pos_split: tuple = brut.split(',')
            data_return_tuple: tuple = (
                int(pos_split[0]), int(pos_split[1]), int(pos_split[2]))
            print(f"Parsing coordinates: \"{brut}\"")
            print(f"Parsing coordinates: \"{data_return_tuple}\"")
            self.pos_players: tuple = data_return_tuple
            self.distance_between(position_base)
        except BaseException:
            print(f"Parsing invalid coordinates: \"{brut}\"")
            print("Error parsing coordinates:"
                  "invalid literal for int() with"
                  f"base 10: \"{brut}\"")
            print("Error details - Type: ValueError, Args:"
                  f"(\"invalid literal for int() with base 10: '{brut}'\",)")
            data_return_tuple: tuple = None
        return data_return_tuple

    def print_cord_players(self) -> None:
        print(f"{self.name_players} at x={self.pos_players[0]}, y="
              f"{self.pos_players[1]}, z={self.pos_players[2]}")
        print(
            f"Coordinates: X={self.pos_players[0]}, "
            f"Y={self.pos_players[1]}, "
            f"Z={self.pos_players[2]}"
        )

    def distance_between(self, pos2: tuple) -> None:
        distance: float = math.sqrt((pos2[0] -
                                     self.pos_players[0])**2 +
                                    (pos2[1] -
                                     self.pos_players[1])**2 +
                                    (pos2[2] -
                                     self.pos_players[2])**2)
        print(f"Distance between {pos2} and "
              f"{self.pos_players}:"
              f"{distance:.2f}")


def create_pos(x: int, y: int, z: int) -> tuple:
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        position_created: tuple = (x, y, z)
        return position_created
    else:
        print(f"Parsing invalid coordinates: \"{x},{y},{z}\"")


def main() -> None:
    print("=== Game Coordinate System ===\n")
    position_created: create_pos = create_pos(10, 20, 5)
    position_base: create_pos = create_pos(0, 0, 0)
    if position_created is not None:
        Players = CreatePlayers("Players", position_created)
        Players.distance_between(position_base)
        print()
        Players.split_arg_distance("3,4,0", position_base)
        print()
        Players.split_arg_distance("abc,def,ghi", position_base)
        print()
        Players.print_cord_players()


if __name__ == '__main__':
    main()
