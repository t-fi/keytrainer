#!python3

from curses import wrapper
import US_Layout
from screens import TypingScreen, setup_curses_colors


def main(stdscr):
    setup_curses_colors()

    main_screen = TypingScreen(stdscr)
    main_screen.update(None)
    main_screen.draw()
    while True:
        key = get_key(stdscr)
        main_screen.update(key)
        main_screen.draw()


def get_key(stdscr):
    try:
        return stdscr.getkey()
    except Exception as e:
        print('Cannot get key')
        print(e)
        stdscr.refresh()
        return None


wrapper(main)
