import sys
import game_basics as gb
import pygame
from pygame import freetype
from pygame.sprite import (Sprite, RenderUpdates)
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEMOTION,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
)

from enum import Enum


# TODO: save data - load save changes buttons list to save1, save2, save3

# temp
# Blue (Munsell) = (85, 130, 139)
# Dark Slate Grey = (59, 96, 100)
# Fluorescent cyan = (48, 242, 242)
# Mindaro = (195, 235, 120)
# Asparagus = (109, 163, 77)

class BuyButton(gb.ButtonBackground):
    """ Adds one to item specified in buy, takes cost from item specified in cost"""
    def __init__(self, surface, centre_pos, font, text_rgb, bg_rgb_def,
                 bg_rgb_hover, pre_var_text, post_var_text, var_func, buy_func,
                 buy_amount):
        """
        :type buy_func: function or None
        :param buy_func: full function used to change the desired amount excluding the ()
        :type buy_amount: int or None
        :param buy_amount: the amount of the item to add
        """
        super().__init__(surface, centre_pos, font, text_rgb, bg_rgb_def,
                         bg_rgb_hover, pre_var_text, post_var_text, var_func, action=buy_func)
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
        surface, _ = self.font.render(text=text, fgcolor=self.text_rgb, bgcolor=self.bg_rgb)
        self.image = surface.convert_alpha()
        self.rect = self.image.get_rect(center=self.centre_pos)
        return

    def act(self):
        self.buy_func(self.buy_amount)
        # self.cost_func(- self.cost_amount())


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

    def initialise(self, upgrades, amount):
        self.upgrades = upgrades
        self.amount_of = amount

    def change_amount_float(self, change):
        self.amount_of += change

##    def upgrade(self, amount):
##        """upgrade everything, amount is amount of upgrades"""
##        self.upgrades += amount
##        self.production_amount = 1
##        self.cost = 1
##        for i in range(self.upgrades):
##            self.production_amount *= 1.1
##            # print(self.production_amount) #test
##            self.cost *= 1.2
##            if i > 9 and i % 10 == 0:
##                self.production_amount *= 2
##        # print(self.production_amount) #test
##        self.round_all()
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

##    def buy(self, amount, currency_holder=game.currency_holder):
##        if currency_holder.get_amount() >= self.cost:
##            currency_holder.set_amount(currency_holder.get_amount - s



# class Lists:
#     producers_list = []
#     screen_dimensions = []
#
#
# class GameState(Enum):
#     QUIT = -1
#     TITLE = 0
#     GAME = 1
#
#
# def create_producers():
#     """returns list of them"""
#     currency = DefaultProducer(
#         produces=None
#         # this isn't a producer but uses the class for the change_amount_float function
#     )
#     producer_1 = DefaultProducer(produces=currency)
#     producer_2 = DefaultProducer(produces=producer_1)
#     producer_3 = DefaultProducer(produces=producer_2)
#     producer_4 = DefaultProducer(produces=producer_3)
#     producer_5 = DefaultProducer(produces=producer_4)
#     producer_6 = DefaultProducer(produces=producer_5)
#     producer_7 = DefaultProducer(produces=producer_6)
#     producer_8 = DefaultProducer(produces=producer_7)
#     producer_9 = DefaultProducer(produces=producer_8)
#     producer_10 = DefaultProducer(produces=producer_9)
#     producers_list = [producer_1, producer_2, producer_3, producer_4, producer_5,
#                       producer_6, producer_7, producer_8, producer_9, producer_10]
#     return producers_list
#
#
# def load_saved_data():
#     producers_list = create_producers()
#     upgrades = gb.File("save_data/upgrades")
#     upgrades_list = upgrades.get_file_as_list()
#     amounts = gb.File("save_data/amounts")
#     amounts_list = amounts.get_file_as_list()
#     for i in range(10):
#         producers_list[i].initialise(upgrades_list[i], amounts_list[i])
#     return
#
#
# def test(producers_list):
#     substance = DefaultProducer(
#         produces=None
#         # this isn't a producer but uses the class for the change_amount_float function
#     )
#     test1 = DefaultProducer(substance)
#     print(substance.get_amount())  # 1
#     print(test1.get_amount())  # 1
#     test1.produce()
#     print(substance.get_amount())  # 2
#     test2 = DefaultProducer(test1)
#     print(test1.get_amount())  # 1
#     test2.produce()
#     print(test1.get_amount())  # 2
#     test1.produce()
#     print(substance.get_amount())  # 3
#
#     for i in range(2):
#         # print(producers_list)
#         for producer in producers_list:
#             producer.upgrade(5)
#             producer.produce()
#             print(producer.get_amount())
#     for producer in producers_list:
#         print("\n")
#         print(producer.get_amount())
#         producer.produce()
#         # print("\n")
#         print(": ")
#         print(producer.get_amount())
#         print(producer.produces.get_amount())


# def title_loop(screen):
#     load_saved_data()



class Game:
    """The main game class holding lots of important files"""

    def __init__(self, screen_width, screen_height):
        # Window
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.screen = pygame.display.set_mode((self.screen_width, screen_height))
        self.surface = self.screen
        self.clock = pygame.time.Clock()

        # Game data
        self.game_state = "title"
        self.current_save = 1
        self.producers_list = []
        self.create_producers()
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
        self.currency_holder.change_amount_float(- amount)

    def load_specific_save_data(self, save):
        """save as int"""
        upgrades = gb.File("save_data/save_" + str(save) + "/upgrades.txt")
        upgrades_list = upgrades.get_file_as_int_list()
        amounts = gb.File("save_data/save_" + str(save) + "/amounts.txt")
        amounts_list = amounts.get_file_as_int_list()
        for i in range(10):
            self.producers_list[i].initialise(upgrades_list[i], amounts_list[i])
        money = gb.File("save_data/save_" + str(save) + "/money.txt")
        self.currency_holder.change_amount_float(money.get_file_as_int())
        return

    def load_save_1(self):
        self.current_save = 1
        self.load_specific_save_data(1)

    def load_save_2(self):
        self.current_save = 2
        self.load_specific_save_data(2)

    def load_save_3(self):
        self.current_save = 3
        self.load_specific_save_data(3)

    def load_general_save_data(self):
        current_save_file = gb.File("save_data/general/current_save.txt")
        self.current_save = current_save_file.get_file_as_int()

    def create_producers(self):
        """creates list of them"""
        self.currency_holder = DefaultProducer(
            produces=None,
            # this isn't a producer but uses the class for the change_amount_float function
            cost=0,
            game=self,
        )
        producer_0 = DefaultProducer(produces=self.currency_holder,
                                     cost=1,
                                     game=self)
        self.producers_list = [producer_0]
        for i in range(1, 10):
            self.producers_list.append(DefaultProducer(produces=self.producers_list[int(i - 1)],
                                                       cost=pow(10, i),
                                                       game=self))
        # producer_2 = DefaultProducer(produces=producer_1)
        # producer_3 = DefaultProducer(produces=producer_2)
        # producer_4 = DefaultProducer(produces=producer_3)
        # producer_5 = DefaultProducer(produces=producer_4)
        # producer_6 = DefaultProducer(produces=producer_5)
        # producer_7 = DefaultProducer(produces=producer_6)
        # producer_8 = DefaultProducer(produces=producer_7)
        # producer_9 = DefaultProducer(produces=producer_8)
        # producer_10 = DefaultProducer(produces=producer_9)
        #self.producers_list = [producer_1, producer_2, producer_3, producer_4, producer_5,
        #                       producer_6, producer_7, producer_8, producer_9, producer_10]
        return

    def produce(self):
        for i in range(10):
            self.producers_list[i].produce()

    def title_loop(self):
        pygame.mouse.set_visible(True)

        text_title = gb.Text(
            surface=self.screen,
            centre_pos=(self.screen_width / 2, self.screen_height / 2 - 40),
            font=self.font_default_big,
            text_rgb=self.colour_font_default,
            bg_rgb=self.colour_screen_default,
            pre_var_text="Idle Radiation",
            post_var_text=None,
            var_func=None,
        )
        text_press_any = gb.Text(
            surface=self.screen,
            centre_pos=(self.screen_width / 2, self.screen_height / 2 + 40),
            font=self.font_default_big,
            text_rgb=self.colour_font_default,
            bg_rgb=self.colour_screen_default,
            pre_var_text="Press any button to continue",
            post_var_text=None,
            var_func=None,
        )
        texts = RenderUpdates(text_title, text_press_any)

        self.load_general_save_data()
        while self.game_state == "title":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_state = "quit"
                    return
                elif event.type == KEYDOWN or event.type == MOUSEBUTTONUP:
                    self.game_state = "game"
                    return

            self.screen.fill(self.colour_screen_default)
            texts.update()

            self.clock.tick(30)
            pygame.display.flip()

    # def menu_loop(self):
    #     pygame.mouse.set_visible(True)
    #     self.create_producers()
    #
    #     screen = 1
    #
    #     def main_screen():
    #         def save_continue():
    #             match self.current_save:
    #                 case 1:
    #                     self.load_save_1()
    #                 case 2:
    #                     self.load_save_2()
    #                 case 3:
    #                     self.load_save_3()
    #             self.game_state = "game"
    #
    #         button_continue = gb.ButtonEnlarge(
    #             surface=self.screen,
    #             centre_pos=(self.screen_width / 2, self.screen_height / 2 - 30),
    #             text_name="Courier",
    #             text_size=40,
    #             text_bold=False,
    #             text_scale=1.2,
    #             text_rgb=self.colour_font_default,
    #             bg_rgb=self.colour_screen_default,
    #             pre_var_text="Continue",
    #             post_var_text=None,
    #             var_func=None,
    #             action=save_continue,
    #         )
    #         button_new = gb.ButtonEnlarge(
    #             surface=self.screen,
    #             centre_pos=(self.screen_width / 2, self.screen_height / 2 - 10),
    #             text_name="Courier",
    #             text_size=40,
    #             text_bold=False,
    #             text_scale=1.2,
    #             text_rgb=self.colour_font_default,
    #             bg_rgb=self.colour_screen_default,
    #             pre_var_text="New Game",
    #             post_var_text=None,
    #             var_func=None,
    #             action=,
    #         )
    #         # button_load = gb.ButtonEnlarge(
    #         #     surface=self.screen,
    #         #     centre_pos=(self.screen_width / 2, self.screen_height / 2 - 10),
    #         #     text_name="Courier",
    #         #     text_size=40,
    #         #     text_bold=False,
    #         #     text_scale=1.2,
    #         #     text_rgb=self.colour_font_default,
    #         #     bg_rgb=self.colour_screen_default,
    #         #     pre_var_text="New Game",
    #         #     post_var_text=None,
    #         #     var_func=None,
    #         #     action=,
    #         # )
    #         #button_quit = gb.Button
    #         buttons_main = RenderUpdates(button_continue)#, button_new, button_load, button_quit)
    #
    #     button_back = gb.ButtonEnlarge(
    #         surface=self.screen,
    #         centre_pos=(self.screen_width / 2, self.screen_height / 2 - 10),
    #         text_name="Courier",
    #         text_size=40,
    #         text_bold=False,
    #         text_scale=1.2,
    #         text_rgb=self.colour_font_default,
    #         bg_rgb=self.colour_screen_default,
    #         pre_var_text="Save 1",
    #         post_var_text=None,
    #         var_func=None,
    #         action=load_options_swap,
    #     )
    #     button_save_1 = gb.Button
    #     button_save_2 = gb.Button
    #     button_save_3 = gb.Button
    #     buttons_saves = RenderUpdates(button_back, button_save_1, button_save_2, button_save_3)
    #
    #     load_options = False
    #
    #     while self.game_state == "menu":
    #         while screen == 1:
    #             mouse_up = False
    #             mouse_pos = pygame.mouse.get_pos()
    #             for event in pygame.event.get():
    #                 if event.type == pygame.QUIT:
    #                     self.game_state = "quit"
    #                     return
    #                 elif event.type == MOUSEBUTTONUP:
    #                     mouse_up = True
    #
    #             self.screen.fill(self.colour_screen_default)
    #
    #             if not load_options:
    #                 buttons_main.update(mouse_pos, mouse_up)
    #             #else:
    #             #    buttons_2.update(mouse_pos, mouse_up)
    #
    #
    #             self.clock.tick(60)
    #             pygame.display.flip()
    #
    # def menu_loop(self):
    #     pygame.mouse.set_visible(True)
    #     self.create_producers()
    #
    #     screen = 1
    #
    #     def screen_main():
            

    def game_loop(self):
        pygame.mouse.set_visible(True)

        def buy(amount):
            self.currency_holder.change_amount_float(- amount) #TODO: Make all functions local functions

        text_money = BuyButton(
            surface=self.screen,
            centre_pos=(self.screen_width / 2, 30),
            font=self.font_default_mid,
            text_rgb=self.colour_font_default,
            bg_rgb_def=self.colour_screen_default,
            bg_rgb_hover=self.colour_screen_default,
            pre_var_text=None,
            post_var_text=None,
            var_func=self.get_money,
            buy_func=None,
            buy_amount=None,
        )
        test_list = []
        for i in range(10):
            test_text_amount = gb.Text(
                surface=self.screen,
                centre_pos=(self.screen_width / 2, 40 * i + 100),
                font=self.font_default_small,
                text_rgb=self.colour_font_default,
                bg_rgb=self.colour_screen_default,
                pre_var_text=None,
                post_var_text=None,
                var_func=self.producers_list[i].get_amount
            )
            test_list.append(test_text_amount)

        button_list = []
        for i in range(10):
            button_list.append(
                BuyButton(
                    surface=self.screen,
                    centre_pos=(self.screen_width / 3, 40 * i + 100),
                    font=self.font_default_small,
                    text_rgb=self.colour_font_default,
                    bg_rgb_def=self.colour_screen_default,
                    bg_rgb_hover=self.colour_button_hover_default,
                    pre_var_text="Buy 1 for ",
                    post_var_text="?",
                    var_func=self.producers_list[i].get_cost,
                    buy_func=self.producers_list[i].buy, # formerly upgrade not buy
                    buy_amount=1,
                    # cost_func=self.currency_holder.change_amount_float,
                    # cost_amount=self.producers_list[i].get_cost,
                )
            )

        texts = RenderUpdates(test_list)
        buttons = RenderUpdates(button_list, text_money)
        PRODUCE = pygame.USEREVENT + 1
        pygame.time.set_timer(PRODUCE, 1000)

        print(button_list)
        print(buttons)
        while True:
            mouse_up = False
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_state = "quit"
                    return
                elif event.type == MOUSEBUTTONUP:
                    mouse_up = True
                if event.type == PRODUCE:
                    self.produce()

            self.screen.fill(self.colour_screen_default)

            texts.update()
            buttons.update(mouse_pos, mouse_up)
            
            self.update_money()
            self.clock.tick(60)
            pygame.display.flip()

    def quit(self):
        pass
        return

    def run(self):
        while True:
            if self.game_state == "title":
                self.title_loop()
            elif self.game_state == "menu":
                self.menu_loop()
            elif self.game_state == "game":
                self.game_loop()
            elif self.game_state == "quit":
                self.quit()
                return
            else:
                return


def main():
    pygame.init()

    game = Game(1600, 900)
    game.run()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
