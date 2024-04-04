def player(prev_play, opponent_history=[]):
    # Incrementally build a strategy that appears predictable but shifts before Mrugesh adapts
    if not opponent_history:
        # Initial move
        return "R"
    if len(opponent_history) < 3:
        # Start with a sequence that suggests a leaning towards "Rock"
        return "P"  # Countering Mrugesh's expected "Rock" response
    if len(opponent_history) < 6:
        # Shift to a sequence suggesting a preference for "Paper" next
        return "S"  # Countering the expected "Paper" response
    if len(opponent_history) < 9:
        # Suggest a new preference for "Scissors"
        return "R"  # Countering the expected "Scissors" response

    # After presenting initial patterns, switch to a more complex strategy:
    last_ten = opponent_history[-10:]
    # Counter the most frequent in the last 10, assuming Mrugesh will predict our "most frequent" pattern
    move_counts = {
        "R": last_ten.count("R"),
        "P": last_ten.count("P"),
        "S": last_ten.count("S"),
    }
    most_frequent = max(move_counts, key=move_counts.get)

    # Anticipate Mrugesh's counter strategy and counter that
    if most_frequent == "R":
        return "P"  # Expecting Mrugesh to counter with "Paper", we play "Scissors"
    elif most_frequent == "P":
        return "S"  # Expecting "Scissors", we play "Rock"
    elif most_frequent == "S":
        return "R"  # Expecting "Rock", we play "Paper"

    # Default to "Rock" if all else fails
    return "R"
