import pygame
import random
from pygame.locals import *
from ball import *

pygame.init()

screen_info = pygame.display.Info()
# screen_size = (screen_info.current_w, screen_info.current_h)

# set size
size = (width, height) = (850, 480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (98, 26, 255)

# ball
balls = []

def main():
    for i in range(4):
        balls.append(Ball((width / 2, height / 2)))
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        screen.fill(color)
        for ball in balls:
            ball.update()
        for ball in balls:
            ball.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()
