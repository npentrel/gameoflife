import argparse
import curses

from game_of_life import GameOfLife


def main(args):
    try:
        stdscr = None
        color = None

        iterations, width, height, state = _read_input()

        if args.curses:
            stdscr = curses.initscr()
            curses.curs_set(0)
            curses.start_color()
            curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
            color = curses.color_pair(1)

        game = GameOfLife(iterations, width, height, state, stdscr, color)
        game.simulate()
        if stdscr:
            curses.endwin()
    except KeyboardInterrupt:
        try:
            curses.endwin()
        except curses.error:
            pass


def _get_input():
    return iter([int(x) for x in input().strip().split(' ')])


def _read_input():
    iterations = next(_get_input())
    width, height = _get_input()
    state = set()

    for y in range(height):
        row = _get_input()
        state.update({(x, y) for x in range(width) if next(row)})

    print()
    return iterations, width, height, state


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Game of Life implementation')
    parser.add_argument('--pretty', dest='curses', action='store_true')
    parser.set_defaults(curses=False)
    args = parser.parse_args()

    main(args)
