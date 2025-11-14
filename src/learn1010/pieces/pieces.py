from learn1010.constants.pieces import PIECES

def get_all_pieces():
    """Return the list of all defined pieces."""
    return PIECES

def piece_block_count(piece):
    """Return how many '1' cells are in this piece."""
    shape = piece["shape"]
    return sum(sum(row) for row in shape)

def print_piece(piece):
    """Print a piece shape nicely for debugging."""
    print(piece["name"])
    for row in piece["shape"]:
        print(" ".join('#' if cell == 1 else '.' for cell in row))
    print()
