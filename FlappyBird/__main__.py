from .pkg import GameEngine
from .pkg import Constants

def run():
    game = GameEngine(Constants.WINDOW_SIZE,
                    Constants.WINDOW_TITLE,
                    Constants.STAGE_SIZE,
                    Constants.STAGE_COLORS,
                    Constants.MARGIN_COLORS,
                    Constants.PILAR_SIZE,
                    Constants.PILAR_SPEED,
                    Constants.PILAR_MIN_DISTANCE,
                    Constants.PILAR_MAX_DISTANCE,
                    Constants.BIRD_SIZE,
                    Constants.CLOCK_FONT,
                    Constants.CLOCK_COLOR,
                    Constants.TEXT_FONT)

    game.run()

if __name__ == '__main__':
    run()