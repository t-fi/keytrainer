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
    'L_pinky': 28,
    'L_ring': 2,
    'L_middle': 42,
    'L_index': 0,

    'R_index': 34,
    'R_middle': 164,
    'R_ring': 78,
    'R_pinky': 221,

    'thumb': 0
}

key_colors = {key: finger_colors[key_fingers[key]] for key in major_keys + minor_keys}


def print_keys(win, pressed_key):
    keys = major_keys if pressed_key in major_keys else minor_keys
    for coord, key in zip(key_coords, keys):
        if key == pressed_key:
            win.addstr(*coord, key, curses.color_pair(key_colors[key]) | curses.A_BOLD | curses.A_REVERSE)
        else:
            win.addstr(*coord, key, curses.color_pair(key_colors[key])) # | curses.A_BOLD | curses.A_UNDERLINE)

    win.refresh()


def main(stdscr):
    curses.curs_set(False)
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)

    keyboard_window = curses.newwin(4, 29, 3, 3)
    while True:
        key = get_key(stdscr)
        print_keys(keyboard_window, key)


def get_key(stdscr):
    try:
        return stdscr.getkey()
    except Exception as e:
        print('Cannot get key')
        print(e)
        return None


wrapper(main)
