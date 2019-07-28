#!python3

import curses
from curses import wrapper
import random

numbers = '1234567890'
small = 'abcdefghijklmnopqrstuvwxyz'
big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
brackets = '[]{}()<>'
punctuation = '`.:,;!?'
slashes_and_dashes = '/\|'
upper_row = '~!@#$%^&*()_+-='
quotes = ''''"'''

symbols = numbers + small + big + brackets + punctuation + slashes_and_dashes + upper_row + quotes

lengths = [random.randint(2, 8) for _ in range(100)]
words = [''.join(random.choices(symbols, k=length)) for length in lengths]
text = ' '.join(words)
typed = []
timing = []


def draw(screen, index, letters_per_minute, error_rate):
    h, w = screen.getmaxyx()
    if h < 3 or w < 75:
        raise RuntimeError(f"window is too small! Required: 5x75, got {h}x{w}")

    screen.clear()
    screen.addstr(2, 4, f"Letters per minute: {letters_per_minute}")
    screen.addstr(2, 46, f"Error rate: {error_rate}%")
    screen.addstr(1, 36, "Λ")
    screen.addstr(2, 36, "|")

    left_pad = 36 - index
    text_cutout = text[max(index - 36, 0):index + 36]
    screen.addstr(0, 0, ' ' * left_pad + text_cutout)


def main(stdscr):
    curses.curs_set(False)
    curses.use_default_colors()
    key = None
    index = 0
    while True:
        draw(stdscr, index, 123, 321)
        # display_key(key, stdscr)
        key = get_key(stdscr)

        if key == text[index]:
            index += 1

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
