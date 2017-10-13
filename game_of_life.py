
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
        pass