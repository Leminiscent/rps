import random


def player(prev_play, opponent_history=[], my_history=[]):
    opponent_history.append(prev_play)
    # Adjust the strategy based on the full history rather than just the last ten plays
    if len(opponent_history) > 10:
        # Calculate the frequency of each move in the opponent's last 10 plays
        last_ten = opponent_history[-10:]
        move_frequencies = {
            "R": last_ten.count("R"),
            "P": last_ten.count("P"),
            "S": last_ten.count("S"),
        }

        # Predict Mrugesh's next move based on the most frequent move we played
        most_frequent_move = max(move_frequencies, key=move_frequencies.get)
        ideal_response = {"P": "S", "R": "P", "S": "R"}
        prediction = ideal_response[most_frequent_move]

        # Introduce variability in our play to confuse Mrugesh
        if random.random() < 0.5:
            # 50% of the time, counter the predicted move
            next_play = prediction
        else:
            # The other 50%, play the same as Mrugesh's predicted move to disrupt the pattern
            next_play = most_frequent_move
    else:
        # Early in the game, play randomly to avoid establishing a clear pattern
        next_play = random.choice(["R", "P", "S"])

    my_history.append(next_play)  # Keep track of our own plays (optional, for analysis)
    return next_play
