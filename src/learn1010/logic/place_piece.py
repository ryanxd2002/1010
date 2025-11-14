from learn1010.constants.logic import DEFAULT_VALUE

def place_piece(board, piece, row, col, value=DEFAULT_VALUE):
    """
    Place the piece on the board with its top-left corner at (row, col).

    Mutates the board in place.
    Assumes the move is valid (can_place == True).
    If it's not valid, raises a ValueError.
    """
    from logic import can_place  # or remove this line if logic.py already has can_place above

    if not can_place(board, piece, row, col):
        raise ValueError("Invalid placement: piece does not fit at the given position")

    shape = piece["shape"]
    piece_h = len(shape)
    piece_w = len(shape[0])

    for i in range(piece_h):
        for j in range(piece_w):
            if shape[i][j] == 1:
                br = row + i
                bc = col + j
                board[br][bc] = value   # default is 1 (filled)
