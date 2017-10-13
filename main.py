from game_of_life import GameOfLife


def main():
    game = GameOfLife(14, 3, 3, [[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    game.simulate()


if __name__ == '__main__':
    main()