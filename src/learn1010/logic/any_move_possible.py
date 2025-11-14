from learn1010.logic.place_piece import can_place

def any_move_possible(board, pieces):
    """
    Return True if at least one of the given pieces can be placed
    somewhere on the board. Otherwise, return False.
    """
    height = len(board)
    width = len(board[0]) if height > 0 else 0

    for piece in pieces:
        shape = piece["shape"]
        piece_h = len(shape)
        piece_w = len(shape[0])

        # Try every possible top-left position
        for row in range(height):
            for col in range(width):
                if can_place(board, piece, row, col):
                    return True  # found at least one legal move

    # No placement worked for any piece
    return False
