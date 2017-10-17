import argparse
import curses

from game_of_life import GameOfLife


def main(args):
    try:
        stdscr = None
        iterations, width, height, state = _read_input()

        if args.curses:
            symbol = '*'
            if args.symbol:
                symbol = args.symbol
            stdscr, color = _setup_curses()
            game = GameOfLife(iterations, width, height, state, float(args.sleep), stdscr, color, symbol)
        else:
            game = GameOfLife(iterations, width, height, state, float(args.sleep))

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


def _setup_curses():
    yield curses.initscr()
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    yield curses.color_pair(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Game of Life implementation')
    parser.add_argument('-p', '--pretty', dest='curses', action='store_true', help='use curses library')
    parser.add_argument('-s', '--symbol', help='use specified symbol for simulation')
    parser.add_argument('-t', '--time', dest='sleep', help='time in between states in seconds', default=0.0)
    parser.set_defaults(curses=False)
    args = parser.parse_args()

    main(args)
