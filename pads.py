from abc import ABC, abstractmethod

import curses
import string


class AbstractPad(ABC):
    @abstractmethod
    def __init__(self, size, position):
        self.window = curses.newwin(*size, *position)


class KeyboardPad(AbstractPad):
    def __init__(self, position, layout):
        size = (4, 29)
        self.layout = layout
        self.highlight_key = None
        super().__init__(size, position)

    def draw(self):
        keys = self.layout.major_keys
        if self.highlight_key is None or self.highlight_key in self.layout.minor_keys:
            keys = self.layout.minor_keys

        for coord, key in zip(self.layout.key_coords, keys):
            color = curses.color_pair(self.layout.key_colors[key])
            if key == self.highlight_key:
                color = color | curses.A_BOLD | curses.A_REVERSE
            self.window.addstr(*coord, key, color)


class TextPad(AbstractPad):
    def __init__(self, center_position, width, text):
        size = (2, 2 * width + 1)
        position = (center_position[0], center_position[1] - width)
        self.width = width

        padding = ' ' * width
        self.text = padding + text
        self.current_position = width
        super().__init__(size, position)

    def draw(self):
        self.window.addstr(1, 0, self.text[self.current_position - self.width: self.current_position + self.width])
        self.window.addstr(0, self.width, "V")

    @property
    def current_char(self):
        return self.text[self.current_position]

    def trigger_next(self, pressed_key):
        if self.current_position == len(self.text) - 1:
            return False

        if pressed_key == self.current_char:
            self.current_position += 1
            return True
        else:
            return False


class CurrentKeyPad:
    def __init__(self, position, textwidth=15):
        self.textwidth = textwidth
        self.window = curses.newwin(1, textwidth, *position)

    def draw(self, key: str):
        if key is None:
            return
        if not all(c in string.printable for c in key):
            key = ''.join([hex(ord(c)) for c in key])

        key = key.replace('\n', '\\n')
        try:
            self.window.addstr(0, 0, ' ' * (self.textwidth - 1))
            self.window.addstr(0, 0, key)
        except(curses.error, ValueError):
            self.window.addstr(0, 0, "ERROR         ")
