from learn1010.constants.board import BOARD_SIZE

def create_empty_board():
    """Return a 10x10 board filled with 0s (empty cells)."""
    return [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def print_board(board):
    """Print the board in a simple text form."""
    for row in board:
        # '.' for empty, '#' for filled (later we'll use 1 instead of 0)
        print(" ".join('.' if cell == 0 else '#' for cell in row))
    print()
