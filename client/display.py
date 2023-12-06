import pygame
import threading


class Button:
    def __init__(self, from_left, from_top, width, height):
        self.from_left = from_left
        self.from_top = from_top
        self.width = width
        self.height = height
        self.name = 0

    def set_name(self, name):
        self.name = name

    def Show(self):
        Display.add_rect((self.from_left, self.from_top, self.width, self.height))

    def Hide(self):
        Display.removeRect((self.from_left, self.from_top, self.width, self.height))

    def getPosition(self):
        return (self.x, self.y, self.width, self.height)

    def getName(self):
        return self.name

class Display(object):
    def __init__(self):
        pygame.display.set_caption(title="Game")
        self.WIN = pygame.display.set_mode((1280, 720))

        self.BackGroundColor = (255, 255, 255)

        self.rects = []
        self.custom_objects = []
        self.texts = []
        self.buttons = []
        self.buttonNames = []

        # render_thread = threading.Thread(target=self.render)
        # render_thread.start()

    def add_button(self, name):
        self.buttons[len(self.buttons)] = Button()
        self.buttons[-1].set_name(name)
        self.buttonNames.append(name)

    def get_button(self, x, y):
        for button in self.buttons:
            pos = button.getPosition()
            if pos[0] < x < pos[0] + pos[2]:
                if pos[1] < y < pos[1] + pos[3]:
                    return button.getName()

    def show_button(self, name):
        it = 0

        for item in self.buttonNames:
            if item == name:
                self.buttons[it].Show()
            else:
                it += 1

    def Hide_button(self, name):
        it = 0

        for item in self.buttonNames:
            if item == name:
                self.buttons[it].Hide()
            else:
                it += 1

    def add_rect(self, object, color):  # Rect(left, top, width, height)
        self.rects.append([object, color])

    def removeRect(self, object):
        for item in self.rects:
            if item[0] == object:
                self.rects.remove(item)

    def add_c_object(self, path, pos):
        self.custom_objects.append([path, pos])

    def removeCObject(self, path):
        for item in self.custom_objects:
            if item[0] == path:
                self.custom_objects.remove(item)

    def render_text(self, text, color, place):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text_to_render = font.render(text, False, color)
        self.texts.append([text_to_render, place])

    def render(self):
        self.WIN.fill(self.BackGroundColor)

        for rect in self.rects:
            pygame.draw.rect(self.WIN, self.rects[rect[1]], self.rects[rect[0]])

        for c_object in self.custom_objects:
            self.WIN.blit(pygame.image.load(self.custom_objects[c_object[0]]), self.custom_objects[c_object[1]])

        for text in self.texts:
            self.WIN.blit(self.texts[text[0]], self.texts[text[1]])

        pygame.display.update()
