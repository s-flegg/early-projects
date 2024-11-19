import os.path

import pygame
from pygame import RLEACCEL


class Animation(pygame.sprite.Sprite):
    """A class for loading and drawing animations"""

    def __init__(
        self, surface, centre_pos, file, file_type, frames, frame_mult, tpn_col
    ):
        """
        Precondition: image frames are numbered index 0 (at the end) and in the same location, and same file type
        :type surface:
        :param surface: the surface to draw onto
        :type centre_pos: tuple
        :param centre_pos: the center position
        :type file: str
        :param file: the file path as string
        :type file_type: str
        :param file_type: the file type of the images including .
        :type frames: int
        :param frames: the number of frames
        :type frame_mult: int
        :param frame_mult: the amount of times to repeat each frame
        :type tpn_col: tuple
        :param tpn_col: the transparent colour to be removed from images
        """
        super().__init__()
        self.surface = surface
        self.centre_pos = centre_pos
        self.file = file
        self.file_type = file_type
        self.frames = frames
        self.frame_mult = frame_mult
        self.tpn_col = tpn_col

        self.count = 0
        self.image_list = self.list_images()
        self.rect_list = self.list_rects()

    def list_images(self):
        """Returns image list"""
        image_list = []
        for i in range(self.frames):
            for j in range(self.frame_mult):
                image = pygame.image.load(self.file + str(i) + self.file_type)
                image.set_colorkey(
                    self.tpn_col, RLEACCEL
                )  # removes tpn_col and optimises
                image_list.append(image)
        return image_list

    def list_rects(self, centre_pos=None):
        """Takes centre_pos or uses default, Returns rect list"""
        # use self.centre_pos as default
        if centre_pos is None:
            centre_pos = self.centre_pos

        rect_list = []
        for i in range(self.frames):
            for j in range(self.frame_mult):
                image = self.image_list[i]
                rect = image.get_rect(center=centre_pos)
                rect_list.append(rect)
        return rect_list

    def update(self, centre_pos=None):
        """Takes centre_pos or uses default, updates rect list and draws self.count frame"""
        # use self as default
        if centre_pos is None:
            centre_pos = self.centre_pos

        self.rect_list = self.list_rects(centre_pos)
        self.draw()
        self.count += 1
        return

    def draw(self):
        """Draws current count image"""
        self.surface.blit(self.image_list[self.count], self.rect_list[self.count])
        return


class Text(pygame.sprite.Sprite):
    """Displays text with a variable"""

    def __init__(
        self,
        surface,
        centre_pos,
        font,
        text_rgb,
        bg_rgb,
        pre_var_text,
        post_var_text,
        var_func,
    ):
        """
        :type surface:
        :param surface: the surface to draw on to
        :type centre_pos: tuple
        :param centre_pos: the co-ordinates to draw
        :type font:
        :param font: the font including size
        :type text_rgb: tuple
        :param text_rgb: the RGB colour code for the text
        :type bg_rgb: tuple
        :param bg_rgb: the RGB colour code for background colour, can be None
        :type pre_var_text: str or None
        :param pre_var_text: the text before the variable, can be ""
        :type post_var_text: str or None
        :param post_var_text: the text after the variable, can be None
        :type var_func: function or None
        :param var_func: the function name to get the variable, not including ()
        """
        super().__init__()
        self.surface = surface
        self.centre_pos = centre_pos
        self.font = font
        self.text_rgb = text_rgb
        self.bg_rgb = bg_rgb
        self.pre_var_text = pre_var_text
        self.post_var_text = post_var_text
        if var_func is not None:
            self.var_func = var_func
        else:
            self.var_func = None

        self.create()
        self.image = self.image
        self.rect = self.rect

    def create(self):
        text = None
        if self.var_func is not None:
            if self.pre_var_text is not None and self.post_var_text is not None:
                text = self.pre_var_text + str(self.var_func()) + self.post_var_text
            elif self.pre_var_text is not None:
                text = self.pre_var_text + str(self.var_func())
            elif self.post_var_text is not None:
                text = str(self.var_func()) + self.post_var_text
            else:
                text = str(self.var_func())
        else:
            text = self.pre_var_text
        surface, _ = self.font.render(
            text=text, fgcolor=self.text_rgb, bgcolor=self.bg_rgb
        )
        self.image = surface.convert_alpha()
        self.rect = self.image.get_rect(center=self.centre_pos)
        return

    def update(self):
        self.create()
        self.draw()
        return

    def draw(self):
        self.surface.blit(self.image, self.rect)
        return


class ButtonBackground(Text):
    """Text subclass, basic button with variable, changes background on hover"""

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
        action,
    ):
        """
        :type action: object
        :param action: returns the action when button is pressed
        :type bg_rgb_hover: tuple
        :param bg_rgb_hover: the colour of the button when hovering
        """
        super().__init__(
            surface,
            centre_pos,
            font,
            text_rgb,
            bg_rgb_def,
            pre_var_text,
            post_var_text,
            var_func,
        )
        self.bg_rgb_hover = bg_rgb_hover
        self.action = action

        self.create_default()
        self.image = self.image
        self.rect = self.rect

    def create_default(self):
        self.create()
        return

    def create_hover(self):
        temp = self.bg_rgb
        self.bg_rgb = self.bg_rgb_hover
        self.create()
        self.bg_rgb = temp
        return

    def update(self, mouse_pos, mouse_up):
        """Updates buttons appearance if mouse is hovered and runs action if it is clicked,
        you need to overwrite self.act()
        """
        if self.rect.collidepoint(mouse_pos):
            self.create_hover()
            self.draw()
            if mouse_up:
                self.act()
        else:
            self.create_default()
            self.draw()

    def act(self):
        self.action()
        pass


class ButtonEnlarge(ButtonBackground):
    """Text subclass, basic button with variable, changes size on hover"""

    def __init__(
        self,
        surface,
        centre_pos,
        text_name,
        text_size,
        text_bold,
        text_scale,
        text_rgb,
        bg_rgb,
        pre_var_text,
        post_var_text,
        var_func,
        action,
    ):
        """
        :type text_name: name of the SysFont to use
        :param text_name: str
        :type text_size: size of text
        :param text_size: int
        :type text_bold: should the text be bold
        :param text_bold: boolean
        :type text_scale: multiplier to text size on hover
        :param text_scale: float
        """
        self.font_def = pygame.freetype.SysFont(text_name, text_size, text_bold)
        self.font_enlarge = pygame.freetype.SysFont(
            text_name, text_size * text_scale, text_bold
        )
        super().__init__(
            surface,
            centre_pos,
            self.font_def,
            text_rgb,
            bg_rgb,
            bg_rgb,
            pre_var_text,
            post_var_text,
            var_func,
            action,
        )

    def create_default(self):
        self.font = self.font_def
        self.create()

    def create_hover(self):
        self.font = self.font_enlarge
        self.create()
        return


class File:
    """File management"""

    def __init__(self, file):
        """
        :type file: str
        :param file: the file to be interacted with including path
        """
        self.file = file
        if os.path.isfile(self.file):
            pass
        else:
            self.create_file()

    def create_file(self):
        """creates an empty file"""
        f = open(self.file, "w")
        f.close()
        return

    def overwrite_file(self, text):
        f = open(self.file, "w")
        f.write(str(text))
        f.close()
        return

    def append_file(self, text, new_line=True):
        """Takes new_line as boolean, creates new_line first"""
        text = str(text)
        f = open(self.file, "a")
        if new_line:
            f.write("\n" + text)
        else:
            f.write(text)
        f.close()
        return

    def get_file_as_string(self):
        f = open(self.file)
        s = f.read()
        f.close()
        return s

    def get_file_as_int(self):
        f = open(self.file)
        i = int(f.read())
        f.close()
        return i

    def get_file_as_float(self):
        f = open(self.file)
        i = float(f.read())
        f.close()
        return i

    def get_file_as_list(self):
        """Assumes split on newline"""
        lines = self.get_file_as_string()
        lst = lines.split("\n")
        return lst

    def get_file_as_int_list(self):
        lst = self.get_file_as_list()
        for i in range(len(lst)):
            lst[i] = int(lst[i])
        return lst

    def get_file_as_float_list(self):
        lst = self.get_file_as_list()
        for i in range(len(lst)):
            lst[i] = float(lst[i])
        return lst

    def get_file_as_sorted_int_list(self, reverse=False):
        """Takes reverse as boolean argument"""
        lst = self.get_file_as_int_list()
        lst = lst.sort(reverse=reverse)
        return lst


# class Lists:
#     """Creates lists of items"""
#     def __init__(self, item_list):
#         """
#         :type item_list: list
#         :param item_list: list of the items
#         """
#         self.item_list = item_list
#
#     def overwrite_list(self, new_list):
#         self.item_list = new_list
#         return
#
#     def append_list(self, item):
#         self.item_list.append(item)
#         return
#
#     def insert_into_list(self, pos, item):
#         self.item_list.insert(pos, item)
#         return
#
#     def get_list(self):
#         return self.item_list
