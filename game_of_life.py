ALIVE = 1
DEAD = 0

class GameOfLife:
    """An implementation of the popular Game of Life simulation"""

    def __init__(self, iterations, width, height, state):
        self._iterations = iterations
        self._width = width
        self._height = height
        self._state = state

    def simulate(self):
        self._print_board()
        for _ in range(self._iterations):
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

        count = 0
        for cell in [(left, other) for other in [above, y, below]]:
            if cell in self._state:
                count += 1
        for cell in [(x, other) for other in [above, below]]:
            if cell in self._state:
                count += 1
        for cell in [(right, other) for other in [above, y, below]]:
            if cell in self._state:
                count += 1
        return count

    def _print_board(self):
        output = ""
        for y in range(self._height):
            for x in range(self._width):
                output += '1 ' if (x, y) in self._state else '0 '
            output.rstrip()
            output += '\n'
        print(output)