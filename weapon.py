import pygame
import math


class Weapon():
    def __init__(self, image):
        self.original_image = image
        self.angel = 0
        self.image = pygame.transform.rotate(self.original_image, self.angel)
        self.rect = self.image.get_rect()

    def update(self, player):
        self.rect.center = player.rect.center
        pos = pygame.mouse.get_pos()
        x_dist = pos[0] - self.rect.centerx
        # negative cuz' pygame coordinates increases down the screen
        y_dist = -(pos[1] - self.rect.centery)
        self.angel = math.degrees(math.atan2(y_dist, x_dist))

    def draw(self, surface):
        self.image = pygame.transform.rotate(self.original_image, self.angel)
        surface.blit(
            self.image, ((self.rect.centerx - int(self.image.get_width() / 2)), self.rect.centery - int(self.image.get_height() / 2)))
