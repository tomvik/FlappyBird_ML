from typing import Tuple
from .Rectangle import Rectangle
from ..Common.Common_Types import *

class Bird(Rectangle):
    DROP_RATE = 2
    FLAP_RATE = -15

    def __init__(self,
                 rectangle: PointSize,
                 color: Color,
                 background_color: Color,
                 limits: Limits):
        self.__original_position: Point = Point(rectangle.x, rectangle.y)
        self.__limits: Limits = limits
        super().__init__(rectangle, color, background_color)
        self.__alive: bool = True
        self.__distance_to_pilar: int = 0
        self.__distance_to_pilar: int = 0
        self.__frames_alive: int = 0
    
    # Returns true if the bird is still alive.
    def is_alive(self) -> bool:
        return self.__alive

    # Kills the bird by setting the variable alive to False and drawing the background.
    def died(self) -> None:
        self.__alive = False
        self.draw_background()
    
    # Revives the bird by teleporting it to the original position, drawing it and setting
    # the alive variable to True
    def revive(self) -> None:
        self.__alive = True
        self.teleport(self.__original_position)
        self.draw()

    # Makes the bird fall, if it reaches the ground, it stays there.
    def fall(self) -> None:
        self.draw_background()
        self.move(Direction(0, self.DROP_RATE))
        if(self.outside_area_from_bottom(self.__limits)):
            self.teleport(Point(self.__limits.x_min, self.__limits.y_max-self.get_rectangle().height))
        self.draw()

    # Makes the bird flap, if it reaches the ground, it stays there.
    def flap(self) -> None:
        self.draw_background()
        self.move(Direction(0, self.FLAP_RATE))
        if(self.outside_area_from_top(self.__limits)):
            self.teleport(Point(self.__limits.x_min, self.__limits.y_min))
        self.draw()

    # Updates the bird depending if it flaps or falls.
    def update(self, flap: bool) -> None:
        if(flap):
            self.flap()
        else:
            self.fall()
        self.__frames_alive += 1

    # Returns an integer stating the x_max limit.
    def get_right_position(self) -> int:
        return self.get_limits().x_max

    # Returns an integer stating the y_center of the bird.
    def get_y_midpoint(self) -> int:
        return self.get_center().y

    # Updates the distances to the pilar and hole.
    def update_distances(self, distance_to_pilar: int, distance_to_hole: int) -> None:
        self.__distance_to_pilar = distance_to_pilar
        self.__distance_to_hole = distance_to_hole

   # Gets the distances to the pilar and hole as a tuple.
    def get_distances(self) -> Tuple[int, int]:
        return self.__distance_to_pilar, self.__distance_to_hole

    # Gets the amount of frames that it was alive.
    def get_time_alive(self) -> int:
        return self.__frames_alive

