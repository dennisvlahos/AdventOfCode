"""
Advent of Code 2022 - Day 4
<https://adventofcode.com/2022/day/4>
"""

import utils

ElfPair = tuple[range, range]


def calculate_full_overlap(pairs: list[ElfPair]) -> list[ElfPair]:
    """
    Calculates the elf pairs whose ranges fully overlap each other.

    Args:
        pairs: The list of elf pairs. Each pair is a tuple of ranges.

    Returns:
        A list of fully overlapping elf pairs.
    """
    results = []
    for pair in pairs:
        left = set(pair[0])
        right = set(pair[1])
        if left.issubset(right) or right.issubset(left):
            results.append(pair)

    return results


def calculate_partial_overlap(pairs: list[ElfPair]) -> list[ElfPair]:
    """
    Calculates the elf pairs whose ranges overlap each other at all.

    Args:
        pairs: The list of elf pairs. Each pair is a tuple of ranges.

    Returns:
        A list of overlapping elf pairs.
    """
    results = []
    for pair in pairs:
        left = set(pair[0])
        right = set(pair[1])
        if not left.isdisjoint(right):
            results.append(pair)

    return results


def process_data() -> list[ElfPair]:
    """
    Reads and processes the puzzle input.

    Returns:
        A list of elf pairs. Each pair is a tuple of ranges.
    """
    data = utils.get_data(__file__)
    pairs = [pair.split(",") for pair in data.splitlines()]

    results = []
    for pair in pairs:
        left_start, left_end = pair[0].split("-")
        right_start, right_end = pair[1].split("-")
        results.append(  # Compensate for range() not being inclusive.
            (
                range(int(left_start), int(left_end) + 1),
                range(int(right_start), int(right_end) + 1),
            )
        )

    return results


def main() -> int:
    """
    Calculates and prints both parts of the puzzle.

    Returns:
        The exit code.
    """
    pairs = process_data()
    print("(A) Fully Overlapping:", len(calculate_full_overlap(pairs)))
    print("(B) Partially Overlapping:", len(calculate_partial_overlap(pairs)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
