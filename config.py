## TODO: Synchronize to actor part

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

MACRO1 = 'H'
MACRO2 = 'Y'

ControlDict = {
    "UP": UP,
    "DOWN" : DOWN,
    "LEFT" : LEFT,
    "RIGHT" : RIGHT,

    "LP" : LP,
    "MP" : MP,
    "HP" : HP,

    "LK" : LK,
    "MK" : MK,
    "HK" : HK,

    'MACRO1': MACRO1,
    'MACRO2': MACRO2
}

for each in ControlDict:

    print('\033[1;37;44m▶  {} {} : \033[0m\033[1;37;42m {} \033[0m'.format(each,' '*(6-len(each)),ControlDict[each]),end='  ')

print("\n\n\033[1;37;41m WARNING: \033[0m When you see this line it means \033[1;37;41m ABOVE VARIABLE ARE DEFINED \033[0m and please don't reuse them.")