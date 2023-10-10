import pygame.image
import remember_colors
import save
from Struct import *
from math import ceil
import ariphmetic
import reaction_game
from save import *
from ariphmetic import AriphmeticGame


roboto = 'fonts/font1_roboto.ttf'
Srbija = 'fonts/Srbija Sans.otf'


class Menu:
    def __init__(self, __window):
        self.data = save.DataStructure()
        print(self.data.scores)
        print(self.data.get_data())
        # Основные переменные и флаги
        self.window = __window
        self.need_input = False
        self.input_text = ''
        self.backspacing = False
        self.backspacing_wait = 10000
        self.width = window.get_width()
        self.height = window.get_height()
        self.is_main_menu = True
        self.is_login_menu = False
        self.is_start_menu = False
        self.is_registration_menu = False
        self.is_game_menu = False
        self.is_choice_menu = False
        self.is_memory_menu = False
        self.is_reaction_menu = False
        self.is_logic_menu = False
        self.is_remember_colors = False
        self.is_reaction_game = False
        self.game_is_started = False
        self.game_is_ariphmetic = False
        self.is_end_game = False

        # Элементы интерфейса
        self.tyb_logo = pygame.image.load('images/tyb.png')
        self.information_foto = pygame.image.load('images/information_foto.jpg')
        self.information_foto_1 = pygame.transform.scale(self.information_foto, (390, 240))
        self.tyb_logo_main = pygame.transform.scale(self.tyb_logo, (234, 234))
        self.tyb_logo_second = pygame.transform.scale(self.tyb_logo, (64, 64))
        self.registration_foto = pygame.transform.scale(self.tyb_logo, (137, 139))
        self.login_foto = pygame.transform.scale(self.tyb_logo, (137, 139))
        self.font_header = pygame.font.Font(roboto, 33)
        self.font_header2 = pygame.font.Font(roboto, 20)
        self.font_information = pygame.font.Font(roboto, 20)
        self.font_registration = pygame.font.Font(roboto, 22)
        self.font_login = pygame.font.Font(roboto, 22)
        self.text_header = 'Train Your Brain'
        self.text_header2 = 'Персонализированная тренировка мозга'
        self.text_information1 = 'Train Your Brain'
        self.registration_text = 'Train Your Brain'
        self.login_text = 'Train Your Brain'
        self.header = self.font_header.render(self.text_header, True, 'Black')
        self.header2 = self.font_header2.render(self.text_header2, True, 'Black')
        self.information1 = self.font_information.render(self.text_information1, True, 'Black')
        self.registration_text_1 = self.font_registration.render(self.registration_text, True, 'Black')
        self.login_text_1 = self.font_login.render(self.login_text, True, 'Black')
        # Кнопка старта и анимационный прямоугольник
        self.start_button = Button(
            width=300, height=65, x=(self.width - 300) // 2, y=(self.height - 235),
            window=self.window, border_size=4, border_color=(0, 0, 0),
            text_size=25, button_function=self.start_menu, bgcolor=(3, 3, 3), text_color=(255, 255, 255), text="Начать",
            border_radius=8
        )

        # Кнопка информационной страницы
        self.information_button = Button(
            width=250, height=55, x=(self.width - 250) // 2, y=(self.height - 90),
            window=self.window, border_size=4, border_color=(0, 0, 0),
            text_size=25, button_function=self.choice_menu, bgcolor=(0, 0, 0), text_color=(255, 255, 255), text="Далее"
            , border_radius=8
        )
        self.animation_rectangle_information_button = Rectangle(
            window=self.window, width=255, height=55, x=(self.width - 300) // 2, y=(self.height - 158),
            border_size=4, border_color=(0, 0, 0), bgcolor=0, border_radius=8
        )

        # Кнопка меню регистрации
        self.registration_button_reg = Button(
            width=290, height=55, x=(self.width - 290) // 2, y=(self.height - 163),
            window=self.window, border_size=4, border_color=(0, 0, 0),
            text_size=25, button_function=self.login_menu, bgcolor=(3, 3, 3), text_color=(255, 255, 255),
            text=" ЗАРЕГИСТРИРОВАТЬСЯ", border_radius=8
        )
        self.registration_button_back = Button(
            width=290, height=55, x=(self.width - 290) // 2, y=(self.height - 90),
            window=self.window, border_size=4, border_color=(0, 0, 0),
            text_size=25, button_function=self.main_menu, bgcolor=(3, 3, 3), text_color=(255, 255, 255),
            text="НАЗАД", border_radius=8
        )
        # Кнопки меню для авторизации
        self.login_button_reg = Button(
            width=290, height=55, x=(self.width - 290) // 2, y=(self.height - 163),
            window=self.window, border_size=4, border_color=(0, 0, 0),
            text_size=25, button_function=self.game_menu, bgcolor=(3, 3, 3), text_color=(255, 255, 255),
            text="ВОЙТИ", border_radius=8
        )
        self.login_button_back = Button(
            width=290, height=55, x=(self.width - 290) // 2, y=(self.height - 90),
            window=self.window, border_size=4, border_color=(0, 0, 0),
            text_size=25, button_function=self.main_menu, bgcolor=(3, 3, 3), text_color=(255, 255, 255),
            text="НАЗАД", border_radius=8
        )
        # Кнопки для меню выбора дальнейшего пути
        self.choice_button_guest = Button(
            width=290, height=55, x=(self.width - 290) // 2, y=(self.height - 310),
            window=self.window, border_size=4, border_color=(0, 0, 0),
            text_size=25, button_function=self.game_menu, bgcolor=(3, 3, 3), text_color=(255, 255, 255),
            text="Продолжить как Гость", border_radius=8
        )
        self.choice_button_reg = Button(
            width=290, height=55, x=(self.width - 290) // 2, y=(self.height - 240),
            window=self.window, border_size=4, border_color=(0, 0, 0),
            text_size=25, button_function=self.registration_menu, bgcolor=(3, 3, 3), text_color=(255, 255, 255),
            text="Зарегистрироваться", border_radius=8
        )
        #Кнопки назад
        self.button_1 = Button(
            width=20, height=20, x=10, y=(self.height - 30),
            window=self.window, border_size=4, border_color=(0, 0, 0),
            text_size=1, button_function=self.main_menu, bgcolor=(3, 3, 3), text_color=(3, 3, 3),
            text=".", border_radius=8
        )
        self.button_2 = Button(
            width=20, height=20, x=10, y=(self.height - 30),
            window=self.window, border_size=4, border_color=(0, 0, 0),
            text_size=1, button_function=self.start_menu, bgcolor=(3, 3, 3), text_color=(3, 3, 3),
            text=".", border_radius=8
        )
        self.button_3 = Button(
            width=20, height=20, x=10, y=(self.height - 30),
            window=self.window, border_size=4, border_color=(0, 0, 0),
            text_size=1, button_function=self.start_menu, bgcolor=(3, 3, 3), text_color=(3, 3, 3),
            text=".", border_radius=8
        )
        self.button_4 = Button(
            width=20, height=20, x=10, y=(self.height - 30),
            window=self.window, border_size=4, border_color=(0, 0, 0),
            text_size=1, button_function=self.choice_menu, bgcolor=(3, 3, 3), text_color=(3, 3, 3),
            text=".", border_radius=8
        )
        self.button_5 = Button(
            width=20, height=20, x=10, y=(self.height - 30),
            window=self.window, border_size=4, border_color=(0, 0, 0),
            text_size=1, button_function=self.main_menu, bgcolor=(3, 3, 3), text_color=(3, 3, 3),
            text=".", border_radius=8
        )
        self.button_6 = Button(
            width=20, height=20, x=10, y=(self.height - 30),
            window=self.window, border_size=4, border_color=(0, 0, 0),
            text_size=1, button_function=self.game_menu, bgcolor=(3, 3, 3), text_color=(3, 3, 3),
            text=".", border_radius=8
        )
        self.button_7 = Button(
            width=20, height=20, x=10, y=(self.height - 30),
            window=self.window, border_size=4, border_color=(0, 0, 0),
            text_size=1, button_function=self.game_menu, bgcolor=(3, 3, 3), text_color=(3, 3, 3),
            text=".", border_radius=8
        )
        self.button_8 = Button(
            width=20, height=20, x=10, y=(self.height - 30),
            window=self.window, border_size=4, border_color=(0, 0, 0),
            text_size=1, button_function=self.game_menu, bgcolor=(3, 3, 3), text_color=(3, 3, 3),
            text=".", border_radius=8
        )
        self.end_button = Button(
            width=150, height=50, x=160, y=400,
            window=self.window, border_size=4, border_color=(0, 0, 0),
            text_size=20, button_function=self.game_menu, bgcolor=(3, 3, 3), text_color=(255, 255, 255),
            text="ВЫЙТИ", border_radius=8
        )



        # Интерфейс ознакомительного меню
        self.department_of_information_top = Rectangle(self.window, x=(self.width - 280) // 2, y=135,
                                                   width=280, height=3, bgcolor=(128, 128, 128))
        self.department_of_information_middle = Rectangle(self.window, x=(self.width - 180) // 2, y=self.height - 305,
                                                       width=170, height=1, bgcolor=(128, 128, 128))
        self.department_of_information_bottom = Rectangle(self.window, x=(self.width - 280) // 2, y=self.height - 110,
                                                   width=280, height=3, bgcolor=(128, 128, 128))
        # Интерфейс регистрационного меню
        self.department_of_registration_top = Rectangle(self.window, x=(self.width - 300) // 2, y=216,
                                                       width=300, height=3, bgcolor=(128, 128, 128))
        self.department_of_registration_middle = Rectangle(self.window, x=40, y=(self.height - 200) // 2 + 10,
                                                          width=1, height=200, bgcolor=(128, 128, 128))
        self.department_of_registration_bottom = Rectangle(self.window, x=(self.width - 300) // 2, y=self.height - 180,
                                                          width=300, height=3, bgcolor=(128, 128, 128))
        self.field_of_registration = Rectangle(self.window, x=(self.width - 300) // 2, y=self.height - 400,
                                                           width=300, height=40, bgcolor=(255, 255, 255), border_radius=7,
                                               border_color=(12, 0, 0), border_size=2)
        # Интерфейс меню для выбора дальнейшего пути
        self.department_of_choice_top = Rectangle(self.window, x=(self.width - 250) // 2, y=135,
                                                        width=250, height=3, bgcolor=(128, 128, 128))
        self.department_of_choice_middle = Rectangle(self.window, x=(self.width - 170) // 2, y=330,
                                                           width=170, height=1, bgcolor=(128, 128, 128))
        self.department_of_choice_bottom = Rectangle(self.window, x=(self.width - 250) // 2, y=self.height - 170,
                                                           width=250, height=3, bgcolor=(128, 128, 128))
        self.game_widget1 = GameWidget(window=window, x=5, y=140, width=self.width-10, height=150, border_radius=55,
                                       bgcolor=(255, 255, 255), border_size=2, border_color=(208, 209, 214),
                                       img_source='images/brain1.png', game_name='I - МЫШЛЕНИЕ', button_text='ИГРАТЬ', font=roboto)
        # Меню с блоками под игры
        self.game_widget2 = GameWidget(window=window, x=5, y=320, width=self.width - 10, height=150, border_radius=55,
                                       bgcolor=(255, 255, 255), border_size=2, border_color=(208, 209, 214),
                                       img_source='images/reaction.png', game_name='II - РЕАКЦИЯ', button_text='ИГРАТЬ',
                                       font=roboto)
        self.game_widget3 = GameWidget(window=window, x=5, y=500, width=self.width - 10, height=150, border_radius=55,
                                       bgcolor=(255, 255, 255), border_size=2, border_color=(208, 209, 214),
                                       img_source='images/memory.png', game_name='III - ПАМЯТЬ', button_text='ИГРАТЬ',
                                       font=roboto)
        self.top_widget = GameWidgetTop(window=window, x=0, y=0, width=self.width, height=90, border_radius=30,
                                       bgcolor=(255, 255, 255), border_size=2, border_color=(208, 209, 214),
                                       img_source='images/tyb.png', text=self.data.name, button_text='ИГРАТЬ',
                                       font=roboto, img_profile='images/profile1.png', text_level='LEVEL: 77',
                                        font_1=Srbija, img_button='images/menu.png')
        # Страница с играми на память
        self.top_widget = GameWidgetTop(window=window, x=0, y=0, width=self.width, height=90, border_radius=30,
                                        bgcolor=(255, 255, 255), border_size=2, border_color=(208, 209, 214),
                                        img_source='images/tyb.png', text=self.data.name, button_text='ИГРАТЬ',
                                        font=roboto, img_profile='images/profile1.png', text_level='LEVEL: 77',
                                        font_1=Srbija, img_button='images/menu.png')
        self.department_of_memory_menu = Rectangle(self.window, x=20, y=280,
                                                  width=self.width - 40, height=4, bgcolor=(128, 128, 128), border_radius=10)
            # Информация в меню игр
        self.information_game = GameInfo(window=window, x=0, y=100, width=self.width, height=90, border_radius=30,
                                        bgcolor=(255, 255, 255), border_size=2, border_color=(255, 255, 255),
                                        img_source='images/memory.png', game_name='БЛОК III - ПАМЯТЬ',
                                        font=roboto)
            # Игры
        self.game_paint = BlockWithGames(window=window, x=5, y=290, width=self.width - 10, height=150, border_radius=55,
                                       bgcolor=(255, 255, 255), border_size=2, border_color=(208, 209, 214),
                                       img_source='images/paint.png', game_name='ЦВЕТА', button_text='ИГРАТЬ',
                                       font=roboto, text_level='LEVEL: 5', text_time='THE BEST TIME: 37 sec')
        # Страница с играми на реакцию
        self.top_widget = GameWidgetTop(window=window, x=0, y=0, width=self.width, height=90, border_radius=30,
                                        bgcolor=(255, 255, 255), border_size=2, border_color=(208, 209, 214),
                                        img_source='images/tyb.png', text=self.data.name, button_text='ИГРАТЬ',
                                        font=roboto, img_profile='images/profile1.png', text_level='LEVEL: 77',
                                        font_1=Srbija, img_button='images/menu.png')
        self.department_of_reaction_menu = Rectangle(self.window, x=20, y=280,
                                                   width=self.width - 40, height=4, bgcolor=(128, 128, 128),
                                                   border_radius=10)
            # Информация в меню игр
        self.information_game_reaction = GameInfo(window=window, x=0, y=100, width=self.width, height=90, border_radius=30,
                                         bgcolor=(255, 255, 255), border_size=2, border_color=(255, 255, 255),
                                         img_source='images/reaction.png', game_name='БЛОК II - РЕАКЦИЯ',
                                         font=roboto)
            # Игры
        self.button_of_reaction = BlockWithGames(window=window, x=5, y=290, width=self.width - 10, height=150, border_radius=55,
                                         bgcolor=(255, 255, 255), border_size=2, border_color=(208, 209, 214),
                                         img_source='images/button.png', game_name='КНОПКА', button_text='ИГРАТЬ',
                                         font=roboto, text_level=f"Рекорд : {self.data.get_score('reaction_game')}", text_time='')
        # Страница с играми на логику
        self.top_widget = GameWidgetTop(window=window, x=0, y=0, width=self.width, height=90, border_radius=30,
                                        bgcolor=(255, 255, 255), border_size=2, border_color=(208, 209, 214),
                                        img_source='images/tyb.png', text=self.data.name, button_text='ИГРАТЬ',
                                        font=roboto, img_profile='images/profile1.png', text_level='LEVEL: 77',
                                        font_1=Srbija, img_button='images/menu.png')
        self.department_of_logic_menu = Rectangle(self.window, x=20, y=280,
                                                     width=self.width - 40, height=4, bgcolor=(128, 128, 128),
                                                     border_radius=10)
            # Информация в меню игр
        self.information_game_logic = GameInfo(window=window, x=0, y=100, width=self.width, height=90,
                                                  border_radius=30,
                                                  bgcolor=(255, 255, 255), border_size=2, border_color=(255, 255, 255),
                                                  img_source='images/brain1.png', game_name='БЛОК I - ЛОГИКА',
                                                  font=roboto)
            # Игры
        self.math_of_reaction = BlockWithGames(window=window, x=5, y=290, width=self.width - 10, height=150,
                                               border_radius=55,
                                               bgcolor=(255, 255, 255), border_size=2, border_color=(208, 209, 214),
                                               img_source='images/math.png', game_name='ПРИМЕРЫ',
                                               button_text='ИГРАТЬ',
                                               font=roboto, text_level=f"Рекорд: {self.data.get_score('ariphmetic')}", text_time='')

    def print_text(self, message, x, y, font_size=25, font_type=None, font_color='black', bold=True):
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render(message, bold, font_color)
        self.window.blit(text, (x, y))

    def start_menu(self, args=None):
        font = pygame.font.Font(roboto, 20)
        self.is_login_menu, self.is_start_menu, self.is_main_menu, self.is_registration_menu = False, True, False, False
        self.game_is_ariphmetic = False
        self.window.blit(self.tyb_logo_second, ((self.width - self.tyb_logo_second.get_size()[0]) // 2, 19))
        self.window.blit(self.information_foto_1, (((self.width - self.information_foto_1.get_size()[0]) // 2), 150))
        self.department_of_information_top.draw_rectangle()
        self.department_of_information_middle.draw_rectangle()
        self.print_text('Проверьте свои возможности на', 45, 400, bold=True, font_type=Srbija)
        self.print_text('нашей платформе TYB', 110, 425, bold=True, font_type=Srbija)
        self.print_text('Настраивайте программу', 90, 450, bold=True, font_type=Srbija)
        self.print_text('тренировок, анализируйте вашу', 45, 475, bold=True, font_type=Srbija)
        self.print_text('производительность, отслеживайте', 20, 500, bold=True, font_type=Srbija)
        self.print_text('ваш прогресс.', 160, 525, bold=True, font_type=Srbija)
        self.department_of_information_bottom.draw_rectangle()
        information1_size_x = self.font_information.size(self.text_information1)[0]
        self.window.blit(self.information1, ((self.width - information1_size_x) // 2, 103))
        self.information_button.draw_button()
        if args is not None:
            if self.information_button.collidepoint(args[0]):
                for event in args[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.information_button.button_function_complete()
                        break
        self.button_1.draw_button()
        if args is not None:
            if self.button_1.collidepoint(args[0]):
                for event in args[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.button_1.button_function_complete()
                        break

    def choice_menu(self, args=None):
        self.is_login_menu, self.is_start_menu, self.is_main_menu, self.is_registration_menu = False, False, False, False
        self.is_game_menu = False
        self.game_is_ariphmetic = False
        self.is_choice_menu = True
        if self.data.name.strip() != '':
            self.is_choice_menu = False
            self.is_game_menu = True
            return None
        self.window.blit(self.tyb_logo_second, ((self.width - self.tyb_logo_second.get_size()[0]) // 2, 19))
        self.choice_button_guest.draw_button()
        self.choice_button_reg.draw_button()
        self.department_of_choice_top.draw_rectangle()
        self.department_of_choice_middle.draw_rectangle()
        self.department_of_choice_bottom.draw_rectangle()
        self.print_text('Если ты хочешь сохранить свой', 55, 150, font_size=24, font_type=Srbija)
        self.print_text('прогресс и отслеживать его в', 65, 175, font_size=24, font_type=Srbija)
        self.print_text('профиле, рекомендуем', 100, 200, font_size=24, font_type=Srbija)
        self.print_text('зарегистрироваться.', 115, 225, font_size=24, font_type=Srbija)
        self.print_text('Для регистрации и авторизации', 50, 250, font_size=24, font_type=Srbija)
        self.print_text('потребуется Интернет-подключение.', 25, 275, font_size=24, font_type=Srbija)
        if args is not None:
            if self.choice_button_reg.collidepoint(args[0]):
                for event in args[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.choice_button_reg.button_function_complete()
                        break
            if self.choice_button_guest.collidepoint(args[0]):
                for event in args[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.choice_button_guest.button_function_complete()
                        break
        self.button_2.draw_button()
        if args is not None:
            if self.button_2.collidepoint(args[0]):
                for event in args[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.button_2.button_function_complete()
                        break

    def game_menu(self, args=None):
        self.top_widget = GameWidgetTop(window=window, x=0, y=0, width=self.width, height=90, border_radius=30,
                                        bgcolor=(255, 255, 255), border_size=2, border_color=(208, 209, 214),
                                        img_source='images/tyb.png', text=self.data.name, button_text='ИГРАТЬ',
                                        font=roboto, img_profile='images/profile1.png', text_level='LEVEL: 77',
                                        font_1=Srbija, img_button='images/menu.png')
        self.math_of_reaction = BlockWithGames(window=window, x=5, y=290, width=self.width - 10, height=150,
                                               border_radius=55,
                                               bgcolor=(255, 255, 255), border_size=2, border_color=(208, 209, 214),
                                               img_source='images/math.png', game_name='ПРИМЕРЫ',
                                               button_text='ИГРАТЬ',
                                               font=roboto, text_level=f"Рекорд: {self.data.get_score('ariphmetic')}",
                                               text_time='')
        self.button_of_reaction = BlockWithGames(window=window, x=5, y=290, width=self.width - 10, height=150,
                                                 border_radius=55,
                                                 bgcolor=(255, 255, 255), border_size=2, border_color=(208, 209, 214),
                                                 img_source='images/button.png', game_name='КНОПКА',
                                                 button_text='ИГРАТЬ',
                                                 font=roboto,
                                                 text_level=f"Рекорд : {self.data.get_score('reaction_game')}",
                                                 text_time='')
        self.is_end_game = False
        self.game_is_started = False
        self.is_login_menu, self.is_start_menu, self.is_main_menu, self.is_registration_menu = False, False, False, False
        self.is_game_menu = True
        self.game_is_ariphmetic = False
        self.game_widget1.button.button_function = self.logic_menu
        self.game_widget2.button.button_function = self.reaction_menu
        self.game_widget3.button.button_function = self.memory_menu
        self.game_widget1.draw()
        self.game_widget2.draw()
        self.game_widget3.draw()
        self.top_widget.draw()
        if args is not None:
            if self.game_widget1.button.collidepoint(args[0]):
                for event in args[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.game_widget1.button.button_function_complete()
                        break
        if args is not None:
            if self.game_widget2.button.collidepoint(args[0]):
                for event in args[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.game_widget2.button.button_function_complete()
                        break
        if args is not None:
            if self.game_widget3.button.collidepoint(args[0]):
                for event in args[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.game_widget3.button.button_function_complete()
                        break
        self.button_3.draw_button()
        if args is not None:
            if self.button_3.collidepoint(args[0]):
                for event in args[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.button_3.button_function_complete()
                        break

    def registration_menu(self, args=None):
        self.field_of_registration.draw_rectangle()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            self.need_input = True
        self.print_text(self.input_text, (self.width - 280) // 2, self.height - 400, font_size=35, font_color='black')
        self.is_login_menu, self.is_start_menu, self.is_main_menu, self.is_registration_menu = False, False, False, True
        self.game_is_ariphmetic = False
        self.window.blit(self.registration_foto, ((self.width - self.registration_foto.get_size()[0]) // 2, 19))
        registration_size_x = self.font_registration.size(self.registration_text)[0]
        self.window.blit(self.registration_text_1, ((self.width - registration_size_x) // 2, 176))
        self.department_of_registration_top.draw_rectangle()
        self.department_of_registration_middle.draw_rectangle()
        self.department_of_registration_bottom.draw_rectangle()
        self.registration_button_back.draw_button()
        self.registration_button_reg.draw_button()
        if args is not None:
            if self.registration_button_reg.collidepoint(args[0]):
                for event in args[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.registration_button_reg.button_function_complete()
                        break
            if self.registration_button_back.collidepoint(args[0]):
                for event in args[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.registration_button_back.button_function_complete()
                        break
        self.button_4.draw_button()
        if args is not None:
            if self.button_4.collidepoint(args[0]):
                for event in args[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.button_4.button_function_complete()
                        break

    def login_menu(self, args=None):
        self.data.put_data(name=self.input_text)
        self.is_login_menu, self.is_start_menu, self.is_main_menu, self.is_registration_menu = True, False, False, False
        self.game_is_ariphmetic = False
        self.window.blit(self.login_foto, ((self.width - self.login_foto.get_size()[0]) // 2, 19))
        login_size_x = self.font_login.size(self.login_text)[0]
        self.window.blit(self.login_text_1, ((self.width - login_size_x) // 2, 176))
        self.department_of_registration_top.draw_rectangle()
        self.department_of_registration_middle.draw_rectangle()
        self.department_of_registration_bottom.draw_rectangle()
        self.login_button_reg.draw_button()
        self.login_button_back.draw_button()
        if args is not None:
            if self.login_button_reg.collidepoint(args[0]):
                for event in args[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.login_button_reg.button_function_complete()
                        break
            if self.login_button_back.collidepoint(args[0]):
                for event in args[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.login_button_back.button_function_complete()
                        break
        self.button_5.draw_button()
        if args is not None:
            if self.button_5.collidepoint(args[0]):
                for event in args[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.button_5.button_function_complete()
                        break

    def main_menu(self, events=None):
        self.window.blit(self.tyb_logo_main, ((self.width - self.tyb_logo_main.get_size()[0]) // 2, 66))
        self.print_text('Train Your Brain', 110, 320, font_size=35, font_type=roboto)
        self.print_text('Персонализированная тренировка мозга', 15, 375, font_size=22, font_type=Srbija)
        self.is_login_menu, self.is_start_menu, self.is_main_menu, self.is_registration_menu = False, False, True, False
        self.start_button.draw_button()
        # Анимация кнопки СТАРТ
        if events is not None:
            if self.start_button.collidepoint(events[0]):  # Прямая анимация
                for event in events[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.start_button.button_function_complete()
                        break

    def memory_menu(self, args=None):
        self.is_login_menu, self.is_start_menu, self.is_main_menu, self.is_registration_menu = False, False, False, False
        self.is_game_menu = False
        self.is_choice_menu = False
        self.game_is_ariphmetic = False
        self.is_memory_menu = True
        self.game_paint.button.button_function = self.remember_colors
        self.top_widget.draw()
        self.information_game.draw()
        self.department_of_memory_menu.draw_rectangle()
        self.game_paint.draw()
        if args is not None:
            if self.game_paint.button.collidepoint(args[0]):
                for event in args[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.game_paint.button.button_function_complete()
                        break
        self.button_6.draw_button()
        if args is not None:
            if self.button_6.collidepoint(args[0]):
                for event in args[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.button_6.button_function_complete()
                        break

    def reaction_menu(self, args=None):
        self.is_login_menu, self.is_start_menu, self.is_main_menu, self.is_registration_menu = False, False, False, False
        self.is_game_menu = False
        self.is_choice_menu = False
        self.is_memory_menu = False
        self.game_is_ariphmetic = False
        self.is_reaction_menu = True
        self.button_of_reaction.button.button_function = self.reaction_game
        self.top_widget.draw()
        self.information_game_reaction.draw()
        self.department_of_reaction_menu.draw_rectangle()
        self.button_of_reaction.draw()
        if args is not None:
            if self.button_of_reaction.button.collidepoint(args[0]):
                for event in args[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.button_of_reaction.button.button_function_complete()
                        break
        self.button_7.draw_button()
        if args is not None:
            if self.button_7.collidepoint(args[0]):
                for event in args[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.button_7.button_function_complete()
                        break

    def logic_menu(self, args=None):
        self.is_login_menu, self.is_start_menu, self.is_main_menu, self.is_registration_menu = False, False, False, False
        self.is_game_menu = False
        self.is_choice_menu = False
        self.is_memory_menu = False
        self.game_is_ariphmetic = False
        self.is_reaction_menu = False
        self.is_logic_menu = True
        self.math_of_reaction.button.button_function = self.ariphmetic
        self.top_widget.draw()
        self.information_game_logic.draw()
        self.department_of_logic_menu.draw_rectangle()
        self.math_of_reaction.draw()
        if args is not None:
            if self.math_of_reaction.button.collidepoint(args[0]):
                for event in args[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.math_of_reaction.button.button_function_complete()
                        break
        self.button_8.draw_button()
        if args is not None:
            if self.button_8.collidepoint(args[0]):
                for event in args[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.button_8.button_function_complete()
                        break

    def remember_colors(self, args=None):
        self.is_login_menu, self.is_start_menu, self.is_main_menu, self.is_registration_menu = False, False, False, False
        self.is_game_menu = False
        self.is_choice_menu = False
        self.is_memory_menu = False
        self.is_reaction_menu = False
        self.is_logic_menu = False
        self.game_is_ariphmetic = False
        self.is_remember_colors = True

    def ariphmetic(self, args=None):
        self.is_login_menu, self.is_start_menu, self.is_main_menu, self.is_registration_menu = False, False, False, False
        self.is_game_menu = False
        self.is_choice_menu = False
        self.is_memory_menu = False
        self.is_reaction_menu = False
        self.is_logic_menu = False
        self.is_remember_colors = False
        self.game_is_ariphmetic = True

    def reaction_game(self, args=None):
        self.is_login_menu, self.is_start_menu, self.is_main_menu, self.is_registration_menu = False, False, False, False
        self.is_game_menu = False
        self.is_choice_menu = False
        self.is_memory_menu = False
        self.is_reaction_menu = False
        self.is_logic_menu = False
        self.is_remember_colors = False
        self.game_is_ariphmetic = False
        self.is_reaction_game = True

    def end_game(self, win, args=None):
        self.game_is_started = False
        self.is_login_menu, self.is_start_menu, self.is_main_menu, self.is_registration_menu = False, False, False, False
        self.is_game_menu = False
        self.is_choice_menu = False
        self.is_memory_menu = False
        self.is_reaction_menu = False
        self.is_logic_menu = False
        self.is_remember_colors = False
        self.game_is_ariphmetic = False
        self.is_reaction_game = False
        self.is_end_game = True
        self.end_button.draw_button()
        if args is not None:
            if self.end_button.collidepoint(args[0]):
                for event in args[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.end_button.button_function_complete()
                        break

        text_font = pygame.font.Font('fonts/font1_roboto.ttf', 35)
        text_level = text_font.render("YOU WIN", True, (0, 0, 0))
        text_font_1 = pygame.font.Font('fonts/font1_roboto.ttf', 32)
        text_level_1 = text_font_1.render("YOU LOSE", True, (0, 0, 0))
        if win:
            self.window.blit(text_level, (160, 150))
            self.win = True
        else:
            self.window.blit(text_level_1, (160, 150))
            self.win = False


if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((480, 700))
    menu = Menu(window)
    running = True
    game = None
    while running:
        window.fill((255, 255, 255))
        __events = pygame.event.get()
        if menu.is_main_menu:
            menu.main_menu((pygame.mouse.get_pos(), __events))
        elif menu.is_start_menu:
            menu.start_menu((pygame.mouse.get_pos(), __events))
        elif menu.is_registration_menu:
            menu.registration_menu((pygame.mouse.get_pos(), __events))
        elif menu.is_game_menu:
            menu.game_menu((pygame.mouse.get_pos(), __events))
        elif menu.is_choice_menu:
            menu.choice_menu((pygame.mouse.get_pos(), __events))
        elif menu.is_memory_menu:
            menu.memory_menu((pygame.mouse.get_pos(), __events))
        elif menu.is_reaction_menu:
            menu.reaction_menu((pygame.mouse.get_pos(), __events))
        elif menu.is_logic_menu:
            menu.logic_menu((pygame.mouse.get_pos(), __events))
        elif menu.is_end_game:
            menu.end_game(win=menu.win, args=(pygame.mouse.get_pos(), __events))
        elif menu.is_remember_colors:
            current_time = pygame.time.get_ticks()
            if not menu.game_is_started:
                game = remember_colors.RememberColorsGame(window=window, count_of_colors=9, font=roboto)
                game.end_button_fnc_set(menu.end_game)
                menu.game_is_started = True
            if not game.is_randomized and game.is_started:
                delta_time = current_time - game.start_time
                if delta_time >= 5000:
                    game.randomize_position()
            elif not game.is_started:
                game.start_time = current_time
            mouse_position = pygame.mouse.get_pos()
            game.draw_game((mouse_position, __events, current_time - game.start_time))
        elif menu.game_is_ariphmetic:
            if not menu.game_is_started:
                menu.game_is_started = True
                game = ariphmetic.AriphmeticGame(window, roboto)
            elif not game.game_ended:
                game.draw_game((__events, pygame.mouse.get_pos()))
            elif game.game_ended:
                game.end_game(__events)
                menu.data.put_data(ariphmetic=game.get_score())
            for event in __events:
                if event.type == game.fault_event_id or event.type == game.end_time_event_id:
                    score = event.score
                    message = event.message
                    game.game_ended = True
                    game.end_message = message
                elif event.type == game.close_game_event_id:
                    menu.game_menu()
                    menu.game_is_started = False
        elif menu.is_reaction_game:
            if not menu.game_is_started:
                game = reaction_game.ReactionGame(window=window, font=roboto, exit_button_fnc=menu.game_menu)
                game.start_game()
                menu.game_is_started = True
            if game.game_ended:
                menu.data.put_data(reaction_game=game.get_score(), reverse=True)
            game.draw(events=__events)
        if menu.backspacing:
            if menu.backspacing_wait <= 0:
                menu.input_text = menu.input_text[:-1]
                menu.backspacing_wait = 1000
            menu.backspacing_wait -= 100
        for event in __events:
            if event.type == pygame.QUIT:
                running = False
                menu.data.save()
            if menu.need_input and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu.need_input = False
                    menu.input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                        menu.backspacing = True
                else:
                    if len(menu.input_text) < 10 and event.key != pygame.K_TAB:
                        menu.input_text += event.unicode
            if menu.need_input and event.type == pygame.KEYUP:
                if event.key == pygame.K_BACKSPACE:
                    menu.input_text = menu.input_text[:-1]
                    menu.backspacing_wait = 10000
                    menu.backspacing = False
        pygame.display.flip()