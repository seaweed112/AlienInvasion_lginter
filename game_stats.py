"""
game_stats.py
Lincoln Ginter
Alien Invasion Arcade Game - (Track 1)
7/28/2026
Initial repo forked from RedBeard41
Purpose: Track player's stats

"""
class GameStats:
    """Class to track game stats"""
    def __init__(self, ai_game):
        """Initialize stats"""
        self.settings = ai_game.settings
        self.high_score = 0
        self.reset_stats()

    def reset_stats(self):
        """Begin tracking the amount of lives the player has left"""
        self.ships_left = self.settings.ship_lives
        self.score = 0
        self.level = 1