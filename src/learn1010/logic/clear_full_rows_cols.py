def clear_lines(board):
    """
    Clear all completely filled rows and columns.
    
    Mutates the board in place.
    Returns:
        cells_cleared, rows_cleared, cols_cleared
    """
    height = len(board)
    width = len(board[0]) if height > 0 else 0

    full_rows = []
    full_cols = []

    # 1) Find full rows
    for r in range(height):
        if all(board[r][c] != 0 for c in range(width)):
            full_rows.append(r)

    # 2) Find full columns
    for c in range(width):
        if all(board[r][c] != 0 for r in range(height)):
            full_cols.append(c)

    cells_cleared = 0

    # 3) Clear full rows
    for r in full_rows:
        for c in range(width):
            if board[r][c] != 0:
                board[r][c] = 0
                cells_cleared += 1

    # 4) Clear full columns
    for c in full_cols:
        for r in range(height):
            if board[r][c] != 0:
                board[r][c] = 0
                cells_cleared += 1

    return cells_cleared, len(full_rows), len(full_cols)
