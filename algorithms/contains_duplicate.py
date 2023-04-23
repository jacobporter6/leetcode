"""
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""  # noqa: E501
import pytest


def contains_duplicate(nums: list[int]) -> bool:
    sorted_nums = sorted(nums)

    previous = None
    for current in sorted_nums:
        if previous == current:
            return True
        previous = current

    return False


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ],
)
def test_contains_duplicate(nums: list[int], expected: bool) -> None:
    assert contains_duplicate(nums) == expected
