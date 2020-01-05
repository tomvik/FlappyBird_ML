import pygame
from pkg import Rectangle, Size


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


Rectangle.Rectangle.set_window(WINDOW_SIZE, WINDOW_TITLE)

wait_for_enter()

pygame.display.update()