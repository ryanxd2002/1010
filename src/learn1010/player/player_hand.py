from learn1010.pieces.pieces import print_piece

def print_hand(hand):
    """Show the current hand with indexes."""
    print("Current hand:")
    for i, piece in enumerate(hand):
        print(f"[{i}] {piece['name']}")
        print_piece(piece)

def get_player_move(hand):
    """
    Ask the player which piece to place and where.
    Returns (piece_index, row, col) or None if player quits.
    """
    while True:
        choice = input("Choose piece index (or 'q' to quit): ").strip()
        if choice.lower() == 'q':
            return None

        # Validate piece index
        if not choice.isdigit():
            print("Please enter a number for the piece index.")
            continue

        piece_index = int(choice)
        if piece_index < 0 or piece_index >= len(hand):
            print("Invalid index. Try again.")
            continue

        # Get row
        row_str = input("Row (0-9): ").strip()
        col_str = input("Col (0-9): ").strip()

        if not (row_str.isdigit() and col_str.isdigit()):
            print("Row and column must be numbers. Try again.")
            continue

        row = int(row_str)
        col = int(col_str)

        return piece_index, row, col
