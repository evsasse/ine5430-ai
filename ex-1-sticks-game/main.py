from random import randint

MIN_PLAYERS = 2
MAX_PLAYERS = 5
INITIAL_STICKS = 3

class Player:
    def __init__(self, name, players):
        self.name = name
        self.sticks = INITIAL_STICKS

        self.other_players_sticks = {}
        for player in players:
            if player == name:  continue
            self.other_players_sticks[player] = INITIAL_STICKS

    # def fix_knowledge_winner(self, winner)

    def __guess(self, at_least_per_player):
        at_least = self.holding + len(self.other_players_sticks) * at_least_per_player
        # print("= Player '{}' would guess at least {}, because {}".format(self.name, at_least, [self.holding, len(self.other_players_sticks) * at_least_per_player]))
        return randint(at_least, sum(self.other_players_sticks.values()))

    def guess(self, other_guesses, at_least_per_player = 0):
        to_guess = self.__guess(at_least_per_player)
        while to_guess in other_guesses:
            to_guess = self.__guess(at_least_per_player)
        # print("= Player '{}' is guessing {}, because {}".format(self.name, to_guess, [other_guesses, at_least_per_player]))
        return to_guess

    def hold(self, at_least = 0):
        self.holding = randint(at_least, self.sticks)
        return self.holding

def __main__():
    players = []
    players_names = list(range(0, MAX_PLAYERS))
    for player_name in players_names:
        players.append(Player(player_name, players_names))

    winner = None
    round_number = 0
    # while(winner is None):
    if True:
        print(' === Starting round #{} === '.format(round_number))

        at_least_per_player = 1 if round_number == 0 else 0

        round_holds = [player.hold(at_least_per_player) for player in players]
        print(' = Shh! = Players have holded: {}, for a total of: {}'.format(round_holds, sum(round_holds)))

        round_guesses = []
        for player in players:
            round_guesses.append(player.guess(round_guesses, at_least_per_player))

        print(' = Players have guessed {}'.format(round_guesses))

__main__()
