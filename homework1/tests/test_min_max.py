import pytest

from homework1.src.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        ("test_file01.txt", (1, 5)),
        ("test_file02.txt", (10, 20)),
        ("test_file03.txt", (0, 1000)),
    ],
)
def test_minimum_maximum(file_name, expected_result):
    actual_result = find_maximum_and_minimum(file_name)
    assert actual_result == expected_result
