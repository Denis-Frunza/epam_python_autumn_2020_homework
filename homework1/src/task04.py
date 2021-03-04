"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    a_plus_b = {}
    for a in A:
        for b in B:
            a_plus_b[a + b] = a_plus_b.get(a + b, 0) + 1

    cnt = 0
    for c in C:
        for d in D:
            cnt += a_plus_b.get(-c - d, 0)
    return cnt
