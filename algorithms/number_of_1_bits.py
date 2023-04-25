"""
https://leetcode.com/problems/number-of-1-bits/

Write a function that takes the binary representation of an unsigned integer 
and returns the number of '1' bits it has (also known as the Hamming weight).
"""  # noqa: E501
import pytest


def number_of_1_bits(n_string: str) -> int:
    counter = 0
    n = int(n_string, 2)
    while n > 0:
        counter += n % 2
        n >>= 1

    return counter


@pytest.mark.parametrize(
    "n, expected",
    [
        ("00000000000000000000000000001011", 3),
        ("00000000000000000000000010000000", 1),
        ("11111111111111111111111111111101", 31),
        ("0000000", 0),
    ],
)
def test_number_of_1_bits(n: str, expected: int) -> None:
    assert number_of_1_bits(n) == expected
