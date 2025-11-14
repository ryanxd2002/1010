import copy

from learn1010.logic.clear_full_rows_cols import clear_lines


def test_clear_no_full_lines():
    board = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0],
    ]

    before = copy.deepcopy(board)
    cleared, rows, cols = clear_lines(board)

    assert (cleared, rows, cols) == (0, 0, 0)
    assert board == before


def test_clear_single_full_row():
    board = [
        [0, 0, 0],
        [1, 1, 1],  # full row
        [0, 1, 0],
    ]

    cleared, rows, cols = clear_lines(board)

    assert rows == 1
    assert cols == 0
    assert cleared == 3
    # the full row should be cleared to zeros
    assert board[1] == [0, 0, 0]


def test_clear_single_full_col():
    board = [
        [0, 1, 0],
        [0, 1, 0],
        [1, 1, 0],
    ]

    # column 1 is full
    cleared, rows, cols = clear_lines(board)

    assert cols == 1
    assert rows == 0
    assert cleared == 3
    # column 1 should be zeros
    for r in range(len(board)):
        assert board[r][1] == 0


def test_clear_rows_and_cols_with_overlap():
    # A 3x3 board fully filled: all rows and all cols full.
    board = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]

    cleared, rows, cols = clear_lines(board)

    # All 9 cells cleared, 3 rows and 3 cols reported
    assert rows == 3
    assert cols == 3
    assert cleared == 9
    # board should be all zeros
    assert all(all(cell == 0 for cell in row) for row in board)


def test_partial_multiple_lines():
    board = [
        [1, 1, 1, 1],  # full row
        [0, 1, 0, 1],
        [1, 1, 1, 1],  # full row
        [0, 0, 0, 0],
    ]

    # Columns: col1 is full (1,1,1,0) -> not full because of last 0; col2 not full; col3 not full
    cleared, rows, cols = clear_lines(board)

    assert rows == 2
    assert cols == 0
    # cleared cells should equal cells in the two full rows: 4 + 4 = 8
    assert cleared == 8
