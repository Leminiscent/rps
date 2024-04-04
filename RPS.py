import random


def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    # Since Mrugesh counters the most frequent move in the last ten,
    # we can try to manipulate what he perceives as most frequent.
    # This block sets up a pattern to feed into Mrugesh's logic.
    if len(opponent_history) <= 10:
        # Start with a sequence that doesn't reveal a clear pattern
        pattern = ["R", "P", "S", "S", "P", "R", "R", "S", "P", "S"]
        return pattern[len(opponent_history) - 1]
    else:
        # After the initial sequence, predict Mrugesh's move based on our own last play
        last_ten = opponent_history[
            -11:-1
        ]  # Exclude the very last play to adjust for the append at the start
        most_frequent = max(set(last_ten), key=last_ten.count)

        # Counter Mrugesh's predicted move
        ideal_response = {"P": "S", "R": "P", "S": "R"}
        # However, to avoid being predictable, vary the response slightly
        if len(opponent_history) % 3 == 0:
            return ideal_response[most_frequent]
        elif len(opponent_history) % 3 == 1:
            return (
                most_frequent  # Play what Mrugesh expects to counter, adding confusion
            )
        else:
            # Randomize the third option to avoid detectable patterns
            return random.choice(["R", "P", "S"])
