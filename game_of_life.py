
class GameOfLife:
    """An implementation of the popular Game of Life simulation"""

    ALIVE = 1
    DEAD = 0

    def __init__(self, iterations, width, height, state):
        self.iterations = iterations
        self.width = width
        self.height = height
        self.state = state

    def simulate(self):
        for _ in range(self.iterations):
            self._print_board()

    def _print_board(self):
        output = ""
        for h in range(self.height):
            for w in range(self.width):
                output += '1 ' if (w, h) in self.state else '0 '
            output.rstrip()
            output += '\n'
        print(output)