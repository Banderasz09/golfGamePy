import pygame
import threading

class Display:
    def __init__(self):
        pygame.display.set_caption(title="Game")
        self.WIN = pygame.display.set_mode((1280, 720))

        self.BackGroundColor = (255, 255, 255)

        self.rects = []
        self.custom_objects = []
        self.texts = []

        # render_thread = threading.Thread(target=self.render)
        # render_thread.start()

    def add_rect(self, object, color): # Rect(left, top, width, height)
        self.rects.append([object, color])

    def add_c_object(self, path, pos):
        self.custom_objects.append([pygame.image.load(path), pos])

    def render_text(self, text, color, place):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text_to_render = font.render(text, False, color)
        self.texts.append([text_to_render, place])

    def render(self):
        self.WIN.fill(self.BackGroundColor)

        for rect in self.rects:
            pygame.draw.rect(self.WIN, self.rects[rect[1]], self.rects[rect[0]])

        for c_object in self.custom_objects:
            self.WIN.blit(self.custom_objects[c_object[0]], self.custom_objects[c_object[1]])

        for text in self.texts:
            self.WIN.blit(self.texts[text[0]], self.texts[text[1]])

        pygame.display.update()
