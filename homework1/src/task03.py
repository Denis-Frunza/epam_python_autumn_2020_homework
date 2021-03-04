"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from pathlib import Path
from typing import Tuple

BASE_DIR = Path("/tmp").resolve(strict=True)
DATA_DIR = Path(BASE_DIR).joinpath(
    "/home/denis/epam_python_autumn_2020_homework/homework1/tests/test_files"
)


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(Path(DATA_DIR).joinpath(file_name)) as f:
        values = [int(record) for record in f]
        return min(values), max(values)
