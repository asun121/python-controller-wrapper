from __future__ import print_function
import random
import time
from inputs import get_gamepad


def average(lst):
    return sum(lst) / len(lst)

def frc_639_mappings():
    while True:
        events = get_gamepad()
        for event in events:
            if(event.ev_type == "Absolute" and event.code == "ABS_Z" and event.state > 0):
                return("acquisitionRight")
            if (event.ev_type == "Absolute" and event.code == "ABS_RZ" and event.state > 0):
                return("acquisitionBoth")

            if(event.ev_type == "Key" and event.code == "BTN_WEST" and event.state == 1):
                x = True
                return("acquisitionToggled")
            if (event.ev_type == "Key" and event.code == "BTN_WEST" and event.state == 0):
                x = False

            if(event.ev_type == "Key" and event.code == "BTN_NORTH" and event.state == 1):
                y = True
                return("shootMaxSpeed")
            if (event.ev_type == "Key" and event.code == "BTN_NORTH" and event.state == 0):
                y = False

            if (event.ev_type == "Key" and event.code == "BTN_EAST" and event.state == 1):
                a = True
                return("ShooterPistonsToggled")
            if (event.ev_type == "Key" and event.code == "BTN_EAST" and event.state == 0):
                a = False

            if (event.ev_type == "Key" and event.code == "BTN_SOUTH" and event.state == 1):
                a = True
                return("ShootNormalSpeed")
            if (event.ev_type == "Key" and event.code == "BTN_SOUTH" and event.state == 0):
                a = False

randTimes = []
actionArr = ["acquisitionBoth","acquisitionRight","acquisitionToggled", "shootMaxSpeed", "ShooterPistonsToggled", "ShootNormalSpeed"]
trials = 15;

for i in range(trials):
    randTimes.append(random.randint(1,3))

i = 0
times = []

while True:
    ellapsed = 0;
    action = random.randint(0,5)
    time.sleep(randTimes[i])
    print("DO THIS: " + actionArr[action])
    timeStart = time.time()
    user_input = frc_639_mappings()
    if(user_input == actionArr[action]):
        ellapsed = time.time() - timeStart
        times.append(ellapsed)
        print(ellapsed)
    else:
        i = i-1
        print("misinput")

    if i == trials - 1:
        print("Finished")
        print("-----AVERAGE TIME-----" + str(average(times)))
        break;
    i +=1