from learn1010.board.board import create_empty_board, print_board
from learn1010.pieces.pieces import print_piece, piece_block_count
from learn1010.pieces.generate_pieces import generate_hand
from learn1010.logic.any_move_possible import any_move_possible
from learn1010.logic.check_valid import can_place
from learn1010.logic.place_piece import place_piece
from learn1010.logic.clear_full_rows_cols import clear_lines
from learn1010.constants.pieces import PIECES_IN_HAND
from learn1010.score.basic_score import calculate_score


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


def main():
    board = create_empty_board()
    score = 0
    hand = generate_hand(PIECES_IN_HAND)

    print("Welcome to 1010 (console version)!")
    print("Fill rows/columns completely to clear them.")
    print("Type 'q' when choosing a piece to quit.\n")

    while True:
        print("Current board:")
        print_board(board)
        print(f"Score: {score}")
        print_hand(hand)

        # Check for game over BEFORE asking for a move
        if not any_move_possible(board, hand):
            print("No more possible moves. Game over!")
            print("Final score:", score)
            break

        move = get_player_move(hand)
        if move is None:
            print("You quit the game.")
            print("Final score:", score)
            break

        piece_index, row, col = move
        piece = hand[piece_index]

        if not can_place(board, piece, row, col):
            print("You can't place that piece there. Try again.\n")
            continue

        # Place the piece
        place_piece(board, piece, row, col)

        # Scoring: blocks placed + bonus for cleared cells
        blocks = piece_block_count(piece)
        cleared_cells, rows_cleared, cols_cleared = clear_lines(board)

        score += calculate_score(piece, rows_cleared + cols_cleared)

        print(f"Placed '{piece['name']}' at ({row}, {col}).")
        if rows_cleared or cols_cleared:
            print(f"Cleared {rows_cleared} rows and {cols_cleared} columns!")
        print(f"+{blocks} for blocks, +{cleared_cells} for clears. New score: {score}\n")

        # Remove used piece from hand
        del hand[piece_index]

        # If hand is empty, deal new 3 pieces
        if not hand:
            print("All pieces used. Dealing new hand...\n")
            hand = generate_hand(PIECES_IN_HAND)


if __name__ == "__main__":
    main()
