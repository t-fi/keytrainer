#!python3

import curses
from curses import wrapper
import random

from time import time

US_MAJOR = \
    """                     ~ ! @ # $ % ^ & * ( ) _ +
                        Q W E R T Y U I O P { } |
                         A S D F G H J K L : "
                          Z X C V B N M < > ?"""

US_MINOR = \
    """                     ` 1 2 3 4 5 6 7 8 9 0 - =
                        q w e r t y u i o p [ ] \\
                         a s d f g h j k l ; '
                          z x c v b n m , . /"""

fingers = {
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



numbers = '1234567890'
small = 'abcdefghijklmnopqrstuvwxyz'
big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
brackets = '[]{}()<>'
punctuation = '`.:,;!?'
slashes_and_dashes = '/\\|'
upper_row = '~!@#$%^&*()_+-='
quotes = ''''"'''

symbols = numbers + small + big + brackets + punctuation + slashes_and_dashes + upper_row + quotes

lengths = [random.randint(2, 8) for _ in range(100)]
words = [''.join(random.choices(symbols, k=length)) for length in lengths]
text = ' '.join(words)
typed = []


def draw(screen, index, letters_per_minute, error_rate):
    h, w = screen.getmaxyx()
    if h < 3 or w < 75:
        raise RuntimeError(f"window is too small! Required: 5x75, got {h}x{w}")

    screen.clear()
    screen.addstr(2, 4, f"Keys per minute: {letters_per_minute}")
    screen.addstr(2, 46, f"Error rate: {error_rate}‰")
    screen.addstr(1, 36, "Λ")
    screen.addstr(2, 36, "|")

    left_pad = 36 - index
    text_cutout = text[max(index - 36, 0):index + 36]
    screen.addstr(0, 0, ' ' * left_pad + text_cutout)


def draw_keyboard(screen):
    screen.addstr(3, 0, US_MINOR)


def main(stdscr):
    curses.curs_set(False)
    curses.use_default_colors()
    key = None
    index = 0
    errors = 0
    start_time = 0
    while True:

        error_rate = errors / index * 1000 if index > 0 else 0
        letters_per_minute = 60 * index / (time() - start_time)
        draw(stdscr, index, letters_per_minute, int(error_rate))

        draw_keyboard(stdscr)

        key = get_key(stdscr)
        if not index:
            start_time = time()

        if key == text[index]:
            index += 1
        else:
            errors += 1

        stdscr.refresh()


def get_key(stdscr):
    try:
        return stdscr.getkey()
    except Exception as e:
        print('Cannot get key')
        print(e)
        return None


def display_key(key, stdscr):
    try:
        stdscr.addstr(1, 0, str(key))
    except Exception as e:
        print('Cannot display key')
        print(e)


wrapper(main)
