import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

time.sleep(5)

def PressEnter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

for i in range(30):
    
    time.sleep(4)

    keyboard.press(Key.ctrl)
    keyboard.press('e')
    keyboard.release(Key.ctrl)
    keyboard.release('e')

    time.sleep(1)

    PressEnter()

    time.sleep(1)

    keyboard.press(Key.left)
    keyboard.release(Key.left)

    time.sleep(1)

    PressEnter()
    
    PressEnter()

    keyboard.press(Key.alt)
    keyboard.press(Key.right)
    keyboard.release(Key.alt)
    keyboard.release(Key.right)

