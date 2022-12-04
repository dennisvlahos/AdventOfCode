"""
Advent of Code 2022 - Day 3
<https://adventofcode.com/2022/day/3>
"""

import string

import utils

ListOfItems = list[str]
ListOfRucksacks = list[ListOfItems]


def find_duplicate_items(rucksacks: ListOfRucksacks) -> ListOfItems:
    """
    Finds the duplicate item types in each rucksack.

    Args:
        rucksacks: The list of rucksacks. Each sack is a list of items.

    Returns:
        A list of duplicate item types per rucksack.
    """
    results = []
    for sack in rucksacks:
        compartment_size = int(len(sack) / 2)
        compartment_a = sack[:compartment_size]
        compartment_b = sack[compartment_size:]

        duplicates = set(compartment_a) & set(compartment_b)
        results.extend(list(duplicates))

    return results


def find_group_duplicates(rucksacks: ListOfRucksacks) -> ListOfItems:
    """
    Finds the duplicate item types in each group of elves.

    Args:
        rucksacks: The list of rucksacks. Each sack is a list of items.

    Returns:
        A list of duplicate item types per group.
    """
    amount_of_groups = int(len(rucksacks) / 3)
    results = []

    for view_cursor in range(amount_of_groups):
        view = slice(view_cursor * 3, 3 + view_cursor * 3)
        sack_a, sack_b, sack_c = rucksacks[view]
        duplicates = set(sack_a) & set(sack_b) & set(sack_c)
        results.extend(list(duplicates))

    return results


def calculate_priorities(items: ListOfItems) -> list[int]:
    """
    Calculates the priorities of each item in a list.

    Args:
        items: The list of items.

    Returns:
        The list of priorities, one for each item type.
    """
    ranking = dict(zip(string.ascii_letters, range(1, 53)))

    results = []
    for item in items:
        results.append(ranking[item])

    return results


def main() -> int:
    """
    Calculates and prints both parts of the puzzle.

    Returns:
        The exit code.
    """
    data = utils.get_data(__file__)
    rucksacks = [list(sack) for sack in data.splitlines()]

    duplicates = find_duplicate_items(rucksacks)
    priorities = calculate_priorities(duplicates)
    print("(A) Duplicate priorities:", sum(priorities))

    group_duplicates = find_group_duplicates(rucksacks)
    group_priorities = calculate_priorities(group_duplicates)
    print("(B) Group priorities:", sum(group_priorities))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
