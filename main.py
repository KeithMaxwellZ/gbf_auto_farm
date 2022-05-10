import random
import time
import threading
from var import *
from util import *
import pyWinhook as pyHook

RUNNING = True
PAUSE = False


def execute(target, order: list):
    global RUNNING
    if order is None:
        RUNNING = False
        raise Exception("Order Cannot be None!")
    for i in order:
        while PAUSE:
            time.sleep(1)
        xs = random.randint(-i[1][0], i[1][0])
        px = i[0][0] + xs
        ys = random.randint(-i[1][1], i[1][1])
        py = i[0][1] + ys
        wait = i[2] + random.uniform(0, i[3] + 0.01)
        rep = random.randint(1, i[4])
        print(i[5], file=STDOUT)
        for _ in range(rep):
            click(target, pos_x=int(px / 1.2), pos_y=int(py / 1.2))
            rwait = random.uniform(0, 0.05)
            time.sleep(rwait)
        print("DEBUG:", px, xs, py, ys, wait, rep, file=G2)
        time.sleep(wait)


def supervisor():
    def onKeyboardEvent(event: pyHook.KeyboardEvent):
        global PAUSE
        if event.KeyID == 36:
            if not RUNNING:
                exit(0)
            # home
            if PAUSE:
                print("resumed")
            else:
                print("paused")
            PAUSE = not PAUSE
        return 1

    print("supervisor started")
    hm = pyHook.HookManager()
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()

    win32gui.PumpMessages()


def start_round(target, order, rounds: int = 50):
    print("rounds started")
    global RUNNING
    try:
        for i in range(0, rounds):
            print(f"======= Round {i} =======")
            execute(target, order)
    finally:
        RUNNING = False

    RUNNING = False

if __name__ == '__main__':
    # find_window()
    dbg_target = 44107804
    t1 = threading.Thread(target=supervisor)
    t2 = threading.Thread(target=start_round, args=(dbg_target, camp_star))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
