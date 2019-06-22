from notes import *
from progressions import *
from write import *
from staff import *

chords = make_chords()
staff = Staff(chords, staff_width = 6)
print(staff)