"""
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""  # noqa: E501
import pytest


def find_vol(heights: list[int], vol: int = 0) -> int:
    """
    Find the volume of water to the left of the first maximum
    """
    if heights and (max_ := max(heights)):
        idx = heights.index(max_)
        vol += sum((max_ - height) for height in heights[:idx])

        if idx != (len(heights) - 1):
            return find_vol(heights[idx + 1 :], vol)

    return vol


def trapping_rain_water(heights: list[int]) -> int:
    """
    Find the amount of water that can be trapped between the bars
    """
    maximum = max(heights)
    max_idx = heights.index(maximum)

    vol_left = find_vol(heights[:max_idx][::-1])
    vol_right = find_vol(heights[max_idx + 1 :])

    return vol_right + vol_left


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([2, 0, 1, 0], 1),
        ([0, 1, 0, 1], 2),
        ([0, 1, 0], 1),
    ],
)
def test_find_vol(test_input, expected):
    assert find_vol(test_input) == expected


# TODO expand test cases
@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
    ],
)
def test_trapping_rain_water(test_input, expected):
    assert trapping_rain_water(test_input) == expected
