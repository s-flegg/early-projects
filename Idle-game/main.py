import sys

import game_basics as gb
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, MOUSEBUTTONUP
from pygame.sprite import RenderUpdates

# TODO: simple animation background, icons for producers showing amount, upgrades,
# and buybutton with cost
# TODO: dimboost, galaxyboost, tickspeed boost


class BuyButton(gb.ButtonBackground):
    """Adds one to item specified in buy, takes cost from item specified in cost"""

    def __init__(
        self,
        surface,
        centre_pos,
        font,
        text_rgb,
        bg_rgb_def,
        bg_rgb_hover,
        pre_var_text,
        post_var_text,
        var_func,
        buy_func,
        buy_amount,
    ):
        """
        :type buy_func: function or None
        :param buy_func: full function used to change the desired
        amount excluding the ()
        :type buy_amount: int or None
        :param buy_amount: the amount of the item to add
        """
        super().__init__(
            surface,
            centre_pos,
            font,
            text_rgb,
            bg_rgb_def,
            bg_rgb_hover,
            pre_var_text,
            post_var_text,
            var_func,
            action=buy_func,
        )
        self.buy_func = buy_func
        self.buy_amount = buy_amount
        self.var_str = "{:.2e}".format(self.var_func())

    def create(self):
        text = None
        if self.var_func is not None:
            self.var_str = "{:.2e}".format(self.var_func())
            if self.pre_var_text is not None and self.post_var_text is not None:
                text = self.pre_var_text + str(self.var_str) + self.post_var_text
            elif self.pre_var_text is not None:
                text = self.pre_var_text + str(self.var_str)
            elif self.post_var_text is not None:
                text = str(self.var_str) + self.post_var_text
            else:
                text = str(self.var_str)
        else:
            text = self.pre_var_text
        surface, _ = self.font.render(
            text=text, fgcolor=self.text_rgb, bgcolor=self.bg_rgb
        )
        self.image = surface.convert_alpha()
        self.rect = self.image.get_rect(center=self.centre_pos)
        return

    def act(self):
        if self.buy_func is not None:
            self.buy_func(self.buy_amount)
        # self.cost_func(- self.cost_amount())


class Icons(pygame.sprite.Sprite):
    """Producer icon, shows name, amount, upgrades and cost, contains buy button"""

    def __init__(self, surface, centre_pos, bg_colour, name, producer, data):
        """
        :type name: str
        :param name: The displayed name of the producer
        :type producer: int
        :param producer: position in producers_list
        :type centre_pos: tuple
        :param centre_pos: the centre of the icon
        """
        super().__init__()
        self.destination = surface
        self.centre_pos = centre_pos
        self.bg_colour = bg_colour
        self.name = name
        self.producer = producer
        self.data = data

        self.width = 600
        self.height = 20

        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(self.bg_colour)

        self.text_name = gb.Text(
            surface=self.surface,
            centre_pos=(self.width / 5 * 1, self.height / 2),
            font=self.data.font_default_small,
            text_rgb=self.data.colour_font_default,
            bg_rgb=self.data.colour_screen_default,
            pre_var_text=self.name,
            post_var_text=None,
            var_func=None,  # FIXME: in gb change Text to CentredText and create
            # StartPosText, using CentredText as masterclass, changing centre using
            # width and height then use centred text here
        )
        self.text_upgrade = BuyButton(
            surface=self.surface,
            centre_pos=(self.width / 5 * 2, self.height / 2),
            font=self.data.font_default_small,
            text_rgb=self.data.colour_font_default,
            bg_rgb_def=self.data.colour_screen_default,
            bg_rgb_hover=self.data.colour_screen_default,
            pre_var_text=None,
            post_var_text=None,
            var_func=self.data.producers_list[self.producer].get_upgrades,
            buy_func=None,
            buy_amount=None,
        )
        self.text_amount = BuyButton(
            surface=self.surface,
            centre_pos=(self.width / 5 * 3, self.height / 2),
            font=self.data.font_default_small,
            text_rgb=self.data.colour_font_default,
            bg_rgb_def=self.data.colour_screen_default,
            bg_rgb_hover=self.data.colour_screen_default,
            pre_var_text=None,
            post_var_text=None,
            var_func=self.data.producers_list[self.producer].get_amount,
            buy_func=None,
            buy_amount=None,
        )
        self.button_buy = BuyButton(
            surface=self.surface,
            centre_pos=(self.width / 5 * 4, self.height / 2),
            font=self.data.font_default_small,
            text_rgb=self.data.colour_font_default,
            bg_rgb_def=self.data.colour_screen_default,
            bg_rgb_hover=self.data.colour_button_hover_default,
            pre_var_text=None,
            post_var_text=None,
            var_func=self.data.producers_list[self.producer].get_cost,
            buy_func=self.data.producers_list[self.producer].buy,
            buy_amount=1,
        )
        self.texts = RenderUpdates(self.text_name)
        self.buttons = RenderUpdates(
            self.button_buy, self.text_amount, self.text_upgrade
        )
        self.image = self.surface.convert_alpha()
        self.rect = self.image.get_rect(center=self.centre_pos)

    def update(self, mouse_pos, mouse_up):
        t = list(mouse_pos)
        t[0] -= self.centre_pos[0]
        t[0] += self.width / 2
        t[1] -= self.centre_pos[1]
        t[1] += self.height / 2
        t = tuple(t)
        self.texts.update()
        self.buttons.update(t, mouse_up)
        self.image = self.surface.convert_alpha()
        self.rect = self.image.get_rect(center=self.centre_pos)
        self.draw()
        return

    def draw(self):
        self.destination.blit(self.image, self.rect)


class DefaultProducer:
    """
    Default producer, produces x of y every 1 second
    1.1x production mult per upgrade
    1.2x cost mult per upgrade
    2x production mult every 10 upgrades
    base production of 1
    """

    def __init__(self, produces, cost, game):
        """
        Args:
            produces: the name of the currency or producer that is produced
            cost: the initial cost
            game: the game class that everything is stored in
        """
        self.produces = produces
        self.production_amount = 1
        self.upgrades = 1
        self.amount_of = 0
        self.cost = cost
        self.game = game

    def get_amount(self):
        return self.amount_of

    def get_upgrades(self):
        return self.upgrades

    def get_cost(self):
        return self.cost

    def set_amount(self, amount):
        self.amount_of = amount

    def initialise(self, upgrades, amount, cost):
        self.upgrades = upgrades
        self.amount_of = amount
        self.cost = cost

    def change_amount_float(self, change):
        self.amount_of += change

    def add_upgrades(self, amount):
        self.upgrades += amount

    def upgrade_production_amount(self, amount):
        for i in range(amount):
            self.production_amount *= 1.1

    def calc_cost(self, amount):
        if amount == 1:
            return self.cost
        else:
            temp = self.cost
            for i in range(amount):
                temp *= 1.2
        return temp

    def set_cost(self, amount):
        if amount == 1:
            self.cost *= 1.2
        else:
            self.cost = self.calc_cost(amount)

    def buy(self, amount):
        cost = self.calc_cost(amount)
        if self.game.get_money() >= cost and self.produces.get_amount() >= 1:
            if self.amount_of == 0:
                self.amount_of = 1
            self.game.buy(cost)
            self.add_upgrades(amount)
            self.upgrade_production_amount(amount)
            self.set_cost(amount)
            self.round_all()

    def produce(self):
        amount_produced = self.production_amount * self.amount_of
        self.produces.change_amount_float(amount_produced)

    def round_all(self):
        """Rounds all values to 2 dp"""
        self.production_amount = round(self.production_amount, 2)
        self.upgrades = round(self.upgrades, 2)
        self.amount_of = round(self.amount_of, 2)
        self.cost = round(self.cost, 2)


class Data:
    """The main game class holding lots of important files"""

    def __init__(self, screen_width, screen_height):
        # Window
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.surface = self.screen
        self.clock = pygame.time.Clock()

        # Game data
        self.game_state = "initialise"
        self.current_save = 1
        self.producers_list = []
        self.currency_holder = DefaultProducer(
            produces=None,
            # this isn't a producer but uses the class for the
            # change_amount_float function
            cost=0,
            game=self,
        )
        self.money = self.currency_holder.get_amount()

        # Colours
        self.colour_screen_default = (59, 96, 100)
        self.colour_font_default = (48, 242, 242)
        self.colour_button_hover_default = (85, 130, 139)

        # Fonts
        self.font_default_small = pygame.freetype.SysFont("Courier", 20, False)
        self.font_default_mid = pygame.freetype.SysFont("Courier", 40, False)
        self.font_default_big = pygame.freetype.SysFont("Courier", 60, False)

    def update_money(self):
        self.money = round(self.currency_holder.get_amount(), 2)

    def get_money(self):
        return self.money

    def buy(self, amount):
        self.currency_holder.change_amount_float(-amount)

    def load_general_save_data(self):
        current_save_file = gb.File("save_data/general/current_save.txt")
        self.current_save = current_save_file.get_file_as_int()
        return

    def load_specific_save_data(self, save):
        """save as int"""
        upgrades = gb.File("save_data/save_" + str(save) + "/upgrades.txt")
        upgrades_list = upgrades.get_file_as_int_list()
        amounts = gb.File("save_data/save_" + str(save) + "/amounts.txt")
        amounts_list = amounts.get_file_as_float_list()
        costs = gb.File("save_data/save_" + str(save) + "/costs.txt")
        costs_list = costs.get_file_as_float_list()
        for i in range(10):
            self.producers_list[i].initialise(
                upgrades_list[i], amounts_list[i], costs_list[i]
            )
        money = gb.File("save_data/save_" + str(save) + "/money.txt")
        self.currency_holder.set_amount(money.get_file_as_float())
        return

    def save(self):
        current = gb.File("save_data/general/current_save.txt")
        current.overwrite_file(self.current_save)

        upgrades = gb.File("save_data/save_" + str(self.current_save) + "/upgrades.txt")
        amounts = gb.File("save_data/save_" + str(self.current_save) + "/amounts.txt")
        costs = gb.File("save_data/save_" + str(self.current_save) + "/costs.txt")
        money = gb.File("save_data/save_" + str(self.current_save) + "/money.txt")

        money.overwrite_file(self.get_money())
        upgrades.overwrite_file(self.producers_list[0].get_upgrades())
        amounts.overwrite_file(self.producers_list[0].get_amount())
        costs.overwrite_file(self.producers_list[0].get_cost())
        for i in range(1, 10):
            upgrades.append_file(self.producers_list[i].get_upgrades())
            amounts.append_file(self.producers_list[i].get_amount())
            costs.append_file(self.producers_list[i].get_cost())
        return


class Initialise:
    def __init__(self, data):
        self.data = data

    def create_producers(self):
        producer_0 = DefaultProducer(
            produces=self.data.currency_holder, cost=1, game=self.data
        )
        self.data.producers_list = [producer_0]
        for i in range(1, 10):
            self.data.producers_list.append(
                DefaultProducer(
                    produces=self.data.producers_list[int(i - 1)],
                    cost=pow(10, i),
                    game=self.data,
                )
            )
        return

    def run(self):
        self.create_producers()
        self.data.load_general_save_data()
        self.data.load_specific_save_data(self.data.current_save)
        self.data.game_state = "title"
        return


class Title:
    def __init__(self, data):
        self.data = data

    def run(self):
        pygame.mouse.set_visible(True)

        text_title = gb.Text(
            surface=self.data.screen,
            centre_pos=(self.data.screen_width / 2, self.data.screen_height / 2 - 40),
            font=self.data.font_default_big,
            text_rgb=self.data.colour_font_default,
            bg_rgb=self.data.colour_screen_default,
            pre_var_text="Idle Radiation",
            post_var_text=None,
            var_func=None,
        )
        text_press_any = gb.Text(
            surface=self.data.screen,
            centre_pos=(self.data.screen_width / 2, self.data.screen_height / 2 + 40),
            font=self.data.font_default_big,
            text_rgb=self.data.colour_font_default,
            bg_rgb=self.data.colour_screen_default,
            pre_var_text="Press any button to continue",
            post_var_text=None,
            var_func=None,
        )
        texts = RenderUpdates(text_title, text_press_any)

        while self.data.game_state == "title":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.data.game_state = "quit"
                    return
                elif event.type == KEYDOWN or event.type == MOUSEBUTTONUP:
                    self.data.game_state = "menu"
                    return

            self.data.screen.fill(self.data.colour_screen_default)
            texts.update()

            self.data.clock.tick(30)
            pygame.display.flip()


class Menu:
    def __init__(self, data):
        self.data = data
        self.screen = 1
        self.leave = False
        return

    def back(self):
        self.screen = 1
        self.leave = True
        return

    def screen_main(self):
        def set_game_state_play():
            self.data.game_state = "play"
            self.leave = True
            return

        def new_game():
            self.screen = 2
            self.leave = True
            return

        def load_game():
            self.screen = 3
            self.leave = True
            return

        def set_game_state_quit():
            self.data.game_state = "quit"
            self.leave = True
            return

        self.leave = False

        button_continue = gb.ButtonEnlarge(
            surface=self.data.screen,
            centre_pos=(self.data.screen_width / 2, self.data.screen_height / 2 - 75),
            text_name="Courier",
            text_size=40,
            text_bold=False,
            text_scale=1.2,
            text_rgb=self.data.colour_font_default,
            bg_rgb=self.data.colour_screen_default,
            pre_var_text="Continue",
            post_var_text=None,
            var_func=None,
            action=set_game_state_play,
        )
        button_new = gb.ButtonEnlarge(
            surface=self.data.screen,
            centre_pos=(self.data.screen_width / 2, self.data.screen_height / 2 - 25),
            text_name="Courier",
            text_size=40,
            text_bold=False,
            text_scale=1.2,
            text_rgb=self.data.colour_font_default,
            bg_rgb=self.data.colour_screen_default,
            pre_var_text="New Game",
            post_var_text=None,
            var_func=None,
            action=new_game,
        )
        button_load = gb.ButtonEnlarge(
            surface=self.data.screen,
            centre_pos=(self.data.screen_width / 2, self.data.screen_height / 2 + 25),
            text_name="Courier",
            text_size=40,
            text_bold=False,
            text_scale=1.2,
            text_rgb=self.data.colour_font_default,
            bg_rgb=self.data.colour_screen_default,
            pre_var_text="Load Save",
            post_var_text=None,
            var_func=None,
            action=load_game,
        )
        button_quit = gb.ButtonEnlarge(
            surface=self.data.screen,
            centre_pos=(self.data.screen_width / 2, self.data.screen_height / 2 + 75),
            text_name="Courier",
            text_size=40,
            text_bold=False,
            text_scale=1.2,
            text_rgb=self.data.colour_font_default,
            bg_rgb=self.data.colour_screen_default,
            pre_var_text="Quit",
            post_var_text=None,
            var_func=None,
            action=set_game_state_quit,
        )
        buttons = RenderUpdates(button_continue, button_new, button_load, button_quit)

        while True:
            mouse_up = False
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.data.game_state = "quit"
                    return
                elif event.type == MOUSEBUTTONUP:
                    mouse_up = True

            self.data.screen.fill(self.data.colour_screen_default)

            buttons.update(mouse_pos, mouse_up)
            if self.leave:
                return

            self.data.clock.tick(60)
            pygame.display.flip()

    def screen_new(self):
        def new_save(save):
            self.data.current_save = save
            current_save_file = gb.File("save_data/general/current_save.txt")
            current_save_file.overwrite_file(save)

            upgrades_file = gb.File("save_data/save_" + str(save) + "/upgrades.txt")
            amounts_file = gb.File("save_data/save_" + str(save) + "/amounts.txt")
            costs_file = gb.File("save_data/save_" + str(save) + "/costs.txt")
            money_file = gb.File("save_data/save_" + str(save) + "/money.txt")

            upgrades_file.overwrite_file(1)
            amounts_file.overwrite_file(0)
            costs_file.overwrite_file(1)
            money_file.overwrite_file(1)
            for i in range(1, 10):
                upgrades_file.append_file(1)
                amounts_file.append_file(0)
                costs_file.append_file(pow(10, i))

            Initialise.load_general_save_data(self)
            Initialise.load_specific_save_data(self, save)
            self.data.update_money()

            self.data.game_state = "play"
            self.leave = True
            return

        def new_save_1():
            new_save(1)
            return

        def new_save_2():
            new_save(2)
            return

        def new_save_3():
            new_save(3)
            return

        self.leave = False

        button_save_1 = gb.ButtonEnlarge(
            surface=self.data.screen,
            centre_pos=(self.data.screen_width / 2, self.data.screen_height / 2 - 75),
            text_name="Courier",
            text_size=40,
            text_bold=False,
            text_scale=1.2,
            text_rgb=self.data.colour_font_default,
            bg_rgb=self.data.colour_screen_default,
            pre_var_text="Save 1",
            post_var_text=None,
            var_func=None,
            action=new_save_1,
        )
        button_save_2 = gb.ButtonEnlarge(
            surface=self.data.screen,
            centre_pos=(self.data.screen_width / 2, self.data.screen_height / 2 - 25),
            text_name="Courier",
            text_size=40,
            text_bold=False,
            text_scale=1.2,
            text_rgb=self.data.colour_font_default,
            bg_rgb=self.data.colour_screen_default,
            pre_var_text="Save 2",
            post_var_text=None,
            var_func=None,
            action=new_save_2,
        )
        button_save_3 = gb.ButtonEnlarge(
            surface=self.data.screen,
            centre_pos=(self.data.screen_width / 2, self.data.screen_height / 2 + 25),
            text_name="Courier",
            text_size=40,
            text_bold=False,
            text_scale=1.2,
            text_rgb=self.data.colour_font_default,
            bg_rgb=self.data.colour_screen_default,
            pre_var_text="Save 3",
            post_var_text=None,
            var_func=None,
            action=new_save_3,
        )
        button_back = gb.ButtonEnlarge(
            surface=self.data.screen,
            centre_pos=(self.data.screen_width / 2, self.data.screen_height / 2 + 75),
            text_name="Courier",
            text_size=40,
            text_bold=False,
            text_scale=1.2,
            text_rgb=self.data.colour_font_default,
            bg_rgb=self.data.colour_screen_default,
            pre_var_text="Back",
            post_var_text=None,
            var_func=None,
            action=self.back,
        )
        buttons = RenderUpdates(
            button_save_1, button_save_2, button_save_3, button_back
        )

        while True:
            mouse_up = False
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.data.game_state = "quit"
                    return
                elif event.type == MOUSEBUTTONUP:
                    mouse_up = True

            self.data.screen.fill(self.data.colour_screen_default)

            buttons.update(mouse_pos, mouse_up)
            if self.leave:
                return

            self.data.clock.tick(60)
            pygame.display.flip()

    def screen_load(self):
        def load_save(save):
            self.data.current_save = save
            current_save_file = gb.File("save_data/general/current_save.txt")
            current_save_file.overwrite_file(save)
            Initialise.load_specific_save_data(self, save)

            self.data.game_state = "play"
            self.leave = True
            return

        def load_save_1():
            load_save(1)
            return

        def load_save_2():
            load_save(2)
            return

        def load_save_3():
            load_save(3)
            return

        self.leave = False

        button_save_1 = gb.ButtonEnlarge(
            surface=self.data.screen,
            centre_pos=(self.data.screen_width / 2, self.data.screen_height / 2 - 75),
            text_name="Courier",
            text_size=40,
            text_bold=False,
            text_scale=1.2,
            text_rgb=self.data.colour_font_default,
            bg_rgb=self.data.colour_screen_default,
            pre_var_text="Save 1",
            post_var_text=None,
            var_func=None,
            action=load_save_1,
        )
        button_save_2 = gb.ButtonEnlarge(
            surface=self.data.screen,
            centre_pos=(self.data.screen_width / 2, self.data.screen_height / 2 - 25),
            text_name="Courier",
            text_size=40,
            text_bold=False,
            text_scale=1.2,
            text_rgb=self.data.colour_font_default,
            bg_rgb=self.data.colour_screen_default,
            pre_var_text="Save 2",
            post_var_text=None,
            var_func=None,
            action=load_save_2,
        )
        button_save_3 = gb.ButtonEnlarge(
            surface=self.data.screen,
            centre_pos=(self.data.screen_width / 2, self.data.screen_height / 2 + 25),
            text_name="Courier",
            text_size=40,
            text_bold=False,
            text_scale=1.2,
            text_rgb=self.data.colour_font_default,
            bg_rgb=self.data.colour_screen_default,
            pre_var_text="Save 3",
            post_var_text=None,
            var_func=None,
            action=load_save_3,
        )
        button_back = gb.ButtonEnlarge(
            surface=self.data.screen,
            centre_pos=(self.data.screen_width / 2, self.data.screen_height / 2 + 75),
            text_name="Courier",
            text_size=40,
            text_bold=False,
            text_scale=1.2,
            text_rgb=self.data.colour_font_default,
            bg_rgb=self.data.colour_screen_default,
            pre_var_text="Back",
            post_var_text=None,
            var_func=None,
            action=self.back,
        )
        buttons = RenderUpdates(
            button_save_1, button_save_2, button_save_3, button_back
        )

        while True:
            mouse_up = False
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.data.game_state = "quit"
                    return
                elif event.type == MOUSEBUTTONUP:
                    mouse_up = True

            self.data.screen.fill(self.data.colour_screen_default)

            buttons.update(mouse_pos, mouse_up)
            if self.leave:
                return

            self.data.clock.tick(60)
            pygame.display.flip()

    def run(self):
        if self.screen == 1:
            self.screen_main()
            return
        elif self.screen == 2:
            self.screen_new()
            return
        elif self.screen == 3:
            self.screen_load()
            return


class Play:
    def __init__(self, data):
        self.data = data

    def run(self):
        def produce():
            for i in range(10):
                self.data.producers_list[i].produce()

        pygame.mouse.set_visible(True)

        text_money = BuyButton(
            surface=self.data.screen,
            centre_pos=(self.data.screen_width / 2, 30),
            font=self.data.font_default_mid,
            text_rgb=self.data.colour_font_default,
            bg_rgb_def=self.data.colour_screen_default,
            bg_rgb_hover=self.data.colour_screen_default,
            pre_var_text=None,
            post_var_text=None,
            var_func=self.data.get_money,
            buy_func=None,
            buy_amount=None,
        )
        # button_list = []
        # for i in range(10):
        #     button_list.append(
        #         BuyButton(
        #             surface=self.data.screen,
        #             centre_pos=(self.data.screen_width / 3, 40 * i + 100),
        #             font=self.data.font_default_small,
        #             text_rgb=self.data.colour_font_default,
        #             bg_rgb_def=self.data.colour_screen_default,
        #             bg_rgb_hover=self.data.colour_button_hover_default,
        #             pre_var_text="Buy 1 for ",
        #             post_var_text="?",
        #             var_func=self.data.producers_list[i].get_cost,
        #             buy_func=self.data.producers_list[i].buy,
        #             buy_amount=1,
        #         )
        #     )

        buttons = RenderUpdates(text_money)  # , button_list)

        produce_event = pygame.USEREVENT + 1
        pygame.time.set_timer(produce_event, 1000)

        # icon_test_list = []
        # for i in range(10):
        #     icon_test_list.append(
        #         Icons(
        #             surface=self.data.screen,
        #             centre_pos=(self.data.screen_width / 3 * 2, 40 * i + 100),
        #             bg_colour=self.data.colour_screen_default,
        #             name="test" + str(i),
        #             producer=i,
        #             data=self.data,
        #         )
        #     )
        # icons = RenderUpdates(icon_test_list)

        # test1 = Icons(
        #             surface=self.data.screen,
        #             centre_pos=(self.data.screen_width // 3 * 2, 160),
        #             bg_colour=self.data.colour_screen_default,
        #             name="test1",
        #             producer=1,
        #             data=self.data,
        #         )
        # test2 = Icons(
        #             surface=self.data.screen,
        #             centre_pos=(self.data.screen_width // 3 * 2, 180),
        #             bg_colour=self.data.colour_screen_default,
        #             name="test2",
        #             producer=2,
        #             data=self.data,
        #         )
        # icons = RenderUpdates(test1, ) #test2)

        def producer_icon(name, i):
            return Icons(
                surface=self.data.screen,
                centre_pos=(self.data.screen_width // 3, 50 * i + 100),
                bg_colour=self.data.colour_screen_default,
                name=name,
                producer=i,
                data=self.data,
            )

        producers_icon_list = [
            producer_icon("Thallium-206", 0),
            producer_icon("Bismuth-212", 1),
            producer_icon("Lead-212", 2),
            producer_icon("Polonium-216", 3),
            producer_icon("Radon-220", 4),
            producer_icon("Radium-224", 5),
            producer_icon("Thorium-228", 6),
            producer_icon("Actinium-228", 7),
            producer_icon("Radium-228", 8),
            producer_icon("Thorium-232", 9),
        ]
        icons = RenderUpdates(producers_icon_list)

        while True:
            mouse_up = False
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.data.game_state = "quit"
                    return
                elif event.type == MOUSEBUTTONUP:
                    mouse_up = True
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.data.save()
                        self.data.game_state = "menu"
                        return
                if event.type == produce_event:
                    produce()

            self.data.screen.fill(self.data.colour_screen_default)

            buttons.update(mouse_pos, mouse_up)

            icons.update(mouse_pos, mouse_up)

            self.data.update_money()
            self.data.clock.tick(60)
            pygame.display.flip()


class Quit:
    def __init__(self, data):
        self.data = data

    def run(self):
        self.data.save()
        self.data.game_state = ""
        return


class Run:
    def __init__(self, screen_width, screen_height):
        self.data = Data(screen_width, screen_height)
        self.initialise = Initialise(self.data)
        self.title = Title(self.data)
        self.menu = Menu(self.data)
        self.play = Play(self.data)
        self.quit = Quit(self.data)

    def run(self):
        while True:
            if self.data.game_state == "initialise":
                self.initialise.run()
            elif self.data.game_state == "title":
                self.title.run()
            elif self.data.game_state == "menu":
                self.menu.run()
            elif self.data.game_state == "play":
                self.play.run()
            elif self.data.game_state == "quit":
                self.quit.run()
            else:
                pygame.quit()
                sys.exit()


def main():
    pygame.init()

    screen_width = 1600
    screen_height = 900

    game = Run(screen_width, screen_height)
    game.run()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
