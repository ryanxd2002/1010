# pieces.py

# Each piece is a dict with:
# - "name": for debugging/printing
# - "shape": a 2D list of 0/1 values
#
# 1 means the cell is part of the piece, 0 means empty (padding).

PIECES = [
    # 1-block
    {
        "name": "single",
        "shape": [
            [1]
        ]
    },

    # 2-block line
    {
        "name": "line2_h",
        "shape": [
            [1, 1]
        ]
    },
    {
        "name": "line2_v",
        "shape": [
            [1],
            [1]
        ]
    },

    # 3-block line
    {
        "name": "line3_h",
        "shape": [
            [1, 1, 1]
        ]
    },
    {
        "name": "line3_v",
        "shape": [
            [1],
            [1],
            [1]
        ]
    },

    # 4-block line
    {
        "name": "line4_h",
        "shape": [
            [1, 1, 1, 1]
        ]
    },
    {
        "name": "line4_v",
        "shape": [
            [1],
            [1],
            [1],
            [1]
        ]
    },

    # 5-block line (very 1010-style)
    {
        "name": "line5_h",
        "shape": [
            [1, 1, 1, 1, 1]
        ]
    },
    {
        "name": "line5_v",
        "shape": [
            [1],
            [1],
            [1],
            [1],
            [1]
        ]
    },

    # 2x2 square
    {
        "name": "square2",
        "shape": [
            [1, 1],
            [1, 1]
        ]
    },

    # 3x3 square
    {
        "name": "square3",
        "shape": [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
    },

    # L-shape (3 blocks)
    {
        "name": "L3_down_right",
        "shape": [
            [1, 0],
            [1, 0],
            [1, 1]
        ]
    },

    # Another L-shape (rotated)
    {
        "name": "L3_down_left",
        "shape": [
            [0, 1],
            [0, 1],
            [1, 1]
        ]
    },

    # Plus shape (cross)
    {
        "name": "plus",
        "shape": [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]
        ]
    },
]
