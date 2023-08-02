from pynput.mouse import Button, Controller
from time import sleep
import keyboard

mouse = Controller()

def start_clicking():
    print("Click")
    mouse.press(Button.left)
    mouse.release(Button.left)
    # sleep(0.005)

print("Listening...")

autoclicker_enabled = False

# Infinite loop
while True:
    if keyboard.is_pressed(",") and autoclicker_enabled == False:
        autoclicker_enabled = True
        print("ON")
        while autoclicker_enabled:
            sleep(0.1)
            start_clicking()

            if keyboard.is_pressed(",") and autoclicker_enabled:
                autoclicker_enabled = False
                print("OFF")
                sleep(0.1)
