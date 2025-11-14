def can_place(board, piece, row, col):
    """
    Return True if the piece can be legally placed on the board
    with its top-left corner at (row, col).
    """
    shape = piece["shape"]
    piece_h = len(shape)
    piece_w = len(shape[0])

    for i in range(piece_h):          # i = row in piece shape
        for j in range(piece_w):      # j = col in piece shape
            if shape[i][j] == 1:

                # Board coordinates this block would occupy
                br = row + i
                bc = col + j

                # Check bounds
                if br < 0 or br >= len(board):
                    return False
                if bc < 0 or bc >= len(board[0]):
                    return False

                # Check if board cell is empty
                if board[br][bc] != 0:
                    return False

    # All checks passed!
    return True
