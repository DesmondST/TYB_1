import Struct
import math
import random
import pygame


def is_simple(a):
    for i in range(2, int(math.sqrt(a))):
        if a % i == 0:
            return False
    else:
        return True


class AriphmeticGame:
    def __init__(self, window, font):
        self.start_time = 0
        self.clock = pygame.time.Clock
        self.score = 0
        self.end_message = ''
        self.end_time_event_id = pygame.USEREVENT
        self.fault_event_id = pygame.USEREVENT + 1
        self.close_game_event_id = pygame.USEREVENT + 2
        self.counter = pygame.USEREVENT + 3
        self.counter_time = 30
        self.counter_event = pygame.event.Event(self.counter)
        self.end_time_event = pygame.event.Event(self.end_time_event_id, message='Время вышло', score=self.score)
        self.fault_event = pygame.event.Event(self.fault_event_id, message='Вы ошиблись', score=self.score)
        self.game_ended = False
        self.window = window
        self.font = font
        self.answer_forms = []
        self.expression = ''
        self.main_font = pygame.font.Font(font, 30)
        self.render_main_text = self.main_font.render('Решите пример', True, (0, 0, 0))
        self.expression_font = pygame.font.Font(font, 25)
        self.game_logic()

    @staticmethod
    def generate_expression():
        operations = ['+', '-', '*', '/']
        operation = random.randint(0, 3)
        maximum = 99
        if operations[operation] == '*':
            maximum = 30
        a = random.randint(10, maximum)
        b = random.randint(1, maximum)
        if operations[operation] == '-':
            expression = f'{max(a, b)} - {min(a, b)}'
        elif operations[operation] == '/':
            while is_simple(a):
                a = random.randint(10, 55)
            while a % b != 0 or a == b:
                b = random.randint(2, a)
            expression = f'{max(a, b)} / {min(a, b)}'
        else:
            expression = f'{a} {operations[operation]} {b}'
        return expression, int(eval(expression))

    def game_logic(self):
        self.counter_time = 30
        self.end_time_event.score = self.score
        self.fault_event.score = self.score
        pygame.time.set_timer(self.end_time_event, 30*10**3, loops=1)
        pygame.time.set_timer(self.counter_event, 1000, loops=1)
        expression, right_answer = self.generate_expression()
        right = random.randint(0, 3)
        width = 200
        height = 50
        margin_x = 80//3
        margin_y = 25
        answers = []
        answers.append(right_answer)
        answer_forms = []
        for i in range(4):
            x = margin_x * (i % 2 + 1) + width * (i % 2)
            y = margin_y * (i//2 + 1) + height * (i // 2) + 250
            if i == right:
               answer_form = Struct.AnswerForm(self.window, x, y, width, height, (255, 255, 255), border_radius=10, answer=right_answer,
                                               is_right=True, font=self.font, font_size=25, text_color=(0, 0, 0))
            else:
                answer = random.randint(round(max(right_answer-100, 0)), round(right_answer+100))
                while answer in answers:
                    answer = random.randint(round(max(right_answer - 100, 0)), round(right_answer + 100))
                answer_form = Struct.AnswerForm(self.window, x, y, width, height, (255, 255, 255), border_radius=10, answer=answer,
                                                is_right=False, font=self.font, font_size=25, text_color=(0, 0, 0))
            answer_forms.append(answer_form)
        self.answer_forms = answer_forms
        self.expression = expression

    def draw_game(self, events=None):
        self.window.blit(self.render_main_text, ((480 - self.main_font.size('Решите пример')[0]) // 2, 130))
        render_expression = self.expression_font.render(self.expression, True, (0, 0, 0))
        self.window.blit(render_expression, ((480 - self.expression_font.size(self.expression)[0])//2, 150 + self.main_font.size('Решите пример')[1]))
        render_expression = self.expression_font.render(str(self.counter_time), True, (0, 0, 0))
        self.window.blit(render_expression, (0, 0))
        br = Struct.Rectangle(self.window, 0, 225, 480, 5, bgcolor=(0, 0, 0),
                              border_size=0, border_color=0, border_radius=0)
        br.draw_rectangle()
        for i in self.answer_forms:
            i.draw()
        if events is not None:
            for event in events[0]:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for answer_form in self.answer_forms:
                        if answer_form.collidepoint(events[1]):
                            if answer_form.is_right:
                                self.score += 1
                                self.game_logic()
                            else:
                                pygame.event.post(self.fault_event)
                elif event.type == self.counter:
                    pygame.time.set_timer(self.counter_event, 1000, loops=1)
                    self.counter_time -= 1

    def close_game(self):
        pygame.event.post(pygame.event.Event(self.close_game_event_id))

    def end_game(self, events=None):
        button = Struct.Button(self.window, x=190, y=400, width=100, height=100, text_size=45, text_color=(0, 0, 0),
                               font_name=self.font, text='ВЫЙТИ', button_function=self.close_game)
        button.draw_button()
        text_end_level = str(self.end_message)
        score_end_level = f'Количество очков: {self.score}'
        text_font = pygame.font.Font('fonts/font1_roboto.ttf', 25)
        text_level = text_font.render(score_end_level, True, (0, 0, 0))
        text_font_1 = pygame.font.Font('fonts/font1_roboto.ttf', 25)
        text_level_1 = text_font_1.render(text_end_level, True, (0, 0, 0))
        self.window.blit(text_level, (120, 150))
        self.window.blit(text_level_1, (120, 120))
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    button.button_function_complete()
        self.game_ended = True
