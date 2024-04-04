import random


def player(prev_play, opponent_history=[], my_history=[]):
    # Initialize counter moves map
    counter_moves = {"R": "P", "P": "S", "S": "R"}

    # Handle the first move or when prev_play is empty
    if not prev_play:
        guess = "R"  # Choosing "R" as a default first move
    else:
        opponent_history.append(prev_play)

        # Quincy strategy counter: if the opponent follows a fixed pattern
        if (
            len(set(opponent_history[-5:])) <= 2
        ):  # Detecting repetition or simple pattern
            guess = counter_moves[prev_play]
        else:
            # Dynamic strategy for Abbey and Kris based on more complex pattern recognition
            if len(my_history) > 2:
                last_two_me = my_history[-2:]
                if last_two_me[0] == last_two_me[1]:
                    guess = counter_moves[
                        counter_moves[last_two_me[0]]
                    ]  # Counter the counter-move
                else:
                    guess = counter_moves[
                        random.choice(["R", "P", "S"])
                    ]  # Adding randomness
            else:
                guess = random.choice(["R", "P", "S"])

            # Strategy against Mrugesh: Analyzing opponent's most common move
            if opponent_history:
                most_common = max(set(opponent_history), key=opponent_history.count)
                guess = counter_moves[most_common]

    my_history.append(guess)
    return guess
