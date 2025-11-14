from learn1010.pieces.pieces import get_all_pieces, piece_block_count, print_piece


def test_get_all_pieces_structure_and_nonempty():
    pieces = get_all_pieces()
    assert isinstance(pieces, list)
    assert len(pieces) > 0
    for p in pieces:
        assert isinstance(p, dict)
        assert 'name' in p and isinstance(p['name'], str)
        assert 'shape' in p and isinstance(p['shape'], list)
        for row in p['shape']:
            assert isinstance(row, list)
            for cell in row:
                assert cell in (0, 1)


def test_piece_block_count_matches_shape_sum():
    pieces = get_all_pieces()
    for p in pieces:
        # compute expected count
        expected = sum(sum(row) for row in p['shape'])
        assert piece_block_count(p) == expected


def test_piece_block_count_empty_shape():
    empty = {"name": "empty", "shape": []}
    assert piece_block_count(empty) == 0


def test_print_piece_outputs_correct_symbols(capsys):
    piece = {"name": "X", "shape": [[1, 0], [0, 1]]}
    print_piece(piece)
    out = capsys.readouterr().out
    lines = out.splitlines()
    # name line + 2 shape lines + blank line
    assert lines[0] == "X"
    assert lines[1] == "# ."
    assert lines[2] == ". #"
    assert lines[3] == ""
