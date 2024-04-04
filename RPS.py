import random


def player(prev_play, opponent_history=[]):
    if not prev_play:
        guess = "R"
    else:
        opponent_history.append(prev_play)

    counter_moves = {"R": "P", "P": "S", "S": "R"}
    if len(opponent_history) > 2:
        if opponent_history[-1] == opponent_history[-2]:
            guess = counter_moves[opponent_history[-1]]
        else:
            most_common = max(set(opponent_history), key=opponent_history.count)
            guess = counter_moves[most_common]
    else:
        guess = random.choice(["R", "P", "S"])

    if len(opponent_history) % 5 == 0:
        guess = random.choice(["R", "P", "S"])

    return guess
