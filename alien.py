"""
alien.py
Lincoln Ginter
Alien Invasion Arcade Game - (Track 1)
7/28/2026
Initial repo forked from RedBeard41
"""
import pygame
from pygame.sprite import Sprite
from pathlib import Path

class Alien(Sprite):
    """Class for the main enemy type"""
    def __init__(self, ai_game):
        """Initialize the alien and set its position"""
        super().__init__()
        self.screen = ai_game.screen
        image_path = Path('Assets') / 'images' / 'enemy_4.png'
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.settings = ai_game.settings

    def update(self):
        """Make the alien move"""
        self.rect.x += self.settings.alien_speed * self.settings.fleet_direction

    def check_edges(self):
        """Returns True if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)