def calculate_score(piece, cleared_lines):
    return sum(map(sum, piece["shape"])) + cleared_lines * 10