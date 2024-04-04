def player(prev_play, opponent_history=[]):
    # Quincy's pattern: "R", "R", "P", "P", "S"
    # Ideal responses: "P", "P", "S", "S", "R"

    # Append the opponent's last play to the history
    opponent_history.append(prev_play)

    # The length of the pattern before it repeats
    pattern_length = 5
    # Map Quincy's plays to our counter plays
    counter_moves = {"R": "P", "P": "S", "S": "R"}

    # Determine our move based on Quincy's pattern
    if len(opponent_history) > 0:
        # Find Quincy's last play's position in the pattern
        last_move_index = (len(opponent_history) - 1) % pattern_length
        # Predict Quincy's next move in the sequence
        predicted_next_move = ["R", "R", "P", "P", "S"][last_move_index]
        # Select the ideal response to Quincy's predicted next move
        guess = counter_moves[predicted_next_move]
    else:
        # Default guess for the first move
        guess = "P"

    return guess
