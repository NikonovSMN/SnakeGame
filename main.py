import pygame
import sys
from settings import Settings
from snake import Snake
from tail_snake import TailSnake
from apple import Apple
import time

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # Задаём размеры окна и название окна
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        pygame.display.set_caption(self.settings.title)

        # Создаём экземляры змеи и яблок
        self.snake = Snake(self.screen)
        self.snake_tails = pygame.sprite.Group()
        self.apples = pygame.sprite.Group()

        # список предыдущих координат
        self.coordinates_snake = []
        self.coordinates_snake.append((self.snake.x, self.snake.y))

        self.clock = pygame.time.Clock()
    # Основной игровой цикл
    def run_game(self):
        #  and not pygame.sprite.spritecollideany(self.snake, self.snake_tails) and self.stena()
        while True and not pygame.sprite.spritecollideany(self.snake, self.snake_tails) and self.stena():

            self._check_events()
            self._create_apple()
            self._pick_up_apple()
            self._update_coord()
            self.snake.update()
            self.snake_tails.update()
            self._new_coord()
            self._update_screen()
            self.clock.tick(30)



    def stena(self):
        if self.snake.rect.x < 0 or self.snake.rect.y < 0:
            return False

        if self.snake.rect.x > self.settings.width or self.snake.rect.y > self.settings.height - 25:
            return False

        return True


    # Проверка ивентов
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(self.coordinates_snake)
                sys.exit()


            elif event.type == pygame.KEYDOWN:
                self._ckeck_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._ckeck_keyup_events(event)

    # Проверка ивентов нажатия
    def _ckeck_keydown_events(self, event):
        if event.key == pygame.K_LEFT and not self.snake.moving_right:
            self.snake.moving_left = True
            self.snake.moving_right = False
            self.snake.moving_up = False
            self.snake.moving_down = False

        if event.key == pygame.K_RIGHT and not self.snake.moving_left:
            self.snake.moving_left = False
            self.snake.moving_right = True
            self.snake.moving_up = False
            self.snake.moving_down = False

        if event.key == pygame.K_UP and not self.snake.moving_down:
            self.snake.moving_left = False
            self.snake.moving_right = False
            self.snake.moving_up = True
            self.snake.moving_down = False

        if event.key == pygame.K_DOWN and not self.snake.moving_up:
            self.snake.moving_left = False
            self.snake.moving_right = False
            self.snake.moving_up = False
            self.snake.moving_down = True

    # Проверка ивентов отпускания клавиши
    def _ckeck_keyup_events(self, event):
        pass

    # Создаём яблоко (не пересекается с другими яблоками и создается не больше self.settings.apple_count)
    def _create_apple(self):
        apple = Apple(self.screen)
        if not pygame.sprite.spritecollideany(apple, self.apples) and len(self.apples) < self.settings.apple_count:
                self.apples.add(apple)

    # Подбираем яблоки
    def _pick_up_apple(self):
        if pygame.sprite.spritecollideany(self.snake, self.apples):
            self.apples.remove(pygame.sprite.spritecollideany(self.snake, self.apples))
            self._create_tail()

    # Создаём хвост
    def _create_tail(self):
        tail = TailSnake(self.screen)
        self.snake_tails.add(tail)

    # очищает список старых координат и записывает новые
    def _new_coord(self):
        self.coordinates_snake.clear()

        # self.coordinates_snake.append(self.snake.rect.topleft)
        self.coordinates_snake.append((self.snake.rect.x, self.snake.rect.y))
        for tail in self.snake_tails.sprites():
            self.coordinates_snake.append((tail.rect.x, tail.rect.y))

    # записывает новые координаты для хвоста
    def _update_coord(self):
        if len(self.coordinates_snake):
            self.coordinates_snake.reverse()
            for tail in self.snake_tails.sprites():
                tail.x, tail.y = self.coordinates_snake.pop()


            # Обновление экрана и элементов на нём
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.snake.draw_snake()

        tails = self.snake_tails.sprites()
        for tail in tails:
            tail.draw_tail()

        for apple in self.apples.sprites():
            apple.draw_apple()


        pygame.display.flip()

if __name__ == "__main__":
    snake = SnakeGame()
    snake.run_game()
