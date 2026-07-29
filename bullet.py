"""
bullet.py
Lincoln Ginter
Alien Invasion Arcade Game - (Track 1)
7/28/2026
Initial repo forked from RedBeard41
"""
import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """Class to manage bullets fired from the player's ship"""
    def __init__(self, ai_game):
        """Create the bullet at the front of the ship"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        #Create bullet
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        #Set it to the ships midleft
        self.rect.midleft = ai_game.ship.rect.midleft
        
        #Store position as a float for the horizontal movement
        self.x = float(self.rect.x)

    def update(self): 
        """Move the bullet left across the screen"""
        self.x -= self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)