"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""  # noqa: E501
import pytest


def climbing_stairs(n: int) -> int:
    """
    Climbing stairs
    """
    ni, nj = 0, 1
    for _ in range(n):
        n = ni + nj
        ni = nj
        nj = n

    return n


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
    ],
)
def test_climbing_stairs(test_input, expected):
    assert climbing_stairs(test_input) == expected
