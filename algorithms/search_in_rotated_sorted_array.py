"""
https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""  # noqa: E501

import pytest


def unpivot_array(nums: list[int], pivot: int) -> list[int]:
    return nums[pivot:] + nums[:pivot]


def search_in_rotated_sorted_array(nums: list[int], target: int) -> int:
    # get left and right pointers
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2

        # handle quickest case
        if (mid_val := nums[middle]) == target:
            return middle
        elif left == right:
            return -1

        left_val = nums[left]
        right_val = nums[right]

        if left_val < mid_val:
            # left side is sorted
            if left_val <= target < mid_val:
                right = middle - 1
            else:
                left = middle + 1

        else:
            # right side is sorted
            if mid_val < target <= right_val:
                left = middle + 1
            else:
                right = middle - 1

    return -1


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([6, 7, 1, 2, 3, 4, 5], 7, 1),
        ([6, 7, 1, 2, 3, 4, 5], 5, 6),
        ([6, 7, 1, 2, 3, 4, 5], 6, 0),
        ([6, 7, 1, 2, 3, 4], 7, 1),
        ([6, 7, 1, 2, 3, 4], 4, 5),
        ([6, 7, 1, 2, 3, 4], 6, 0),
        ([6, 7, 1, 2, 3, 4], 2, 3),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([5, 6, 7, 8, 0, 1, 2, 4], 3, -1),
        ([6, 7, 8, 0, 1, 2, 4, 5], 3, -1),
        ([1], 0, -1),
    ],
)
def test_search_in_rotated_sorted_array(nums: list[int], target: int, expected: int):
    assert search_in_rotated_sorted_array(nums, target) == expected
