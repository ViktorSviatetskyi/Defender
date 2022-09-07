import pygame, sys
from bullet import Bullet
from kuilo import Kuilo
import time


def events(screen, gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gun.mright = True
            elif event.key == pygame.K_LEFT:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gun.mright = False
            elif event.key == pygame.K_LEFT:
                gun.mleft = False


def update(bg_color, screen, gun, kuilo, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    kuilo.draw(screen)
    pygame.display.flip()


def update_bullets(screen, kuilo, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collections = pygame.sprite.groupcollide(bullets, kuilo, True, True)
    if len(kuilo) == 0:
        bullets.empty()
        create_army(screen, kuilo)


def inos_check(stats, screen, gun, kuilo, bullets):
    screen_rect = screen.get_rect()
    for kuilos in kuilo.sprites():
        if kuilos.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, gun, kuilo, bullets)
            break


def create_army(screen, inos):
    kuilo = Kuilo(screen)
    ino_width = kuilo.rect.width
    number_ino_x = int((900 - 2 * ino_width) / ino_width)
    ino_height = kuilo.rect.height
    number_ino_y = int((800 - 100 - 2 * ino_height) / ino_height)

    for row_number in range(number_ino_y - 3):
        for ino_number in range(number_ino_x):
            ino = Kuilo(screen)
            ino.x = ino_width + ino_width * ino_number
            ino.y = ino_height + ino_height * row_number
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_number
            inos.add(ino)


def gun_kill(stats, screen, gun, kuilo, bullets):
    stats.guns_left -= 1
    kuilo.empty()
    bullets.empty()
    create_army(screen, kuilo)
    gun.create_gun()
    time.sleep(1.5)


def update_inos(stats, screen, gun, kuilo, bullets):
    kuilo.update()
    if pygame.sprite.spritecollideany(gun, kuilo):
        gun_kill(stats, screen, gun, kuilo, bullets)
    inos_check(stats, screen, gun, kuilo, bullets)
