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
        self.__original_position = Point(rectangle.x, rectangle.y)
        self.__limits = limits
        super().__init__(rectangle, color, background_color)
        self.__alive = True
    
    # Returns true if the bird is still alive.
    def is_alive(self):
        return self.__alive

    # Kills the bird by setting the variable alive to False and drawing the background.
    def died(self):
        self.__alive = False
        self.draw_background()
    
    # Revives the bird by teleporting it to the original position, drawing it and setting
    # the alive variable to True
    def revive(self):
        self.__alive = True
        self.teleport(self.__original_position)
        self.draw()

    # Makes the bird fall, if it reaches the ground, it stays there.
    def fall(self):
        self.draw_background()
        self.move(Direction(0, self.DROP_RATE))
        if(self.outside_area_from_bottom(self.__limits)):
            self.teleport(Point(self.__limits.x_min, self.__limits.y_max-self.get_rectangle().height))
        self.draw()

    # Makes the bird flap, if it reaches the ground, it stays there.
    def flap(self):
        self.draw_background()
        self.move(Direction(0, self.FLAP_RATE))
        if(self.outside_area_from_top(self.__limits)):
            self.teleport(Point(self.__limits.x_min, self.__limits.y_min))
        self.draw()

    # Updates the bird depending if it flaps or falls.
    def update(self, flap: bool):
        if(flap):
            self.flap()
        else:
            self.fall()

