from notes import *
import random

# # # # # # # # # # # # # # # # #
# Functions to find next chords #
# # # # # # # # # # # # # # # # #

def new_chord_same_note(key, chord, old_chord_tone = None, new_chord_tone = None, new_quality = None, new_type = None):
    """ get chord with same note as current chord """
    old_chord_tone_weights = [1, 1, 1, 1]
    new_quality_weights = [1, 1]
    new_chord_tone_weights = [1, 1, 1, 1]
    new_type_seventh_weights = [2, 2, 2, 2, 1, 1, 1]
    new_type_triad_weights = [2, 2, 1, 1]
    if old_chord_tone == None:
        if chord.quality == "triad":
            old_chord_tone = random.choice([1]*old_chord_tone_weights[0] + [3]*old_chord_tone_weights[1] + [5]*old_chord_tone_weights[2])
        elif chord.quality == "seventh":
            old_chord_tone = random.choice([1]*old_chord_tone_weights[0] + [3]*old_chord_tone_weights[1] + [5]*old_chord_tone_weights[2] + [7]*old_chord_tone_weights[3])
    if new_quality == None:
        new_quality = random.choice([True]*new_quality_weights[0] + [False]*new_quality_weights[1])
    if new_chord_tone == None:
        if new_quality:
            new_chord_tone = random.choice([1]*new_chord_tone_weights[0] + [3]*new_chord_tone_weights[1] + [5]*new_chord_tone_weights[2] + [7]*new_chord_tone_weights[3])
        else:
            new_chord_tone = random.choice([1]*new_chord_tone_weights[0] + [3]*new_chord_tone_weights[1] + [5]*new_chord_tone_weights[2])
    if new_type == None:
        if new_quality:
            new_type = random.choice(["major"]*new_type_seventh_weights[0] +  ["minor"]*new_type_seventh_weights[1] + ["major minor"]*new_type_seventh_weights[2] + ["minor major"]*new_type_seventh_weights[3] + ["half diminished"]*new_type_seventh_weights[4] + ["full diminished"]*new_type_seventh_weights[5] + ["augmented"]*new_type_seventh_weights[6])
        else:
            new_type = random.choice(["major"]*new_type_triad_weights[0] + ["minor"]*new_type_triad_weights[1] + ["diminished"]*new_type_triad_weights[2] + ["augmented"]*new_type_triad_weights[3])
    new_chord = Chord(False, new_quality, note = chord.get_note(old_chord_tone), chord_tone = new_chord_tone, chord_type = new_type)
    return new_chord

def new_chord_neighbor_note(key, chord, old_chord_tone = None, new_chord_tone = None, neighbor_func = None, new_quality = None, new_type = None):
    """ get chord with neighboring note to current chord """
    old_chord_tone_weights = [1, 1, 1, 1]
    new_quality_weights = [1, 1]
    new_chord_tone_weights = [1, 1, 1, 1]
    new_type_seventh_weights = [2, 2, 2, 2, 1, 1, 1]
    new_type_triad_weights = [2, 2, 1, 1]
    neighbor_func_weights = [1, 1, 1, 1]
    if old_chord_tone == None:
        if chord.quality == "triad":
            old_chord_tone = random.choice([1]*old_chord_tone_weights[0] + [3]*old_chord_tone_weights[1] + [5]*old_chord_tone_weights[2])
        elif chord.quality == "seventh":
            old_chord_tone = random.choice([1]*old_chord_tone_weights[0] + [3]*old_chord_tone_weights[1] + [5]*old_chord_tone_weights[2] + [7]*old_chord_tone_weights[3])
    if new_quality == None:
        new_quality = random.choice([True]*new_quality_weights[0] + [False]*new_quality_weights[1])
    if new_chord_tone == None:
        if new_quality:
            new_chord_tone = random.choice([1]*new_chord_tone_weights[0] + [3]*new_chord_tone_weights[1] + [5]*new_chord_tone_weights[2] + [7]*new_chord_tone_weights[3])
        else:
            new_chord_tone = random.choice([1]*new_chord_tone_weights[0] + [3]*new_chord_tone_weights[1] + [5]*new_chord_tone_weights[2])
    if new_type == None:
        if new_quality:
            new_type = random.choice(["major"]*new_type_seventh_weights[0] +  ["minor"]*new_type_seventh_weights[1] + ["major minor"]*new_type_seventh_weights[2] + ["minor major"]*new_type_seventh_weights[3] + ["half diminished"]*new_type_seventh_weights[4] + ["full diminished"]*new_type_seventh_weights[5] + ["augmented"]*new_type_seventh_weights[6])
        else:
            new_type = random.choice(["major"]*new_type_triad_weights[0] + ["minor"]*new_type_triad_weights[1] + ["diminished"]*new_type_triad_weights[2] + ["augmented"]*new_type_triad_weights[3])
    if neighbor_func == None:
        neighbor_func = random.choice([0]*neighbor_func_weights[0] + [1]*neighbor_func_weights[1] + [2]*neighbor_func_weights[2] + [3]*neighbor_func_weights[3])
    if neighbor_func == 0:
        new_chord = Chord(False, new_quality, note = chord.get_note(old_chord_tone).add_half_step(), chord_tone = new_chord_tone, chord_type = new_type)
    elif neighbor_func == 1:
        new_chord = Chord(False, new_quality, note = chord.get_note(old_chord_tone).add_whole_step(), chord_tone = new_chord_tone, chord_type = new_type)
    elif neighbor_func == 2:
        new_chord = Chord(False, new_quality, note = chord.get_note(old_chord_tone).sub_half_step(), chord_tone = new_chord_tone, chord_type = new_type)
    elif neighbor_func == 3:
        new_chord = Chord(False, new_quality, note = chord.get_note(old_chord_tone).sub_whole_step(), chord_tone = new_chord_tone, chord_type = new_type)
    return new_chord

def new_tonal_chord(key, new_quality = None, new_scale_degree = None):
    """ get chord based on key of current chord """
    new_scale_degree_weights = [1, 1, 1, 1, 1, 1, 1, 1]
    new_quality_weights = [1, 2]
    if new_scale_degree == None:
        new_scale_degree = random.choice([1]*new_scale_degree_weights[0] + [2]*new_scale_degree_weights[1] + [3]*new_scale_degree_weights[2] + [4]*new_scale_degree_weights[3] + [5]*new_scale_degree_weights[4] + [6]*new_scale_degree_weights[5] + [7]*new_scale_degree_weights[6])
    if new_quality == None:
        new_quality = new_quality = random.choice([True]*new_quality_weights[0] + [False]*new_quality_weights[1])
    new_chord = Chord(True, key = key, scale_degree = new_scale_degree)
    return new_chord

def new_function_chord(key, chord, progression = None):
    """ get note based on chord progression function """
    progression_types = ["5-1M", "5-1m", "5-6m", "5-6M", "7-1M", "7-1m"]
    progression_type_weights = [1, 1, 1, 1, 1, 1]
    
    if progression == None:
        weighted = []
        if chord.chord_type == "major minor":
            for i in range(4):
                weighted.extend([progression_types[i]]*progression_type_weights[i])
        elif chord.chord_type == "diminished":
            for i in range(4, 6):
                weighted.extend([progression_types[i]]*progression_type_weights[i])
        else:
            for i in range(len(progression_types)):
                weighted.extend([progression_types[i]]*progression_type_weights[i])
        progression = random.choice(weighted)
    if progression == "5-1M":
        new_chord = Chord(False, seventh = False, note = chord.get_note(1), chord_tone = 5, chord_type = "major")
    elif progression == "5-1m":
        new_chord = Chord(False, seventh = False, note = chord.get_note(1), chord_tone = 5, chord_type = "minor")
    if progression == "7-1M":
        new_chord = Chord(False, seventh = False, note = chord.get_note(1).add_half_step(), chord_tone = 1, chord_type = "major")
    if progression == "7-1m":
        new_chord = Chord(False, seventh = False, note = chord.get_note(1).add_half_step(), chord_tone = 1, chord_type = "minor")
    if progression == "5-6m":
        new_chord = Chord(False, seventh = False, note = chord.get_note(1).add_whole_step(), chord_tone = 1, chord_type = "minor")
    if progression == "5-6M":
        new_chord = Chord(False, seventh = False, note = chord.get_note(1).add_half_step(), chord_tone = 1, chord_type = "major")
    return new_chord