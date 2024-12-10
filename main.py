import time
import threading
import random
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

# Pressing '~' will enable and disable auto-clicker
TOGGLE_KEY = KeyCode(char="~")

# Define the range for the random delay (in seconds)
DELAY_RANGE = (0.8, 2)

clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left)
            # Add a random delay between clicks
            time.sleep(random.uniform(*DELAY_RANGE))
        else:
            time.sleep(0.1)  # Short delay when not clicking to reduce CPU usage

def toggle_event(key):
    global clicking
    if key == TOGGLE_KEY:
        clicking = not clicking

click_thread = threading.Thread(target=clicker)
click_thread.daemon = True
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
