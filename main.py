from game_of_life import GameOfLife


def main():
    game = GameOfLife(14, 3, 3, [(1, 1)])
    game.simulate()

if __name__ == '__main__':
    main()