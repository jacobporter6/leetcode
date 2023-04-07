"""
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"
"""  # noqa: E501

from collections import deque
from typing import Deque

import pytest


def pop_palindrome(string: str) -> str:  # O(N^2)
    # fail fast
    if len(string) < 2:
        return string

    longest_palindrome = ""
    # TODO: Would it be quicker if we started at the centre
    # and worked outwards?
    for i in range(0, len(string) - 1):  # O(N)
        if len(longest_palindrome) > (len(string) - i):
            break

        finder = PalindromeFinder(string, i)
        if len(p := finder.find_palindrome()) > len(longest_palindrome):  # O(N)
            longest_palindrome = p

    return longest_palindrome


class PalindromeFinder:
    def __init__(
        self,
        string: str,
        centre: int,
    ):
        self.string = string
        self.centre = centre

    def find_palindrome(self) -> str:
        longest_palindrome = self.check_even_palindrome()  # O(N)
        if len(p := self.check_odd_palindrome()) > len(longest_palindrome):  # O(N)
            longest_palindrome = p

        return longest_palindrome

    def check_even_palindrome(self) -> str:
        """
        Check for an even length palindrome at string index
        given by centre
        """
        i, j = (-1, 0)  # initial offset
        palindrome: Deque[str] = deque()
        radius = min(len(self.string) - self.centre, self.centre)

        return self._check_palindrome(i, j, palindrome, radius)

    def check_odd_palindrome(self) -> str:
        """
        Check for an odd length palindrome at string index
        given by centre
        """
        i, j = (-1, 1)  # initial offset
        palindrome: Deque[str] = deque([self.string[self.centre]])
        radius = min(len(self.string) - (self.centre + 1), self.centre)

        return self._check_palindrome(i, j, palindrome, radius)

    def _check_palindrome(
        self,
        i: int,
        j: int,
        palindrome: deque,
        radius: int,
    ) -> str:
        for r in range(radius):
            if (left := self.string[self.centre + (i - r)]) == (
                right := self.string[self.centre + (j + r)]
            ):
                palindrome.appendleft(left)
                palindrome.append(right)

            else:
                break

        return "".join(palindrome)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("", ""),
        ("babad", "bab"),  # or "aba"
        ("cbbd", "bb"),
        ("cbbbd", "bbb"),
        ("cbbbc", "cbbbc"),
        ("bananas", "anana"),
        ("banana", "anana"),
        ("anal", "ana"),
        ("hannah", "hannah"),
        ("hannahs", "hannah"),
    ],
)
def test_pop_palindrome(test_input: str, expected: str):
    assert pop_palindrome(test_input) == expected
