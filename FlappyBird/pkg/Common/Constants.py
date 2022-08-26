from typing import List, Tuple
from .Common_Types import *

# Simulation constants
FILE_NAME: str = "stats_of_run_"

# Window constants
WINDOW_WIDTH: int = 1200
WINDOW_HEIGHT: int = 700
WINDOW_SIZE: Size = Size(WINDOW_WIDTH, WINDOW_HEIGHT)
WINDOW_TITLE: str = "FlappyBird with ML Simulator"

# Color pallete
CLEAR_GREY: Color = Color(211, 211, 211)
DARK_GREY: Color = Color(140, 140, 140)
BLACK: Color = Color(0, 0, 0)
WHITE: Color = Color(255, 255, 255)
STAGE_BACKGROUND: Color = Color(113, 145, 146)
STAGE_PILARS: Color = Color(95, 103, 105)
WINDOW_BACKGROUND: Color = Color(60, 66, 69)
TEXT_COLOR: Color = Color(223, 205, 195)

# Birds constants
BIRD_SIZE: int = 5
BIRDS_COLOR: List[Color] = [Color(204, 0, 0), Color(204, 102, 0),
                            Color(204, 204, 0), Color(102, 204, 0),
                            Color(0, 204, 0), Color(0, 204, 102),
                            Color(0, 204, 204), Color(0, 102, 204),
                            Color(0, 0, 204), Color(102, 0, 204)]

# Stage constants
STAGE_SIZE: Size = Size(800, 500)
PILAR_SIZE: Size = Size(20, 40)
PILAR_MAX_DISTANCE: int = 200
PILAR_MIN_DISTANCE: int = 100
PILAR_SPEED: int = 1
WALLS_DIMENSIONS: Size = Size(((WINDOW_WIDTH-STAGE_SIZE.width)/2),
                              ((WINDOW_HEIGHT-STAGE_SIZE.height)/2))
STAGE_COLORS: Tuple[Color, Color] = (STAGE_BACKGROUND, STAGE_PILARS)
MARGIN_COLORS: Tuple[Color, Color] = (WINDOW_BACKGROUND, TEXT_COLOR)
STAGE_CENTER: Point = Point(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

CLOCK_FONT: Font = Font("Trebuchet MS", 25)
CLOCK_COLOR: Color = BLACK
TEXT_FONT: Font = Font("Trebuchet MS", 15)

INITIAL_BIRDS: str = "Initial_Birds"
MAX_GENERATION: str = "Max_Generations"
GENERATION: str = "Generation"

TEXTBOX_MATRIX_IS_INPUT: List[bool] = [False, True,
                                       False, True,
                                       False, True]

TEXTBOX_MATRIX: List[Tuple[str, str]] = \
    [("", "Birds:"), (INITIAL_BIRDS, "1    "),
     ("", "Max generations:"), (MAX_GENERATION, "4    "),
     ("", "Generation:"), (GENERATION, "0    ")]

INSTRUCTIONS_TEXTBOXES: List[Tuple[str, str]] = \
    [("", "Pre-game Instructions:"), ("", " "),
     ("", "Press enter to start."), ("", " "),
     ("", " "), ("", " "),
     ("", "In-game Instructions:"), ("", " "),
     ("", "Key:  "), ("", "Effect:"),
     ("", "Exit   "), ("", "Quit the game")]

INSTRUCTIONS_INPUT: List[bool] = [False] * len(INSTRUCTIONS_TEXTBOXES)
