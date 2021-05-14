class Settings:
    def __init__(self):
        # window settings
        self.title = 'Snake'  # Название окна
        self.width = 800  # Ширина окна
        self.height = 600  # Высота окна
        self.bg_color = (50, 50, 50)

        # snake settings
        self.snake_speed = 10 # Скорость перемещения змейки
        self.snake_width = 10
        self.snake_height = 10
        self.snake_color = (50, 130, 0)

        # tail snake settings
        self.snake_tail_width = 10
        self.snake_tail_height = 10
        self.snake_tail_color = (50, 160, 0)

        # apple settings
        self.apple_count = 50  # Максимальное кол-во яблок на поле
        self.apple_width = 10
        self.apple_height = 10
        self.apple_color = (240, 50, 50)