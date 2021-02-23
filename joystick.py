from inputs import get_gamepad

def button_input():
    while True:
        events = get_gamepad()
        for event in events:
            if(event.ev_type == "Absolute" and event.code == "ABS_Y" and event.state > 0):
                return("leftJoystickUp")
            if (event.ev_type == "Absolute" and event.code == "ABS_Y" and event.state < 0):
                return("leftJoystickDown")

            if(event.ev_type == "Key" and event.code == "BTN_WEST" and event.state == 1):
                return("buttonXPress")
            if (event.ev_type == "Key" and event.code == "BTN_WEST" and event.state == 0):
                return("buttonXRelease")

            if(event.ev_type == "Key" and event.code == "BTN_NORTH" and event.state == 1):
                return("buttonYPress")

            if (event.ev_type == "Key" and event.code == "BTN_NORTH" and event.state == 0):
                return ("buttonYRelease")

            if (event.ev_type == "Key" and event.code == "BTN_EAST" and event.state == 1):
                return("buttonBPress")

            if (event.ev_type == "Key" and event.code == "BTN_EAST" and event.state == 0):
                return ("buttonBRelease")

            if (event.ev_type == "Key" and event.code == "BTN_SOUTH" and event.state == 1):
                return("buttonAPress")

            if (event.ev_type == "Key" and event.code == "BTN_SOUTH" and event.state == 0):
                return ("buttonARelease")
