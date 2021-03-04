import pytest

from homework1.src.task04 import check_sum_of_four


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (((1, 2), (-2, -1), (-1, 2), (0, 2)), 2),
    ],
)
def test__sum_of_four(value, expected_result):
    actual_result = check_sum_of_four(*value)
    assert actual_result == expected_result
