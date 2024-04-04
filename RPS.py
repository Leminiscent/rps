import random


def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    # Counter moves map
    counter_moves = {"R": "P", "P": "S", "S": "R"}

    # Strategy for Quincy: Directly counter the pattern
    if len(opponent_history) <= 5:
        # Pattern is R, R, P, P, S - directly counter it
        return ["P", "P", "S", "S", "R"][len(opponent_history) % 5]

    # Strategy for opponents with detectable patterns
    if len(opponent_history) > 2:
        # Attempt to predict the next move based on history
        guess = counter_moves[opponent_history[-1]]

        # Adjust strategy if a pattern is detected
        last_two = "".join(opponent_history[-2:])
        if last_two in ["RR", "PP", "SS"]:  # Opponent might be playing a sequence
            guess = counter_moves[guess]  # Counter the counter-move
    else:
        guess = random.choice(["R", "P", "S"])  # Fallback to random choice

    return guess
