"""
https://leetcode.com/problems/wildcard-matching/

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).
"""  # noqa: E501
import pytest


def wildcard_matching(string: str, pattern: str) -> bool:
    # string can be made none by match
    new_string: str | None = None

    # split into discrete chunks bounded by wildcards
    patterns = pattern.split("*")

    burn = False
    for idx, pattern in enumerate(patterns):
        if pattern == "":
            burn = True
            continue

        if (new_string := match(string, pattern, burn)) is not None:
            string = new_string
            burn = idx != (len(patterns) - 1)
        else:
            return False

    return (string and burn) or (not string)


def match(string: str, pattern: str, burn: bool = False) -> str | None:
    """
    Match the start of string to pattern
    and return the remainder of string

    If burn is True, then drop letters from string
    until we find a match

    If no match is found, return None
    """
    # What to do if wildcard
    if not pattern:
        return string

    while len(string):
        if len((new_string := string.removeprefix(pattern))) != len(string):
            return new_string
        elif burn:
            string = string[1:]
        else:
            return None

    return None


@pytest.mark.parametrize(
    "test_input, pattern, expected",
    [
        ("aa", "?a", True),
        ("aa", "a?", True),
        ("aa", "a", False),
        ("aa", "*", True),
        ("cb", "?a", False),
        ("adceb", "*a*b", True),
        ("adceb", "*a*?", True),
        ("adceb", "*a?*b", True),
        ("adceb", "a???b*", True),
        ("acdcb", "a*c?b", False),
        ("", "", True),
        ("", "*", True),
        ("", "?", False),
        ("", "a", False),
        ("", "a*", False),
        ("", "a?", False),
        ("", "a*b", False),
        ("", "a*b?", False),
    ],
)
def test_wildcard_matching(test_input: str, pattern: str, expected: bool):
    assert wildcard_matching(test_input, pattern) == expected
