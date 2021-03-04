import pytest

from homework1.src.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["values", "expected_result"],
    [
        ((1, 3, -1, -3, 5, 3, 6, 7), 16),
        ((2, 1, 5, 1, 3, 2), 9),
    ],
)
def test_max_subarray_with_length(values, expected_result):
    actual_result = find_maximal_subarray_sum(values, 3)
    assert actual_result == expected_result
