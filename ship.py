"""
ship.py
Lincoln Ginter
Alien Invasion Arcade Game - (Track 1)
7/28/2026
Initial repo forked from RedBeard41
Purpose: Define the player's ship

"""
from pathlib import Path
import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    """Class for the player's ship"""
    def __init__(self, ai_game):
        super().__init__()
        """Create ship and its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        # Load image with pathlib
        image_path = Path('Assets') / 'images' / 'ship.png'
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.center_ship()

        # Movement flags for vertical movement
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Move the ship vertically based on movement flags"""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Update the rect object with  the new position
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship on the screen"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Position ship centered on the right edge of the screen"""
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)