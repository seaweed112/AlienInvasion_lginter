"""
Alien Invasion.py
Lincoln Ginter
Alien Invasion Arcade Game - (Track 1)
7/28/2026
Initial repo forked from RedBeard41
Purpose: Main game file to initialize Pygame, manage main game loop, and coordinate events.
"""
import sys
import pygame
from time import sleep

from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.game_active = False

        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.resolution)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Alien Invasion - Track 1")

        self.bg_color = self.settings.bg_color
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.play_button = Button(self, "Play")

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_aliens()
                self._update_bullets()
                self._update_aliens()
                
            self._update_screen()
            self.clock.tick(60)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )
        if collisions:
            self.stats.score += self.settings.alien_points
            self.sb.prep_score()
            
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increease_speed()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self._reset_game()

    def _reset_game(self):
        self.stats.reset_stats()
        self.sb.prep_score()
        self.game_active = True

        self.bullets.empty()
        self.aliens.empty()

        self._create_fleet()
        self.ship.center_ship()

        pygame.mouse.set_visible(False)
        self.settings.initialize_dynamic_settings()

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_up = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_up = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_down = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)

        self.sb.show_score()

        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        current_x, current_y = alien_width, alien_height

        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y) 
                current_x += 2 * alien_width

            current_y += 2 * alien_width
            current_x = alien_width

    def _create_alien(self, x_position, y_position):
        """Create enemies for the fleet"""
        new_alien = Alien(self)
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """Update the positions of each enemy"""
        self._check_fleet_edges()
        self.aliens.update()
        
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _ship_hit(self):
        """React to being hit by an enemy"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_fleet_edges(self):
        """React to aliens reaching the borders of the screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Move down and reverse direction"""
        for alien in self.aliens.sprites(): 
            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """If the aliens reach the bottom of the screen, kill the player."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break
 
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()