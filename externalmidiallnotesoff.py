import rtmidi
import time
from contextlib import closing


class ExternalMidiAllNotesOff(object):
    """
    make sure external synth notes do not hang when interrupting a running script
    """
    def __init__(self, portname):
        self.midiout = rtmidi.MidiOut()
        self.portname = portname
        for idx, p in enumerate(self.midiout.get_ports()):
            if self.portname == p:
                #print(f"opening port {idx}")
                self.midiout.open_port(idx, name=portname)

    def close(self):
        ALL_SOUND_OFF = 120
        ALL_NOTES_OFF = 123
        for channel in range(16):
            cmd = 0xb0 + channel
            notes_off_msg = [cmd,ALL_NOTES_OFF, 0]
            sound_off_msg = [cmd, ALL_SOUND_OFF, 0]
            self.midiout.send_message(notes_off_msg)
            time.sleep(0.01)
            self.midiout.send_message(sound_off_msg)
            time.sleep(0.01)

        self.midiout.close_port()
        del self.midiout

    def do_test(self):
        note_on = [0x90, 60, 112]  # channel 1, middle C, velocity 112
        note_off = [0x80, 60, 0]
        self.midiout.send_message(note_on)
        time.sleep(1.0)
        self.midiout.send_message(note_off)
        time.sleep(0.1)

if __name__ == "__main__":
    with closing(ExternalMidiAllNotesOff('INTEGRA-7:INTEGRA-7 MIDI 1 24:0')) as c:
        c.do_test()