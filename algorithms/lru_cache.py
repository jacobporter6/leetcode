# https://leetcode.com/problems/lru-cache/

# Design a data structure that follows the
# constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

#    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#    int get(int key) Return the value of the key if the key exists, otherwise return -1.
#    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

# The functions get and put must each run in O(1) average time complexity.
from collections import UserDict
from dataclasses import dataclass

@dataclass
class Node:
    prev: str | None
    next_: str | None
    value: int


class LRUCache(UserDict):
    def __init__(
        self,
        capacity: int,
    ):
        super().__init__()
        self.capacity = capacity

        self.head: str = ""
        self.tail: str = ""


    def _update_head(self, key: str) -> None:
        if (head_node := self.super_get(self.head)) is not None:
            head_node.prev = key
        if not self.tail:
            self.tail = self.head
        # update LRU Cache head
        self.head = key

    def _pop_tail(self) -> None:
        tail_node: Node = super().__getitem__(self.tail)
        new_tail: Node = super().__getitem__(tail_node.prev)

        self.tail = tail_node.prev
        new_tail.next_ = None
        super().__delitem__(self.tail)

    def _unchain_node(self, key: str) -> None:
        node: Node = super().__getitem__(key)
        if (left_node := self.super_get(node.prev)) is not None:
            left_node.next_ = node.next_
            if not left_node.next_:
                self.tail = node.prev

        if (right_node := self.super_get(node.next_)) is not None:
            right_node.prev = node.prev

    def super_get(self, key: str, default=None) -> int | None:
        try:
            return super().__getitem__(key)
        except KeyError:
            return default

    def __getitem__(self, key) -> int | None:
        """
        Get an item from Cache, moving to the head
        """
        if (item := self.super_get(key)) is not None:
            # update head node
            self._unchain_node(key)
            self._update_head(key)

            return item.value

        return None
    
    def __setitem__(self, key: str, value: int):
        """
        Set an item to the head of the Cache
        if length exceeds limit, then pop from tail
        """
        if not isinstance(key, str):
            raise ValueError("Key must be a string")
        if not key:
            raise ValueError("Key must not be empty")
        if not isinstance(value, int):
            raise ValueError("Value must be an integer")

        # add to Cache
        node = Node("", self.head, value)
        super().__setitem__(key, node)

        # update head node
        self._update_head(key)

        if self.__len__() > self.capacity:
            self._pop_tail()


import pytest


def test_lru_cache():
    initial_insert = {
        "baz": 0,
        "bar": -1,
        "foo": 10,
    }

    lru_cache = LRUCache(capacity=3)
    for key, value in initial_insert.items():
        lru_cache[key] = value

    assert lru_cache.head == "foo"
    assert lru_cache.tail == "baz"

    assert lru_cache["bar"] == -1
    assert lru_cache.head == "bar"
    assert lru_cache.tail == "baz"

    assert lru_cache["baz"] == 0
    assert lru_cache.head == "baz"
    assert lru_cache.tail == "foo"

    assert lru_cache["qux"] is None
    lru_cache["qux"] = 20
    assert lru_cache.head == "qux"
    assert lru_cache.tail == "bar"
    assert len(lru_cache) == 3
