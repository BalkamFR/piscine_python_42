from typing import Generator , Iterator
import random
import time

class GameData:
    all_event:list = ['leveled up', 'found treasure', 'killed monster']
    all_players_found_treasure:int = 0
    all_players_killed:int = 0
    all_players_level_up:int = 0

    random.shuffle(all_event)
    all_players:list = [] 
    def __init__(self, players_name:str):
        self.players_name:str = players_name
        self.level:int = 0
        self.event:str = "None"
        GameData.all_players.append(self)

    def __repr__(self):
        return (self.players_name)
    
    def get_players_info(self) -> str:
        return(f"Player {self} ({self.level}) {self.event}")

    def apply_event_players(self, event:str, index:int):
        self.event = event
        if event == 'leveled up':
            self.level += 8
            GameData.all_players_level_up += 1
        if event == 'killed monster':
            self.level += 5
            GameData.all_players_killed += 1
        if event == 'found treasure':
            self.level += 12
            GameData.all_players_found_treasure += 1
        if index <= 3:
            print(f"Event {index}: {self.get_players_info()}")
        random.shuffle(GameData.all_event)
        

    @classmethod
    def generate_events_random(cls):
        nbr_event:int = 1

        while True:
            GameData.all_players[0].apply_event_players(GameData.all_event[0], nbr_event)
            nbr_event += 1
            yield nbr_event
            GameData.all_players[1].apply_event_players(GameData.all_event[1], nbr_event)
            nbr_event += 1
            yield nbr_event
            GameData.all_players[2].apply_event_players(GameData.all_event[2], nbr_event)
            nbr_event += 1
            yield nbr_event

    @staticmethod
    def generate_event():
        i:int = 0
        total_event:int = 1000
        time_start:float = time.time() 
        game = GameData.generate_events_random()
        while i < total_event:
            next(game)
            i += 1
        print("...\n")
        print("=== Stream Analytics ===")
        print(f"Total events processed: {total_event}")
        print(f"High-level players (10+): {GameData.all_players_killed}")
        print(f"Treasure events: {GameData.all_players_found_treasure}")
        print(f"Level-up events: {GameData.all_players_level_up}\n")
        print("Memory usage: Constant (streaming)")
        time_finish = time.time() - time_start
        print(f"Processing time: {time_finish:.3f} secondes")


def create_games() -> None:
    print("=== Game Data Stream Processor ===")
    bob = GameData("bob")
    alice = GameData("alice")
    charlie = GameData("charlie")
    GameData.generate_event()
    

def fibonacci():
    a: int = 0
    b: int = 1
    c: int = 0
    while True:
        yield a
        c = a
        a = a + b
        b = c


def find_nextprime(nb:int) -> int:
    c: int = 1
    res: int = 1
    while (res < nb):
        if (nb % res == 0):
            c += 1
        res += 1
    if (c > 2):
        return (0)
    return (1)


def prime() :
    i: int = 2
    while True:
        if find_nextprime(i) == 1:
            yield i
        i += 1

def generator_demonstration() -> None:
    print("\n=== Generator Demonstration ===")
    i: int = 0
    fibo = fibonacci()
    print("Fibonacci sequence (first 10): ", end='')
    while i < 10:
        print(next(fibo), end='')
        if i != 9:
            print("", end=', ')
        i += 1
    i = 0
    print("\nPrime numbers (first 5): ", end='')
    pri = prime()
    while i < 5:
        print(next(pri), end='')
        if i != 4:
            print("", end=', ')
        i += 1
    print()


def main() -> None:
    create_games()
    generator_demonstration()


if __name__ == '__main__':
    main()
