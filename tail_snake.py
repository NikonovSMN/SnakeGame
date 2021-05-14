import pygame
from pygame.sprite import Sprite
from settings import Settings


class TailSnake(Sprite):
    def __init__(self, screen):
        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = Settings()
        self.color = self.settings.snake_tail_color

        # Создаём элемент хвоста змеи
        self.rect = pygame.Rect(0, 0, self.settings.snake_tail_width, self.settings.snake_tail_height)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Флаги перемещения
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_tail(self):
        pygame.draw.rect(self.screen, self.color, self.rect)