"""
https://leetcode.com/problems/product-of-array-except-self/

Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""  # noqa: E501
import pytest


def create_rolling_product(nums: list[int]) -> list[int]:
    last = 1
    rolling_product: list[int] = [last]
    for i in nums[:-1]:
        last *= i
        rolling_product.append(last)

    return rolling_product


def product_of_array_except_self(nums: list[int]):
    forward_rolling_product = create_rolling_product(nums)
    backward_rolling_product = create_rolling_product(nums[::-1])

    output: list[int] = []
    for i in range(len(nums)):
        output.append(forward_rolling_product[i] * backward_rolling_product[-(i + 1)])

    return output


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ],
)
def test_product_of_array_except_self(nums: list[int], expected: list[int]):
    assert product_of_array_except_self(nums) == expected
