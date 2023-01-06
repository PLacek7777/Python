import pygame
import sys
from network import Network

width = 500
height = 500

#Window Setup
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
#Network Variables
clientNum = 0

#Player Class
class Player:

    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = (x, y, width, height)
        self.vel = 3.5

    def draw(self, win):
        pygame.draw.rect(win, self.colour, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
            
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
            
        if keys[pygame.K_DOWN]:
            self.y += self.vel
            
        if keys[pygame.K_UP]:
            self.y -= self.vel

        self.rect = (self.x, self.y, self.width, self.height)

#Funcion For Updating The Window            
def redrawWin(win, player):
    win.fill((255,255,255))
    player.draw(win)
    pygame.display.update()

def main():
    run = True

    n = Network()
    startPos = n.get_pos()

    p = Player(50, 50, 100, 100, (0, 255, 0))
    clock = pygame.time.Clock()

    #Main Game Loop
    while run:
        clock.tick(60)
        for event in pygame.event.get():

            #Checking For Events

            if event == pygame.QUIT:
                run = False
                print("EXIT")
                sys.exit()

        p.move()
        redrawWin(win, p)

#Starting The Game
main()
