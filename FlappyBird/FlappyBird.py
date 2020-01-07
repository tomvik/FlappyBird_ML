import pygame
from typing import List, Tuple

from pkg import Size, Color, Font
from pkg import Stage
from pkg import Constants


def wait_for_enter():
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN \
                        and event.key == pygame.K_RETURN:
                    waiting = False

pygame.init()

stage = Stage(Constants.WINDOW_SIZE,
              Constants.WINDOW_TITLE,
              Constants.STAGE_SIZE,
              Constants.STAGE_COLORS,
              Constants.MARGIN_COLORS,
              Constants.PILAR_SIZE,
              Constants.PILAR_SPEED,
              Constants.PILAR_MIN_DISTANCE,
              Constants.PILAR_MAX_DISTANCE,
              Constants.CLOCK_FONT,
              Constants.CLOCK_COLOR,
              Constants.TEXT_FONT)

pygame.display.update()
wait_for_enter()
while stage.update_clock():
    pygame.display.update()
    pass
#wait_for_enter()

pygame.display.update()
