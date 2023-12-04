from display import Display
import pygame
class Button:
    def __init__(self):
        self.from_left = 0
        self.from_top = 0
        self.width = 0
        self.height = 0

    def set_pos(self, from_left, from_top, width, height):
        self.from_left = from_left
        self.from_top =  from_top
        self.width = width
        self.height = height

    def isclicked(self):
        pass

class UI:
    def main_menu(self):
        pass

    def conn_screen(self):
        pass

    def end_screen(self):
        pass

    def license_screen(self):
        pass

