"""
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

E.g. 1
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]

E.g. 2
Input: l1 = [0], l2 = [0]
Output: [0]

E.g. 3
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""  # noqa: E501

from itertools import zip_longest
import pytest

INPUT_FIXTURE_TYPE = tuple[list[int], ...]


def add_lists(l1: list[int], l2: list[int]) -> list[int]:
    """
    Add two linked lists
    """
    output = []
    carry = 0
    for i, j in zip_longest(l1, l2, fillvalue=0):
        sum_ = i + j + carry
        output.append(sum_ % 10)
        # To be brought into the next sum
        carry = sum_ // 10

    # any remaining carry should be appended before returning
    if carry:
        output.append(carry)

    return output


# JP Interview Bonus: Can this easily be extended to several lists?
def add_several_lists(*lists: list[int]) -> list[int]:
    """
    Add two linked lists
    """
    output = []
    carry = 0
    for xs in zip_longest(*lists, fillvalue=0):
        sum_ = sum(xs, carry)
        output.append(sum_ % 10)
        # To be brought into the next sum
        carry = sum_ // 10

    # any remaining carry should be appended before returning
    if carry:
        output.append(carry)

    return output


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (([2, 4, 3], [5, 6, 4]), [7, 0, 8]),
        (([0], [0]), [0]),
        (([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]), [8, 9, 9, 9, 0, 0, 0, 1]),
    ],
)
def test_add_lists(test_input: INPUT_FIXTURE_TYPE, expected: list[int]):
    assert add_lists(*test_input) == expected


# Bonus tests because this is the natural follow on
@pytest.mark.parametrize(
    "test_input,expected",
    [
        (([2, 4, 3], [5, 6, 4]), [7, 0, 8]),
        (([0], [0]), [0]),
        (([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]), [8, 9, 9, 9, 0, 0, 0, 1]),
        (([3, 4, 3], [7, 1], [0, 4, 0, 2]), [0, 0, 4, 2]),
    ],
)
def test_add_several_lists(test_input: INPUT_FIXTURE_TYPE, expected: list[int]):
    assert add_several_lists(*test_input) == expected
