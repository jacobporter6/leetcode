"""
https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins
of different denominations and an integer amount
representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any
combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""  # noqa: E501
from collections import deque
from typing import Deque
import pytest


def get_coin_number(
    coins: list[int], amount: int, nodes: set[int] | None = None
) -> int:
    """
    Target: 11
    Coins: [1, 2, 5]

    Let f(n) be the minimum number of coins required to make up amount n

    Therefore,
    f(11) = min(f([11 - 1] = 10), f([11 - 2] = 9), f([11 - 5] = 6)) + 1

    f(10) = min(f([10 - 2] = 8), f([10 - 5] = 5)) + 1
    f(9) = min(f(4), f(7)) + 1
    f(6) = min(f(1)) + 1
    """
    # Keep track of previously calculated values
    solns: list[int] = [amount + 1] * (amount + 1)

    # f(0) = 0
    solns[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                solns[i] = min(solns[i], solns[i - coin] + 1)

    return solns[amount] if (solns[amount] <= amount) else -1


def old_get_coin_number(coins_: list[int], amount: int) -> int:
    """
    Get number of coins required from array to make up amount
    """
    # I know that in terms of box stacking algorithms you should start biggest
    # and work to smallest, so as a first try I would reverse sort my list
    # and attempt to fill using largest coins to smallest
    coins: Deque[int] = deque(sorted(coins_, reverse=True))

    def _get_coin_number(coins: Deque[int], amount: int) -> int:
        count = 0
        sum_ = 0

        for coin in coins:
            while 1:
                if sum_ == amount:
                    return count

                if (new_sum := sum_ + coin) <= amount:
                    sum_ = new_sum
                    count += 1

                else:
                    break

        return -1

    while len(coins) > 0:
        if (coin_number := _get_coin_number(coins, amount)) == -1:
            coins.popleft()

        else:
            return coin_number

    return -1


@pytest.mark.parametrize(
    "test_input,amount,expected",
    [
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
        ([3, 5], 6, 2),
    ],
)
def test_get_coin_number(
    test_input: list[int],
    amount: int,
    expected: int,
):
    assert get_coin_number(test_input, amount) == expected
