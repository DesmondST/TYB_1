import pygame.event
import random
import Struct


class ReactionGame:
    def __init__(self, window, font, exit_button_fnc):
        self.font = font
        self.score_font = pygame.font.Font(self.font, 20)
        self.restart_game_button = Struct.Button(window=window, x=161, y=450, width=150, height=50, text_size=15,
                                                 text_color=(0, 0, 0), border_color=(0, 0, 0), border_size=4, border_radius=20,
                                                 font_name=font, text='Сыграть еще раз', button_function=self.start_game)
        self.window = window
        self.reacton_button = Struct.ReactionButton(window=window, x=190, y=300, width=100, height=100, fnc_good=self.end_reaction_good,
                                                    fnc_bad=self.end_reaction_bad)
        self.exit_button = Struct.Button(
            width=20, height=20, x=10, y=670,
            window=self.window, border_size=4, border_color=(0, 0, 0),
            text_size=1, bgcolor=(3, 3, 3), text_color=(3, 3, 3),
            text=".", border_radius=8, button_function=exit_button_fnc
        )
        self.event_end_reaction_good_id = pygame.USEREVENT
        self.event_end_reaction_bad_id = pygame.USEREVENT + 2
        self.event_start_reaction_id = pygame.USEREVENT + 1
        self.score = None
        self.game_ended = False

    def start_game(self):
        self.game_ended = False
        event = pygame.event.Event(self.event_start_reaction_id)
        millis = random.randint(500, 4000)
        pygame.time.set_timer(event, millis, loops=1)

    def draw(self, events):
        self.reacton_button.draw_rectangle()
        self.exit_button.draw_button()
        if self.game_ended:
            self.end_game()
        for event in events:
            if event.type == self.event_start_reaction_id:
                self.reacton_button.start_reaction()
                self.reacton_button.change_bgcolor((255, 0, 0))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.reacton_button.collidepoint(event.pos):
                    self.reacton_button.complete_button_function()
                elif self.restart_game_button.collidepoint(event.pos) and self.game_ended:
                    self.restart_game_button.button_function_complete()
                elif self.exit_button.collidepoint(event.pos):
                    self.exit_button.button_function_complete()
            if event.type == self.event_end_reaction_good_id:
                self.game_ended = True
                self.score = event.score
            elif event.type == self.event_end_reaction_bad_id:
                self.game_ended = True
                self.score = -1
        return None

    def end_reaction_good(self):
        self.reacton_button.change_bgcolor((128, 128, 128))
        event = pygame.event.Event(self.event_end_reaction_good_id, score=self.reacton_button.end_reaction())
        pygame.event.post(event)

    def end_reaction_bad(self):
        event = pygame.event.Event(self.event_end_reaction_bad_id)
        pygame.event.post(event)

    def end_game(self):
        score_render = self.score_font.render(f'{self.score}', True, (0, 0, 0))
        self.window.blit(score_render, ((480-self.score_font.size(f'{self.score}')[0]) // 2, 200))
        self.restart_game_button.draw_button()
