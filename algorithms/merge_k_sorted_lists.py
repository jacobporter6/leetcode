"""
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists,
each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""  # noqa: E501
from collections import defaultdict
from typing import DefaultDict

import pytest


def merge_k_lists(lists: list[list[int]]) -> list[int]:
    """
    Merge k sorted lists
    """
    lists = [list_[::-1] for list_ in lists if list_]

    output = []

    merge_queue: DefaultDict[int, list[int]] = defaultdict(list)
    empty_lists: set[int] = set()

    # set initial state
    for idx, list_ in enumerate(lists):
        merge_queue[list_.pop()].append(idx)

    while 1:
        # Get the next smallest value
        if merge_queue:
            smallest = min(merge_queue)
            list_indices: list[int] = merge_queue.pop(smallest)

            output.extend(len(list_indices) * [smallest])

            for idx in list_indices:
                if list_ := lists[idx]:
                    merge_queue[list_.pop()].append(idx)
                else:
                    empty_lists.add(idx)

            # We're done
            if len(empty_lists) == len(lists):
                break
        else:
            break

    return output


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            [
                [1, 4, 5],
                [1, 3, 4],
                [2, 6],
            ],
            [1, 1, 2, 3, 4, 4, 5, 6],
        ),
        (
            [],
            [],
        ),
        (
            [[]],
            [],
        ),
    ],
)
def test_merge_k_lists(test_input, expected):
    assert merge_k_lists(test_input) == expected
