import sys
import pygame

pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
color = (0, 0, 0)
ball = pygame.image.load("ball.png")
rect = ball.get_rect()
speed = [5, 5]  # 设置移动的x轴、y轴距离
clock = pygame.time.Clock()  # 设置时钟

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    rect = rect.move(speed)
    if rect.left < 0 or rect.right > width:
        speed[0] = -speed[0]
    if rect.top < 0 or rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(color)
    screen.blit(ball, rect)
    pygame.display.flip()
