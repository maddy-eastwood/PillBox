import math, random
import pygame, sys


class Playingfield:
    NO_INTERSECTION = 0
    LEFT_BASE = 1
    RIGHT_BASE = 2
    OTHER_INTERSECTION = 3
    OFF_SCREEN_LEFT_RIGHT_BOTTOM = 4

    def __init__(self, height, width, screen):
        self.height = height
        self.width = width
        self.screen = screen
        self.reset_game_parameters()
        self.compute_field()
        self.buttons = Buttons(screen)
        self.update_game_buttons()

    # add game screen buttons to button dictionary / reset button dictionary
    def update_game_buttons(self):
        self.buttons.add_button(
            event='quit',
            width=int(self.width * 0.07),
            height=int(self.height * 0.05),
            x=self.width / 2 - self.width * 0.05,
            y=self.height - 0.05 * self.height,
            font_size=int(0.03 * self.height),
            label='QUIT')

        self.buttons.add_button(
            event='restart',
            width=int(self.width * 0.07),
            height=int(self.height * 0.05),
            x=self.width / 2 + self.width * 0.05,
            y=self.height - 0.05 * self.height,
            font_size=int(0.03 * self.height),
            label='RESTART')

        self.buttons.add_button(
            event='player1_score',
            width=int(self.width * 0.19),
            height=int(self.height * 0.05),
            x=self.width / 10,
            y=self.height / 30,
            font_size=int(0.03 * self.height),
            label=f'PLAYER 1 SCORE: {self.player1_score}'
        )

        self.buttons.add_button(
            event='player2_score',
            width=int(self.width * 0.19),
            height=int(self.height * 0.05),
            x=self.width - self.width / 10,
            y=self.height / 30,
            font_size=int(0.03 * self.height),
            label=f'PLAYER 2 SCORE: {self.player2_score}'
        )

        self.buttons.add_button(
            event='angle1',
            width=int(self.width * 0.1),
            height=int(self.height * 0.06),
            x=self.width / 15,
            y=self.height - 0.05 * self.height,
            font_size=int(0.03 * self.height),
            label=f'ANGLE: {self.angle1}°',
            color='honeydew'
        )

        self.buttons.add_button(
            event='angle2',
            width=int(self.width * 0.1),
            height=int(self.height * 0.06),
            x=self.width - self.width / 15,
            y=self.height - 0.05 * self.height,
            font_size=int(0.03 * self.height),
            label=f'ANGLE: {self.angle1}°',
            color='honeydew'
        )

        self.buttons.add_button(
            event='velocity1',
            width=int(self.width * 0.12),
            height=int(self.height * 0.06),
            x=self.width / 5,
            y=self.height - 0.05 * self.height,
            font_size=int(0.03 * self.height),
            label=f'SPEED: {self.velocity1}m/s',
            color='honeydew'
        )

        self.buttons.add_button(
            event='velocity2',
            width=int(self.width * 0.12),
            height=int(self.height * 0.06),
            x=self.width - self.width / 5,
            y=self.height - 0.05 * self.height,
            font_size=int(0.03 * self.height),
            label=f'SPEED: {self.velocity2}m/s',
            color='honeydew'
        )

        self.buttons.add_button(
            event='fire1',
            width=int(self.width * 0.1),
            height=int(self.height * 0.06),
            x=self.width / 3,
            y=self.height - 0.05 * self.height,
            font_size=int(0.03 * self.height),
            label='FIRE',
            color='red'
        )

        self.buttons.add_button(
            event='fire2',
            width=int(self.width * 0.1),
            height=int(self.height * 0.06),
            x=self.width - self.width / 3,
            y=self.height - 0.05 * self.height,
            font_size=int(0.03 * self.height),
            label='FIRE',
            color='red'
        )

    def reset_game_parameters(self):
        self.player1_score = 0
        self.player2_score = 0
        self.angle1 = 45
        self.angle2 = 45
        self.velocity1 = 50
        self.velocity2 = 50


    def compute_field(self):
        # pick the x positions for the mountain corners + top
        self.x_lplane = random.randint(int(0.1 * self.width), int(0.4 * self.width))
        self.x_rplane = random.randint(int(0.6 * self.width), int(0.9 * self.width))
        plane_distance = self.x_rplane - self.x_lplane
        self.x_top = self.x_lplane + random.randint(int(0.1 * plane_distance), int(0.9 * plane_distance))

        # pick x positions for the bases
        self.x_lbase = random.randint(int(0.1 * self.x_lplane), int(0.9 * self.x_lplane))
        self.x_rbase = self.x_rplane + random.randint(int(0.1 * (self.width - self.x_rplane)),
                                                      int(0.9 * (self.width - self.x_rplane)))

        # y positions for the mountain corners + top
        self.y_lplane = random.randint(int(0.4 * self.height), int(0.9 * self.height))
        self.y_rplane = random.randint(int(0.4 * self.height), int(0.9 * self.height))
        mt_top_space = min(self.y_rplane, self.y_lplane)
        self.y_top = random.randint(int(0.1 * mt_top_space), int(0.9 * mt_top_space))

        # make base boxes
        self.base_width = int(0.04 * self.width)
        self.base_height = int(0.015 * self.height)

    def draw(self):
        self.screen.fill('skyblue1')

        # draw left plane
        pygame.draw.line(
            self.screen,
            'springgreen4',
            (0, self.y_lplane),
            (self.x_lplane, self.y_lplane),
            4
        )

        # draw right plane
        pygame.draw.line(
            self.screen,
            'springgreen4',
            (self.x_rplane, self.y_rplane),
            (self.width, self.y_rplane),
            4
        )

        # draw mountain
        pygame.draw.line(
            self.screen,
            'springgreen4',
            (self.x_lplane, self.y_lplane),
            (self.x_top, self.y_top),
            4
        )
        pygame.draw.line(
            self.screen,
            'springgreen4',
            (self.x_top, self.y_top),
            (self.x_rplane, self.y_rplane),
            4
        )

        # draw base rectangles
        left_base_surf = pygame.Surface((self.base_width, self.base_height))
        left_base_surf.fill('violetred')
        left_base_rect = left_base_surf.get_rect(center=(self.x_lbase, self.y_lplane - self.base_height / 2))
        self.screen.blit(left_base_surf, left_base_rect)

        right_base_surf = pygame.Surface((self.base_width, self.base_height))
        right_base_surf.fill('violetred')
        right_base_rect = right_base_surf.get_rect(center=(self.x_rbase, self.y_rplane - self.base_height / 2))
        self.screen.blit(right_base_surf, right_base_rect)

        # draw floor
        soil_surf = pygame.Surface((self.width, 0.1 * self.height))
        soil_surf.fill('chocolate4')
        soil_rect = soil_surf.get_rect(topleft=(0, self.height - 0.1 * self.height))
        self.screen.blit(soil_surf, soil_rect)

        # draw buttons
        self.buttons.draw_buttons()

    @staticmethod
    def compute_line_constants(xi: float, xf: float, yi: float, yf: float) -> ([None | float], [None | float]):
        if xf == xi:
            return (None, None)
        else:
            m = (yf - yi) / (xf - xi)
            b = -xi * m + yi
            return m, b

    @staticmethod
    def is_intersection(xi_bullet: float, xf_bullet: float, yi_bullet: float, yf_bullet: float,
                        xi_test: float, xf_test: float, yi_test: float, yf_test) -> bool:

        m_bullet, b_bullet = Playingfield.compute_line_constants(xi_bullet, xf_bullet, yi_bullet, yf_bullet)
        m_test, b_test = Playingfield.compute_line_constants(xi_test, xf_test, yi_test, yf_test)

        if m_bullet != m_test:
            if m_bullet is None:
                x_intersection = xi_bullet
                if yf_bullet != yi_test:
                    return False
            elif m_test is None:
                x_intersection = xi_test
                if yi_test != yi_bullet:
                    return False
            else:
                x_intersection = (b_test - b_bullet) / (m_bullet - m_test)

            # segment range checks

            # check x range of the bullet segment
            if xi_bullet <= x_intersection <= xf_bullet or \
                    xf_bullet <= x_intersection <= xi_bullet:
                # check the x range of the test segment
                if xi_test <= x_intersection <= xf_test or \
                        xf_test <= x_intersection <= xi_test:
                    return True

        return False

    def check_game_intersections(self, xi_bullet: float, xf_bullet: float, yi_bullet: float, yf_bullet: float) -> int:
        # mountain
        # bases
        # planes
        # off-screeen

        # test left mountain
        if Playingfield.is_intersection(xi_bullet, xf_bullet, yi_bullet, yf_bullet,
                                        self.x_lplane, self.x_top, self.y_lplane, self.y_top):
            return Playingfield.OTHER_INTERSECTION

        # test right mountain
        elif Playingfield.is_intersection(xi_bullet, xf_bullet, yi_bullet, yf_bullet,
                                          self.x_top, self.x_rplane, self.y_top, self.y_rplane):
            return Playingfield.OTHER_INTERSECTION

        # test left base from top
        elif Playingfield.is_intersection(xi_bullet, xf_bullet, yi_bullet, yf_bullet,
                                          self.x_lbase - self.base_width / 2, self.x_lbase + self.base_width / 2,
                                          self.y_lplane, self.y_lplane):
            return Playingfield.LEFT_BASE

        # test right base from top
        elif Playingfield.is_intersection(xi_bullet, xf_bullet, yi_bullet, yf_bullet,
                                          self.x_rbase - self.base_width / 2, self.x_rbase + self.base_width / 2,
                                          self.y_rplane, self.y_rplane):
            return Playingfield.RIGHT_BASE

        # test left plane
        elif Playingfield.is_intersection(xi_bullet, xf_bullet, yi_bullet, yf_bullet,
                                        0, self.x_lplane, self.y_lplane, self.y_lplane):
            return Playingfield.OTHER_INTERSECTION

        # test right plane
        elif Playingfield.is_intersection(xi_bullet, xf_bullet, yi_bullet, yf_bullet,
                                        self.x_rplane, self.width, self.y_rplane, self.y_rplane):
            return Playingfield.OTHER_INTERSECTION

        # test if bullet falls off the screen to the left, right, or bottom
        elif xf_bullet < 0 or xf_bullet > self.width or yf_bullet > (self.height - 0.1 * self.height):
            return Playingfield.OFF_SCREEN_LEFT_RIGHT_BOTTOM

        else:
            return Playingfield.NO_INTERSECTION


class Buttons:
    fill_color = 'maroon1'

    def __init__(self, screen):
        self.button_dict = {}
        self.screen = screen
        self.selected_button = None

    def add_button(self,
                   event: str,
                   label: str,
                   x: int,
                   y: int,
                   width: int,
                   height: int,
                   font_size: float,
                   color: str = fill_color):
        self.button_dict[event] = {'label': label,
                                   'x': x,
                                   'y': y,
                                   'width': width,
                                   'height': height,
                                   'color': color,
                                   'font_size': font_size
                                   }

    @staticmethod
    def button(x_size, y_size, x_coord, y_coord, font_size, text, screen, color=fill_color):
        button_surf = pygame.Surface((x_size, y_size))
        button_surf.fill(color)
        button_rect = button_surf.get_rect(center=(x_coord, y_coord))
        button_text = pygame.font.Font(None, font_size)
        button_text_surf = button_text.render(text, True, 'dark blue')
        button_text_rect = button_text_surf.get_rect(center=button_rect.center)
        screen.blit(button_surf, button_rect)
        screen.blit(button_text_surf, button_text_rect)

    def draw_button(self, event: str):
        Buttons.button(
            self.button_dict[event]['width'],
            self.button_dict[event]['height'],
            self.button_dict[event]['x'],
            self.button_dict[event]['y'],
            self.button_dict[event]['font_size'],
            self.button_dict[event]['label'],
            self.screen,
            color=self.button_dict[event]['color'])

    def draw_buttons(self):
        for event in self.button_dict.keys():
            self.draw_button(event)

    def check_buttons(self, x: float, y: float) -> list:
        # this method will check whether a button has been pressed
        event_list = []
        for event in self.button_dict.keys():
            if (self.button_dict[event]['x'] - self.button_dict[event]['width'] / 2 <= x <= self.button_dict[event][
                'x'] + self.button_dict[event]['width'] / 2) and \
                    (self.button_dict[event]['y'] - self.button_dict[event]['height'] / 2 <= y <=
                     self.button_dict[event]['y'] + self.button_dict[event]['height'] / 2):
                event_list.append(event)
        return event_list

    def select_button(self, event: str):
        pygame.draw.rect(
            surface=self.screen,
            color='red',
            rect=pygame.rect.Rect(self.button_dict[event]['x'] - self.button_dict[event]['width'] / 2,
                                  self.button_dict[event]['y'] - self.button_dict[event]['height'] / 2,
                                  self.button_dict[event]['width'] + self.button_dict[event]['width'] / 50,
                                  self.button_dict[event]['height']),
            width=int(self.button_dict[event]['height'] / 15))
        self.selected_button = event

    def unselect_button(self, event: str):
        pygame.draw.rect(
            surface=self.screen,
            color=self.button_dict[event]['color'],
            rect=pygame.rect.Rect(self.button_dict[event]['x'] - self.button_dict[event]['width'] / 2,
                                  self.button_dict[event]['y'] - self.button_dict[event]['height'] / 2,
                                  self.button_dict[event]['width'] + self.button_dict[event]['width'] / 50,
                                  self.button_dict[event]['height']),
            width=int(self.button_dict[event]['height'] / 15))


class Bullet:
    SPEED_SCALE: float = 1
    GRAVITY: float = 9.81  # m/s^2

    def __init__(self, screen, velocity, angle, xi, yi, seconds):
        self.velocity = velocity
        self.angle = angle
        self.screen = screen
        self.xi = xi
        self.yi = yi
        self.seconds = seconds
        self.current_x = self.xi
        self.current_y = self.yi

    def draw_bullet(self):
        pygame.draw.rect(self.screen, 'black', [int(self.current_x), int(self.current_y), 2, 2])

    def update_bullet_1(self, time):
        # split up initial velocity into x and y components
        self.velocity_x0 = self.velocity * math.cos(math.radians(self.angle))
        self.velocity_y0 = self.velocity * math.sin(math.radians(self.angle))

        self.current_x = self.xi + self.velocity_x0 * time
        self.current_y = self.yi - self.velocity_y0 * time + 0.5 * self.GRAVITY * time ** 2

    def update_bullet_2(self, time):
        self.velocity_x0 = self.velocity * math.cos(math.radians(self.angle))
        self.velocity_y0 = self.velocity * math.sin(math.radians(self.angle))

        self.current_x = self.xi - self.velocity_x0 * time
        self.current_y = self.yi - self.velocity_y0 * time + 0.5 * self.GRAVITY * time ** 2