import config
import keys
import time

controller = keys.Keys()
controller.directKey("S",controller.key_release)

# move action
def move_left(controller):
    controller.directKey("A")
    time.sleep(1)
    controller.directKey("A",controller.key_release)

def move_right(controller):
    controller.directKey("D")
    time.sleep(1)
    controller.directKey("D",controller.key_release)

def move_up(controller):
    controller.directKey("W")
    time.sleep(1)
    controller.directKey("W",controller.key_release)

def move_down(controller):
    controller.directKey("S")
    time.sleep(1)
    controller.directKey("S",controller.key_release)

# basic action
def LP(controller):
    controller.directKey("J")
    time.sleep(0.005)
    controller.directKey("J",controller.key_release)

def MP(controller):
    controller.directKey("K")
    time.sleep(0.005)
    controller.directKey("K",controller.key_release)

def HP(controller):
    controller.directKey("L")
    time.sleep(0.005)
    controller.directKey("L",controller.key_release)

def LK(controller):
    controller.directKey("U")
    time.sleep(0.005)
    controller.directKey("U",controller.key_release)

def MK(controller):
    controller.directKey("I")
    time.sleep(0.005)
    controller.directKey("I",controller.key_release)

def HK(controller):
    controller.directKey("O")
    time.sleep(0.005)
    controller.directKey("O",controller.key_release)

def throw(controller):
    controller.directKey("U")
    controller.directKey("J")
    time.sleep(0.08)
    controller.directKey("U",controller.key_release)
    controller.directKey("J",controller.key_release)



# Filia combo
def _RingletSpike(controller):
    controller.directKey("S")
    time.sleep(0.001)
    controller.directKey("D")
    time.sleep(0.001)
    controller.directKey("S",controller.key_release)
    time.sleep(0.001)
    controller.directKey("D",controller.key_release)
    controller.directKey("J")
    controller.directKey("J",controller.key_release)

def _RingletPsych(controller):
    # This one seems to be a little useless in single player
    controller.directKey("S")
    time.sleep(0.001)
    controller.directKey("D")
    time.sleep(0.001)
    controller.directKey("S",controller.key_release)
    time.sleep(0.001)
    controller.directKey("D",controller.key_release)
    controller.directKey("U")
    controller.directKey("U",controller.key_release)

def _Updo(controller):
    controller.directKey("D")
    time.sleep(0.001)
    controller.directKey("S")
    time.sleep(0.001)
    controller.directKey("D",controller.key_release)
    time.sleep(0.001)
    controller.directKey("D")
    time.sleep(0.001)
    controller.directKey("S",controller.key_release)
    time.sleep(0.001)
    controller.directKey("D",controller.key_release)
    time.sleep(0.001)
    controller.directKey("J")
    controller.directKey("J",controller.key_release)
    time.sleep(0.001)

def _Hairball(controller):

    controller.directKey("S")
    time.sleep(0.001)
    controller.directKey("A")
    time.sleep(0.001)
    controller.directKey("S",controller.key_release)
    time.sleep(0.001)
    controller.directKey("A",controller.key_release)
    controller.directKey("U")
    controller.directKey("U",controller.key_release)

def _FenrirDrive(controller):
    controller.directKey("D")
    time.sleep(0.001)
    controller.directKey("S")
    time.sleep(0.001)
    controller.directKey("D",controller.key_release)
    time.sleep(0.001)
    controller.directKey("D")
    time.sleep(0.001)
    controller.directKey("S",controller.key_release)
    time.sleep(0.001)
    controller.directKey("D",controller.key_release)
    time.sleep(0.001)
    controller.directKey("Y")
    controller.directKey("Y",controller.key_release)

def _Tricobezoar(controller):
    controller.directKey("S")
    time.sleep(0.001)
    controller.directKey("A")
    time.sleep(0.001)
    controller.directKey("S",controller.key_release)
    time.sleep(0.001)
    controller.directKey("A",controller.key_release)
    controller.directKey("Y")
    controller.directKey("Y",controller.key_release)

def _GregorSamson(controller):
    controller.directKey("S")
    time.sleep(0.001)
    controller.directKey("A")
    time.sleep(0.001)
    controller.directKey("S",controller.key_release)
    time.sleep(0.001)
    controller.directKey("A",controller.key_release)
    time.sleep(0.001)
    controller.directKey("H")
    controller.directKey("H",controller.key_release)

_skill_list_FILIA = [_RingletSpike, _FenrirDrive, _GregorSamson, _Tricobezoar, _Updo, _Hairball]
move_list = [move_up, move_down, move_left, move_right]
basic_list = [LP, MP, HP, LK, MK, HK, throw]


class Actor():
    def __init__(self, actionlist) -> None:
        self.actionlist = actionlist

    def move_action(self,id):
        self.actionlist[id]()

class Filia():
    def __init__(self) -> None:
        self.name = 'Filia'
        self.moveActor = Actor(move_list)
        self.basicActor = Actor(basic_list)
        self.skillActor = Actor(_skill_list_FILIA)





if __name__ == "__main__":

    time.sleep(3)
    _FenrirDrive(controller=controller)

