from learn1010.board.board import create_empty_board, print_board
from learn1010.constants.board import BOARD_SIZE


def test_create_empty_board_shape_and_zeros():
    board = create_empty_board()
    assert isinstance(board, list)
    assert len(board) == BOARD_SIZE
    for row in board:
        assert isinstance(row, list)
        assert len(row) == BOARD_SIZE
        assert all(cell == 0 for cell in row)


def test_create_empty_board_independent_instances():
    b1 = create_empty_board()
    b2 = create_empty_board()

    b1[0][0] = 1

    assert b1[0][0] == 1
    assert b2[0][0] == 0


def test_print_board_all_empty(capsys):
    board = create_empty_board()
    print_board(board)

    out = capsys.readouterr().out
    lines = out.splitlines()

    assert len(lines) == BOARD_SIZE + 1

    expected_row = " ".join(["."] * BOARD_SIZE)
    for i in range(BOARD_SIZE):
        assert lines[i] == expected_row

    assert lines[-1] == ""


def test_print_board_with_filled_cell(capsys):
    board = create_empty_board()

    board[0][0] = 1
    board[3][5] = 1

    print_board(board)

    out = capsys.readouterr().out
    lines = out.splitlines()

    first_row = lines[0].split(" ")
    assert first_row[0] == "#"

    row_3 = lines[3].split(" ")
    assert row_3[5] == "#"
