import os
import random
import time
from typing import TextIO
import threading
import sys
import pyWinhook as pyHook
from win32 import win32api, win32gui
import win32con

STDOUT = sys.stdout
STDERR = sys.stderr
NULL = open(os.devnull, 'w')
G1: TextIO
G2: TextIO
G3: TextIO

gwithd = 468
ghight = 870


def initiation():
    global G1, G2, G3
    G1 = NULL
    G2 = NULL
    G3 = NULL


def func2():
    def onMouseEvent(event: pyHook.MouseEvent):
        print(event.Position)
        return 1

    def onKeyboardEvent(event: pyHook.KeyboardEvent):
        print(event.KeyID)
        return 1

    print("start", file=G1)
    hm = pyHook.HookManager()
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()
    hm.MouseAllButtons = onMouseEvent
    hm.HookMouse()

    win32gui.PumpMessages()


if __name__ == '__main__':
    initiation()
    func2()
