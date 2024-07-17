from game import Game
import logging


def main():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    game = Game()
    game.run()


if __name__ == '__main__':
    main()

