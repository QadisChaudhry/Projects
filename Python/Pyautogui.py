import pyautogui as gui
import time
from mss import mss

with mss as sct:
    sct.grab()
