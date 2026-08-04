"""
scoreboard.py
Lincoln Ginter
Alien Invasion Arcade Game - (Track 1)
7/28/2026
Initial repo forked from RedBeard41
"""
import pygame.font

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #Font Settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score
        
        #Prepare the score image
        self.prep_score()

    def prep_score(self):
        """Render the score"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #Show the score at the top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)