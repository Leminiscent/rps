import random


def player(prev_play, opponent_history=[], my_history=[]):
    if not prev_play:
        guess = "R"
    else:
        opponent_history.append(prev_play)

    counter_moves = {"R": "P", "P": "S", "S": "R"}

    # Quincy strategy counter: if the opponent follows a fixed pattern
    if (
        len(set(opponent_history[-5:])) <= 2
    ):  # If the opponent is repeating or following a simple pattern
        guess = counter_moves[prev_play]
    else:
        # For Abbey and Kris: Use a more complex pattern recognition and prediction
        if len(my_history) > 2:
            # Analyzing my own last two moves to predict what Abbey might expect
            last_two_me = my_history[-2:]
            if last_two_me.count(last_two_me[0]) == 2:
                guess = counter_moves[counter_moves[last_two_me[0]]]
            else:
                guess = counter_moves[random.choice(["R", "P", "S"])]
        else:
            guess = random.choice(["R", "P", "S"])

        # For Mrugesh: Countering the frequency strategy by analyzing opponent's history
        if opponent_history:
            most_common = max(set(opponent_history), key=opponent_history.count)
            guess = counter_moves[most_common]

    my_history.append(guess)
    return guess
