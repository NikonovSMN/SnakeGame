import pygame
from pygame.sprite import Sprite
from settings import Settings


class Snake(Sprite):
    def __init__(self, screen):
        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = Settings()
        self.color = self.settings.snake_color

        # Создаём голову змеи и размещаем её в центре
        self.rect = pygame.Rect(0, 0, self.settings.snake_width, self.settings.snake_height)

        self.rect.center = self.screen_rect.center

        # Координаты змеи
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Флаги перемещения
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    # Обновление позиции змеи
    def update(self):
        if self.moving_left and self.rect.left:
            self.x -= self.settings.snake_speed

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.snake_speed

        if self.moving_up and self.rect.top:
            self.y -= self.settings.snake_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.snake_speed

        self.rect.x = self.x
        self.rect.y = self.y

    # Рисуем змею
    def draw_snake(self):
        pygame.draw.rect(self.screen, self.color, self.rect)