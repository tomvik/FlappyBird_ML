from .Common.Common_Types import *
from .SimpleFigures.Pilar import Pilar

class PilarManager:

    def __init__(self,
                 pilar_width: int,
                 pilar_hole_height: int,
                 pilar_min_distance: int,
                 pilar_max_distance: int,
                 pilar_speed: int,
                 stage_limits: Limits,
                 color: Color,
                 background_color: Color):
        self.__pilar_width = pilar_width
        self.__hole_height = pilar_hole_height
        self.__min_distance = pilar_min_distance
        self.__max_distance = pilar_max_distance
        self.__pilar_speed = pilar_speed
        self.__stage_limits = stage_limits
        self.__pilar_color = color
        self.__background_color = background_color

        self.__last_left_position = self.__stage_limits.x_min + self.__max_distance
        self.__pilars = self.__initialize_pilars()

    # Initializes one pilar on the left position.
    def __initialize_pilar(self, left_pos: int):
        return Pilar(self.__pilar_width,
                     self.__hole_height,
                     self.__stage_limits.y_min,
                     self.__stage_limits.y_max,
                     self.__stage_limits.x_min,
                     self.__pilar_color,
                     self.__background_color,
                     left_pos)
    
    # Initializes a set of pilars with the max separation between them.
    def __initialize_pilars(self):
        pilars = list()
        while (self.__last_left_position + self.__pilar_width < self.__stage_limits.x_max):
            pilars.append(self.__initialize_pilar(self.__last_left_position))
            self.__last_left_position += self.__max_distance + self.__pilar_width
        return pilars

    # Apends any new pilars that can be drawn in stage with the separation sent as a parameter.
    def __apend_pilars(self, separation):
        self.__last_left_position += separation + self.__pilar_width
        while (self.__last_left_position + self.__pilar_width < self.__stage_limits.x_max):
            self.__pilars.append(self.__initialize_pilar(self.__last_left_position))
            self.__last_left_position += separation + self.__pilar_width

    # Returns the left limit for the pilars
    def get_pilar_left_limit(self):
        return self.__stage_limits.x_min
    
    # Updates the pilar positions, deleting them if they've crossed the left limit and adding
    # new ones if there's space.
    def update_pilars(self):
        list_size = len(self.__pilars)
        i = 0
        while i < list_size:
            if(self.__pilars[i].update_pilar(self.__pilar_speed) is False):
                self.__pilars.pop(i)
                list_size -= 1
                i -= 1
            i += 1
        self.__last_left_position = self.__pilars[-1].get_left_position()
        self.__apend_pilars(self.__max_distance)