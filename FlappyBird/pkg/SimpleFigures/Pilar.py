import random
from .Rectangle import Rectangle
from ..Common.Common_Types import *

class Pilar:
    
    def __init__(self,
                 pilar_width: int,
                 pilar_hole_height: int,
                 stage_top_limit: int,
                 stage_bottom_limit: int,
                 stage_left_limit: int,
                 color: Color,
                 background_color: Color,
                 left_position: int):
        self._pilar_width = pilar_width
        self._pilar_hole_height = pilar_hole_height
        self._stage_top_limit = stage_top_limit
        self._stage_bottom_limit = stage_bottom_limit
        self._stage_left_limit = stage_left_limit
        self._color = color
        self._background_color = background_color
        self._pilar = self.__initializePilar(left_position)

    def __initializePilar(self, left_position: int):
        hole_initial_pos = random.randint(self._stage_top_limit,
                                          self._stage_bottom_limit - self._pilar_hole_height)
        top_pilar_height = hole_initial_pos - self._stage_top_limit
        bottom_pilar_height = self._stage_bottom_limit - (hole_initial_pos + self._pilar_hole_height)
        pilars_PS = (PointSize(left_position, self._stage_top_limit, 
                               self._pilar_width, top_pilar_height),
                     PointSize(left_position, (hole_initial_pos + self._pilar_hole_height), 
                               self._pilar_width, bottom_pilar_height))
        return (Rectangle(pilars_PS[0], self._color, self._background_color),
                  Rectangle(pilars_PS[1], self._color, self._background_color))

    def updatePilar(self, pixels: int):
        for pilar in self._pilar:
            pilar.draw_background()
            pilar.move(Direction(-pixels, 0))
            pilar.draw()
        pass
