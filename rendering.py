import curses


def setup_curses_colors():
    curses.curs_set(False)
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)


class KeyboardPadRenderer:
    def __init__(self, position, layout):
        self.window = curses.newwin(4, 29, *position)
        self.layout = layout

    def draw(self):
        for coord, key in zip(self.layout.key_coords, self.layout.minor_keys):
            self.window.addstr(*coord, key, curses.color_pair(self.layout.key_colors[key]))
        self.window.refresh()

    def draw_highlight_key(self, highlighted_key):
        keys = self.layout.major_keys if highlighted_key in self.layout.major_keys else self.layout.minor_keys
        for coord, key in zip(self.layout.key_coords, keys):
            color = curses.color_pair(self.layout.key_colors[key])
            if key == highlighted_key:
                color = color | curses.A_BOLD | curses.A_REVERSE
            self.window.addstr(*coord, key, color)
        self.window.refresh()


class TextPad:
    def __init__(self, center_position, width, text):
        self.window = curses.newwin(2, 2 * width + 1, center_position[0], center_position[1] - width)
        self.width = width

        padding = ' ' * width
        self.text = padding + text
        self.current_position = width

    def draw(self):
        self.window.addstr(1, 0, self.text[self.current_position - self.width: self.current_position + self.width])
        self.window.addstr(0, self.width, "V")
        self.window.refresh()

    @property
    def current_char(self):
        return self.text[self.current_position]

    def trigger_next(self, pressed_key):
        if pressed_key == self.current_char:
            self.current_position += 1
            return True
        else:
            return False


