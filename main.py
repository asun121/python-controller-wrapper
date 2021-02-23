from __future__ import print_function
import random
from inputs import get_gamepad

def main():
    i = 0.25;
    while True:
        events = get_gamepad()
        for event in events:
            print(i)
            if(event.ev_type == "Absolute" and event.code == "ABS_Y" and event.state > 0):
                print("indexerIntaking")
            if (event.ev_type == "Absolute" and event.code == "ABS_Y" and event.state < 0):
                print("indexerOutputting")

            if(event.ev_type == "Key" and event.code == "BTN_WEST" and event.state == 1):
                x = True
                print("acquisitionToggled")
            if (event.ev_type == "Key" and event.code == "BTN_WEST" and event.state == 0):
                x = False

            if(event.ev_type == "Key" and event.code == "BTN_NORTH" and event.state == 1):
                y = True
                print("shootMaxSpeed")
            if (event.ev_type == "Key" and event.code == "BTN_NORTH" and event.state == 0):
                y = False

            if (event.ev_type == "Key" and event.code == "BTN_EAST" and event.state == 1):
                a = True
                print("ShooterPistonsToggled")
            if (event.ev_type == "Key" and event.code == "BTN_EAST" and event.state == 0):
                a = False

            if (event.ev_type == "Key" and event.code == "BTN_SOUTH" and event.state == 1):
                a = True
                print("ShootNormalSpeed")
            if (event.ev_type == "Key" and event.code == "BTN_SOUTH" and event.state == 0):
                a = False
            i += .25

if __name__ == "__main__":
    main()