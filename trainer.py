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


def main(stdscr):
    key = None
    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        stdscr.addstr(0, 0, f"h: {h}, w: {w}")
        try:
            stdscr.addstr(1, 0, str(key))
        except Exception as e:
            print('Cannot display key')
            print(e)

        try:
            key = stdscr.getkey()
        except Exception as e:
            print('Cannot get key')
            print(e)

        stdscr.refresh()


wrapper(main)
