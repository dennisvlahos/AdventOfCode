"""
Advent of Code 2022 - Day 1
<https://adventofcode.com/2022/day/1>
"""

import utils

ElfExpedition = list[list[str]]


def calculate_elf_calories(elves: ElfExpedition) -> list[int]:
    """
    Calculates the calories that each elf is carrying.

    Args:
        elves: The list of elves. Each elf is a list of calories.

    Returns:
        A list of calorie amounts, one entry per elf.
    """
    return [sum(int(food) for food in elf) for elf in elves]


def calculate_most_calories(elves: ElfExpedition) -> int:
    """
    Calculates the highest amount of calories among the elves.

    Args:
        elves: The list of elves. Each elf is a list of calories.

    Returns:
        The highest calorie amount.
    """
    return max(calculate_elf_calories(elves))


def calculate_top_three_elf_calories(elves: ElfExpedition) -> int:
    """
    Calculates the top three calorie amounts carried by the elves.

    Args:
        elves: The list of elves. Each elf is a list of calories.

    Returns:
        The three highest calorie amounts.
    """
    return sum(sorted(calculate_elf_calories(elves))[-3:])


def main() -> int:
    """
    Calculates and prints both parts of the puzzle.

    Returns:
        The exit code.
    """
    data = utils.get_data(__file__)
    elves = [elf.splitlines() for elf in data.split("\n\n")]

    print("(A) Most calories:", calculate_most_calories(elves))
    print("(B) Top three calories:", calculate_top_three_elf_calories(elves))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
