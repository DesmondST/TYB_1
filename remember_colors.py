import pygame.time
from ariphmetic import *
from Struct import *
from random import randint


def position_in_the_table(rec_id, table_size_x):
    position_x = rec_id % table_size_x
    position_y = rec_id // table_size_x
    position_x = (67+84) * position_x + 47
    position_y = 141 + (47+84) * position_y
    return position_x, position_y


class RememberColorsGame:
    def __init__(self, window, count_of_colors, font):
        self.start_time = 0
        self.font = font
        #  flags
        self.is_randomized = False
        self.is_started = False
        self.win = None
        self.delta_time = None
        self.right_ids = None
        self.rectangles_borders = None
        self.rectangles = None
        self.color = [
            (128, 128, 128),  # серый
            (191, 155, 145),  # бежевый
            (249, 220, 92),  # желтый
            (49, 133, 252),  # голубой
            (36, 130, 50),  # Зеленый
            (253, 197, 245),  # розовый
            (201, 13, 14),  # красный
            (30, 56, 69),  # темно-синий
            (50, 35, 59),  # темно-фиолетовый
            (99, 80, 55),  # коричневый
            (69, 4, 17),  # темно-красный
            (0, 0, 0),  # черный
        ]
        self.window = window
        self.count_of_colors = count_of_colors
        self.new_game()
        #  top nav bar position and button positions
        self.top_nav_bar = Rectangle(
            window=window, width=468, height=86, x=6, y=13, border_radius=43, border_color=(128, 128, 128), border_size=4
        )
        self.end_button = ButtonWithImg(
            window=window, width=27, height=27, x=480 - 60, y=13+(86-27)/2,
            text_size=15, text_color='Black', button_function=self.end_game,
            img_source='images/end_level.png')
        self.text_time_font = pygame.font.Font(font, 35)
        self.start_game_text = ['Сейчас у тебя будет 5 секунд,',
                                'чтобы запомнить расположение',
                                'всех цветов, ты готов?']
        self.tyb_logo = pygame.image.load('images/tyb.png')
        self.tyb_logo = pygame.transform.scale(self.tyb_logo, (53, 53))
        #  start game instruction
        self.start_game_text_font = pygame.font.Font(font, 30)
        self.start_game_button = Button(
            window=window, width=480, height=720, x=0, y=0, bgcolor=(128, 128, 128),
            button_function=self.start_game
        )

    def draw_game(self, __events):
        k = 0
        #  render nav_bar
        self.top_nav_bar.draw_rectangle()
        self.window.blit(self.tyb_logo, (34, 13+(86 - 53)/2))
        if self.is_started:
            if not self.is_randomized:
                text = f'{5 - __events[2] // 1000}'
                text_size_x, text_size_y = self.text_time_font.size(text)
                text_time_surface = self.text_time_font.render(text, True, (255, 0, 0))
                self.window.blit(text_time_surface, (6 + (468 - text_size_x) // 2, 13+(86 - text_size_y) // 2))

            else:
                text = f'{__events[2] // 1000 - 5}'
                text_size_x, text_size_y = self.text_time_font.size(text)
                text_time_surface = self.text_time_font.render(text, True, (255, 0, 0))
                self.window.blit(text_time_surface, (6 + (468 - text_size_x) // 2, 13+(86 - text_size_y) // 2))

            self.end_button.draw_button()
            for rectangle in self.rectangles:
                rectangle.draw_rectangle()
            for rectangle in self.rectangles_borders:
                rectangle.draw_rectangle()
            if self.is_randomized:
                for event in __events[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for rectangle in self.rectangles:
                            if rectangle.collidepoint(__events[0]):
                                rectangle.is_in_using = True
                        if self.end_button.collidepoint(__events[0]):
                            self.end_game()
                            self.end_button.button_function_complete(self.win)
                    if event.type == pygame.MOUSEMOTION:
                        for rectangle in self.rectangles[::-1]:
                            if rectangle.is_in_using:
                                rectangle.left, rectangle.top = rectangle.left + event.rel[0], rectangle.top + \
                                                                event.rel[1]
                                break
                    elif event.type == pygame.MOUSEBUTTONUP:
                        for rectangle in self.rectangles:
                            rectangle.is_in_using = False
                            k = 0
                            for border in self.rectangles_borders:
                                a = rectangle.magniting(border)  # проверка на пересечение квадратика и рамочки
                                if a is True:
                                    # новый x и y для квадратика который был в рамочке
                                    self.rectangles[k].left = rectangle.start_x
                                    self.rectangles[k].top = rectangle.start_y
                                    # новый x и y для рамочки
                                    border.left = rectangle.start_x - 4
                                    border.top = rectangle.start_y - 4
                                    # получение индекса прямоугольника, который пересекся
                                    index = self.rectangles.index(rectangle)
                                    # объявление новой позиции для рамочки, в которой находился этот прямоугольничек
                                    self.rectangles_borders[index].left = rectangle.left - 4
                                    self.rectangles_borders[index].top = rectangle.top - 4
                                    # объявление новой стартовой позиции для рамочек
                                    self.rectangles[k].start_x = rectangle.start_x
                                    self.rectangles[k].start_y = rectangle.start_y
                                    rectangle.start_x = rectangle.left
                                    rectangle.start_y = rectangle.top
                                k += 1
        else:
            self.delta_time = __events[2]
            self.start_game_button.draw_button()
            for i in self.start_game_text:
                text_surface = self.start_game_text_font.render(i, True, (255, 0, 0))
                text_size_x, text_size_y = self.start_game_text_font.size(i)
                self.window.blit(text_surface, ((480 - text_size_x) / 2, text_size_y * k))
                k += 1
            for event in __events[1]:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_game_button.collidepoint(__events[0]):
                        self.start_game_button.button_function()
        return None

    def randomize_position(self):
        new_ids = []  # новые id
        k = 0  # счетчик
        while len(new_ids) < self.count_of_colors:  # цикл для рандомизации
            new_id = randint(0, self.count_of_colors - 1)  # генератор нового айди
            if new_id != self.right_ids[k] and new_id not in new_ids:  # проверка айди на валидность
                new_ids.append(new_id)  # добавление айди в список
                k += 1  # увелечение счетчика
        k = 0  # обнуление счетчика
        for rectangle in self.rectangles:  # пробег по всем элементам в массиве rectangles
            rec_id = new_ids[k]
            # генерация новой позиции для цветного прямоугольника
            rectangle.left, rectangle.top = position_in_the_table(rec_id, 3)
            rectangle.start_x, rectangle.start_y = rectangle.left, rectangle.top  # объвяление новой стартовой позиции
            self.rectangles_borders[k].left, self.rectangles_borders[
                k].top = rectangle.left - 4, rectangle.top - 4  # объявление новой позиции рамочки
            k += 1  # прибавление счетчика
        self.is_randomized = True

    def new_game(self):
        # объекты интерфейса
        self.rectangles = []
        self.rectangles_borders = []
        # генерация списка кнопок
        for i in range(self.count_of_colors):
            rectangle = RectangleForGame(
                window=self.window, width=84, height=84, x=0, y=0, bgcolor=self.color[i]
            )
            self.rectangles.append(rectangle)
        # генерация положения кнопок
        self.right_ids = []
        while len(self.right_ids) != self.count_of_colors:
            random_id = randint(0, self.count_of_colors - 1)
            if random_id not in self.right_ids:
                self.right_ids.append(random_id)
        k = 0
        for rectangle in self.rectangles:
            rectangle.id = self.right_ids[k]
            rec_id = rectangle.id
            rectangle.left, rectangle.top = position_in_the_table(rec_id, 3)
            k += 1
        # генерация рамочек, куда вставлять кнопки
        for rectangle in self.rectangles:
            self.rectangles_borders.append(
                Rectangle(
                    window=self.window, width=rectangle.width + 8, height=rectangle.height + 8, x=rectangle.left - 4,
                    y=rectangle.top - 4, border_size=4, border_color=(128, 128, 128), border_radius=5
                )
            )

    def end_game(self):
        for rectangle in self.rectangles:
            pos_x, pos_y = position_in_the_table(rectangle.id, 3)
            if not (rectangle.left == pos_x and rectangle.top == pos_y):
                self.win = False
                break
        else:
            self.win = True

    def start_game(self):
        self.is_started = True

    def end_button_fnc_set(self, function):
        self.end_button.button_function = function



