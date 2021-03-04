import pytest

from homework1.src.task02 import check_fibonacci


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ((1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144), True),
        ((0, 1, 1, 3, 4), False),
        ((5, 6, 8, 9), False),
        ((5, 0, 1), False),
        ((0, 0, 0, 0), False),
        ((3, 3, 3, 3, 3), False),
        ((1, 1, 1, 1), False),
    ],
)
def test_fibonacci_sequence(value: int, expected_result: bool):
    actual_result = check_fibonacci(value)

    assert actual_result == expected_result
