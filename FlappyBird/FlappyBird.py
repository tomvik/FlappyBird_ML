import pygame
from typing import List, Tuple

from pkg import Size, Color, Font
from pkg import Stage


def wait_for_enter():
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN \
                        and event.key == pygame.K_RETURN:
                    waiting = False

pygame.init()

# Window constants
WINDOW_WIDTH: int = 1200
WINDOW_HEIGHT: int = 700
WINDOW_SIZE: Size = Size(WINDOW_WIDTH, WINDOW_HEIGHT)
WINDOW_TITLE: str = "Evolution Simulator"

# Color pallete
CLEAR_GREY: Color = Color(211, 211, 211)
DARK_GREY: Color = Color(140, 140, 140)
BLACK: Color = Color(0, 0, 0)
WHITE: Color = Color(255, 255, 255)

# Stage constants
STAGE_SIZE: Size = Size(800, 500)
WALLS_DIMENSIONS: Size = Size(((WINDOW_WIDTH-STAGE_SIZE.width)/2),
                              ((WINDOW_HEIGHT-STAGE_SIZE.height)/2))
STAGE_COLORS: Tuple[Color, Color] = (CLEAR_GREY, DARK_GREY)

CLOCK_FONT: Font = Font("Trebuchet MS", 25)
CLOCK_COLOR: Color = BLACK
TEXT_FONT: Font = Font("Trebuchet MS", 15)


stage = Stage(WINDOW_SIZE, WINDOW_TITLE, STAGE_SIZE, STAGE_COLORS,
                      CLOCK_FONT, CLOCK_COLOR, TEXT_FONT)
pygame.display.update()

wait_for_enter()

pygame.display.update()