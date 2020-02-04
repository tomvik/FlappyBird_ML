import pygame
from typing import Dict, List, Tuple

from .Common.Common_Types import *
from .BirdManager import BirdManager
from .PilarManager import PilarManager
from .Stage import Stage

class GameEngine:

    def __init__(self,
                 window_size: Size,
                 window_title: str,
                 stage_size: Size,
                 stage_colors: Tuple[Color, Color],
                 margin_colors: Tuple[Color, Color],
                 pilar_size: Size,
                 pilar_speed: int,
                 pilar_min_distance: int,
                 pilar_max_distance: int,
                 bird_size: int,
                 clock_font: Font,
                 clock_font_color: Color,
                 text_box_font: Font):
        pygame.init()
        self.__stage = Stage(window_size,
                             window_title,
                             stage_size,
                             stage_colors,
                             margin_colors,
                             clock_font,
                             clock_font_color,
                             text_box_font)
        self.__pilar_manager = PilarManager(pilar_size.width,
                                            pilar_size.height,
                                            pilar_min_distance,
                                            pilar_max_distance,
                                            pilar_speed,
                                            self.__stage.get_pilar_limits(),
                                            self.__stage.get_pilar_color(),
                                            self.__stage.get_stage_color())
        bird_point_size = PointSize(self.__pilar_manager.get_pilar_left_limit(), window_size.height/2, bird_size, bird_size)
        self.__birds_manager = BirdManager(bird_point_size,
                                           [Color(204, 0, 0)],
                                           self.__stage.get_stage_color(),
                                           self.__stage.get_birds_limits())
        pygame.display.update()
        self.wait_for_enter()
    
    def wait_for_enter(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN \
                        and event.key == pygame.K_RETURN:
                    waiting = False

    def run(self):
        while self.__stage.update_clock():
            self.__pilar_manager.update_pilars()
            keys = [False]
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    keys = [True]
            self.__birds_manager.update_birds(keys)
            pygame.display.update()

        pygame.display.update()
        pass
