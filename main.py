from game_of_life import GameOfLife


def main():
    game = GameOfLife(3, 6, 6, {(3,1), (3,3), (3, 2), (1, 2), (2,3)})
    game.simulate()

if __name__ == '__main__':
    main()