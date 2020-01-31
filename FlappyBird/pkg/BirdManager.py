from typing import List
from .Common.Common_Types import *
from .SimpleFigures.Bird import Bird

class BirdManager:

    def __init__(self,
                 rectangle: PointSize,
                 bird_colors: List[Color],
                 background_color: Color,
                 limits: Limits):
        self.__original_rectangle = rectangle
        self.__bird_colors = bird_colors
        self.__background_color = background_color
        self.__limits = limits
        self.__birds = self.__init_tuple_of_birds()
        print(len(self.__birds))

    # Initializes one bird with the selected color and returns it.
    def __init_one_bird(self, color: Color):
        return Bird(self.__original_rectangle,
                    color,
                    self.__background_color,
                    self.__limits)

    # Initializes a tuple of birds with the amount of colors initialized with.
    def __init_tuple_of_birds(self):
        birds = list()
        for color in self.__bird_colors:
            birds.append(self.__init_one_bird(color))
        return tuple(birds)

    # Makes all birds fall.
    def fall_birds(self):
        for bird in self.__birds:
            bird.fall()

    # Flaps the selected bird. Key must go from 0 to the number of birds -1
    def flap_bird(self, key: int):
        self.__birds[key].flap()

    def update_birds(self, keys: List[bool]):
        for i in range(len(self.__birds)):
            self.__birds[i].update(keys[i])
