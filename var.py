import os
import sys
from typing import TextIO

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


initiation()

# [Position, random_range, delay, delay_random, repeat, comment]
# Campaign star quest
camp_star = [
    [(43, 118), (0, 0), 1.5, 0, 1, "bookmark"],
    [(205, 510), (100, 45), 3, 0.5, 5, "firend summon"],
    [(361, 770), (70, 5), 5.5, 2, 5, "start"],
    [(45, 525), (20, 15), 8.5, 1, 1, "auto"],
    [(105, 75), (0, 0), 4.8, 3, 1, "refresh"],
]
