import pygame
import pygame.locals
import time

class Player(pygame.sprite.Sprite):
    def __init__(self, img, fwd, bwd, cw, ccw, spawnX, spawnY, direction, hasFlag):
        pygame.sprite.Sprite.__init__(self)  # initialising parent class
        self.image = pygame.image.load(img)  # loading sprite
        self.rect = self.image.get_rect()  # getting the size of the image
        self.direction = direction  # declaring the direction of the player
        self.controls = {'forward': fwd, 'backward': bwd, 'clockwise': cw,
                         'counterclockwise': ccw}  # declaring the controls
        self.spawn = {'x': spawnX, 'y': spawnY}  # setting spawn variables
        self.rect.x, self.rect.y = self.spawn['x'], self.spawn['y']  # setting the spawn
        self.hasFlag = hasFlag

    def update(self, keysPressed):
        # ~ Movement ~ #
        self.rect.x += (keysPressed[self.controls['forward']]) * (
            8 if self.direction == 1 else (-8 if self.direction == 3 else 0))
        self.rect.x -= (keysPressed[self.controls['backward']]) * (
            8 if self.direction == 1 else (-8 if self.direction == 3 else 0))

        self.rect.y += (keysPressed[self.controls['forward']]) * (
            8 if self.direction == 2 else (-8 if self.direction == 0 else 0))
        self.rect.y -= (keysPressed[self.controls['backward']]) * (
            8 if self.direction == 2 else (-8 if self.direction == 0 else 0))

        # ~ Direction Changing ~ #

        if keysPressed[self.controls['clockwise']]:
            self.direction += 1
            if self.direction > 3:
                self.direction = 0

        if keysPressed[self.controls['counterclockwise']]:
            self.direction -= 1
            if self.direction < 0:
                self.direction = 3

        # ~ Border Creation ~ #
        self.rect.left = min(max(0, self.rect.left), 800)
        self.rect.right = min(max(0, self.rect.right), 800)
        self.rect.top = min(max(0, self.rect.top), 800)
        self.rect.bottom = min(max(0, self.rect.bottom), 800)

        time.sleep(0.05)

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # drawing the players to the screen

    def getRectX(self):
        return self.rect.x

    def getRectY(self):
        return self.rect.y

    def getHasflag(self):
        return self.hasFlag


class BluePlayer(Player):
    def __init__(self, img, spawnX, spawnY, hasFlag):
        Player.__init__(self, img,
                        pygame.locals.K_w, pygame.locals.K_s,
                        pygame.locals.K_d, pygame.locals.K_a, spawnX, spawnY, 1,
                        hasFlag)  # initialising the parent class


class RedPlayer(Player):
    def __init__(self, img, spawnX, spawnY, hasFlag):
        Player.__init__(self, img,
                        pygame.locals.K_UP, pygame.locals.K_DOWN,
                        pygame.locals.K_RIGHT, pygame.locals.K_LEFT, spawnX, spawnY, 3,
                        hasFlag)  # initialising the parent class