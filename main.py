import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

### Pressing 'x' will enable and disable auto-clicker
TOGGLE_KEY = KeyCode(char = "x") 

clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.00001) # Change this value in order to determine frequency of the click


def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking

click_thread = threading.Thread(target = clicker)
click_thread.start()

with Listener(on_press = toggle_event) as listener:
    listener.join()
