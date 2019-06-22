# pitches based on http://pages.mtu.edu/~suits/notefreqs.html
# from C4 (261.63) to B4 (493.88)

# # # # #
# NOTES #
# # # # #

class Note:
    def __init__(self, n, pitch, o = None):
        self.note = n # a string representing the note
        self.octave = o # a number representing the octave of the note
        self.pitch = pitch

    def __str__(self):
        if not self.octave == None:
            return self.note + str(self.octave)
        return self.note

    def __eq__ (self, other):
        if other == None:
            return False
        if self.octave == None or other.octave == None:
            return self.note == other.note
        return self.abs_pitch() == other.abs_pitch()

    def __ge__(self, other): # true if self >= other
        if self.octave == None or other.octave == None:
            raise Exception("Cannot compare notes without octaves.")
        if self.octave > other.octave:
            return True
        return self.abs_pitch() >= other.abs_pitch()

    def __le__(self, other): # true if self <= other
        if self.octave == None or other.octave == None:
            raise Exception("Cannot compare notes without octaves.")
        return self.abs_pitch() <= other.abs_pitch()   

    def abs_pitch(self):
        if self.octave == None:
            raise Exception("Cannot get absolute pitch without octave.")
        return self.pitch * 2**(self.octave - 4)

    def sub_by_step(self, other):
        """ return tuple of number of steps upward from self to other upward,
        negative number of steps from self to other downward (based on letter name) """
        if str(self)[0] == "A":
            num_self = 0
        elif str(self)[0] == "B":
            num_self = 1
        elif str(self)[0] == "C":
            num_self = 2
        elif str(self)[0] == "D":
            num_self = 3
        elif str(self)[0] == "E":
            num_self = 4
        elif str(self)[0] == "F":
            num_self = 5
        elif str(self)[0] == "G":
            num_self = 6
        else:
            raise Exception("Invalid note: " + str(self))

        if str(other)[0] == "A":
            num_other = 0
        elif str(other)[0] == "B":
            num_other = 1
        elif str(other)[0] == "C":
            num_other = 2
        elif str(other)[0] == "D":
            num_other = 3
        elif str(other)[0] == "E":
            num_other = 4
        elif str(other)[0] == "F":
            num_other = 5
        elif str(other)[0] == "G":
            num_other = 6
        else:
            raise Exception("Invalid note: " + str(other))

        diff = abs(num_other - num_self)
        other_diff = 7 - diff

        if num_other in [num_self, (num_self+1)%7, (num_self+2)%7, (num_self+3)%7]:
            # smaller difference is moving upward or staying same
            return (min(diff, other_diff), -max(diff, other_diff))
        else:
            # smaller difference is moving downward
            return (max(diff, other_diff), -min(diff, other_diff))

def make_note(s, o = None):
    if s[-1] in "1234567890":
        s = s[:-1]
    if s == "Abb":
        return Abb(o)
    if s == "Ab":
        return Ab(o)
    if s == "A":
        return A(o)
    if s == "Ax":
        return Ax(o)
    if s == "Axx":
        return Axx(o)
    if s == "Bbb":
        return Bbb(o)
    if s == "Bb":
        return Bb(o)
    if s == "B":
        return B(o)
    if s == "Bx":
        return Bx(o)
    if s == "Bxx":
        return Bxx(o)
    if s == "Cbb":
        return Cbb(o)
    if s == "Cb":
        return Cb(o)
    if s == "C":
        return C(o)
    if s == "Cx":
        return Cx(o)
    if s == "Cxx":
        return Cxx(o)
    if s == "Dbb":
        return Dbb(o)
    if s == "Db":
        return Db(o)
    if s == "D":
        return D(o)
    if s == "Dx":
        return Dx(o)
    if s == "Dxx":
        return Dxx(o)
    if s == "Ebb":
        return Ebb(o)
    if s == "Eb":
        return Eb(o)
    if s == "E":
        return E(o)
    if s == "Ex":
        return Ex(o)
    if s == "Exx":
        return Exx(o)
    if s == "Fbb":
        return Fbb(o)
    if s == "Fb":
        return Fb(o)
    if s == "F":
        return F(o)
    if s == "Fx":
        return Fx(o)
    if s == "Fxx":
        return Fxx(o)
    if s == "Gbb":
        return Gbb(o)
    if s == "Gb":
        return Gb(o)
    if s == "G":
        return G(o)
    if s == "Gx":
        return Gx(o)
    if s == "Gxx":
        return Gxx(o)
    raise Exception("Incorrect input for make_note(): " + s)

##### A #####

class A(Note):
    def __init__(self, o = None):
        super().__init__("A", 440.00, o)

    def add_half_step(self):
        return Bb()
    
    def add_whole_step(self):
        return B()
    
    def sub_half_step(self):
        return Gx()
    
    def sub_whole_step(self):
        return G()

    def sharp(self):
        return Ax()
    
    def flat(self):
        return Ab()

class Ab(Note):
    def __init__(self, o = None):
        super().__init__("Ab", 415.30, o)

    def add_half_step(self):
        return Bbb()
    
    def add_whole_step(self):
        return Bb()
    
    def sub_half_step(self):
        return G()
    
    def sub_whole_step(self):
        return Gb()

    def sharp(self):
        return A()
    
    def flat(self):
        return Abb()

class Ax(Note):
    def __init__(self, o = None):
        super().__init__("Ax", 466.16, o)
    
    def add_half_step(self):
        return B()
    
    def add_whole_step(self):
        return Bx()
    
    def sub_half_step(self):
        return Gxx()
    
    def sub_whole_step(self):
        return Gx()

    def sharp(self):
        return Axx()
    
    def flat(self):
        return A()

class Abb(Note):
    def __init__(self, o = None):
        super().__init__("Abb", 392.00, o)

    def add_half_step(self):
        return Ab()
    
    def add_whole_step(self):
        return Bbb()
    
    def sub_half_step(self):
        return Gb()
    
    def sub_whole_step(self):
        return Gbb()

    def sharp(self):
        return Ab()
    
    def flat(self):
        return Gb()

class Axx(Note):
    def __init__(self, o = None):
        super().__init__("Axx", 493.88, o)
    
    def add_half_step(self):
        return Bx()
    
    def add_whole_step(self):
        return Bxx()
    
    def sub_half_step(self):
        return Ax()
    
    def sub_whole_step(self):
        return Gxx()

    def sharp(self):
        return Bx()
    
    def flat(self):
        return Ax()

##### B #####

class B(Note):
    def __init__(self, o = None):
        super().__init__("B", 493.88, o)

    def add_half_step(self):
        return C()
    
    def add_whole_step(self):
        return Cx()
    
    def sub_half_step(self):
        return Ax()
    
    def sub_whole_step(self):
        return A()

    def sharp(self):
        return Bx()
    
    def flat(self):
        return Bb()

class Bb(Note):
    def __init__(self, o = None):
        super().__init__("Bb", 466.16, o)

    def add_half_step(self):
        return Cb()
    
    def add_whole_step(self):
        return C()
    
    def sub_half_step(self):
        return A()
    
    def sub_whole_step(self):
        return Ab()

    def sharp(self):
        return B()
    
    def flat(self):
        return Bbb()

class Bx(Note):
    def __init__(self, o = None):
        super().__init__("Bx", 523.25, o)
    
    def add_half_step(self):
        return Cx()
    
    def add_whole_step(self):
        return Cxx()
    
    def sub_half_step(self):
        return Axx()
    
    def sub_whole_step(self):
        return Ax()

    def sharp(self):
        return Bxx()
    
    def flat(self):
        return B()

class Bbb(Note):
    def __init__(self, o = None):
        super().__init__("Bbb", 440.00, o)

    def add_half_step(self):
        return Bb()
    
    def add_whole_step(self):
        return Cb()
    
    def sub_half_step(self):
        return Ab()
    
    def sub_whole_step(self):
        return Abb()

    def sharp(self):
        return Bb()
    
    def flat(self):
        return Ab()

class Bxx(Note):
    def __init__(self, o = None):
        super().__init__("Bxx", 554.37, o)
    
    def add_half_step(self):
        return Cxx()
    
    def add_whole_step(self):
        return Dx()
    
    def sub_half_step(self):
        return Bx()
    
    def sub_whole_step(self):
        return Axx()

    def sharp(self):
        return Cxx()
    
    def flat(self):
        return Bx()

##### C #####

class C(Note):
    def __init__(self, o = None):
        super().__init__("C", 261.63, o)

    def add_half_step(self):
        return Db()
    
    def add_whole_step(self):
        return D()
    
    def sub_half_step(self):
        return B()
    
    def sub_whole_step(self):
        return Bb()

    def sharp(self):
        return Cx()
    
    def flat(self):
        return Cb()

class Cb(Note):
    def __init__(self, o = None):
        super().__init__("Cb", 246.94, o)

    def add_half_step(self):
        return Dbb()
    
    def add_whole_step(self):
        return Db()
    
    def sub_half_step(self):
        return Bb()
    
    def sub_whole_step(self):
        return Bbb()

    def sharp(self):
        return C()
    
    def flat(self):
        return Cbb()

class Cx(Note):
    def __init__(self, o = None):
        super().__init__("Cx", 277.18, o)
    
    def add_half_step(self):
        return D()
    
    def add_whole_step(self):
        return Dx()
    
    def sub_half_step(self):
        return Bx()
    
    def sub_whole_step(self):
        return B()

    def sharp(self):
        return Cxx()
    
    def flat(self):
        return C()

class Cbb(Note):
    def __init__(self, o = None):
        super().__init__("Cbb", 233.08, o)

    def add_half_step(self):
        return Cb()
    
    def add_whole_step(self):
        return Dbb()
    
    def sub_half_step(self):
        return Bbb()
    
    def sub_whole_step(self):
        return Ab()

    def sharp(self):
        return Cb()
    
    def flat(self):
        return Bbb()

class Cxx(Note):
    def __init__(self, o = None):
        super().__init__("Cxx", 293.66, o)
    
    def add_half_step(self):
        return Dx()
    
    def add_whole_step(self):
        return Dxx()
    
    def sub_half_step(self):
        return Bxx()
    
    def sub_whole_step(self):
        return Bx()

    def sharp(self):
        return Dx()
    
    def flat(self):
        return Cx()

##### D #####

class D(Note):
    def __init__(self, o = None):
        super().__init__("D", 293.66, o)

    def add_half_step(self):
        return Eb()
    
    def add_whole_step(self):
        return E()
    
    def sub_half_step(self):
        return Cx()
    
    def sub_whole_step(self):
        return C()

    def sharp(self):
        return Dx()
    
    def flat(self):
        return Db()

class Db(Note):
    def __init__(self, o = None):
        super().__init__("Db", 277.18, o)

    def add_half_step(self):
        return Ebb()
    
    def add_whole_step(self):
        return Eb()
    
    def sub_half_step(self):
        return C()
    
    def sub_whole_step(self):
        return Cb()

    def sharp(self):
        return D()
    
    def flat(self):
        return Dbb()

class Dx(Note):
    def __init__(self, o = None):
        super().__init__("Dx", 311.13, o)
    
    def add_half_step(self):
        return E()
    
    def add_whole_step(self):
        return Ex()
    
    def sub_half_step(self):
        return Cxx()
    
    def sub_whole_step(self):
        return Cx()

    def sharp(self):
        return Dxx()
    
    def flat(self):
        return D()

class Dbb(Note):
    def __init__(self, o = None):
        super().__init__("Dbb", 261.63, o)

    def add_half_step(self):
        return Db()
    
    def add_whole_step(self):
        return Ebb()
    
    def sub_half_step(self):
        return Cb()
    
    def sub_whole_step(self):
        return Cbb()

    def sharp(self):
        return Db()
    
    def flat(self):
        return Cb()

class Dxx(Note):
    def __init__(self, o = None):
        super().__init__("Dxx", 329.63, o)
    
    def add_half_step(self):
        return Ex()
    
    def add_whole_step(self):
        return Exx()
    
    def sub_half_step(self):
        return Dx()
    
    def sub_whole_step(self):
        return Cxx()

    def sharp(self):
        return Ex()
    
    def flat(self):
        return Dx()

##### E #####

class E(Note):
    def __init__(self, o = None):
        super().__init__("E", 329.63, o)

    def add_half_step(self):
        return F()
    
    def add_whole_step(self):
        return Fx()
    
    def sub_half_step(self):
        return Dx()
    
    def sub_whole_step(self):
        return D()

    def sharp(self):
        return Ex()
    
    def flat(self):
        return Eb()

class Eb(Note):
    def __init__(self, o = None):
        super().__init__("Eb", 311.13, o)

    def add_half_step(self):
        return Fb()
    
    def add_whole_step(self):
        return F()
    
    def sub_half_step(self):
        return D()
    
    def sub_whole_step(self):
        return Db()

    def sharp(self):
        return E()
    
    def flat(self):
        return Ebb()

class Ex(Note):
    def __init__(self, o = None):
        super().__init__("Ex", 349.23, o)
    
    def add_half_step(self):
        return Fx()
    
    def add_whole_step(self):
        return Fxx()
    
    def sub_half_step(self):
        return Dxx()
    
    def sub_whole_step(self):
        return Dx()

    def sharp(self):
        return Exx()
    
    def flat(self):
        return E()

class Ebb(Note):
    def __init__(self, o = None):
        super().__init__("Ebb", 293.66, o)

    def add_half_step(self):
        return Fbb()
    
    def add_whole_step(self):
        return Fb()
    
    def sub_half_step(self):
        return Db()
    
    def sub_whole_step(self):
        return Dbb()

    def sharp(self):
        return Eb()
    
    def flat(self):
        return Db()

class Exx(Note):
    def __init__(self, o = None):
        super().__init__("Exx", 369.99, o)
    
    def add_half_step(self):
        return Fxx()
    
    def add_whole_step(self):
        return Gx()
    
    def sub_half_step(self):
        return Ex()
    
    def sub_whole_step(self):
        return Dxx()

    def sharp(self):
        return Fxx()
    
    def flat(self):
        return Ex()

##### F #####

class F(Note):
    def __init__(self, o = None):
        super().__init__("F", 349.23, o)

    def add_half_step(self):
        return Gb()
    
    def add_whole_step(self):
        return G()
    
    def sub_half_step(self):
        return E()
    
    def sub_whole_step(self):
        return Eb()

    def sharp(self):
        return Fx()
    
    def flat(self):
        return Fb()

class Fb(Note):
    def __init__(self, o = None):
        super().__init__("Fb", 329.63, o)

    def add_half_step(self):
        return Gbb()
    
    def add_whole_step(self):
        return Gb()
    
    def sub_half_step(self):
        return Eb()
    
    def sub_whole_step(self):
        return Ebb()

    def sharp(self):
        return F()
    
    def flat(self):
        return Fbb()

class Fx(Note):
    def __init__(self, o = None):
        super().__init__("Fx", 369.99, o)
    
    def add_half_step(self):
        return G()
    
    def add_whole_step(self):
        return Gx()
    
    def sub_half_step(self):
        return Ex()
    
    def sub_whole_step(self):
        return E()

    def sharp(self):
        return Fxx()
    
    def flat(self):
        return F()

class Fbb(Note):
    def __init__(self, o = None):
        super().__init__("Fbb", 311.13, o)

    def add_half_step(self):
        return Fb()
    
    def add_whole_step(self):
        return Gbb()
    
    def sub_half_step(self):
        return Ebb()
    
    def sub_whole_step(self):
        return Db()

    def sharp(self):
        return Fb()
    
    def flat(self):
        return Ebb()

class Fxx(Note):
    def __init__(self, o = None):
        super().__init__("Fxx", 392.00, o)
    
    def add_half_step(self):
        return Gx()
    
    def add_whole_step(self):
        return Gxx()
    
    def sub_half_step(self):
        return Exx()
    
    def sub_whole_step(self):
        return Ex()

    def sharp(self):
        return Gx()
    
    def flat(self):
        return Fx()

##### G #####

class G(Note):
    def __init__(self, o = None):
        super().__init__("G", 392.00, o)

    def add_half_step(self):
        return Ab()
    
    def add_whole_step(self):
        return A()
    
    def sub_half_step(self):
        return Fx()
    
    def sub_whole_step(self):
        return F()

    def sharp(self):
        return Gx()
    
    def flat(self):
        return Gb()

class Gb(Note):
    def __init__(self, o = None):
        super().__init__("Gb", 369.99, o)

    def add_half_step(self):
        return Abb()
    
    def add_whole_step(self):
        return Ab()
    
    def sub_half_step(self):
        return F()
    
    def sub_whole_step(self):
        return Fb()

    def sharp(self):
        return G()
    
    def flat(self):
        return Gbb()

class Gx(Note):
    def __init__(self, o = None):
        super().__init__("Gx", 415.30, o)
    
    def add_half_step(self):
        return A()
    
    def add_whole_step(self):
        return Ax()
    
    def sub_half_step(self):
        return Fxx()
    
    def sub_whole_step(self):
        return Fx()

    def sharp(self):
        return Gxx()
    
    def flat(self):
        return G()

class Gbb(Note):
    def __init__(self, o = None):
        super().__init__("Gbb", 349.23, o)

    def add_half_step(self):
        return Gb()
    
    def add_whole_step(self):
        return Abb()
    
    def sub_half_step(self):
        return Fb()
    
    def sub_whole_step(self):
        return Fbb()

    def sharp(self):
        return Gb()
    
    def flat(self):
        return Fb()

class Gxx(Note):
    def __init__(self, o = None):
        super().__init__("Gxx", 440.00, o)
    
    def add_half_step(self):
        return Ax()
    
    def add_whole_step(self):
        return Axx()
    
    def sub_half_step(self):
        return Gx()
    
    def sub_whole_step(self):
        return Fxx()

    def sharp(self):
        return Ax()
    
    def flat(self):
        return Gx()

# # # # #
# KEYS  #
# # # # #
class Key:
    def __init__(self, tonic, m):
        if m == "major":
            self.mode = "major"
            self.one = tonic
            self.two = self.one.add_whole_step()
            self.three = self.two.add_whole_step()
            self.four = self.three.add_half_step()
            self.five = self.four.add_whole_step()
            self.six = self.five.add_whole_step()
            self.seven = self.six.add_whole_step()
        elif m == "minor":
            self.mode = "minor"
            self.one = tonic
            self.two = self.one.add_whole_step()
            self.three = self.two.add_half_step()
            self.four = self.three.add_whole_step()
            self.five = self.four.add_whole_step()
            self.six = self.five.add_half_step()
            self.seven = self.six.add_whole_step()
        else:
            raise Exception("Invalid Mode: " + m)
        
    def __str__(self):
        return str(self.one) + " " + self.mode + ":\n" + str(self.one) + "\n" + str(self.two) + "\n" + str(self.three) + "\n" + str(self.four) + "\n" + str(self.five) + "\n" + str(self.six) + "\n" + str(self.seven) + "\n" + str(self.one)

    def get_note(self, degree):
        """ get note based on scale degree int """
        if degree == 1:
            return self.one
        if degree == 2:
            return self.two
        if degree == 3:
            return self.three
        if degree == 4:
            return self.four
        if degree == 5:
            return self.five
        if degree == 6:
            return self.six
        if degree == 7:
            return self.seven
        raise Exception("Invalid Scale Degree: " + str(degree))

# # # # # #
# CHORDS  #
# # # # # #

class Chord:
    def __init__(self, use_key, seventh = False, key = None, scale_degree = None, note = None, chord_tone = None, chord_type = None):
        # seventh: if true make 7th chord, else make triad
        # use_key: boolean; if true, generate based on key, if false, generate based on note
            # key: need key (Key object), scale degree (int), seventh (bool)
            # note: need note (Note object), chord_tone (int), seventh (bool), chord_type (str)
        if use_key:
            if key == None or scale_degree == None:
                raise Exception("Need key and scale degree to make chord by key.")
            self.chord = []
            self.chord.append(key.get_note(scale_degree))
            second_tone = (scale_degree + 1) % 7 + 1
            self.chord.append(key.get_note(second_tone))
            third_tone = (second_tone + 1) % 7 + 1
            self.chord.append(key.get_note(third_tone))
            if seventh:
                fourth_tone = (third_tone + 1) % 7 + 1
                self.chord.append(key.get_note(fourth_tone))
                self.quality = "seventh"
            else:
                self.quality = "triad"
            if key.mode == "major":
                if seventh:
                    if scale_degree in [1, 4]:
                        self.chord_type = "major"
                    elif scale_degree == 5:
                        self.chord_type = "major minor"
                    elif scale_degree in [2, 3, 6]:
                        self.chord_type = "minor"
                    elif scale_degree == 7:
                        self.chord_type = "half diminished"
                else:
                    if scale_degree in [1, 4, 5]:
                        self.chord_type = "major"
                    elif scale_degree in [2, 3, 6]:
                        self.chord_type = "minor"
                    elif scale_degree == 7:
                        self.chord_type = "diminished"
            elif key.mode == "minor":
                if seventh:
                    if scale_degree in [3, 6]:
                        self.chord_type = "major"
                    elif scale_degree == 7:
                        self.chord_type = "major minor"
                    elif scale_degree in [1, 4, 5]:
                        self.chord_type = "minor"
                    elif scale_degree == 2:
                        self.chord_type = "half diminished"
                else:
                    if scale_degree in [3, 6, 7]:
                        self.chord_type = "major"
                    elif scale_degree in [1, 4, 5]:
                        self.chord_type = "minor"
                    elif scale_degree == 2:
                        self.chord_type = "diminished"
        else:
            if note == None or chord_tone == None or chord_type == None:
                raise Exception("Need note, chord_tone, and chord_type to make chord by note.")
            if not chord_tone in [1, 3, 5, 7]:
                raise Exception("Chord tone must be in chord - 1, 3, 5, or 7.")
            self.chord = []
            self.chord_type = chord_type
            if chord_tone == 1:
                if seventh:
                    self.quality = "seventh"
                    if chord_type == "major":
                        second_tone = note.add_whole_step().add_whole_step()
                        third_tone = second_tone.add_whole_step().add_half_step()
                        fourth_tone = third_tone.add_whole_step().add_whole_step()
                    elif chord_type == "minor":
                        second_tone = note.add_whole_step().add_half_step()
                        third_tone = second_tone.add_whole_step().add_whole_step()
                        fourth_tone = third_tone.add_whole_step().add_half_step()
                    elif chord_type == "major minor":
                        second_tone = note.add_whole_step().add_whole_step()
                        third_tone = second_tone.add_whole_step().add_half_step()
                        fourth_tone = third_tone.add_whole_step().add_half_step()
                    elif chord_type == "minor major":
                        second_tone = note.add_whole_step().add_half_step()
                        third_tone = second_tone.add_whole_step().add_whole_step()
                        fourth_tone = third_tone.add_whole_step().add_whole_step()
                    elif chord_type == "half diminished":
                        second_tone = note.add_whole_step().add_half_step()
                        third_tone = second_tone.add_whole_step().add_half_step()
                        fourth_tone = third_tone.add_whole_step().add_whole_step()
                    elif chord_type == "full diminished":
                        second_tone = note.add_whole_step().add_half_step()
                        third_tone = second_tone.add_whole_step().add_half_step()
                        fourth_tone = third_tone.add_whole_step().add_half_step()
                    elif chord_type == "augmented":
                        second_tone = note.add_whole_step().add_whole_step()
                        third_tone = second_tone.add_whole_step().add_whole_step()
                        fourth_tone = third_tone.add_whole_step().add_half_step()
                    else:
                        raise Exception("Not a valid chord type: " + chord_type)
                    self.chord = [note, second_tone, third_tone, fourth_tone]
                else:
                    self.quality = "triad"
                    if chord_type == "major":
                        second_tone = note.add_whole_step().add_whole_step()
                        third_tone = second_tone.add_whole_step().add_half_step()
                    elif chord_type == "minor":
                        second_tone = note.add_whole_step().add_half_step()
                        third_tone = second_tone.add_whole_step().add_whole_step()
                    elif chord_type == "diminished":
                        second_tone = note.add_whole_step().add_half_step()
                        third_tone = second_tone.add_whole_step().add_half_step()
                    elif chord_type == "augmented":
                        second_tone = note.add_whole_step().add_whole_step()
                        third_tone = second_tone.add_whole_step().add_whole_step()
                    else:
                        raise Exception("Not a valid chord type: " + chord_type)
                    self.chord = [note, second_tone, third_tone]
            elif chord_tone == 3:
                if seventh:
                    self.quality = "seventh"
                    if chord_type == "major":
                        first_tone = note.sub_whole_step().sub_whole_step()
                        third_tone = note.add_whole_step().add_half_step()
                        fourth_tone = third_tone.add_whole_step().add_whole_step()
                    elif chord_type == "minor":
                        first_tone = note.sub_whole_step().sub_half_step()
                        third_tone = note.add_whole_step().add_whole_step()
                        fourth_tone = third_tone.add_whole_step().add_half_step()
                    elif chord_type == "major minor":
                        first_tone = note.sub_whole_step().sub_whole_step()
                        third_tone = note.add_whole_step().add_half_step()
                        fourth_tone = third_tone.add_whole_step().add_half_step()
                    elif chord_type == "minor major":
                        first_tone = note.sub_whole_step().sub_half_step()
                        third_tone = note.add_whole_step().add_whole_step()
                        fourth_tone = third_tone.add_whole_step().add_whole_step()
                    elif chord_type == "half diminished":
                        first_tone = note.sub_whole_step().sub_half_step()
                        third_tone = note.add_whole_step().add_half_step()
                        fourth_tone = third_tone.add_whole_step().add_whole_step()
                    elif chord_type == "full diminished":
                        first_tone = note.sub_whole_step().sub_half_step()
                        third_tone = note.add_whole_step().add_half_step()
                        fourth_tone = third_tone.add_whole_step().add_half_step()
                    elif chord_type == "augmented":
                        first_tone = note.sub_whole_step().sub_whole_step()
                        third_tone = note.add_whole_step().add_whole_step()
                        fourth_tone = third_tone.add_whole_step().add_whole_step()
                    else:
                        raise Exception("Not a valid chord type: " + chord_type)
                    self.chord = [first_tone, note, third_tone, fourth_tone]
                else:
                    self.quality = "triad"
                    if chord_type == "major":
                        first_tone = note.sub_whole_step().sub_whole_step()
                        third_tone = note.add_whole_step().add_half_step()
                    elif chord_type == "minor":
                        first_tone = note.sub_whole_step().sub_half_step()
                        third_tone = note.add_whole_step().add_whole_step()
                    elif chord_type == "diminished":
                        first_tone = note.sub_whole_step().sub_half_step()
                        third_tone = note.add_whole_step().add_half_step()
                    elif chord_type == "augmented":
                        first_tone = note.sub_whole_step().sub_whole_step()
                        third_tone = note.add_whole_step().add_whole_step()
                    else:
                        raise Exception("Not a valid chord type: " + chord_type)
                    self.chord = [first_tone, note, third_tone]
            elif chord_tone == 5:
                if seventh:
                    self.quality = "seventh"
                    if chord_type == "major":
                        second_tone = note.sub_whole_step().sub_half_step()
                        first_tone = second_tone.sub_whole_step().sub_whole_step()
                        fourth_tone = note.add_whole_step().add_whole_step()
                    elif chord_type == "minor":
                        second_tone = note.sub_whole_step().sub_whole_step()
                        first_tone = second_tone.sub_whole_step().sub_half_step()
                        fourth_tone = note.add_whole_step().add_half_step()
                    elif chord_type == "major minor":
                        second_tone = note.sub_whole_step().sub_half_step()
                        first_tone = second_tone.sub_whole_step().sub_whole_step()
                        fourth_tone = note.add_whole_step().add_half_step()
                    elif chord_type == "minor major":
                        second_tone = note.sub_whole_step().sub_whole_step()
                        first_tone = second_tone.sub_whole_step().sub_half_step()
                        fourth_tone = note.add_whole_step().add_whole_step()
                    elif chord_type == "half diminished":
                        second_tone = note.sub_whole_step().sub_half_step()
                        first_tone = second_tone.sub_whole_step().sub_half_step()
                        fourth_tone = note.add_whole_step().add_whole_step()
                    elif chord_type == "full diminished":
                        second_tone = note.sub_whole_step().sub_half_step()
                        first_tone = second_tone.sub_whole_step().sub_half_step()
                        fourth_tone = note.add_whole_step().add_half_step()
                    elif chord_type == "augmented":
                        second_tone = note.sub_whole_step().sub_whole_step()
                        first_tone = second_tone.sub_whole_step().sub_whole_step()
                        fourth_tone = note.add_whole_step().add_half_step()
                    else:
                        raise Exception("Not a valid chord type: " + chord_type)
                    self.chord = [first_tone, second_tone, note, fourth_tone]
                else:
                    self.quality = "triad"
                    if chord_type == "major":
                        second_tone = note.sub_whole_step().sub_half_step()
                        first_tone = second_tone.sub_whole_step().sub_whole_step()
                    elif chord_type == "minor":
                        second_tone = note.sub_whole_step().sub_whole_step()
                        first_tone = second_tone.sub_whole_step().sub_half_step()
                    elif chord_type == "diminished":
                        second_tone = note.sub_whole_step().sub_half_step()
                        first_tone = second_tone.sub_whole_step().sub_half_step()
                    elif chord_type == "augmented":
                        second_tone = note.sub_whole_step().sub_whole_step()
                        first_tone = second_tone.sub_whole_step().sub_whole_step()
                    else:
                        raise Exception("Not a valid chord type: " + chord_type)
                    self.chord = [first_tone, second_tone, note]
            elif chord_tone == 7:
                if not seventh:
                    raise Exception("Cannot construct triad from seventh chord tone.")
                else:
                    self.quality = "seventh"
                    if chord_type == "major":
                        third_tone = note.sub_whole_step().sub_whole_step()
                        second_tone = third_tone.sub_whole_step().sub_half_step()
                        first_tone = second_tone.sub_whole_step().sub_whole_step()
                    elif chord_type == "minor":
                        third_tone = note.sub_whole_step().sub_half_step()
                        second_tone = third_tone.sub_whole_step().sub_whole_step()
                        first_tone = second_tone.sub_whole_step().sub_half_step()
                    elif chord_type == "major minor":
                        third_tone = note.sub_whole_step().sub_half_step()
                        second_tone = third_tone.sub_whole_step().sub_half_step()
                        first_tone = second_tone.sub_whole_step().sub_whole_step()
                    elif chord_type == "minor major":
                        third_tone = note.sub_whole_step().sub_whole_step()
                        second_tone = third_tone.sub_whole_step().sub_whole_step()
                        first_tone = second_tone.sub_whole_step().sub_half_step()
                    elif chord_type == "half diminished":
                        third_tone = note.sub_whole_step().sub_whole_step()
                        second_tone = third_tone.sub_whole_step().sub_half_step()
                        first_tone = second_tone.sub_whole_step().sub_half_step()
                    elif chord_type == "full diminished":
                        third_tone = note.sub_whole_step().sub_half_step()
                        second_tone = third_tone.sub_whole_step().sub_half_step()
                        first_tone = second_tone.sub_whole_step().sub_half_step()
                    elif chord_type == "augmented":
                        third_tone = note.sub_whole_step().sub_half_step()
                        second_tone = third_tone.sub_whole_step().sub_whole_step()
                        first_tone = second_tone.sub_whole_step().sub_whole_step()
                    else:
                        raise Exception("Not a valid chord type: " + chord_type)
                    self.chord = [first_tone, second_tone, third_tone, note]
    
    def __str__(self):
        out = str(self.chord[0]) + " " + self.chord_type + " " + self.quality + " chord: "
        for note in self.chord:
            out += str(note) + " "
        return out[:-1]

    def get_note(self, tone):
        # get note based on chord tone:
        if tone == 1:
            return self.chord[0]
        if tone == 3:
            return self.chord[1]
        if tone == 5:
            return self.chord[2]
        if tone == 7:
            if self.quality == "seventh":
                return self.chord[3]
            else:
                raise Exception("Cannot return 7th degree of a triad.")
        raise Exception("Cannot return tone: " + str(tone))