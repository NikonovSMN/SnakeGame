import pygame
from random import randint
from pygame.sprite import Sprite
from settings import Settings


class Apple(Sprite):
    def __init__(self, screen):
        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = Settings()
        self.color = self.settings.apple_color

        # Создаём яблоко

        #self.rect = pygame.Rect(0, 0, self.settings.apple_width, self.settings.apple_height)
        self.image = pygame.image.load('picture\\toad.png')

        self.rect = self.image.get_rect()
        self.rect.x = randint(0, self.settings.width - self.settings.apple_width)
        self.rect.y = randint(0, self.settings.height - self.settings.apple_height)

        # Координаты яблока
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    # Рисуем яблоко
    def draw_apple(self):
        #pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)