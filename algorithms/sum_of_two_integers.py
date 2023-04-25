"""
https://leetcode.com/problems/sum-of-two-integers/

Given two integers a and b, return the sum of the two integers without using the operators + and -.
"""  # noqa: E501
from itertools import zip_longest

import pytest


def convert_to_bits(num: int) -> list[int]:
    bits: list[int] = []
    while num > 0:
        bits.append(num % 2)
        num //= 2

    return bits or [0]


def convert_to_int(bits: list[int]) -> int:
    num = 0
    for bit in bits:
        num = (num << 1) | bit

    return num


def sum_bits(a: list[int], b: list[int]) -> list[int]:
    output: list[int] = []
    carry = 0
    for x, y in zip_longest(a, b, fillvalue=0):
        if (x & y) & carry:
            output.append(1)
        elif (x ^ y) & carry:
            output.append(0)
        elif x & y:
            carry = 1
            output.append(0)
        else:
            output.append(int(x ^ y))

    if carry:
        output.append(carry)

    return output


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([0], [0], [0]),
        ([1], [0], [1]),
        ([0, 1], [1, 0], [1, 1]),
        ([1, 0], [1, 1], [0, 0, 1]),
        ([1, 1, 0], [1, 1, 1], [0, 1, 0, 1]),
    ],
)
def test_sum_bits(a, b, expected):
    assert sum_bits(a, b) == expected


def sum_of_two_integers(a: int, b: int) -> int:
    a_bits = convert_to_bits(a)
    b_bits = convert_to_bits(b)

    summed_bits = sum_bits(a_bits, b_bits)

    return convert_to_int(summed_bits)


@pytest.mark.parametrize(
    "num, expected",
    [
        (0, [0]),
        (1, [1]),
        (2, [0, 1]),
        (3, [1, 1]),
        (4, [0, 0, 1]),
        (5, [1, 0, 1]),
        (6, [0, 1, 1]),
        (7, [1, 1, 1]),
    ],
)
def test_convert_to_bits(num: int, expected: list[int]):
    assert convert_to_bits(num) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (-2, 3, 1),  # doesn't handle
        (2, 3, 5),
        (-5, -8, -13),  # doesn't handle
    ],
)
def test_sum_of_two_integers(a: int, b: int, expected: int):
    assert sum_of_two_integers(a, b) == expected
