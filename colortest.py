import curses


def main(stdscr):
    curses.start_color()
    curses.use_default_colors()
    stdscr.addstr(f"{curses.COLORS}\n")
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    try:
        for i in range(0, 258):
            stdscr.addstr(f"{i} ", curses.color_pair(i))
        stdscr.addstr("\nhallo", curses.color_pair(2))
        stdscr.addstr("\nhallo", curses.color_pair(2) | curses.A_BLINK)
        stdscr.addstr("\nhallo", curses.color_pair(2) | curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr("\nhallo", curses.color_pair(2) | curses.A_DIM)
        stdscr.addstr("\nhallo", curses.color_pair(2) | curses.A_REVERSE)
        stdscr.addstr("\nhallo", curses.color_pair(2) | curses.A_UNDERLINE)
    except curses.ERR:
        # End of screen reached
        pass
    stdscr.getch()


curses.wrapper(main)
