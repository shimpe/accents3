from itertools import tee
from expremigen.patterns.pseq import Pseq
from expremigen.musicalmappings.nanonotation import NanoNotation
from expremigen.musicalmappings.constants import REST
import abjad
import scamp
import random

inf = int(1e6) # for small values of infinity

instrument_lookup = {
    'flute': abjad.instruments.Flute(),
    'oboe': abjad.instruments.Oboe(),
    'clarinet': abjad.instruments.ClarinetInBFlat(),
    'bassoon': abjad.instruments.Bassoon(),
    'horns': abjad.instruments.FrenchHorn(),
    'trumpets': abjad.instruments.Trumpet(),
    'violins': abjad.instruments.Violin(),
    'violins2': abjad.instruments.Violin(),
    'viola': abjad.instruments.Viola(),
    'cello': abjad.instruments.Cello(),
    'contrabass': abjad.instruments.Contrabass()
}

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def check_range(instrument_name, note):
    global instrument_lookup
    if instrument_name in instrument_lookup:
        instrument = instrument_lookup[instrument_name]
        lowest = instrument.pitch_range.start_pitch + 60 # abjad's weird numbering convention to midi note number
        highest = instrument.pitch_range.stop_pitch + 60
        return lowest <= note <= highest


def dur_to_beat(dur):
    return dur*4


def perform_cell(input_string, repeats, max_duration, parts, instrument_name, key, check_range=False):
    total_duration = 0
    n = NanoNotation()
    note_pattern = Pseq(n.midinumbers(input_string), repeats)
    dur_pattern =  Pseq(n.dur(input_string), repeats)
    for n,d in zip(note_pattern, dur_pattern):
        if total_duration < max_duration:
            prop = {}
            if random.randint(0,10) > 7:
                accent = 1.0
                prop["articulations"] = "accent"
            else:
                accent = 0.6

            duration = dur_to_beat(d)
            if total_duration + duration > max_duration:
                duration = max_duration - total_duration #  cut off the rhythm to remain inside measure

            if key:
                prop["key"] = key

            if check_range and not check_range(instrument_name, n):
                print(f"Warning: instrument {instrument_name} goes out of range with note {n}")

            if n == REST:
                scamp.wait(duration)
            else:
                parts[instrument_name].play_note(n, 0.7*accent, duration, properties=prop if prop else None)
            total_duration += duration

        else:
            return

def perform_cell_spicy(input_string, repeats, max_duration, parts, instrument_name, key, check_range=False):
    total_duration = 0
    n = NanoNotation()
    note_pattern = Pseq(n.midinumbers(input_string), repeats)
    dur_pattern = Pseq(n.dur(input_string), repeats)
    if len(n.midinumbers(input_string)) == 1 and repeats <= 1:
        perform_cell(input_string, repeats, max_duration, parts, instrument_name, key, check_range)
    else:
        last_encountered_nd2 = None
        for nd1, nd2 in pairwise(zip(note_pattern, dur_pattern)):
            last_encountered_nd2 = nd2
            if total_duration < max_duration:
                prop = {}
                if random.randint(0,10) > 7:
                    accent = 1.0
                    prop["articulations"] = "accent"
                else:
                    accent = 0.6

                n1 = nd1[0]
                n2 = nd2[0]
                d = nd1[1]
                duration = dur_to_beat(d)

                if total_duration + duration > max_duration:
                    duration = max_duration - total_duration #  cut off the rhythm to remain inside measure

                if key:
                    prop["key"] = key

                if check_range and not check_range(instrument_name, n):
                    print(f"Warning: instrument {instrument_name} goes out of range with note {n}")

                all_notes, all_durs = transform_note_duration(duration, n1, n2)

                for n, d in zip(all_notes, all_durs):
                    if n == REST:
                        scamp.wait(d)
                    else:
                        parts[instrument_name].play_note(n, 0.7*accent, d, properties=prop if prop else None)
                    total_duration += d
            else:
                return

        if last_encountered_nd2 is not None:
            n = last_encountered_nd2[0]
            d = last_encountered_nd2[1]
            if n == REST:
                scamp.wait(d)
            else:
                parts[instrument_name].play_note(n, 0.7 * accent, duration, properties=prop if prop else None)
            total_duration += d


def transform_note_duration(duration, n1, n2):
    all_notes = []
    max_division = int(duration*4) # limit rhythmic complexity
    extra_notes = random.randint(0, max_division)
    if extra_notes >= 1 and n1 != REST and n2 != REST:
        step = int((n2 - n1) / (extra_notes + 1))
        if step == 0:
            # step 0 is boring.. invent some new notes
            for i in range(extra_notes):
                all_notes.append(n1 + i*( -1 if (i % 2 == 0) else 1))
        else:
            # interpolate between the notes (use chromatic scale, no microtonality)
            for i in range(extra_notes):
                all_notes.append(n1 + i * step)
        all_durs = [duration / extra_notes] * extra_notes
    else:
        all_notes = [n1]
        all_durs = [duration]

    return all_notes, all_durs