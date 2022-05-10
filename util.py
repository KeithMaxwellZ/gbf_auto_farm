import time
from win32 import win32api, win32gui
import win32con

from var import *


def click(target: int, pos_x=0, pos_y=0):
    print(f"clicked: {pos_x} {pos_y}", file=G2)
    pos_long = win32api.MAKELONG(pos_x, pos_y)

    win32api.PostMessage(target, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, pos_long)
    time.sleep(0.05)
    win32api.PostMessage(target, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, pos_long)


def find_window():
    hl = []
    targets = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hl)
    for i in hl:
        title = win32gui.GetWindowText(i)
        if "Granblue Fantasy - Google Chrome" in title:
            targets.append(i)

    print(targets, file=G1)

    final = []
    for i in targets:
        lst = []
        win32gui.EnumChildWindows(i, lambda cb, param: param.append(cb), lst)
        print("----------", file=G1)
        for j in lst:
            print(f"{hex(i)} {hex(j)} {j} | {win32gui.GetClassName(j)} | {win32gui.GetWindowText(j)}", file=G1)
            if win32gui.GetClassName(j) == "Intermediate D3D Window":
                final.append(j)

    return final, targets


if __name__ == '__main__':
    r1, r2 = find_window()
    print(r1, r2)
