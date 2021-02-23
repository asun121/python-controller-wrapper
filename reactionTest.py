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
            if(event.ev_type == "Absolute" and event.code == "ABS_Y" and event.state > 0):
                return("indexerIntaking")
            if (event.ev_type == "Absolute" and event.code == "ABS_Y" and event.state < 0):
                return("indexerOutputting")

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
actionArr = ["indexerIntaking", "indexerOutputting", "acquisitionToggled", "shootMaxSpeed", "ShooterPistonsToggled", "ShootNormalSpeed"]
trials = 5;

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
        print("misinput")

    if i == trials - 1:
        print("Finished")
        print("-----AVERAGE TIME-----" + average(times))
        break;
    i +=1