import curses
from curses import wrapper
from time import time

start_ends = [[0, 25], [3, 28], [4, 25], [5, 24]]
key_coords = []
for row, start_end in enumerate(start_ends):
    for i in range(*start_end, 2):
        key_coords.append([row, i])

major_keys = '~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'
minor_keys = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"

finger_keys = {
    'L_pinky': '`12qaz~!@QAZ',
    'L_ring': '3wsx#WSX',
    'L_middle': '4edc$EDC',
    'L_index': '5rfv6tgb%RFV^TGB',

    'R_index': '7yhn8ujm&YHN*UJM',
    'R_middle': '9ik,(IK<',
    'R_ring': '0ol.)OL>',
    'R_pinky': """-p;/=[']\\_P:?+{"}|""",

    'thumb': ' '
}

key_fingers = {key: finger for finger, keys in finger_keys.items() for key in keys}

finger_colors = {
    'L_pinky': 1,
    'L_ring': 2,
    'L_middle': 3,
    'L_index': 4,

    'R_index': 5,
    'R_middle': 6,
    'R_ring': 8,
    'R_pinky': 1,

    'thumb': 0
}

key_colors = {key: finger_colors[key_fingers[key]] for key in major_keys + minor_keys}


def print_keys(win):
    for coord, key in zip(key_coords, minor_keys):
        pass
        # win.addstr(*coord, str(key_colors[key]), curses.color_pair(key_colors[key]))
        #win.addstr(str(key_colors[key]), curses.color_pair(key_colors[key]))
        win.addstr(*coord, key, curses.color_pair(key_colors[key]))
    win.refresh()


def main(stdscr):
    curses.curs_set(False)
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)

    keyboard_window = curses.newwin(4, 29, 3, 3)
    while True:
        print_keys(keyboard_window)


wrapper(main)
