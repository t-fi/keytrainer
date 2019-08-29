import curses


def main(stdscr):
    curses.start_color()
    curses.use_default_colors()
    stdscr.addstr(f"{curses.COLORS}\n")
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    try:
        for i in range(0, 511):
            stdscr.addstr(f"{i} ", curses.color_pair(i))
        stdscr.addstr('\n')
        for i in range(0, 511):
            stdscr.addstr(f"{i} ", curses.color_pair(i) | curses.A_BOLD | curses.A_UNDERLINE)

        stdscr.addstr("\nnormal", curses.color_pair(2))
        stdscr.addstr("\nblink", curses.color_pair(2) | curses.A_BLINK)
        stdscr.addstr("\nbold", curses.color_pair(2) | curses.A_BOLD)
        stdscr.addstr("\ndim", curses.color_pair(2) | curses.A_DIM)
        stdscr.addstr("\nreverse", curses.color_pair(2) | curses.A_REVERSE)
        stdscr.addstr("\nunderline", curses.color_pair(2) | curses.A_UNDERLINE)
    except curses.ERR:
        # End of screen reached
        pass
    stdscr.getch()


curses.wrapper(main)
