"""
Advent of Code 2022 - Day 2
<https://adventofcode.com/2022/day/2>
"""

import enum

import utils

ListOfCommands = list[tuple[str, str]]


class Move(enum.Enum):
    """
    The possible moves in a game of rock paper scissors.
    """

    ROCK = enum.auto()
    PAPER = enum.auto()
    SCISSORS = enum.auto()


class Result(enum.Enum):
    """
    The result of a round of rock paper scissors.
    """

    WIN = enum.auto()
    LOSE = enum.auto()
    DRAW = enum.auto()


def translate(character: str) -> Move:
    """
    Translates a command to actionable moves.

    Args:
        character: A single character command string.

    Returns:
        The matching move.
    """
    return {
        "A": Move.ROCK,
        "X": Move.ROCK,
        "B": Move.PAPER,
        "Y": Move.PAPER,
        "C": Move.SCISSORS,
        "Z": Move.SCISSORS,
    }[character]


def play_round(opponent_move: Move, player_move: Move) -> Result:
    """
    Plays a round of rock paper scissors.

    Args:
        opponent_move: The opponent's move.
        player_move: The player's move.

    Returns:
        The result of the round.
    """
    if opponent_move is player_move:
        return Result.DRAW

    if (
        (opponent_move is Move.ROCK and player_move is Move.PAPER)
        or (opponent_move is Move.PAPER and player_move is Move.SCISSORS)
        or (opponent_move is Move.SCISSORS and player_move is Move.ROCK)
    ):
        return Result.WIN

    return Result.LOSE


def score_round(player_move: Move, result: Result) -> int:
    """
    Scores a round of rock paper scissors.

    Args:
        player_move: The player's move.
        result: The round's result.

    Returns:
        The score this round gives to the player.
    """
    score = 0

    if player_move is Move.ROCK:
        score += 1
    elif player_move is Move.PAPER:
        score += 2
    else:
        score += 3

    if result is Result.WIN:
        score += 6
    elif result is Result.DRAW:
        score += 3

    return score


def action_based_strategy(rounds: ListOfCommands) -> int:
    """
    Plays the tournament assuming that each round in the input is formatted
    according to "opponent_command, player_command".

    Args:
        rounds: The rounds to simulate. Each round is a tuple of two commands.

    Returns:
        The score this strategy gives to the player.
    """
    score = 0
    for rnd in rounds:
        opponent_command = translate(rnd[0])
        player_command = translate(rnd[1])
        result = play_round(opponent_command, player_command)
        score += score_round(player_command, result)

    return score


def result_based_strategy(rounds: ListOfCommands) -> int:
    """
    Plays the tournament assuming that each round in the input is formatted
    according to "opponent_command, required_result".

    Args:
        rounds: The rounds to simulate. Each round is a tuple of two commands.

    Returns:
        The score this strategy gives to the player.
    """
    score = 0
    for rnd in rounds:
        opponent_command = translate(rnd[0])
        required_result = rnd[1]

        if required_result == "Y":  # Draw.
            player_command = opponent_command

        elif required_result == "X":  # Lose.
            if opponent_command is Move.ROCK:
                player_command = Move.SCISSORS
            elif opponent_command is Move.PAPER:
                player_command = Move.ROCK
            else:
                player_command = Move.PAPER

        else:  # Win.
            if opponent_command is Move.ROCK:
                player_command = Move.PAPER
            elif opponent_command is Move.PAPER:
                player_command = Move.SCISSORS
            else:
                player_command = Move.ROCK

        result = play_round(opponent_command, player_command)
        score += score_round(player_command, result)

    return score


def main() -> int:
    """
    Calculates and prints both parts of the puzzle.

    Returns:
        The exit code.
    """
    data = utils.get_data(__file__)
    rounds = [(rnd[0], rnd[2]) for rnd in data.splitlines()]

    print("(A) Score:", action_based_strategy(rounds))
    print("(B) Score:", result_based_strategy(rounds))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
