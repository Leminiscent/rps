# RPS

This repository contains a Python-based simulation for playing the Rock Paper Scissors (RPS) game. The game includes different player strategies, including both predefined bots and a dynamic player algorithm that adapts its strategy based on opponent behavior. Additionally, it features a testing module for evaluating the performance of the dynamic player against the bots.

## Files Description

- `RPS_game.py`: Defines the game logic, bot strategies, and the function to play the game between two players.
- `RPS.py`: Contains the implementation of a dynamic player strategy that changes its moves based on the opponent's play history.
- `test_module.py`: Includes unit tests to evaluate the performance of the dynamic player strategy against predefined bots.
- `main.py`: Entry point to play games using the implemented strategies and to run unit tests.

## Strategies

The following bot strategies are implemented:

- **Quincy**: Follows a simple repeated pattern.
- **Mrugesh**: Adapts its moves based on the most frequent move of the opponent in the last ten rounds.
- **Kris**: Counts on the opponent's last move to decide its next move.
- **Abbey**: Uses a more complex strategy that considers the sequence of the opponent's last two moves to predict the next move.

## Usage

To play the game or run the tests, make sure Python is installed on your system. You can run the game simulations or tests directly from the command line.

### Playing Against Bots

To play against a specific bot, you can run the `main.py` file after uncommenting the respective line for the bot you want to play against. You can choose to play interactively by uncommenting the line for playing against a bot interactively.

### Running Unit Tests

To run the unit tests and evaluate the performance of the dynamic player strategy against the bots, uncomment the last line in `main.py` and run the file. The tests will automatically execute, providing feedback on the strategy's success rate against each bot.
