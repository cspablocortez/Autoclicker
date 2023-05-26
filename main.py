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