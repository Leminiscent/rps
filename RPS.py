import random


def player(prev_play, opponent_history=[]):
    if len(opponent_history) == 0:
        opponent_history.append(prev_play)
        return "R"  # Starting with Rock

    # Count the frequencies of Mrugesh's plays
    play_count = {"R": 0, "P": 0, "S": 0}
    for play in opponent_history:
        if play in play_count:
            play_count[play] += 1

    # Find Mrugesh's least used move and our counter to it
    least_used = min(play_count, key=play_count.get)
    counter_to_least_used = {"R": "P", "P": "S", "S": "R"}

    # Every few moves, switch strategies to keep Mrugesh guessing
    if len(opponent_history) % 5 == 0:
        # Play counter to Mrugesh's least used move, expecting him to use it more
        move = counter_to_least_used[least_used]
    elif len(opponent_history) % 5 == 1:
        # Play counter to Mrugesh's last play directly
        counter_moves = {"R": "P", "P": "S", "S": "R"}
        move = counter_moves[prev_play]
    else:
        # Follow a pattern that's hard for Mrugesh to predict
        pattern = ["R", "S", "P", "P", "S", "R"]
        move = pattern[len(opponent_history) % len(pattern)]

    opponent_history.append(prev_play)
    return move
