import scamp
from utils import perform_cell, perform_cell_spicy, inf
import random
from externalmidiallnotesoff import ExternalMidiAllNotesOff
from contextlib import closing

random.seed(0)

# tone row 'd', 'b', 'e', 'b', 'g', 'g#', 'f#', 'd#', 'a', 'a#', 'c', 'g',
#          'f', 'c#', 'a#', 'e', 'd', 'd#', 'c', 'g#', 'f#', 'f', 'a', 'c#'

instrument1 = '1'
instrument2 = '2'
instrument3 = '3'
instrument4 = '4'
key = "G# major"

first_to_render = 1
last_to_render = 25


def cell1(parts, cell_performer):
    # d
    scamp.fork(cell_performer, args=("d6_8 r_8", inf, 8, parts, instrument1, key))
    scamp.fork(cell_performer, args=("b4_4", inf, 8, parts, instrument2, key))
    scamp.fork(cell_performer, args=("g4_4", inf, 8, parts, instrument3, key))
    scamp.fork(cell_performer, args=("g3_4", inf, 8, parts, instrument4, key))


def cell2(parts, cell_performer):
    # b
    scamp.fork(cell_performer, args=("b5_8", inf, 8, parts, instrument1, key))
    scamp.fork(cell_performer, args=("g4_4 f4_8", inf, 8, parts, instrument2, key))
    scamp.fork(cell_performer, args=("f4_8 d4_8", inf, 8, parts, instrument3, key))
    scamp.fork(cell_performer, args=("g3_4", inf, 8, parts, instrument4, key))


def cell3(parts, cell_performer):
    # e
    scamp.fork(cell_performer, args=("c6_8 g5 c6 d6", inf, 8, parts, instrument1, key))
    scamp.fork(cell_performer, args=("g5_8 e_16", inf, 8, parts, instrument2, key))
    scamp.fork(cell_performer, args=("e4_8 f4_4", inf, 8, parts, instrument3, key))
    scamp.fork(cell_performer, args=("c4_4", inf, 8, parts, instrument4, key))


def cell4(parts, cell_performer):
    # b
    scamp.fork(cell_performer, args=("b5_8 d6_16", inf, 4, parts, instrument1, key))
    scamp.fork(cell_performer, args=("a-4_8 a-5_8", inf, 4, parts, instrument2, key))
    scamp.fork(cell_performer, args=("f4_8 d4_4 c4_8", inf, 4, parts, instrument3, key))
    scamp.fork(cell_performer, args=("c3_4", inf, 4, parts, instrument4, key))


def cell5(parts, cell_performer):
    # g
    scamp.fork(cell_performer, args=("c6_8.", inf, 4, parts, instrument1, key))
    scamp.fork(cell_performer, args=("g4_4", inf, 4, parts, instrument2, key))
    scamp.fork(cell_performer, args=("e4_8 d4_4 c4_8", inf, 4, parts, instrument3, key))
    scamp.fork(cell_performer, args=("c4_4", inf, 4, parts, instrument4, key))


def cell6(parts, cell_performer):
    # g#
    scamp.fork(cell_performer, args=("c#6_8 d#6_16", inf, 4, parts, instrument1, key))
    scamp.fork(cell_performer, args=("c5_4", inf, 4, parts, instrument2, key))
    scamp.fork(cell_performer, args=("g#4_8", inf, 4, parts, instrument3, key))
    scamp.fork(cell_performer, args=("f#3_4", inf, 4, parts, instrument4, key))


def cell7(parts, cell_performer):
    # f#
    scamp.fork(cell_performer, args=("c#6_16 c#6_8", inf, 4, parts, instrument1, key))
    scamp.fork(cell_performer, args=("a#5_4", inf, 4, parts, instrument2, key))
    scamp.fork(cell_performer, args=("f#4_8.", inf, 4, parts, instrument3, key))
    scamp.fork(cell_performer, args=("f#3_4", inf, 4, parts, instrument4, key))


def cell8(parts, cell_performer):
    # d#
    scamp.fork(cell_performer, args=("d#6_4 f6_8", inf, 8, parts, instrument1, key))
    scamp.fork(cell_performer, args=("c5_8 f5_4", inf, 8, parts, instrument2, key))
    scamp.fork(cell_performer, args=("a3_4 g3_4", inf, 8, parts, instrument3, key))
    scamp.fork(cell_performer, args=("f3_4", inf, 8, parts, instrument4, key))


def cell9(parts, cell_performer):
    # a
    scamp.fork(cell_performer, args=("a5_8 r_8", inf, 4, parts, instrument1, key))
    scamp.fork(cell_performer, args=("f4_16 e4_16 ", inf, 4, parts, instrument2, key))
    scamp.fork(cell_performer, args=("c4_4", inf, 4, parts, instrument3, key))
    scamp.fork(cell_performer, args=("f2_4", inf, 4, parts, instrument4, key))


def cell10(parts, cell_performer):
    # b-
    scamp.fork(cell_performer, args=("b-5_8 r_8", inf, 4, parts, instrument1, key))
    scamp.fork(cell_performer, args=("g4_8 f4_8 e4_8", inf, 4, parts, instrument2, key))
    scamp.fork(cell_performer, args=("d4_4", inf, 4, parts, instrument3, key))
    scamp.fork(cell_performer, args=("f3_4", inf, 4, parts, instrument4, key))


def cell11(parts, cell_performer):
    # c
    scamp.fork(cell_performer, args=("c6_8 r_8", inf, 4, parts, instrument1, key))
    scamp.fork(cell_performer, args=("a4_16 g4_8", inf, 4, parts, instrument2, key))
    scamp.fork(cell_performer, args=("e4_4 f4_8", inf, 4, parts, instrument3, key))
    scamp.fork(cell_performer, args=("f3_4", inf, 4, parts, instrument4, key))


def cell12(parts, cell_performer):
    # g
    scamp.fork(cell_performer, args=("g5_8 a5_16", inf, 4, parts, instrument1, key))
    scamp.fork(cell_performer, args=("e4-_8 d4_8", inf, 4, parts, instrument2, key))
    scamp.fork(cell_performer, args=("b-3_4", inf, 4, parts, instrument3, key))
    scamp.fork(cell_performer, args=("f3_4", inf, 4, parts, instrument4, key))


def cell13(parts, cell_performer):
    # f
    scamp.fork(cell_performer, args=("f5_8.", inf, 8, parts, instrument1, key))
    scamp.fork(cell_performer, args=("c4_8", inf, 8, parts, instrument2, key))
    scamp.fork(cell_performer, args=("a3_16.", inf, 8, parts, instrument3, key))
    scamp.fork(cell_performer, args=("f3_4.", inf, 8, parts, instrument4, key))


def cell14(parts, cell_performer):
    # c# / d-
    scamp.fork(cell_performer, args=("d-5_8", inf, 4, parts, instrument1, key))
    scamp.fork(cell_performer, args=("a-4_8", inf, 4, parts, instrument2, key))
    scamp.fork(cell_performer, args=("e4_4", inf, 4, parts, instrument3, key))
    scamp.fork(cell_performer, args=("a3_4", inf, 4, parts, instrument4, key))


def cell15(parts, cell_performer):
    # b-
    scamp.fork(cell_performer, args=("e-5_8.", inf, 4, parts, instrument1, key))
    scamp.fork(cell_performer, args=("b-4_4", inf, 4, parts, instrument2, key))
    scamp.fork(cell_performer, args=("g-4_4.", inf, 4, parts, instrument3, key))
    scamp.fork(cell_performer, args=("a-3_8", inf, 4, parts, instrument4, key))


def cell16(parts, cell_performer):
    # e
    scamp.fork(cell_performer, args=("e5_16 c5 d", inf, 4, parts, instrument1, key))
    scamp.fork(cell_performer, args=("c5_8 g4_8", inf, 4, parts, instrument2, key))
    scamp.fork(cell_performer, args=("g4_4 e4_8", inf, 4, parts, instrument1, key))
    scamp.fork(cell_performer, args=("g4_4 e4_8", inf, 4, parts, instrument3, key))
    scamp.fork(cell_performer, args=("g3_4", inf, 4, parts, instrument4, key))


def cell17(parts, cell_performer):
    # d
    scamp.fork(cell_performer, args=("d5_16 e-5_16", inf, 2, parts, instrument1, key))
    scamp.fork(cell_performer, args=("c5_8", inf, 2, parts, instrument2, key))
    scamp.fork(cell_performer, args=("g-4_4", inf, 2, parts, instrument3, key))
    scamp.fork(cell_performer, args=("a-3_4", inf, 2, parts, instrument4, key))


def cell18(parts, cell_performer):
    # e-
    scamp.fork(cell_performer, args=("e-5_8 d5_16", inf, 2, parts, instrument1, key))
    scamp.fork(cell_performer, args=("c5_8", inf, 2, parts, instrument2, key))
    scamp.fork(cell_performer, args=("g-4_4", inf, 2, parts, instrument3, key))
    scamp.fork(cell_performer, args=("a-3_4", inf, 2, parts, instrument4, key))


def cell19(parts, cell_performer):
    # c
    scamp.fork(cell_performer, args=("c5_8", inf, 4, parts, instrument1, key))
    scamp.fork(cell_performer, args=("g4_8", inf, 4, parts, instrument2, key))
    scamp.fork(cell_performer, args=("e4_4", inf, 4, parts, instrument3, key))
    scamp.fork(cell_performer, args=("c3_4", inf, 4, parts, instrument4, key))


def cell20(parts, cell_performer):
    # g#
    scamp.fork(cell_performer, args=("g#5_8 g#5_8 a5_8", inf, 4, parts, instrument1, key))
    scamp.fork(cell_performer, args=("e4_8 g#4_4", inf, 4, parts, instrument2, key))
    scamp.fork(cell_performer, args=("d4_4 c#4_8", inf, 4, parts, instrument3, key))
    scamp.fork(cell_performer, args=("e3_4", inf, 4, parts, instrument4, key))


def cell21(parts, cell_performer):
    # f#
    scamp.fork(cell_performer, args=("c#6_8", inf, 2, parts, instrument1, key))
    scamp.fork(cell_performer, args=("a4_8.", inf, 2, parts, instrument2, key))
    scamp.fork(cell_performer, args=("f#4_4.", inf, 2, parts, instrument3, key))
    scamp.fork(cell_performer, args=("f#3_4", inf, 2, parts, instrument4, key))


def cell22(parts, cell_performer):
    # f
    scamp.fork(cell_performer, args=("c#6_8 e6_16 d6_16", inf, 2, parts, instrument1, key))
    scamp.fork(cell_performer, args=("a4_8 g#4_8", inf, 2, parts, instrument2, key))
    scamp.fork(cell_performer, args=("f4_4 e4_16", inf, 2, parts, instrument3, key))
    scamp.fork(cell_performer, args=("f3_4", inf, 2, parts, instrument4, key))


def cell23(parts, cell_performer):
    # a
    scamp.fork(cell_performer, args=("a5_8 b5_16 g#5_8", inf, 4, parts, instrument1, key))
    scamp.fork(cell_performer, args=("e4_8 f4_8", inf, 4, parts, instrument2, key))
    scamp.fork(cell_performer, args=("d4_4 c#4_8", inf, 4, parts, instrument3, key))
    scamp.fork(cell_performer, args=("e3_4.", inf, 4, parts, instrument4, key))


def cell24(parts, cell_performer):
    # c#
    scamp.fork(cell_performer, args=("c#6_8", inf, 8, parts, instrument1, key))
    scamp.fork(cell_performer, args=("a4_8", inf, 8, parts, instrument2, key))
    scamp.fork(cell_performer, args=("e4_4", inf, 8, parts, instrument3, key))
    scamp.fork(cell_performer, args=("a2_4", inf, 8, parts, instrument4, key))


def cell25(parts, cell_performer):
    scamp.fork(cell_performer, args=("a5_16 r_8", inf, 8, parts, instrument1, key))
    scamp.fork(cell_performer, args=("e4_8", inf, 8, parts, instrument2, key))
    scamp.fork(cell_performer, args=("c#4_4", inf, 8, parts, instrument3, key))
    scamp.fork(cell_performer, args=("a2_4", inf, 8, parts, instrument4, key))


def cell26(parts, cell_performer):
    scamp.fork(cell_performer, args=("a5_1", inf, 4, parts, instrument1, key))
    scamp.fork(cell_performer, args=("e4_1", inf, 4, parts, instrument2, key))
    scamp.fork(cell_performer, args=("c#4_1", inf, 4, parts, instrument3, key))
    scamp.fork(cell_performer, args=("a2_1", inf, 4, parts, instrument4, key))


if __name__ == '__main__':
    with closing(ExternalMidiAllNotesOff('INTEGRA-7:INTEGRA-7 MIDI 1 24:0')) as c:
        s = scamp.Session()
        #s.fast_forward_in_beats(1000)
        parts = {}

        internal_synth = False # set to true if you don't have an external synth

        if internal_synth:
            parts[instrument1] = s.new_part(instrument1)
            parts[instrument2] = s.new_part(instrument2)
            parts[instrument3] = s.new_part(instrument3)
            parts[instrument4] = s.new_part(instrument4)
        else:
            # synth lead / saw lead 3
            parts[instrument1] = s.new_midi_part(instrument1, midi_output_device= 'INTEGRA-7:INTEGRA-7 MIDI 1 24:0',
                                                 midi_output_name="INTEGRA-7 S", num_channels=1, start_channel=0)
            # synth lead / saw lead 25
            parts[instrument2] = s.new_midi_part(instrument2, midi_output_device= 'INTEGRA-7:INTEGRA-7 MIDI 1 24:0',
                                                 midi_output_name="INTEGRA-7 A", num_channels=1, start_channel=1)
            # synth lead / anavox ld 4
            parts[instrument3] = s.new_midi_part(instrument3, midi_output_device= 'INTEGRA-7:INTEGRA-7 MIDI 1 24:0',
                                                 midi_output_name="INTEGRA-7 T", num_channels=1, start_channel=2)
            # synth bass / syn bs 3
            parts[instrument4] = s.new_midi_part(instrument4, midi_output_device= 'INTEGRA-7:INTEGRA-7 MIDI 1 24:0',
                                                 midi_output_name="INTEGRA-7 B", num_channels=1, start_channel=3)

        s.start_transcribing()
        s.tempo = 120
        repeats = 1

        generators = [
            cell1, cell2, cell3,
            cell4, cell5, cell6,
            cell7, cell8, cell9,
            cell10, cell11, cell12,
            cell13, cell14, cell15,
            cell16, cell17, cell18,
            cell19, cell20, cell21,
            cell22, cell23, cell24
        ]

        cells_to_render = set([f"cell{n}" for n in range(first_to_render, last_to_render+1)])

        for _ in range(repeats):
            for gen in generators:
                if gen.__name__ in cells_to_render:
                    print(f"generating {gen.__name__}")
                    gen(parts, perform_cell)
                    s.wait_for_children_to_finish()

            for gen in generators:
                if gen.__name__ in cells_to_render:
                    print(f"generating spicy {gen.__name__}")
                    gen(parts, perform_cell_spicy)
                    s.wait_for_children_to_finish()

            for gen in generators:
                if gen.__name__ in cells_to_render:
                    print(f"generating {gen.__name__}")
                    gen(parts, perform_cell)
                    s.wait_for_children_to_finish()

        # final chord
        if last_to_render > 24:
            cell25(parts, perform_cell)
            s.wait_for_children_to_finish()

            cell26(parts, perform_cell)
            s.wait_for_children_to_finish()

        performance = s.stop_transcribing()
        performance.to_score(title="biebabeloeba", composer="Stefaan Himpe", max_divisor=16).show_xml()
