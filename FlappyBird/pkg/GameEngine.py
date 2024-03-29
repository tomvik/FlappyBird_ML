import multiprocessing
import neat
import numpy as np
import os
import pickle
import pygame
from typing import Dict, List, Tuple

from .Common.Common_Types import *
from .Common import Constants
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
        bird_point_size = PointSize(self.__pilar_manager.get_pilar_left_limit(
        ), window_size.height/2, bird_size, bird_size)
        pygame.display.update()

        self.wait_for_enter()
        stage_data = self.__load_stage_state()
        self.__max_generation = stage_data[Constants.MAX_GENERATION]
        self.__birds_manager = BirdManager(bird_point_size,
                                           Constants.BIRDS_COLOR[0:stage_data[Constants.INITIAL_BIRDS]],
                                           self.__stage.get_stage_color(),
                                           self.__stage.get_birds_limits(),
                                           stage_data[Constants.MAX_GENERATION])
        pygame.display.update()

    def __del__(self):
        pygame.quit()

    # Returns a list of the values of the text_boxes.
    def __load_stage_state(self) -> Dict[str, int]:
        return self.__stage.get_text_values()

    # Updates the pilars and birdsn and if there's any collision, it kills the bird.
    def __update_pilars_and_birds(self, keys: List[int]): #-> Tuple[List[Tuple[int, int], List[int]]]:
        self.__pilar_manager.update_pilars()
        self.__birds_manager.update_birds(keys)
        self.__birds_manager.collision_check(
            self.__pilar_manager.get_leftmost_pilar())

        return self.__birds_manager.get_distances(), self.__birds_manager.get_times()

    # Restarts the pilars and birds for a new round.
    def __restart_game(self):
        self.__pilar_manager.restart_pilars()
        self.__birds_manager.restart_birds()
        self.__stage.reset_clock()
        self.__stage.new_round_stage(self.__birds_manager.get_generation())

    # Holds until an enter was pressed
    def wait_for_enter(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if self.__is_enter(event):
                    waiting = False

    # Returns true if the key pressed was enter.
    def __is_enter(self, event: pygame.event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return True
        return False

    # Returns true if quit or escape have been pressed.
    def __maybe_quit(self, event: pygame.event) -> bool:
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True
        return False

    # Handles the events during the game.
    def __handle_in_game_events(self) -> int:
        for event in pygame.event.get():
            if self.__maybe_quit(event):
                return 1
            if self.__is_enter(event):
                return 2
        return 0

    # Main loop that runs the game.
    # def run(self):
    #     case = 0
    #     while self.__birds_manager.is_there_another_generation():
    #         while self.__birds_manager.is_any_bird_alive():
    #             self.__stage.update_clock()
    #             keys = [0]*self.__birds_manager.number_of_birds()
    #             case = self.__handle_in_game_events()
    #             if case == 1:
    #                 break
    #             elif case == 2:
    #                 keys[0] = 1
    #             distances, times = self.__update_pilars_and_birds(keys)
    #             print(distances, times)
    #             pygame.display.update()
    #         if case == 1:
    #             break
    #         self.__restart_game()

    #     pygame.display.update()

    def eval_genome(self, genome, config):
        net = neat.nn.FeedForwardNetwork.create(genome, config)

        fitnesses = []

        # case = 0
        runs_per_net = 2
        for runs in range(runs_per_net):

            fitness = 0
            keys = [0]*self.__birds_manager.number_of_birds()
            while self.__birds_manager.is_any_bird_alive() and fitness < 200000:
                self.__stage.update_clock()
                distances, times = self.__update_pilars_and_birds(keys)
                pygame.display.update()

                inputs = [-distances[0][1]]
                keys[0] = np.argmax(net.activate(inputs)) # two outputs, 0 or 1

                fitness += times[0] - abs(distances[0][1])
                # fitness = -abs(distances[0][1])

                print(inputs, fitness, keys)


            fitnesses.append(fitness)


            # if case == 1:
            #     break

            self.__restart_game()

        # pygame.display.update()

        print('FITNESSES', fitnesses)

        return np.mean(fitnesses)

    def eval_genomes(self, genomes, config):
        for genome_id, genome in genomes:
            genome.fitness = self.eval_genome(genome, config)

    # def run(self):
    #     local_dir = os.path.dirname(__file__)
    #     config_path = os.path.join(local_dir, 'config')
    #     config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
    #                      neat.DefaultSpeciesSet, neat.DefaultStagnation,
    #                      config_path)

    #     pop = neat.Population(config)
    #     stats = neat.StatisticsReporter()
    #     pop.add_reporter(stats)
    #     pop.add_reporter(neat.StdOutReporter(True))

    #     pe = neat.ThreadedEvaluator(1, self.eval_genome)
    #     print('HEY')
    #     winner = pop.run(pe.evaluate)

    #     print(winner)

    #     # Save the winner.
    #     with open('winner', 'wb') as f:
    #         pickle.dump(winner, f)

    def run(self):
        with open('winner', 'rb') as f:
            c = pickle.load(f)

        print('Loaded genome:')
        print(c)

        # Load the config file, which is assumed to live in
        # the same directory as this script.
        local_dir = os.path.dirname(__file__)
        config_path = os.path.join(local_dir, 'config')
        config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                            neat.DefaultSpeciesSet, neat.DefaultStagnation,
                            config_path)

        

        net = neat.nn.FeedForwardNetwork.create(c, config)


        case = 0
        fitness = 0
        keys = [0]*self.__birds_manager.number_of_birds()
        while self.__birds_manager.is_any_bird_alive():
            self.__stage.update_clock()
            case = self.__handle_in_game_events()
            if case == 1:
                break
            elif case == 2:
                keys[0] = 1
            distances, times = self.__update_pilars_and_birds(keys)
            pygame.display.update()

            inputs = [-distances[0][1]]
            keys[0] = np.argmax(net.activate(inputs)) # two outputs, 0 or 1

            fitness = times[0] - abs(distances[0][1])

            print(inputs, fitness, keys)

