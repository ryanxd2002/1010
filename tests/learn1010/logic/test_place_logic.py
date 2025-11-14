import pytest

from learn1010.logic import place_logic
from learn1010.board import board as board_module
from learn1010.constants.pieces import PIECES


def find_piece(name):
    for p in PIECES:
        if p["name"] == name:
            return p
    raise KeyError(name)


def test_can_place_single_on_empty_board():
    b = board_module.create_empty_board()
    single = find_piece("single")

    assert place_logic.can_place(b, single, 0, 0) is True
    # also at the bottom-right corner
    assert place_logic.can_place(b, single, len(b) - 1, len(b[0]) - 1) is True


def test_cannot_place_when_out_of_bounds():
    b = board_module.create_empty_board()
    line2_h = find_piece("line2_h")

    # placing a horizontal length-2 at col=9 on a 10-wide board goes out of bounds
    assert place_logic.can_place(b, line2_h, 0, 9) is False


def test_cannot_place_with_negative_coordinates():
    b = board_module.create_empty_board()
    single = find_piece("single")

    assert place_logic.can_place(b, single, -1, 0) is False
    assert place_logic.can_place(b, single, 0, -1) is False


def test_cannot_place_overlapping_filled_cell():
    b = board_module.create_empty_board()
    # Mark a cell as occupied
    b[1][1] = 1

    single = find_piece("single")
    assert place_logic.can_place(b, single, 1, 1) is False

    # For a 2x2 square, placing at (0,0) should be False if any of its cells overlap
    square2 = find_piece("square2")
    # overlap cell (1,1) when placing square at (0,0)
    assert place_logic.can_place(b, square2, 0, 0) is False


def test_zeros_in_shape_are_ignored():
    b = board_module.create_empty_board()
    # Create a custom piece with a leading zero cell and a 1 that would be out of bounds
    piece = {"name": "test", "shape": [[0, 1]]}

    # placing at col=9 should be False because the '1' maps to col=10
    assert place_logic.can_place(b, piece, 0, 9) is False
