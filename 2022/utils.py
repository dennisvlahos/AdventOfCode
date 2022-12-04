"""
Advent of Code 2022 - Helper Functions
"""

import pathlib


def get_data(path: pathlib.Path | str) -> str:
    """
    Reads and returns the puzzle input from a file.

    Args:
        path: The path of the calling module.

    Returns:
        The text data from the input.
    """
    data_filename = pathlib.Path(path).name.replace(".py", ".txt")
    data_path = pathlib.Path(path).parent / "data" / data_filename

    with open(data_path, mode="rt", encoding="utf-8") as file:
        return file.read()
