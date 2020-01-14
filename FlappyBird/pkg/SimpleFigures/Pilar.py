import random
from . import Rectangle
from ..Common.Common_Types import *

class Pilar:
    __pilar_width = 0
    __pilar_hole_height = 0
    __stage_top_limit = 0
    __stage_bottom_limit = 0
    __stage_left_limit = 0
    
    def __init__(self, left_position: int,
                 color: Color,
                 background_color: Color):
        random.choice(['top', 'bottom'])
        pass

    def __initializePilar(self, left_position: int, first_one: string):
        if(first_one == 'top'):
            pass
        else:
            pass

    def setClassConstants(self,
                          pilar_width: int,
                          pilar_hole_height: int,
                          stage_top_limit: int,
                          stage_bottom_limit:int,
                          stage_left_limit: int):
        self.__class__.__pilar_width = pilar_width
        self.__class__.__pilar_hole_height = pilar_hole_height
        self.__class__.__stage_top_limit = stage_top_limit
        self.__class__.__stage_bottom_limit = stage_bottom_limit
        self.__class__.__stage_left_limit = stage_left_limit

    def updatePilar(self, pixels: int):
        pass
