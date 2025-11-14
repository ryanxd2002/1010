import importlib
import sys
import types

import pytest

from learn1010.board import board as board_pkg
from learn1010.pieces import pieces as pieces_pkg
from learn1010.pieces import generate_pieces as gen_pkg
from learn1010.logic import check_valid as check_valid_pkg
from learn1010.logic import place_piece as place_piece_pkg
from learn1010.logic import clear_full_rows_cols as clear_pkg
from learn1010.constants.pieces import PIECES


def setup_main_modules(any_move_fn=None, generate_hand_fn=None):
    """Install fake top-level modules 'board', 'pieces', and 'logic' into sys.modules
    so that importing `learn1010.main` (which does `from board import ...`) works.
    """
    # board module
    board_mod = types.ModuleType("board")
    board_mod.create_empty_board = board_pkg.create_empty_board
    board_mod.print_board = board_pkg.print_board

    # pieces module
    pieces_mod = types.ModuleType("pieces")
    # default generate_hand returns three known pieces unless overridden
    if generate_hand_fn is None:
        pieces_mod.generate_hand = lambda: [PIECES[0], PIECES[1], PIECES[2]]
    else:
        pieces_mod.generate_hand = generate_hand_fn
    pieces_mod.print_piece = pieces_pkg.print_piece
    pieces_mod.piece_block_count = pieces_pkg.piece_block_count

    # logic module
    logic_mod = types.ModuleType("logic")
    logic_mod.can_place = check_valid_pkg.can_place
    logic_mod.place_piece = place_piece_pkg.place_piece
    logic_mod.clear_lines = clear_pkg.clear_lines
    if any_move_fn is None:
        logic_mod.any_move_possible = lambda b, h: True
    else:
        logic_mod.any_move_possible = any_move_fn

    # Inject into sys.modules so `from board import ...` etc. succeed
    sys.modules["board"] = board_mod
    sys.modules["pieces"] = pieces_mod
    sys.modules["logic"] = logic_mod

    # Now import (or reload) the main module under package name
    import learn1010.main as main_mod
    importlib.reload(main_mod)
    return main_mod


def test_print_hand_outputs(capsys):
    main_mod = setup_main_modules()

    hand = [PIECES[0], PIECES[1]]
    main_mod.print_hand(hand)

    out = capsys.readouterr().out
    assert "Current hand:" in out
    assert PIECES[0]["name"] in out
    assert PIECES[1]["name"] in out


def test_get_player_move_quit(monkeypatch):
    main_mod = setup_main_modules()

    inputs = iter(["q"])  # first prompt: choose piece index -> 'q'
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

    res = main_mod.get_player_move([])
    assert res is None


def test_get_player_move_valid_after_invalid(monkeypatch):
    main_mod = setup_main_modules()

    # Simulate: invalid non-digit, then valid index 0 and row/col
    inputs = iter(["x", "0", "2", "3"])  # choice 'x' -> retry; then '0', row=2, col=3
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

    res = main_mod.get_player_move([PIECES[0]])
    assert res == (0, 2, 3)


def test_main_exits_when_no_moves(monkeypatch, capsys):
    # any_move_possible should return False to trigger game over
    main_mod = setup_main_modules(any_move_fn=lambda b, h: False)

    # Run main(); it should detect no moves and exit
    main_mod.main()

    out = capsys.readouterr().out
    assert "No more possible moves. Game over!" in out
    assert "Final score:" in out
