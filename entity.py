import pygame
import time




class Entity:
    texture = None
    rect = None
    attackRect = pygame.Rect(0, 0, 0, 0)
    scrollSpeed = 3

    invertSprite = False


    def __init__(self, size, texturePath, position, opaque, entityType="None"):
        self.rect = pygame.Rect(position, size)

        if len(texturePath) > 0 :
            if not opaque:
                self.texture = pygame.image.load(texturePath)
            elif opaque:
                self.texture = pygame.image.load(texturePath).convert_alpha()    

    def getImage(self, spriteSheet, width, height, scale, color, frame):
        image = pygame.Surface((width, height)).convert_alpha()        
        image.blit(spriteSheet, (0, 0), ((frame * width), 0, width, height))    
       
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image
    

    def invert(self, player):
        if self.rect.x > player.rect.x:
            self.invertSprite = True
        else:
            self.invertSprite = False

        if self.invertSprite:
            self.texture = pygame.transform.flip(self.texture, True, False)
            self.texture.set_colorkey((0, 0, 0))
