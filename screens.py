from abc import ABC, abstractmethod
import curses

from pads import KeyboardPad, TextPad
import US_Layout


def setup_curses_colors():
    curses.curs_set(False)
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)


class AbstractScreen(ABC):
    @abstractmethod
    def __init__(self, pads):
        self.pads = pads

    def draw(self):
        for pad in self.pads:
            pad.draw()
            pad.window.noutrefresh()
            curses.doupdate()

    @abstractmethod
    def update(self, key):
        return self


class TypingScreen(AbstractScreen):
    def __init__(self, screen):
        self.keyboard = KeyboardPad((2, 5), US_Layout)
        self.text = TextPad((0, 18), 9, US_Layout.random_words((3, 5), 100))

        pads = self.keyboard, self.text

        super().__init__(pads)

    def update(self, key):
        if not self.text.trigger_next(key):
            curses.flash()
        self.keyboard.highlight_key = self.text.current_char
