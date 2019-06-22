from notes import *
from progressions import *
import random

def make_chords():
    chords = []
    note = C()
    key = Key(note, "major")
    start_chord = Chord(True, seventh = False, scale_degree = 1, key = key)
    chords.append(start_chord)
    for i in range(6):
        t_weights = [1, 1, 3, 1, 1]
        if chords[-1].chord_type in ["major minor", "diminished"]:
            t_weights[3] += 2
        t = random.choice([0]*t_weights[0] + [1]*t_weights[1] + [2]*t_weights[2] + [3]*t_weights[3] + [4]*t_weights[4])
        if t == 0:
            chords.append(new_chord_same_note(key, chords[-1]))
        elif t == 1:
            chords.append(new_chord_neighbor_note(key, chords[-1]))
        elif t == 2:
            if chords[-1].chord_type in ["major", "major minor", "augmented"]:
                chords.append(new_tonal_chord(Key(chords[-1].chord[0], "major")))
            else:
                chords.append(new_tonal_chord(Key(chords[-1].chord[0], "minor")))
        elif t == 3:
            chords.append(new_tonal_chord(key))
        elif t == 4:
            chords.append(new_function_chord(key, chords[-1]))
    return chords