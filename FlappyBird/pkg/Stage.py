import pygame
from typing import Dict, List, Tuple

from .Common.Common_Types import *
from .Common import Constants
from .Math import Distances
from .SimpleFigures.Rectangle import Rectangle
from .SimpleFigures.Clock import Clock
from .SimpleFigures import TextBox


class Stage:
    def __init__(self,
                 window_size: Size,
                 window_title: str,
                 stage_size: Size,
                 stage_colors: Tuple[Color, Color],
                 margin_colors: Tuple[Color, Color],
                 clock_font: Font,
                 clock_font_color: Color,
                 text_box_font: Font):
        Rectangle.set_window(window_size, window_title)
        self.__width = stage_size.width
        self.__height = stage_size.height
        self.__stage_color = stage_colors[0]
        self.__pilar_color = stage_colors[1]
        self.__margin_color = margin_colors[0]
        self.__margin_text_color = margin_colors[1]

        self.__window_width = window_size.width
        self.__window_height = window_size.height
        self.__margin_width = (self.__window_width - self.__width) / 2
        self.__margin_height = (self.__window_height - self.__height) / 2

        self.__margins, self.__stage = self.__initialize_stage()
        self.__text_boxes = self.__initialize_text_boxes(text_box_font)

        clock_pos = Point(self.__width + self.__margin_width + 1,
                          self.__height + self.__margin_height)
        self.__clock = Clock(clock_pos, self.__margin_color, self.__margin_text_color,
                             clock_font, clock_font_color)

    # Initializes the stage and returns its margins and stage.
    def __initialize_stage(self) -> Tuple[List[Rectangle], Rectangle]:
        margin_rects = [PointSize(0, 0,
                                self.__margin_width, self.__window_height),
                      PointSize(0, 0,
                                self.__window_width, self.__margin_height),
                      PointSize(self.__margin_width+self.__width, 0,
                                self.__margin_width, self.__window_height),
                      PointSize(0, self.__margin_height+self.__height,
                                self.__window_width, self.__margin_height)]
        stage_rect = PointSize(self.__margin_width, self.__margin_height,
                               self.__width, self.__height)

        margins = list()
        for margin in margin_rects:
            margins.append(Rectangle(margin, self.__margin_color,
                                   self.__margin_text_color))
        stage = Rectangle(stage_rect, self.__stage_color,
                          self.__pilar_color)
        return margins, stage

    # Initializes the text boxes. This part is partly hard_coded.
    def __initialize_text_boxes(self, font: Font) -> List[TextBox.TextBox]:
        text_boxes = list()

        colors = (self.__margin_text_color, self.__margin_color)
        position = Point(self.__width+(self.__margin_width)+10,
                         self.__margin_height)
        separations = (5, 10)
        per_row = 2
        is_input = Constants.TEXTBOX_MATRIX_IS_INPUT
        data = Constants.TEXTBOX_MATRIX
        text_boxes = TextBox.create_matrix(position, colors, separations,
                                           per_row, is_input, data, font)
        position = Point(5, self.__margin_height)
        is_input = Constants.INSTRUCTIONS_INPUT
        data = Constants.INSTRUCTIONS_TEXTBOXES
        text_boxes += TextBox.create_matrix(position, colors, separations,
                                            per_row, is_input, data, font)
        return text_boxes

    # Returns the index of the box with the desired name.
    def __box_index(self, name: str) -> int:
        for i in range(len(self.__text_boxes)):
            if self.__text_boxes[i].get_name() == name:
                return i
        # Should never reach this case.
        return -1

    # Returns the walls.
    def get_margins(self) -> List[Rectangle]:
        return self.__marginss

    # Returns the stage.
    def get_stage(self) -> Rectangle:
        return self.__stage

    # Returns the stage color.
    def get_stage_color(self) -> Color:
        return self.__stage_color

    # Returns the wall color.
    def get_margin_color(self) -> Color:
        return self.__margin_color

    # Returns the Stage limits as in: x_min, y_min, x_max, y_max
    def get_stage_limits(self) -> Limits:
        return self.__stage.get_limits()

    # Gets the TTL in seconds.
    def get_ttl_seconds(self) -> int:
        return self.__clock.get_ttl()/1000

    def get_fps(self) -> int:
        return self.__clock.get_fps()

    # Draws all the text boxes.
    def draw_input_boxes(self):
        for box in self.__text_boxes:
            if box.is_input():
                box.draw()

    # Returns True if it's under its Time To Live, otherwise False.
    def update_clock(self):
        self.__clock.update_clock()
        self.__clock.draw()
        return self.__clock.still_valid()

    # Return the value of each text_box on a list.
    def get_text_values(self) -> Dict[str, int]:
        return_values = dict()
        for text_box in self.__text_boxes:
            if text_box.is_input():
                key_value = text_box.get_name_value()
                return_values[key_value[0]] = key_value[1]
        return return_values

    # Returns the closest wall to the object, its direction towards it,
    # and the distance to travel.
    def closest_wall_to(self,
                        a: Rectangle) -> Tuple[Rectangle, Direction, int]:
        selected_wall, distance = Distances.closest_of_all_Linf(a,
                                                                self.__margins)
        direction = Distances.cardinal_system_direction(a, selected_wall)
        return selected_wall, direction, distance

    # Resets the clock back to 0.
    def reset_clock(self):
        self.__clock.reset()

    # Sets the new TTL.
    def set_ttl_seconds(self, ttl: int):
        self.__clock.set_ttl(ttl*1000)

    # Sets the new FPS.
    def set_fps(self, fps: int):
        self.__clock.set_fps(fps)

    # Handle the events for each text box.
    def handle_event(self, event: pygame.event):
        for text_box in self.__text_boxes:
            text_box.handle_event(event)

    # Handles the in-game updates.
    def handle_in_game(self, key_value: Dict[str, int]) -> bool:
        for key, value in key_value.items():
            self.__text_boxes[self.__box_index(key)].write(str(value))
        self.draw_input_boxes()
        return self.update_clock()

    # Handles the updates necessary for the new round.
    def new_round_stage(self, key_value: Dict[str, int]):
        self.reset_clock()
        self.handle_in_game(key_value)

    # Changes the boxes that won't be updated anymore to output only, and those
    # that will be to input. The naming is weird, but input are the only ones
    # that get updated.
    def initialize_game(self):
        for box in self.__text_boxes:
            if box.has_name():
                if box.get_name() != Constants.INITIAL_CHARACTERS \
                        and box.get_name() != Constants.INITIAL_FOODS:
                    box.change_type()

    # Changes the boxes that won't be updated anymore to output only, and those
    # that will be to input. The naming is weird, but input are the only ones
    # that get updated.
    def continue_game(self):
        for box in self.__text_boxes:
            if box.has_name():
                if box.get_name() != Constants.TTL \
                        and box.get_name() != Constants.FPS:
                    box.change_type()
        self.__clock.reset()
