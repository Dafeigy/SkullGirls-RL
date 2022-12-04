# test charactor move/action
import actor
import time
import keys

player = actor.Filia()
controller = keys.Keys()

if __name__ == "__main__":
    print("Move Test start")
    time.sleep(1)
    for i in range(len(player.moveActor.actionlist)):
        player.moveActor.take_action(i)(controller)
        time.sleep(1)
    
    print("Basic Test start")
    time.sleep(1)
    for i in range(len(player.basicActor.actionlist)):
        player.basicActor.take_action(i)(controller)
        time.sleep(1)