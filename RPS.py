import random


def player(prev_play, opponent_history=[]):
    if prev_play == "":
        return random.choice(["R", "P", "S"])
    else:
        opponent_history.append(prev_play)

    counter_moves = {"R": "P", "P": "S", "S": "R"}

    if len(opponent_history) <= 5:
        return ["P", "P", "S", "S", "R"][len(opponent_history) % 5]

    if len(opponent_history) > 2:
        guess = counter_moves[opponent_history[-1]]

        last_two = "".join(opponent_history[-2:])
        if last_two in ["RR", "PP", "SS"]:
            guess = counter_moves[guess]
    else:
        guess = random.choice(["R", "P", "S"])

    return guess
