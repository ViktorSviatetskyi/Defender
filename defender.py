import pygame, controls
from gun import Gun
from pygame.sprite import Group


def run():
    pygame.init()
    screen = pygame.display.set_mode((900, 900))
    pygame.display.set_caption('Defender')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen,inos)

    while True:
        controls.events(screen, gun, bullets)
        gun.updategun()
        controls.update(bg_color, screen, gun, inos, bullets)
        controls.update_bullets(bullets)
        controls.update_inos(inos)

run()