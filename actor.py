from config import *
from utils import ActionInfo
import keys
import time

controller = keys.Keys()





# move action
@ActionInfo
def move_left(controller):
    controller.directKey(LEFT)
    time.sleep(0.5)
    controller.directKey(LEFT,controller.key_release)

@ActionInfo
def move_right(controller):
    controller.directKey(RIGHT)
    time.sleep(0.5)
    controller.directKey(RIGHT,controller.key_release)

@ActionInfo
def move_up(controller):
    controller.directKey(UP)
    time.sleep(0.5)
    controller.directKey(UP,controller.key_release)

@ActionInfo
def move_down(controller):
    controller.directKey(DOWN)
    time.sleep(0.5)
    controller.directKey(DOWN,controller.key_release)

# basic action
@ActionInfo
def _LP(controller):
    controller.directKey(LP)
    time.sleep(0.005)
    controller.directKey(LP,controller.key_release)

@ActionInfo
def _MP(controller):
    controller.directKey(MP)
    time.sleep(0.005)
    controller.directKey(MP,controller.key_release)

@ActionInfo
def _HP(controller):
    controller.directKey(HP)
    time.sleep(0.005)
    controller.directKey(HP,controller.key_release)

@ActionInfo
def _LK(controller):
    controller.directKey(LK)
    time.sleep(0.005)
    controller.directKey(LK,controller.key_release)

@ActionInfo
def _MK(controller):
    controller.directKey(MK)
    time.sleep(0.005)
    controller.directKey(MK,controller.key_release)

@ActionInfo
def _HK(controller):
    controller.directKey(HK)
    time.sleep(0.005)
    controller.directKey(HK,controller.key_release)

@ActionInfo
def _throw(controller):
    controller.directKey(LK)
    controller.directKey(LP)
    time.sleep(0.08)
    controller.directKey(LK,controller.key_release)
    controller.directKey(LP,controller.key_release)



# Filia combo，requires direction
def _RingletSpike(controller,reverse=False):
    controller.directKey(DOWN)
    time.sleep(0.001)
    controller.directKey(RIGHT)
    time.sleep(0.001)
    controller.directKey(DOWN,controller.key_release)
    time.sleep(0.001)
    controller.directKey(RIGHT,controller.key_release)
    controller.directKey(LP)
    controller.directKey(LP,controller.key_release)

def _RingletPsych(controller,reverse=False):
    # This one seems to be a little useless in single player
    controller.directKey(DOWN)
    time.sleep(0.001)
    controller.directKey(RIGHT)
    time.sleep(0.001)
    controller.directKey(DOWN,controller.key_release)
    time.sleep(0.001)
    controller.directKey(RIGHT,controller.key_release)
    controller.directKey(LK)
    controller.directKey(LK,controller.key_release)

def _Updo(controller,reverse=False):
    controller.directKey(RIGHT)
    time.sleep(0.001)
    controller.directKey(DOWN)
    time.sleep(0.001)
    controller.directKey(RIGHT,controller.key_release)
    time.sleep(0.001)
    controller.directKey(RIGHT)
    time.sleep(0.001)
    controller.directKey(DOWN,controller.key_release)
    time.sleep(0.001)
    controller.directKey(RIGHT,controller.key_release)
    time.sleep(0.001)
    controller.directKey(LP)
    controller.directKey(LP,controller.key_release)
    time.sleep(0.001)

def _Hairball(controller,reverse=False):

    controller.directKey(DOWN)
    time.sleep(0.001)
    controller.directKey(LEFT)
    time.sleep(0.001)
    controller.directKey(DOWN,controller.key_release)
    time.sleep(0.001)
    controller.directKey(LEFT,controller.key_release)
    controller.directKey(LK)
    controller.directKey(LK,controller.key_release)

def _FenrirDrive(controller,reverse=False):
    controller.directKey(RIGHT)
    time.sleep(0.001)
    controller.directKey(DOWN)
    time.sleep(0.001)
    controller.directKey(RIGHT,controller.key_release)
    time.sleep(0.001)
    controller.directKey(RIGHT)
    time.sleep(0.001)
    controller.directKey(DOWN,controller.key_release)
    time.sleep(0.001)
    controller.directKey(RIGHT,controller.key_release)
    time.sleep(0.001)
    controller.directKey(MACRO2)
    controller.directKey(MACRO2,controller.key_release)

def _Tricobezoar(controller,reverse=False):
    controller.directKey(DOWN)
    time.sleep(0.001)
    controller.directKey(LEFT)
    time.sleep(0.001)
    controller.directKey(DOWN,controller.key_release)
    time.sleep(0.001)
    controller.directKey(LEFT,controller.key_release)
    controller.directKey(MACRO2)
    controller.directKey(MACRO2,controller.key_release)

def _GregorSamson(controller,reverse=False):
    controller.directKey(DOWN)
    time.sleep(0.001)
    controller.directKey(LEFT)
    time.sleep(0.001)
    controller.directKey(DOWN,controller.key_release)
    time.sleep(0.001)
    controller.directKey(LEFT,controller.key_release)
    time.sleep(0.001)
    controller.directKey(MACRO1)
    controller.directKey(MACRO1,controller.key_release)

_skill_list_FILIA = [_RingletSpike, _FenrirDrive, _GregorSamson, _Tricobezoar, _Updo, _Hairball]
move_list = [move_up, move_down, move_left, move_right]
basic_list = [_LP, _MP, _HP, _LK, _MK, _HK, _throw]


class Actor():
    def __init__(self, actionlist:list) -> None:
        self.actionlist = actionlist
        self.model = None
    
    def take_action(self,id:int):
        return self.actionlist[id]


class Filia():
    def __init__(self,) -> None:
        self.name = 'Filia'
        self.moveActor = Actor(move_list)
        self.basicActor = Actor(basic_list)
        self.skillActor = Actor(_skill_list_FILIA)







