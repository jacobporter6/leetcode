"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Examples:
nums = [1, 2, 3, 1], expected_output = 4
nums = [2, 7, 9, 3, 1], expected_output = 12
nums = [2, 3, 2], expected = 4   # naive [3, 2, 2] -> 3
nums = [], expected = 0
"""  # noqa: E501
from __future__ import annotations


import pytest


def rob_houses(
    houses: list[int], value: int = 0, combinations: list[int] | None = None
) -> int:
    combinations = combinations or []

    if houses:
        for idx, x in enumerate(houses[: len(houses) // 2 + 1]):
            return rob_houses(houses[idx + 2 :], value + x, combinations)

    else:
        combinations.append(value)

    return max(combinations)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([2, 3, 2], 4),
        ([], 0),
    ],
)
def test_rob_houses(test_input, expected):
    assert rob_houses(test_input) == expected
