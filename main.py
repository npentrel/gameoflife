from game_of_life import GameOfLife


def main():
    iterations, width, height, state = _read_input()
    game = GameOfLife(iterations, width, height, state)
    game.simulate()


def _get_input():
    return iter([int(x) for x in input().strip().split(' ')])


def _read_input():
    iterations = next(_get_input())
    width, height = _get_input()
    state = set()

    for y in range(height):
        row = _get_input()
        state.update({(x, y) for x in range(width) if next(row)})

    return iterations, width, height, state


if __name__ == '__main__':
    main()