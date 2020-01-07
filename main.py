from random import randint

class Player:
    def __init__(self, idx, start, end, no_of_counters):
        self.IDX = idx
        self.START = start
        self.END = end
        self.current = [0] * no_of_counters
        self.no_of_turns = 0

    def go_to_start(self, counter_idx):
        self.current[counter_idx] = 0
    
    def play_turn(players):
        dice_throw = randint(1,6)
        # Play the turn
            

class Game:
    def __init__(self, no_of_players, length, home_strip, safe_positions, no_of_counters):
        self.NO_OF_PLAYERS = no_of_players
        self.LENGTH = length
        self.HOME_STRIP = home_strip
        self.SAFES = safe_positions
        self.NO_OF_COUNTERS = no_of_counters
        self.players = []
        if (length - home_strip + 1) % no_of_players != 0:
            raise Exception
        if Len(safe_positions) > length:
            raise Exception
        for i in range(0, Len(safe_positions)):
            if safe_positions[i] > length:
                raise Exception

    def initialize_players():
        working_len = self.LENGTH - self.HOME_STRIP + 1
        distance = working_len / self.NO_OF_PLAYERS
        self.players = [Player(i, 1 + (i * distance), ((i * distance) - 1) % working_len)) \
        for i in range(0, self.NO_OF_PLAYERS)]

    def play():
        # Play the game

def main():
    try:
        no_of_runs = int(input('Enter no of game iterations (1): ') or "1")
        no_of_players = int(input('Enter no of players (4): ') or "4")
        length = int(input('Enter length of game, i.e. start to home (57): ') or "57")
        home_strip = int(input('Enter length of home strip (6): ') or "6")
        safe_positions = (input('Enter safe positions (1,9,14,22,27,35,40,48): ') or \
        "1,9,14,22,27,35,40,48").split(",")
        safe_positions = list(map(int, safe_positions)) 
        no_of_counters = int(input('Enter no of counters for each player (4): ') or "4")
        game = Game(no_of_players, length, home_strip, safe_positions, no_of_counters)
    except:
        print('Invalid input.')
    
    players = game.initialize_players()
    run_results = [game.play(players) for i in range(0, no_of_runs)]
    # Output run_results to CSV/Excel file


