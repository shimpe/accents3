def cell1b(parts):
    # d
    scamp.fork(perform_cell, args=("d6_8", inf, 8, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("b4_4", inf, 8, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("g4_4", inf, 8, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("g3_4", inf, 8, parts, instrument4, 'E major'))


def cell2b(parts):
    # g
    scamp.fork(perform_cell, args=("b5_8", inf, 8, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("g4_4", inf, 8, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("f4_4", inf, 8, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("g3_4", inf, 8, parts, instrument4, 'E major'))


def cell3b(parts):
    # e
    scamp.fork(perform_cell, args=("c6_8", inf, 8, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("g5_4", inf, 8, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("e4_4", inf, 8, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("c4_4", inf, 8, parts, instrument4, 'E major'))


def cell4b(parts):
    # b
    scamp.fork(perform_cell, args=("b5_8", inf, 4, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("a-4_4", inf, 4, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("f4_4", inf, 4, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("c3_4", inf, 4, parts, instrument4, 'E major'))


def cell5b(parts):
    # g
    scamp.fork(perform_cell, args=("c6_8", inf, 4, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("g4_4", inf, 4, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("e4_4", inf, 4, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("c4_4", inf, 4, parts, instrument4, 'E major'))


def cell6b(parts):
    # g#
    scamp.fork(perform_cell, args=("c#6_8", inf, 4, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("c5_4", inf, 4, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("g#4_4", inf, 4, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("f#3_4", inf, 4, parts, instrument4, 'E major'))


def cell7b(parts):
    # f#
    scamp.fork(perform_cell, args=("c#6_8", inf, 4, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("a#5_4", inf, 4, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("f#4_4", inf, 4, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("f#3_4", inf, 4, parts, instrument4, 'E major'))


def cell8b(parts):
    # d#
    scamp.fork(perform_cell, args=("d#6_8", inf, 8, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("c5_4", inf, 8, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("a3_4", inf, 8, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("f3_4", inf, 8, parts, instrument4, 'E major'))


def cell9b(parts):
    # a
    scamp.fork(perform_cell, args=("a5_8", inf, 4, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("f4_8", inf, 4, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("c4_4", inf, 4, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("f3_4", inf, 4, parts, instrument4, 'E major'))


def cell10b(parts):
    # b-
    scamp.fork(perform_cell, args=("b-5_8", inf, 4, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("f4_8", inf, 4, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("d4_4", inf, 4, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("f3_4", inf, 4, parts, instrument4, 'E major'))


def cell11b(parts):
    # c
    scamp.fork(perform_cell, args=("c6_8", inf, 4, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("g4_8", inf, 4, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("e4_4", inf, 4, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("f3_4", inf, 4, parts, instrument4, 'E major'))


def cell12b(parts):
    # g
    scamp.fork(perform_cell, args=("g5_8", inf, 4, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("d4_8", inf, 4, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("b-3_4", inf, 4, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("f3_4", inf, 4, parts, instrument4, 'E major'))


def cell13b(parts):
    # f
    scamp.fork(perform_cell, args=("f5_8", inf, 8, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("c4_8", inf, 8, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("a3_4", inf, 8, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("f3_4", inf, 8, parts, instrument4, 'E major'))


def cell14b(parts):
    # c# / d-
    scamp.fork(perform_cell, args=("d-5_8", inf, 4, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("a-4_8", inf, 4, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("e4_4", inf, 4, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("a3_4", inf, 4, parts, instrument4, 'E major'))


def cell15b(parts):
    # b-
    scamp.fork(perform_cell, args=("e-5_8", inf, 4, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("b-5_8", inf, 4, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("g-4_4", inf, 4, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("a-3_4", inf, 4, parts, instrument4, 'E major'))


def cell16b(parts):
    # e
    scamp.fork(perform_cell, args=("e5_8", inf, 4, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("c5_8", inf, 4, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("g4_4", inf, 4, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("g3_4", inf, 4, parts, instrument4, 'E major'))


def cell17b(parts):
    # d
    scamp.fork(perform_cell, args=("d5_8", inf, 2, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("c5_8", inf, 2, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("g-4_4", inf, 2, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("a-3_4", inf, 2, parts, instrument4, 'E major'))


def cell18b(parts):
    # e-
    scamp.fork(perform_cell, args=("e-5_8", inf, 2, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("c5_8", inf, 2, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("g-4_4", inf, 2, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("a-3_4", inf, 2, parts, instrument4, 'E major'))


def cell19b(parts):
    # c
    scamp.fork(perform_cell, args=("c5_8", inf, 4, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("g4_8", inf, 4, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("e4_4", inf, 4, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("c3_4", inf, 4, parts, instrument4, 'E major'))


def cell20b(parts):
    # g#
    scamp.fork(perform_cell, args=("g#5_8", inf, 4, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("e4_8", inf, 4, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("d4_4", inf, 4, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("e3_4", inf, 4, parts, instrument4, 'E major'))


def cell21b(parts):
    # f#
    scamp.fork(perform_cell, args=("c#6_8", inf, 2, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("a4_8", inf, 2, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("f#4_4", inf, 2, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("f#3_4", inf, 2, parts, instrument4, 'E major'))


def cell22b(parts):
    # f
    scamp.fork(perform_cell, args=("c#6_8", inf, 2, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("a4_8", inf, 2, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("f4_4", inf, 2, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("f3_4", inf, 2, parts, instrument4, 'E major'))


def cell23b(parts):
    # a
    scamp.fork(perform_cell, args=("a5_8", inf, 4, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("e4_8", inf, 4, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("d4_4", inf, 4, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("e3_4", inf, 4, parts, instrument4, 'E major'))


def cell24b(parts):
    # c#
    scamp.fork(perform_cell, args=("c#6_8", inf, 8, parts, instrument1, 'E major'))
    scamp.fork(perform_cell, args=("a4_8", inf, 8, parts, instrument2, 'E major'))
    scamp.fork(perform_cell, args=("e4_4", inf, 8, parts, instrument3, 'E major'))
    scamp.fork(perform_cell, args=("a2_4", inf, 8, parts, instrument4, 'E major'))
