import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

# Pressing '~' will enable and disable auto-clicker
TOGGLE_KEY = KeyCode(char="~")

clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left)
        time.sleep(0.3)  # add delay betweexn clicks

def toggle_event(key):
    global clicking
    if key == TOGGLE_KEY:
        clicking = not clicking

click_thread = threading.Thread(target=clicker)
click_thread.daemon = True
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
