from random import randint, shuffle

MIN_PLAYERS = 2
MAX_PLAYERS = 5
INITIAL_STICKS = 3

class Player:
    def __init__(self, name, players_names):
        self.name = name
        self.sticks = INITIAL_STICKS

        self.other_players_sticks = {}
        for player_name in players_names:
            if player_name == name:  continue
            self.other_players_sticks[player_name] = INITIAL_STICKS

    def update_winner_sticks(self, winner_name):
        if self.name == winner_name:
            self.sticks -= 1
        else:
            self.other_players_sticks[winner_name] -= 1

    def can_win(self):
        return self.sticks == 1

    def guess(self, other_players_guesses, at_least_per_player):
        at_least = self.holding + len(self.other_players_sticks) * at_least_per_player

        max_per_other_player = {}
        for player in self.other_players_sticks:
            if player in other_players_guesses:
                max_per_other_player[player] = min(self.other_players_sticks[player], other_players_guesses[player])
            else:
                max_per_other_player[player] = self.other_players_sticks[player]

        at_max = sum(max_per_other_player.values()) + self.holding

        guess_possibilities = list(range(at_least, at_max + 1))
        unused_guesses = [guess for guess in guess_possibilities if guess not in other_players_guesses.values()]
        shuffle(unused_guesses)

        if len(unused_guesses) == 0:
            desperate_guess = max(self.holding, *other_players_guesses.values()) + 1
            print('|= Shh! = All guesses Player {} had are already in use, it is desperately guessing {}'.format(self.name, desperate_guess))
            return desperate_guess
        else:
            return unused_guesses[0]

    def hold(self, at_least):
        self.holding = randint(at_least, self.sticks)
        return self.holding

def __main__():
    players = {}
    players_names = ['João', 'Maria', 'José', 'Marta', 'Juca']
    for player_name in players_names:
        players[player_name] = Player(player_name, players_names)

    winner = None
    round_number = 0

    while winner is None:
        print('=== Starting round #{} === '.format(round_number))
        print('|- Player {} is going to be the first to guess'.format(players_names[0]))

        # cant hold 0 on first round
        at_least_per_player = 1 if round_number == 0 else 0

        round_holds = {}
        for player_name in players_names:
            player = players[player_name]
            round_holds[player_name] = player.hold(at_least_per_player)
        print('|= Shh! = Players are holding: {}, for a total of {}'.format(round_holds, sum(round_holds.values())))

        round_guesses = {}
        round_winner = None
        for player_name in players_names:
            player = players[player_name]
            player_guess = player.guess(round_guesses, at_least_per_player)
            round_guesses[player_name] = player_guess
            if player_guess == sum(round_holds.values()):
                round_winner = player

        print('|- Players have guessed: {}'.format(round_guesses))

        rotate_players_by = 1
        if round_winner is not None:
            if round_winner.can_win():
                winner = round_winner
                print('|- Player {} won the round guessing {}, and won the game'.format(round_winner.name, sum(round_holds.values())))
                print('=== GAME ENDED ===')
            else:
                for player in players.values(): player.update_winner_sticks(round_winner.name)
                print('|- Player {} won the round guessing {}, and has one fewer stick'.format(round_winner.name, sum(round_holds.values())))
                print('|= Shh! = Player {} has {} sticks left'.format(round_winner.name, round_winner.sticks))
                rotate_players_by = players_names.index(round_winner.name)
        else:
            print('|- No players have guessed correctly this round :(')

        # rotates order to be guessed by one, or to the round_winner to be first
        players_names = players_names[rotate_players_by:]+players_names[:rotate_players_by]

        round_number += 1

__main__()
