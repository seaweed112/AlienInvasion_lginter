"""
settings.py
Lincoln Ginter
Alien Invasion Arcade Game - (Track 1)
7/28/2026
Initial repo forked from RedBeard41
"""
class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.resolution = (self.screen_width, self.screen_height)
        self.bg_color = (230, 230, 230)

        self.bullet_width = 15.0
        self.bullet_height = 5.0
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 6

        self.fleet_drop_speed = 10


        self.speedup_scale = 2
        self.score_scale = 1.5

        self.ship_lives = 3

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize dynamic settings"""
        self.ship_speed = 3.0
        self.alien_speed = .1
        self.bullet_speed = 5.0
        self.alien_points = 50
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase the speed settings"""
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)