import pygame
from display import Display
from networking import Network

clock = pygame.time.Clock

network = Network()

def main():
    run = True

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event == pygame.QUIT:
              run = False
            if pygame.mouse.get_pressed(1) == pygame.MOUSEBUTTONDOWN:
                mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
                

    pygame.quit()  
    
if __name__ == "__main__":
    main()