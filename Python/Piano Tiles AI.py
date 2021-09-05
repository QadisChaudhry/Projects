# h5.j4.com/games/Magic-Piano-Online/

import pyautogui
import time
from mss import mss
from pynput import keyboard

start_x = 725
start_y = 775

bbox = (start_x, start_y, start_x + 450, start_y + 1)
cords_x = [0, 150, 300, 449]


def test_time():
    with mss() as sct:
        t1 = time.time()
        for i in range(100):
            img = sct.grab(bbox)
            pyautogui.click(190, 440)
        t2 = time.time()
        print(t2 - t1)


def print_mouse_pos():
    while 1:
        print(pyautogui.position())
        time.sleep(1)


def start():
    with mss() as sct:
        while 1:
            img = sct.grab(bbox)
            for cord in cords_x:
                if img.pixel(cord, 0)[0] < 100:
                    pyautogui.click(start_x + cord, start_y)


time.sleep(1)
start()
