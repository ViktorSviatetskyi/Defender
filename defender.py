import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats


def run():
    pygame.init()
    screen = pygame.display.set_mode((900, 900))
    pygame.display.set_caption('Defender')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    kuilo = Group()
    controls.create_army(screen, kuilo)
    stats = Stats()

    while True:
        controls.events(screen, gun, bullets)
        gun.updategun()
        controls.update(bg_color, screen, gun, kuilo, bullets)
        controls.update_bullets(screen, kuilo, bullets)
        controls.update_inos(stats, screen, gun, kuilo, bullets)


run()
