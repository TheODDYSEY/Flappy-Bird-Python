# world.py
import pygame
from pipe import Pipe
from bird import Bird
from game import GameIndicator
from settings import WIDTH, HEIGHT, pipe_size, pipe_gap, pipe_pair_sizes
import random

class World:
    def __init__(self, screen):
        self.screen = screen
        self.world_shift = 0
        self.current_x = 0
        self.gravity = 0.5
        self.current_pipe = None
        self.pipes = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self._generate_world()
        self.playing = False
        self.game_over = False
        self.passed = True
        self.game = GameIndicator(screen)

    # adds pipe once the last pipe added reached the desired pipe horizontal spaces
    def _add_pipe(self):
        pipe_pair_size = random.choice(pipe_pair_sizes)
        top_pipe_height, bottom_pipe_height = pipe_pair_size[0] * pipe_size, pipe_pair_size[1] * pipe_size
        pipe_top = Pipe((WIDTH, 0 - (bottom_pipe_height + pipe_gap)), pipe_size, HEIGHT, True)
        pipe_bottom = Pipe((WIDTH, top_pipe_height + pipe_gap), pipe_size, HEIGHT, False)
        self.pipes.add(pipe_top)
        self.pipes.add(pipe_bottom)
        self.current_pipe = pipe_top

    # creates the player and the obstacle
    def _generate_world(self):
        self._add_pipe()
        bird = Bird((WIDTH//2 - pipe_size, HEIGHT//2 - pipe_size), 30)
        self.player.add(bird)