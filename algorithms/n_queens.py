"""
https://leetcode.com/problems/n-queens/

The n-queens puzzle is the problem of placing n queens on an n x n 
chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. 
You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space, respectively.
"""  # noqa: E501
from __future__ import annotations

import copy
from dataclasses import dataclass, field
from functools import cached_property

import numpy as np
import pytest


@dataclass
class QueenPosition:
    x: int
    y: int
    n: int = 8

    def __hash__(self):
        return hash(self.x, self.y, self.n)

    @property
    def max_traverse(self):
        return self.n

    @property
    def allowed_directions(self) -> list[tuple[int, int]]:
        """
        Allowed Directions
        Direction vectors for the queen to move in
        """
        return [
            (0, 0),  # self
            (1, 0),  # right
            (1, 1),  # down-right
            (0, 1),  # down
            (-1, 1),  # down-left
            (-1, 0),  # left
            (-1, -1),  # up-left
            (0, -1),  # up
            (1, -1),  # up-right
        ]

    @cached_property
    def moves(self) -> np.ndarray:
        moves = np.zeros((self.n, self.n), dtype=int)
        for xdir, ydir in self.allowed_directions:
            for i in range(1, self.max_traverse):
                if (
                    (new_x := ((i * xdir) + self.x)) < self.n
                    and (new_y := ((i * ydir) + self.y)) < self.n
                    and new_x >= 0
                    and new_y >= 0
                ):
                    moves[new_x, new_y] = 1

        return moves


@dataclass
class ChessBoard:
    size: int

    board: np.ndarray = np.zeros((0, 0), dtype=int)
    available_squares: np.ndarray = np.zeros((0, 0), dtype=int)
    queens: list[QueenPosition] = field(default_factory=list)

    def __post_init__(self):
        self.board = np.zeros((self.size, self.size), dtype=int)
        self.available_squares = np.ma.make_mask(self.available_squares)

    def copy(self) -> ChessBoard:
        return copy.deepcopy(self)

    def add_queen_to_board(self, queen: QueenPosition):
        self.queens.append(queen)
        self.board[queen.x, queen.y] = 1
        self.available_squares = np.ma.mask_or(
            self.available_squares, np.ma.make_mask(queen.moves)
        )


def solve_n_queens(
    n: int, board: ChessBoard | None = None, solutions: list[ChessBoard] | None = None
) -> list[ChessBoard]:
    """
    Solve the n-queens problem
    """
    board = board or ChessBoard(n)
    solutions = solutions or []

    if (row_number := len(board.queens)) == n:
        solutions.append(board)
        return solutions

    # making a mask of np.zeros returns False
    available_squares = (
        board.available_squares
        if isinstance(board.available_squares, np.ndarray)
        else board.board
    )

    if not all(available_squares[row_number]):
        for idx, square in enumerate(available_squares[row_number]):
            if not square:
                queen = QueenPosition(row_number, idx, n)
                new_board = board.copy()
                new_board.add_queen_to_board(queen)

                solutions = solve_n_queens(n, new_board, solutions)

    return solutions


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            (0, 0, 8),
            np.array(
                [
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 0, 0, 0, 0, 0, 0],
                    [1, 0, 1, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 0, 0, 0, 0],
                    [1, 0, 0, 0, 1, 0, 0, 0],
                    [1, 0, 0, 0, 0, 1, 0, 0],
                    [1, 0, 0, 0, 0, 0, 1, 0],
                    [1, 0, 0, 0, 0, 0, 0, 1],
                ]
            ),
        ),
    ],
)
def test_queen_moves(input_, expected):
    queen = QueenPosition(*input_)
    assert queen.moves.all() == expected.all()


@pytest.mark.parametrize(
    "board,queen,available_squares",
    [
        (
            ChessBoard(8),
            QueenPosition(0, 0, 8),
            np.array(
                [
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 1, 1, 1],
                    [0, 1, 0, 1, 1, 1, 1, 1],
                    [0, 1, 1, 0, 1, 1, 1, 1],
                    [0, 1, 1, 1, 0, 1, 1, 1],
                    [0, 1, 1, 1, 1, 0, 1, 1],
                    [0, 1, 1, 1, 1, 1, 0, 1],
                    [0, 1, 1, 1, 1, 1, 1, 0],
                ]
            ),
        ),
    ],
)
def test_add_queen_to_board(board, queen, available_squares):
    board.add_queen_to_board(queen)
    assert board.board.all() == queen.moves.all()
    assert board.available_squares.all() == available_squares.all()


def test_copy_board():
    board = ChessBoard(4)
    queen_1 = QueenPosition(3, 2, 4)
    board.add_queen_to_board(queen_1)

    new_board = board.copy()
    queen_2 = QueenPosition(1, 1, 4)
    new_board.add_queen_to_board(queen_2)

    assert board.queens == [queen_1]
    assert new_board.queens == [queen_1, queen_2]


@pytest.mark.parametrize(
    "input_,expected",
    [
        (4, 2),
        (3, 0),
        (5, 10),
        (2, 0),
        (1, 1),
        (9, 352),
        (8, 92),
        (7, 40),
        (6, 4),
    ],
)
def test_solve_n_queens(input_, expected):
    assert len(solve_n_queens(input_)) == expected
