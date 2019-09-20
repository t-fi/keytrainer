#!python3

import curses
from curses import wrapper
import US_Layout
import rendering

from time import time


def main(stdscr):
    rendering.setup_curses_colors()

    text = US_Layout.random_words([4, 8], 10)

    keyboard = rendering.KeyboardPadRenderer([3, 5], US_Layout)
    text_pad = rendering.TextPad([1, 18], 10, text)
    stdscr.refresh()
    keyboard.draw()
    text_pad.draw()
    stdscr.refresh()
    while True:
        key = get_key(stdscr)
        text_pad.trigger_next(key)
        keyboard.draw_highlight_key(text_pad.current_char)
        text_pad.draw()
        stdscr.refresh()


def get_key(stdscr):
    try:
        return stdscr.getkey()
    except Exception as e:
        print('Cannot get key')
        print(e)
        stdscr.refresh()
        return None


wrapper(main)
