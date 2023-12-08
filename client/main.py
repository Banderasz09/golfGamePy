import pygame
from display import Display
from networking import Network
from ui import UI

clock = pygame.time.Clock

class Game(object):
    def connect(self, ip, port):
        pass

onMenu = True

def main():
    run = True

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event == pygame.QUIT:
              run = False

            if pygame.mouse.get_pressed(1) == pygame.MOUSEBUTTONDOWN:
                mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
                if onMenu:
                    eval(Display.get_button(mouse_pos_x, mouse_pos_y))
                

    pygame.quit()  
    
if __name__ == "__main__":
    main()
