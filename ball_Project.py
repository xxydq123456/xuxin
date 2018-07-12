import pygame
import sys
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("打砖块")
# 定义小球初始坐标
ball_x = 200
ball_y = 100
# 定义小球颜色
ball_color = (255, 0, 0)
# 定义小球半径
ball_r = 50
# 定义小球方向
ball_direction = 0
# 定义小球速度
ball_speed = 10
clock = pygame.time.Clock()
d =200
score = 0
while True:
    clock.tick(60)
    screen.fill((125, 198, 125))
    my_font = pygame.font.SysFont("隶书", 10)
    font_surface = my_font.render("得分:%d" % score, True, (255, 0, 0),(600,500))
    # 定义有个挡板的坐标
    x, y = pygame.mouse.get_pos()
    # 定义挡板的宽度
    baffle_d = 100
    # 画小球
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_r)
    # 小球的运动
    #画挡板
    pygame.draw.line(screen,(ball_color),(x,500),(x+d,500),10)
    if ball_direction == 0:# 小球左下
        ball_x -= ball_speed
        ball_y += ball_speed
    if ball_x - ball_r <= 0:# 小球撞击左边
        if ball_direction == 0:
            ball_direction = 1
        else:
            ball_direction = 2
    if ball_direction == 1:# 右下
        ball_x += ball_speed
        ball_y += ball_speed
    if ball_y + ball_r >= 500:# 下边
     if  ball_x-ball_r >= x-d and ball_x +ball_r <= x+d:
         # 挡板接住小球一次 的 5分
         score += 5
         # 每得20分速度加1
         # screen.blit(font_surface, score)
         # print(score)
         if score % 20 == 0:
             ball_speed += 1
         if score % 40 == 0:
             d -= 20
             # 每撞击一次改变一次颜色
         r = random.randint(0, 255)
         g = random.randint(0, 255)
         b = random.randint(0, 255)
         ball_color = (r, g, b)
         if ball_direction == 1:
           ball_direction = 2
         else:
            ball_direction = 3
    if ball_direction == 2:# 右上
        ball_x += ball_speed
        ball_y -= ball_speed
    if ball_x + ball_r >= 800:# 右边
        if ball_direction == 2:
            ball_direction = 3
        else:
            ball_direction = 0

    if ball_direction == 3:# 左上
        ball_x -= ball_speed
        ball_y -= ball_speed
    if ball_y - ball_r <= 0:# 上边
        if ball_direction == 3:
            ball_direction = 0
        else:
            ball_direction = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()
pygame.quit()
