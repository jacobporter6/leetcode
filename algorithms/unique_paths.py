"""
https://leetcode.com/problems/unique-paths/

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths
that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""  # noqa: E501
import numpy as np
import pytest


def find_unique_paths(m: int, n: int) -> int:
    """
    f(i, j) = f(i - 1, j) + f(i, j - 1)
    """
    grid = np.array([[0] * m] * n, dtype=int)
    if m > 1:
        grid[0][1] = 1
    if n > 1:
        grid[1][0] = 1

    for i in range(n):
        for j in range(m):
            if i - 1 >= 0:
                grid[i][j] += grid[i - 1][j]
            if j - 1 >= 0:
                grid[i][j] += grid[i][j - 1]

    return grid[n - 1][m - 1]


@pytest.mark.parametrize(
    "m,n,expected",
    [
        (3, 7, 28),
        (3, 2, 3),
        (1, 1, 0),
        (3, 1, 1),
        (1, 3, 1),
    ],
)
def test_find_unique_paths(m: int, n: int, expected: int) -> None:
    assert find_unique_paths(m, n) == expected
