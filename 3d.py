import sys
from math import *
from random import randint

import os
import pygame
from pygame.locals import *
from pygame.math import *

# 窗口大小
SCREEN_SIZE = (840, 680)
# 正方体边长
CUBE_SIZE = 300

# pygame 初始化
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
screen = pygame.display.set_mode(SCREEN_SIZE, vsync=True)
font = pygame.font.SysFont("SimHei", 24)
clock = pygame.time.Clock()

# 让pygame完全控制鼠标
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)
# 3D points（所有的小球都在这）
points = []
fov = 90.  # 视野
rov = 5
mov = 90
FPS = 60
is_grab = True


def calculate_viewing_distance(fov_s, screen_width):
    d = (screen_width / 2.0) / tan(fov_s / 2.0)
    return d


def set_points():
    # 边沿的一系列点
    for x in range(0 - 20 * 5, CUBE_SIZE + 1 + 20 * 5, 20):
        edge_x = x == 0 or x == CUBE_SIZE

        for y in range(0 - 20 * 5, CUBE_SIZE + 1 + 20 * 5, 20):
            edge_y = y == 0 or y == CUBE_SIZE

            for z in range(0 - 20 * 5, CUBE_SIZE + 1 + 20 * 5, 20):
                edge_z = z == 0 or z == CUBE_SIZE

                if sum((edge_x, edge_y, edge_z)) >= 2:
                    point_x = float(x) - CUBE_SIZE / 2
                    point_y = float(y) - CUBE_SIZE / 2
                    point_z = float(z) - CUBE_SIZE / 2

                    points.append(Vector3(point_x, point_y, point_z))
    # 随机给一些点
    for i in range(10):
        point_x = randint(0 - CUBE_SIZE, CUBE_SIZE + 1 + CUBE_SIZE)
        point_y = randint(0 - CUBE_SIZE, CUBE_SIZE + 1 + CUBE_SIZE)
        point_z = randint(0 - CUBE_SIZE, CUBE_SIZE + 1 + CUBE_SIZE)
        points.append(Vector3(point_x, point_y, point_z))
    points.sort(key=lambda p: p.z, reverse=True)


def move_points(dv):
    for p in points:
        p.update(p + dv)
    points.sort(key=lambda p_s: p.z, reverse=True)


def rotate_points(p_float, v):
    for p in points:
        p.update(p.rotate(p_float, v))
    points.sort(key=lambda p_s: p.z, reverse=True)


def run():
    global fov, is_grab
    # 视距
    viewing_distance = calculate_viewing_distance(radians(fov), SCREEN_SIZE[0])

    set_points()

    center_x, center_y = SCREEN_SIZE
    center_x /= 2
    center_y /= 2

    ball_w, ball_h = 50, 50
    ball_center_x = ball_w / 2
    ball_center_y = ball_h / 2

    camera_position = Vector3(0.0, 0.0, 0.0)  # 摄像机位置
    # camera_speed = Vector3(30.0, 30.0, 30.0)  # 摄像机速度

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            # 按Esc则退出游戏
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        screen.fill((0, 0, 0))
        pressed_keys = pygame.key.get_pressed()
        # pressed_mouse = pygame.mouse.get_pressed()
        # movement_direction = 0.  # 鼠标偏移量
        if is_grab:
            mouse_rel = pygame.mouse.get_rel()
            drx = mouse_rel[0] * 2 * rov
            dry = mouse_rel[1] * 2 * rov
        else:
            drx, dry = 0, 0
        dx, dy, dz = 0.0, 0.0, 0.0

        # 旋转
        # 绕y轴旋转
        rotate_points(drx * 1 / FPS, Vector3(0.0, -1.0, 0.0))
        # 绕x轴旋转
        rotate_points(dry * 1 / FPS, Vector3(-1.0, 0.0, 0.0))

        if pressed_keys[K_a]:
            dx = +mov * 1 / FPS
        elif pressed_keys[K_d]:
            dx = -mov * 1 / FPS

        if pressed_keys[K_w]:
            dz = -mov * 1 / FPS
        elif pressed_keys[K_s]:
            dz = +mov * 1 / FPS

        if pressed_keys[K_SPACE]:
            dy = -mov * 1 / FPS
        elif pressed_keys[K_LCTRL]:
            dy = +mov * 1 / FPS

        if pressed_keys[K_BACKQUOTE] and is_grab:
            pygame.mouse.set_visible(True)
            pygame.event.set_grab(False)
            is_grab = False
        elif pressed_keys[K_BACKQUOTE]:
            pygame.mouse.set_visible(False)
            pygame.event.set_grab(True)
            is_grab = True

        if pressed_keys[K_o]:
            fov = min(179., fov + 1.)
            w = SCREEN_SIZE[0]
            viewing_distance = calculate_viewing_distance(radians(fov), w)
        elif pressed_keys[K_l]:
            fov = max(1., fov - 1.)
            w = SCREEN_SIZE[0]
            viewing_distance = calculate_viewing_distance(radians(fov), w)

        move_points(Vector3(dx, dy, dz))

        # 绘制点
        for point in points:
            x, y, z = point - camera_position
            if z > 0:
                x = x * viewing_distance / z
                y = -y * viewing_distance / z
                x += center_x
                y += center_y
                bw = min(100 / point.magnitude() * ball_w, center_x)
                # screen.blit(ball, (x - ball_center_x, y - ball_center_y))
                pygame.draw.circle(
                    screen,
                    (255, 0, 0),
                    (int(x - ball_center_x), int(y - ball_center_y)),
                    int(bw)
                )

        # 绘制表
        diagram_width = SCREEN_SIZE[0] / 4
        col = (50, 255, 50)
        diagram_points = [(diagram_width / 2, 100 + viewing_distance / 4), (0, 100), (diagram_width, 100),
                          (diagram_width / 2, 100 + viewing_distance / 4), (diagram_width / 2, 100)]
        pygame.draw.lines(screen, col, False, diagram_points, 2)

        # 绘制文字
        white = (255, 255, 255)
        cam_text = font.render("摄像机 = " + str(camera_position), True, white)
        screen.blit(cam_text, (5, 5))
        fov_text = font.render("视野 = %i" % int(fov), True, white)
        screen.blit(fov_text, (5, 35))
        txt = "视距 = %.3f" % viewing_distance
        d_text = font.render(txt, True, white)
        screen.blit(d_text, (5, 65))

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    run()
