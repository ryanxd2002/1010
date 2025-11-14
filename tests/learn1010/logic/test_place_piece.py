import types
import sys

import pytest

from learn1010.logic import place_piece
from learn1010.board import board as board_module
from learn1010.constants.pieces import PIECES
from learn1010.logic import check_valid
from learn1010.constants.logic import DEFAULT_VALUE


def find_piece(name):
    for p in PIECES:
        if p["name"] == name:
            return p
    raise KeyError(name)


def make_logic_module_with_can_place(fn):
    m = types.ModuleType("logic")
    m.can_place = fn
    return m


def test_place_piece_mutates_board(monkeypatch):
    # Ensure the internal import 'from logic import can_place' resolves to our module
    logic_mod = make_logic_module_with_can_place(check_valid.can_place)
    monkeypatch.setitem(sys.modules, "logic", logic_mod)

    b = board_module.create_empty_board()
    single = find_piece("single")

    place_piece.place_piece(b, single, 2, 3)

    assert b[2][3] == DEFAULT_VALUE


def test_place_piece_with_custom_value(monkeypatch):
    logic_mod = make_logic_module_with_can_place(check_valid.can_place)
    monkeypatch.setitem(sys.modules, "logic", logic_mod)

    b = board_module.create_empty_board()
    square2 = find_piece("square2")

    place_piece.place_piece(b, square2, 0, 0, value=7)

    assert b[0][0] == 7
    assert b[0][1] == 7
    assert b[1][0] == 7
    assert b[1][1] == 7


def test_place_piece_raises_on_invalid(monkeypatch):
    # Make can_place always return False to simulate invalid placement
    logic_mod = make_logic_module_with_can_place(lambda board, piece, r, c: False)
    monkeypatch.setitem(sys.modules, "logic", logic_mod)

    b = board_module.create_empty_board()
    single = find_piece("single")

    with pytest.raises(ValueError):
        place_piece.place_piece(b, single, 0, 0)
