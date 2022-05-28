import pygame
import random

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
cloud = pygame.image.load('chmurka_01.png')
cloud_x, cloud_y = 0, 0
myfont = pygame.font.SysFont('Tahoma', 60)

rects = [[random.randint(0, 800), 0, True] for _ in range(0, 10)]
count = 10

end_displayed = 0
running = True
while running:
    screen.fill((0, 0, 0));
    # ZDARZENIA
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            poz_x, poz_y = event.pos[0], event.pos[1]
            print(poz_x, poz_y)
            for rect in rects:
                if rect[0] <= poz_x <= rect[0] + 20 and rect[1] <= poz_y <= rect[1] + 20:
                    # uderzenie w kwadracik
                    print("hit")
                    rect[-1] = False
                    count -= 1
                    print("count", count)
                    break  # tylko1 znika

    if count == 0:
        textsurface = myfont.render("Wygrales", True, (255, 255, 255))
        screen.blit(textsurface, (0, 0))
        end_displayed += 1

    if count > 0:
        for rect in rects:
            if rect[1] > 600:
                textsurface = myfont.render("Przegrales", True, (255, 255, 255))
                screen.blit(textsurface, (0, 0))
                end_displayed += 1

    if end_displayed >= 180:  # 3sekundy
        running = False

    # LOGIKA
    screen.blit(cloud, (cloud_x, cloud_y))
    cloud_x += 1
    for rect in rects:
        if rect[-1]:  # MINUS PIERWSZY INDEX
            pygame.draw.rect(screen, (255, 0, 0), (rect[0], rect[1], 20, 20))
        rect[0] += random.randint(-1, 1)
        if rect[0] >= 800:
            rect[0] += 1
        if rect[0] <= 20:
            rect[0] += 1
        rect[1] += 1

    # UPDATE
    pygame.display.update()

    clock.tick(60)
pygame.quit()
