from typing import List
from .Common.Common_Types import *
from .SimpleFigures.Bird import Bird
from .SimpleFigures.Pilar import Pilar


class BirdManager:

    def __init__(self,
                 rectangle: PointSize,
                 bird_colors: List[Color],
                 background_color: Color,
                 limits: Limits,
                 max_generation: int):
        self.__original_rectangle = rectangle
        self.__bird_colors = bird_colors
        self.__background_color = background_color
        self.__limits = limits
        self.__birds = self.__init_tuple_of_birds()
        self.__birds_alive = len(self.__birds)
        self.__generation = 0
        self.__max_generation = max_generation

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

    # Updates all the living birds, regarding if they flap or fall.
    def update_birds(self, keys: List[bool]):
        for i in range(len(self.__birds)):
            if self.__birds[i].is_alive():
                self.__birds[i].update(keys[i])

    # Check if any bird who is alive collided with the pilar. If yes, kill it.
    def collision_check(self, pilar: Pilar):
        up, down = pilar.get_pilars()
        for i in range(len(self.__birds)):
            if self.__birds[i].is_alive():
                if self.__birds[i].collides(up) or self.__birds[i].collides(down):
                    self.__birds_alive -= 1
                    self.__birds[i].died()

    # Returns true if there's any alive bird.
    def is_any_bird_alive(self):
        return self.__birds_alive > 0

    # Returns true if the current generation is not yet the max generation
    def is_there_another_generation(self):
        return self.__generation < self.__max_generation

    # Returns the total number of birds.
    def number_of_birds(self):
        return len(self.__birds)

    # Restars all the birds for a new round
    def restart_birds(self):
        self.__generation += 1
        self.__birds_alive = len(self.__birds)
        for i in range(len(self.__birds)):
            self.__birds[i].revive()

    # Returns the current generation
    def get_generation(self) -> int:
        return self.__generation
