import math
import time

ALIVE = 1
DEAD = 0

class GameOfLife:
    """An implementation of the popular Game of Life simulation"""

    def __init__(self, iterations, width, height, state, sleep, stdscr=None, color=None, symbol='*'):
        self._iterations = iterations
        self._width = width
        self._height = height
        self._state = state
        self._sleep = sleep
        self._stdscr = stdscr
        self._color = color
        if self._stdscr:
            self._alive_char = symbol + ' '
            self._dead_char = '  '
        else:
            self._alive_char = '1 '
            self._dead_char = '0 '

    def simulate(self):
        self._print_board()
        for _ in range(self._iterations):
            time.sleep(self._sleep)
            self._apply_rules()
            self._print_board()

    def _is_alive(self, x, y):
        neighbor_count = self._get_neighbor_count(x, y)
        if neighbor_count == 3:
            return ALIVE

        if (x, y) in self._state:
            if neighbor_count == 2:
                return ALIVE

        return DEAD

    def _apply_rules(self):
        self._state = {(x, y) for x in range(self._height) for y in range(self._width) if self._is_alive(x,y)}

    def _get_neighbor_count(self, x, y):
        left = x - 1 if x else self._width - 1
        right = x + 1 if x < self._width - 1 else 0
        above = y - 1 if y else self._height - 1
        below = y + 1 if y < self._height - 1 else 0

        living_neighbors = set()
        for cell in [(left, other) for other in [above, y, below]]:
            if cell in self._state:
                living_neighbors.add(cell)
        for cell in [(x, other) for other in [above, below]]:
            if cell in self._state:
                living_neighbors.add(cell)
        for cell in [(right, other) for other in [above, y, below]]:
            if cell in self._state:
                living_neighbors.add(cell)

        try:
            living_neighbors.remove((x,y))
        except KeyError:
            pass

        return len(living_neighbors)

    def _print_board(self):
        if self._stdscr:
            return self._curses_board()
        output = ""
        for y in range(self._height):
            for x in range(self._width):
                output += self._alive_char if (x, y) in self._state else self._dead_char
            output.rstrip()
            output += '\n'
        print(output)

    def _curses_board(self):
        scrheight, scrwidth = iter(self._stdscr.getmaxyx())
        output = "\n" * ((scrheight - self._height)//2)
        for y in range(self._height):
            output += ' ' * int(math.ceil(scrwidth/2 - self._width))
            for x in range(self._width):
                output += self._alive_char if (x, y) in self._state else self._dead_char
            output.rstrip()
            output += '\n'
        self._stdscr.clear()
        self._stdscr.addstr(output, self._color)
        self._stdscr.refresh()
