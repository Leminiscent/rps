import random


def player(prev_play, opponent_history=[]):
    # Increment the opponent's history with the previous play.
    opponent_history.append(prev_play)

    # Define the ideal response based on Mrugesh's likely action.
    ideal_response = {"P": "S", "R": "P", "S": "R"}

    # For the initial moves, cycle through the responses to avoid a clear pattern.
    if len(opponent_history) < 3:
        return ["P", "S", "R"][len(opponent_history)]

    # Analyze the last few moves to determine Mrugesh's most likely counter.
    last_few = opponent_history[-10:]
    if last_few.count("R") > last_few.count("P") and last_few.count(
        "R"
    ) > last_few.count("S"):
        most_likely = "R"
    elif last_few.count("P") > last_few.count("S"):
        most_likely = "P"
    else:
        most_likely = "S"

    # Counter Mrugesh's anticipated next move based on our most frequent recent move.
    response = ideal_response[most_likely]

    # Introduce a slight unpredictability in our play.
    if len(opponent_history) % 5 == 0:
        # Occasionally throw in a move that doesn't follow the pattern to confuse Mrugesh.
        return random.choice(["R", "P", "S"])
    else:
        return response
