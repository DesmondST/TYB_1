import pygame


class Rectangle(pygame.Rect):
    def __init__(self, window, x=0, y=0, width=0, height=0,
                 bgcolor=0, border_size=0, border_color=0, border_radius=0):
        super(Rectangle, self).__init__((x, y), (width, height))
        self.bgcolor = bgcolor
        self.border_size = border_size
        self.border_color = border_color
        self.window = window
        self.border_radius = border_radius
        if self.border_size is None:
            self.border_color = 0
        if self.bgcolor is None:
            self.bgcolor = 0

    def draw_rectangle(self):
        x, y, width, height = super().left, super().top, super().width, super().height
        if self.bgcolor != 0:
            pygame.draw.rect(self.window, self.bgcolor, [x, y, width, height], border_radius=self.border_radius)
            if self.border_size != 0:
                pygame.draw.rect(self.window, self.border_color, [x, y, width, height],
                                 self.border_size, border_radius=self.border_radius)
        else:
            if self.border_size != 0:
                pygame.draw.rect(self.window, self.border_color, [x, y, width, height],
                                 self.border_size, border_radius=self.border_radius)

    def border_size_change(self, end_border_size, border_size_step):
        if end_border_size != self.border_size:
            if end_border_size - self.border_size < 0:
                self.border_size -= border_size_step
            elif end_border_size - self.border_size > 0:
                self.border_size += border_size_step

    def rotate(self):
        self.width, self.height = self.height, self.width


class RectangleForGame(Rectangle):
    def __init__(self, window=None, x=0, y=0, width=0, height=0,
                 bgcolor=0, border_size=0, border_color=0, border_radius=0):
        super(RectangleForGame, self).__init__(window=window, x=x, y=y, width=width, height=height,
                                               bgcolor=bgcolor, border_size=border_size, border_color=border_color, border_radius=border_radius)
        self.id = 0
        self.is_in_using = False
        self.start_x = None
        self.start_y = None

    def magniting(self, rect):
        if super().colliderect(rect):
            self.left, self.top = rect.left + 4, rect.top + 4
            return True
        return False


class Button(Rectangle):
    def __init__(self, window, x=0, y=0, width=0, height=0, text_size=0, border_size=0, bgcolor=0, text_color=0,
                 border_color=0, border_radius=0, font_name='fonts/font1_roboto.ttf', text='', text_centerx='center',
                 text_centery='center', button_function=None):
        super().__init__(window=window, x=x, y=y, width=width, height=height, bgcolor=bgcolor, border_size=border_size,
                         border_color=border_color, border_radius=border_radius)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bgcolor = bgcolor
        self.text = text
        self.text_size = text_size
        self.font_name = font_name
        self.text_centerx = text_centerx
        self.text_centery = text_centery
        self.button_function = button_function
        self.window = window
        self.border_size = border_size
        self.text_color = text_color
        self.border_color = border_color
        if self.border_size is None:
            self.border_size = 0
        if self.bgcolor is None:
            self.bgcolor = 0

    def draw_button(self):
        rectangle = super(Button, self)
        rectangle.draw_rectangle()
        if self.text.replace(' ', '') != '':
            font = pygame.font.Font(self.font_name, self.text_size)
            text_surface = font.render(self.text, True, self.text_color)
            text_size_x, text_size_y = font.size(self.text)
            if self.text_centerx == "center":  # чтобы текст в кнопке по x был по центру
                if self.text_centery == "center":
                    self.window.blit(text_surface, (self.x + (self.width - text_size_x - self.border_size) // 2, self.y + (
                            self.height - text_size_y - self.border_size) // 2))  # чтобы текст в кнопке по y был по центру
                elif self.text_centery == "top":
                    self.window.blit(text_surface, (
                        self.x + (self.width - text_size_x - self.border_size) // 2,
                        self.y + self.border_size))  # чтобы текст в кнопке по y был сверху
                elif self.text_centery == "bottom":  # чтобы текст в кнопке по y был снизу
                    self.window.blit(text_surface, (self.x + (self.width - text_size_x - self.border_size) // 2,
                                                    self.y + self.height - text_size_y - self.border_size))
            elif self.text_centerx == "left":  # чтобы текст в кнопке по x был слева
                if self.text_centery == "center":  # чтобы текст в кнопке по y был по центру
                    self.window.blit(text_surface, (
                        self.x + self.border_size, self.y + (
                                self.height - text_size_y - self.border_size) // 2))
                elif self.text_centery == "top":  # чтобы текст в кнопке по y был сверху
                    self.window.blit(text_surface, (
                        self.x + self.border_size, self.y + self.border_size))
                elif self.text_centery == "bottom":  # чтобы текст в кнопке по y был снизу
                    self.window.blit(text_surface,
                                     (self.x + self.border_size,
                                      self.y + self.height - text_size_y - self.border_size))
            elif self.text_centerx == "right":  # чтобы текст в кнопке по x был справа
                if self.text_centery == "center":  # чтобы текст в кнопке по y был по центру
                    self.window.blit(text_surface, (self.x + self.width - self.border_size - text_size_x, self.y + (
                            self.height - text_size_y - self.border_size) // 2))
                elif self.text_centery == "top":  # чтобы текст в кнопке по y был сверху
                    self.window.blit(text_surface, (
                        self.x + self.width - self.border_size - text_size_x,
                        self.y + self.border_size))
                elif self.text_centery == "bottom":  # чтобы текст в кнопке по y был снизу
                    self.window.blit(text_surface, (self.x + self.width - self.border_size - text_size_x,
                                                    self.y + self.height - text_size_y - self.border_size))

    def button_function_complete(self, attrs=None):
        if self.button_function is not None and attrs is not None:
            self.button_function(attrs)
        else:
            self.button_function()

    def change_text_color(self, color_step_rgb=(), end_color=None):
        end_color_r = end_color[0]  # Конечный цвет красный канал
        end_color_g = end_color[1]  # Конечный цвет зеленый канал
        end_color_b = end_color[2]  # Конечный цвет синий канал
        color_step_r = color_step_rgb[0]  # Шаг красного канала
        color_step_g = color_step_rgb[1]  # Шаг зеленого канала
        color_step_b = color_step_rgb[2]  # Шаг синего канала
        color_r = self.text_color[0]  # Красный канал
        color_g = self.text_color[1]  # Зеленый канал
        color_b = self.text_color[2]  # Синий канал
        # проверка на осмысленность перемены цвета
        if color_r != end_color_r or color_b != end_color_b or color_g != end_color_g:
            if end_color_r - color_r > 0:
                new_color_r = color_step_r + color_r
            elif end_color_r - color_r < 0:
                new_color_r = color_r - color_step_r
            else:
                new_color_r = color_r
            if end_color_g - color_g > 0:
                new_color_g = color_step_g + color_g
            elif end_color_g - color_g < 0:
                new_color_g = color_g - color_step_g
            else:
                new_color_g = color_g
            if end_color_b - color_b > 0:
                new_color_b = color_step_b + color_b
            elif end_color_b - color_b < 0:
                new_color_b = color_b - color_step_b
            else:
                new_color_b = color_b
            if 0 <= new_color_r <= 255 and 0 <= new_color_g <= 255 and 0 <= new_color_b <= 255:
                self.text_color = (new_color_r, new_color_g, new_color_b)


class ButtonWithImg(Button):
    def __init__(self, window, x=0, y=0, width=0, height=0, text_size=0, border_size=0, bgcolor=0, text_color=0,
                 border_color=0, border_radius=0,
                 font_name='fonts/font1_roboto.ttf', text=' ', text_centerx='center', text_centery='center',
                 button_function=None, img_source=0):
        super(ButtonWithImg, self).__init__(window, x=x, y=y, width=width, height=height, text_size=text_size,
                                            border_size=border_size, bgcolor=bgcolor, text_color=text_color,
                                            border_color=border_color, border_radius=border_radius,
                                            font_name=font_name, text=text, text_centerx=text_centerx,
                                            text_centery=text_centery, button_function=button_function)
        self.is_img = False
        if img_source != 0:
            self.img = pygame.image.load(img_source)
            scale = self.img.get_width() / self.img.get_height()
            self.img = pygame.transform.scale(self.img, (self.width-2*self.border_size, self.height/scale))
            self.is_img = True

    def draw_button(self):
        super(ButtonWithImg, self).draw_button()
        if self.is_img != 0:
            self.window.blit(self.img, (self.x+self.border_size, self.y+self.border_size))


class GameWidget:
    def __init__(self, window, x, y, width, height, bgcolor, border_size, border_color, border_radius, img_source,
                 game_name, button_text, font):
        self.window = window
        self.x = x
        self.y = y
        self.button_text = button_text
        self.img_x = x+border_size+15
        img_height = (height-(border_size+30)*2) + 25
        button_x = width - 200
        self.img_y = (height - img_height - border_size)//2 + self.y
        self.text_x = self.img_x + 15 + img_height
        self.main_rectangle = Rectangle(window=window, x=x, y=y, width=width, height=height, bgcolor=bgcolor,
                                        border_radius=border_radius, border_color=border_color, border_size=border_size)
        self.img = pygame.image.load(img_source)
        self.img = pygame.transform.scale(self.img, (img_height, img_height))
        game_name_font = pygame.font.Font(font, height//6)
        self.game_name = game_name_font.render(game_name, True, (0, 0, 0))
        self.button = Button(window=window, y=(y+height)-15-height//4, x=button_x, width=width//3, height=height//4,
                             text_color=(255, 255, 255), bgcolor=(0, 0, 0), border_radius=5,
                             text=self.button_text, font_name=font, text_size=height//3 - 25)
        self.progress_bar = []
        for i in range(0, 3):
            margin = self.text_x - self.img_x - img_height
            rect_width = (width - self.img_x - img_height - margin*4) // 3
            rect_height = height // 11
            rect_y = (y+height)-15-height//4 - ((y+height)-15-height//4 - self.img_y) // 2
            rect_x = self.text_x + margin*i + rect_width * i
            rect = Rectangle(window, x=rect_x, y=rect_y, width=rect_width, height=rect_height, bgcolor=(21, 209, 45),
                             border_radius=10, border_color=(0, 0, 0), border_size=2)
            self.progress_bar.append(rect)

    def draw(self):
        self.main_rectangle.draw_rectangle()
        self.window.blit(self.img, (self.img_x, self.img_y))
        if self.button_text != '':
            self.button.draw_button()
        self.window.blit(self.game_name, (self.text_x, self.img_y))
        for i in self.progress_bar:
            i.draw_rectangle()


class GameWidgetTop:
    def __init__(self, window, x, y, width, height, bgcolor, border_size, border_color, border_radius,
                 img_source, text, button_text, font, img_profile, text_level, font_1, img_button):
        self.window = window
        self.x = x
        self.y = y
        self.img_x = width // 2 - 25
        self.img_y = height // 2 - 25
        self.img_prof_x = width - 75
        self.img_prof_y = height // 2 - 30
        self.img_button_x = x + 10
        self.img_button_y = height // 3
        button_x = x + 10
        self.text_x = self.img_prof_x - 95
        self.main_rectangle = Rectangle(window=window, x=x, y=y, width=width, height=height, bgcolor=bgcolor,
                                        border_radius=border_radius, border_color=border_color, border_size=border_size)
        self.img = pygame.image.load(img_source)
        self.img = pygame.transform.scale(self.img, (50, 50))
        self.img_prof = pygame.image.load(img_profile)
        self.img_prof = pygame.transform.scale(self.img_prof, (60, 60))
        self.img_button = pygame.image.load(img_button)
        self.img_button = pygame.transform.scale(self.img_button, (30, 30))
        text_font = pygame.font.Font(font, height // 6)
        text_font_1 = pygame.font.Font(font_1, height // 6)
        self.text = text_font.render(text, True, (0, 0, 0))
        self.text_level = text_font_1.render(text_level, True, (128, 128, 128))
        self.button = Button(window=window, y=height // 3, x=button_x, width=50,
                             height=50,
                             text_color=(255, 255, 255), bgcolor=(255, 255, 255), border_radius=5,
                             text=button_text, font_name=font, text_size=height // 3 - 25)

    def draw(self):
        self.main_rectangle.draw_rectangle()
        self.window.blit(self.img, (self.img_x, self.img_y))
        self.window.blit(self.img_prof, (self.img_prof_x, self.img_prof_y))
        self.button.draw_button()
        self.window.blit(self.text, (self.text_x, self.img_y))
        self.window.blit(self.text_level, (self.text_x, self.img_y + 25))
        self.window.blit(self.img_button, (self.img_button_x, self.img_button_y))


class GameInfo:
    def __init__(self, window, x, y, width, height, bgcolor, border_size, border_color, border_radius, img_source,
                 game_name, font):
        self.window = window
        self.x = x
        self.y = y
        self.img_x = 10
        img_height = (height - (border_size + 30) * 2)
        self.img_y = 120
        self.text_x = self.img_x + 15 + img_height
        self.main_rectangle = Rectangle(window=window, x=x, y=y, width=width, height=height, bgcolor=bgcolor,
                                        border_radius=border_radius, border_color=border_color, border_size=border_size)
        self.img = pygame.image.load(img_source)
        self.img = pygame.transform.scale(self.img, (130, 130))
        game_name_font = pygame.font.Font(font, height // 3)
        self.game_name = game_name_font.render(game_name, True, (0, 0, 0))
        self.progress_bar = []
        for i in range(0, 3):
            margin = self.text_x - self.img_x - img_height
            rect_width = 70
            rect_height = height // 7
            rect_y = (y + height) - 15 - height // 4 - ((y + height) - 15 - height // 4 - self.img_y) // 2 + 30
            rect_x = self.text_x + margin * i + rect_width * i + 90
            rect = Rectangle(window, x=rect_x + 10, y=rect_y, width=rect_width, height=rect_height, bgcolor=(21, 209, 45),
                             border_radius=10, border_color=(0, 0, 0), border_size=2)
            self.progress_bar.append(rect)

    def draw(self):
        self.main_rectangle.draw_rectangle()
        self.window.blit(self.img, (self.img_x, self.img_y))
        self.window.blit(self.game_name, (150, self.img_y))
        for i in self.progress_bar:
            i.draw_rectangle()


class BlockWithGames:
    def __init__(self, window, x, y, width, height, bgcolor, border_size, border_color, border_radius, img_source,
                 game_name, button_text, font, text_level, text_time):
        self.window = window
        self.x = x
        self.y = y
        self.button_text = button_text
        self.img_x = x + border_size + 15
        img_height = (height - (border_size + 30) * 2)
        button_x = width - 200
        self.img_y = (height - img_height - border_size) // 2 + self.y
        self.text_x = self.img_x + 15 + img_height
        self.main_rectangle = Rectangle(window=window, x=x, y=y, width=width, height=height, bgcolor=bgcolor,
                                        border_radius=border_radius, border_color=border_color, border_size=border_size)
        self.img = pygame.image.load(img_source)
        self.img = pygame.transform.scale(self.img, (img_height, img_height))
        game_name_font = pygame.font.Font(font, height // 6)
        game_name_font_1 = pygame.font.Font(font, height // 9)
        self.game_name = game_name_font.render(game_name, True, (0, 0, 0))
        self.text_level = game_name_font_1.render(text_level, True, (128, 128, 128))
        self.text_time = game_name_font_1.render(text_time, True, (128, 128, 128))
        self.button = Button(window=window, y=(y + height) - 60 - height // 4, x=button_x + 40, width=width // 3,
                             height=height // 4,
                             text_color=(255, 255, 255), bgcolor=(0, 0, 0), border_radius=5,
                             text=self.button_text, font_name=font, text_size=height // 3 - 25)
        self.progress_bar = []
        for i in range(0, 1):
            margin = self.text_x - self.img_x - img_height
            rect_width = (width - self.img_x - img_height - margin * 4) - 125
            rect_height = height // 20
            rect_y = (y + height) - 15 - height // 4 - ((y + height) - 15 - height // 4 - self.img_y) // 2 - 15
            rect_x = self.text_x + margin * i + rect_width * i
            rect = Rectangle(window, x=rect_x, y=rect_y, width=rect_width, height=rect_height, bgcolor=(128, 128, 128),
                             border_radius=10, border_color=(0, 0, 0), border_size=2)
            self.progress_bar.append(rect)

    def draw(self):
        self.main_rectangle.draw_rectangle()
        self.window.blit(self.img, (self.img_x, self.img_y))
        if self.button_text != '':
            self.button.draw_button()
        self.window.blit(self.game_name, (self.text_x, 305))
        self.window.blit(self.text_level, (self.text_x, 357))
        self.window.blit(self.text_time, (self.text_x, 379))
        for i in self.progress_bar:
            i.draw_rectangle()


class AnswerForm(Rectangle):
    def __init__(self, window, x=0, y=0, width=0, height=0,
                 bgcolor=0, border_size=0, border_color=0, border_radius=0,
                 answer='', is_right=False, font=None, font_size=0, text_color=0):
        super(AnswerForm, self).__init__(window, x, y, width, height,
                                         bgcolor, border_size, border_color, border_radius)
        self.answer = str(answer)
        self.is_right = is_right
        self.font = font
        self.font_size = font_size
        self.text_color = text_color

    def draw(self):
        self.draw_rectangle()
        font = pygame.font.Font(self.font, self.font_size)
        text = font.render(self.answer, True, self.text_color)
        text_x, text_y = font.size(self.answer)
        x = self.x + (self.width - text_x) // 2 + self.border_size
        y = self.y + (self.height - text_y) // 2 + self.border_size
        self.window.blit(text, (x, y))


class ReactionButton(Rectangle):
    def __init__(self, window, x=0, y=0, width=0, height=0,
                 border_size=0, border_color=0, border_radius=0, fnc_good=None, fnc_bad=None):
        super(ReactionButton, self).__init__(window=window, x=x, y=y, width=width, height=height,
                 bgcolor=(128, 128, 128), border_size=border_size, border_color=border_color, border_radius=border_radius)
        self.start_reaction_time = -1
        self.fnc_good = fnc_good
        self.fnc_bad = fnc_bad

    def start_reaction(self):
        self.start_reaction_time = pygame.time.get_ticks()

    def end_reaction(self):
        return(pygame.time.get_ticks() - self.start_reaction_time)/1000

    def complete_button_function(self):
        if self.start_reaction_time != -1:
            self.fnc_good()
        elif self.start_reaction_time == -1:
            self.fnc_bad()


    def change_bgcolor(self, bgcolor):
        self.bgcolor = bgcolor