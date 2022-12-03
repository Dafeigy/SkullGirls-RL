UP = 'W'
DOWN = 'S'
LEFT = 'A'
RIGHT = 'D'

LP = 'J'
MP = 'K'
HP = 'L'

LK = 'U'
MK = 'I'
HK = 'O'

import keys
import ctypes


if __name__ == "__main__":
    control = keys.Keys()
    control.directKey(UP)