from notes import *
import random
from itertools import permutations 

class Staff:
    def __init__(self, chord_progression, time_sig = "4/4", staff_width = 1):
        self.chord_progression = chord_progression # list of chords
        self.time_sig = time_sig
        self.soprano = Soprano()
        self.alto = Alto()
        self.tenor = Tenor()
        self.bass = Bass()

        self.staff = []
        self.staff_width = staff_width
        self.make_arrangement()

    def make_arrangement(self):
        current_measure = []
        len_weights = [1, 1, 1, 1, 1, 1, 1, 1]
        prev_chord = None
        prev_len = 0
        for chord in self.chord_progression:
            chord_len = random.choice([1]*len_weights[0] + [2]*len_weights[1] + [3]*len_weights[2] + [4]*len_weights[3] + [5]*len_weights[4] + [6]*len_weights[5] + [7]*len_weights[6] + [8]*len_weights[7])

            # TO DO assign parts based on inversion, voice leading, ranges (using numbered notes)
            if prev_chord == None:
                new_chord = self.make_first_chord(chord)
            else:
                new_chord = self.make_chord(chord, prev_chord, prev_len)
            s = new_chord[0]
            a = new_chord[1]
            t = new_chord[2]
            b = new_chord[3]

            # end TO DO

            first = True
            for beat in range(chord_len):
                if len(current_measure) == int(self.time_sig.split("/")[0]):
                    self.staff.append(current_measure)
                    current_measure = []
                if first:
                    current_measure.append([s, a, t, b])
                    first = False
                else:
                    current_measure.append(["-", "-", "-", "-"])
            prev_chord = new_chord
        self.staff.append(current_measure)
        return

    def make_first_chord(self, chord):
        if chord.quality == "seventh":
            inversions = list(permutations(chord.chord))
        else:
            inversions = []
            for c in chord.chord:
                inversions += list(permutations(chord.chord + [c]))
        voices = [self.soprano, self.alto, self.tenor, self.bass]
        evals = []
        for i in inversions:
            evals.extend(self.eval_first(i))
        final = random.choice(evals)
        return final

    def eval_first(self, chord):
        """ given a chord inversion (list, without octaves), determine valid arrangement with octaves """
        possible = []
        voices = [self.soprano, self.alto, self.tenor, self.bass]
        for i in range(4):
            temp = []
            for octave in range(2,6):
                note = make_note(str(chord[i]), octave)
                if voices[i].check_range(note):
                    temp.append(note)
            possible.append(temp)
        valid = []
        for s in possible[0]:
            for a in possible[1]:
                for t in possible[2]:
                    for b in possible[3]:
                        # for every combination of parts that's been deemed within range, append those tuple of (notes tuple, total distance)
                        if s >= a and a >= t and t >= b:
                            valid.append((s, a, t, b))
        return valid

    def make_chord(self, chord, prev_chord, prev_len):
        """ chord is a Chord object; prev_chors is a list representing the previous chord's inversion """
        if chord.quality == "seventh":
            inversions = list(permutations(chord.chord))
        else:
            inversions = []
            for c in chord.chord:
                inversions += list(permutations(chord.chord + [c]))
        evals = []
        for i in inversions:
            evals.extend(self.eval_inversion(i, prev_chord))
        evals.sort(key = lambda e: e[1])
        weighted_evals = []
        # linear weighting
        for i in range(len(evals)):
            weighted_evals.extend([evals[i]] * (len(evals) - i))
        # exponential weighting
        # for i in range(len(evals)):
        #     weighted_evals.extend([evals[i]] * int(len(evals) / 2**i))
        final = random.choice(weighted_evals)
        return final[0]

    def eval_inversion(self, chord, prev_chord):
        """ given a chord inversion, return all possible set chords with octaves within range and without part crossing, where each part moves at most an octave, with a score indicating the total movement of all parts """
        distances = []
        voices = [self.soprano, self.alto, self.tenor, self.bass]
        for i in range(4):
            temp = []
            dist_up, dist_down = prev_chord[i].sub_by_step(chord[i])
            same_oct_note = make_note(str(chord[i]), prev_chord[i].octave)
            if same_oct_note == prev_chord[i]:
                upper_note = make_note(str(chord[i]), prev_chord[i].octave + 1)
                lower_note = make_note(str(chord[i]), prev_chord[i].octave - 1)
                if voices[i].check_range(same_oct_note):
                    temp.append((same_oct_note, 0))
                if voices[i].check_range(upper_note):
                    temp.append((upper_note, 7))
                if voices[i].check_range(lower_note):
                    temp.append((lower_note, 7))
            elif same_oct_note >= prev_chord[i]:
                lower_note = make_note(str(chord[i]), prev_chord[i].octave - 1)
                if voices[i].check_range(same_oct_note):
                    temp.append((same_oct_note, dist_up))
                if voices[i].check_range(lower_note):
                    temp.append((lower_note, -dist_down))
            else:
                upper_note = make_note(str(chord[i]), prev_chord[i].octave + 1)
                if voices[i].check_range(same_oct_note):
                    temp.append((same_oct_note, -dist_down))
                if voices[i].check_range(upper_note):
                    temp.append((upper_note, dist_up))
            distances.append(temp)
        valid = []
        for s in distances[0]:
            for a in distances[1]:
                for t in distances[2]:
                    for b in distances[3]:
                        # for every combination of parts that's been deemed within range, append those tuple of (notes tuple, total distance)
                        if s[0] >= a[0] and a[0] >= t[0] and t[0] >= b[0]:
                            valid.append(((s[0], a[0], t[0], b[0]), s[1] + a[1] + t[1] + b[1]))
        # if len(valid) > 0:
        #     chordi = valid[0]
        #     # note_tup = chordi[0]
        #     # # distance = chordi[1]
        #     # print(chordi)
        #     print(chordi[1])
        #     for i in range(len(chord)):
        #         print(chordi[0][i], prev_chord[i])
        return valid

    def __str__(self):
        staff_str = ""
        s_s = "S || "
        a_s = "A || "
        t_s = "T || "
        b_s = "B || "
        measure_no = 0
        for measure in self.staff:
            for beat in measure:
                s_s += str(beat[0]) + " "*(5-len(str(beat[0])))
                a_s += str(beat[1]) + " "*(5-len(str(beat[1])))
                t_s += str(beat[2]) + " "*(5-len(str(beat[2])))
                b_s += str(beat[3]) + " "*(5-len(str(beat[3])))
            if measure_no % self.staff_width == 0 and not measure_no == 0:
                staff_str += s_s + "|\n" + a_s + "|\n" + t_s + "|\n" + b_s + "|\n\n"
                s_s = ""
                a_s = ""
                t_s = ""
                b_s = ""
            elif measure_no == len(self.staff) - 1:
                staff_str += s_s + "||\n" + a_s + "||\n" + t_s + "||\n" + b_s + "||\n"
            else:
                s_s += "| "
                a_s += "| "
                t_s += "| "
                b_s += "| "
            measure_no += 1
        return staff_str

class Voice:
    def __init__(self, voice_range):
        self.voice_range = voice_range

    def check_range(self, note):
        return note >= self.voice_range[0] and note <= self.voice_range[1]

class Soprano(Voice):
    def __init__(self):
        super().__init__((C(4), A(5)))

class Alto(Voice):
    def __init__(self):
        super().__init__((F(3), D(5)))

class Tenor(Voice):
    def __init__(self):
        super().__init__((C(3), A(4)))

class Bass(Voice):
    def __init__(self):
        super().__init__((F(2), D(4)))