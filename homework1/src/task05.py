"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    max_sum = 0
    window_sum = 0
    window_start = 0
    for window_end, num in enumerate(nums):
        window_sum += num
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[window_start]
            window_start += 1
    return max_sum
