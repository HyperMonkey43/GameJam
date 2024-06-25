import pygame
import random
import game
import button

def staticloadEntities():
    global PlayBtn, ControlsBtn, QuitBtn

# Before Starting the Game
game = game.Game()
staticloadEntities()
while True:
    while game.startMenu:       
        game.startMenu()
    
    game.getEvent()

    game.update()
    game.clock.tick(60)

 