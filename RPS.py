def player(prev_play, opponent_history=[]):
    # Avoid repeating the same move more than twice in the last four plays
    if len(opponent_history) >= 4:
        last_four = opponent_history[-4:]
        if last_four.count(last_four[-1]) > 2:
            return {"R": "P", "P": "S", "S": "R"}[
                last_four[-1]
            ]  # Switch to a counter-move
    else:
        # For the first move, play "Rock"
        if not opponent_history:
            return "R"
        # If there's a tie, switch the move
        if prev_play == opponent_history[-1]:
            return {"R": "P", "P": "S", "S": "R"}[prev_play]

    # Default strategy: counter the last move
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    if prev_play:
        return counter_moves[prev_play]
    return "R"
