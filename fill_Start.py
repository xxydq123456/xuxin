import pygame
import sys
import random
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("满天星")
# 定义两个类表存放坐标
Start_X = []
Start_Y = []
# 生成500个坐标  迭代遍历0到499
for i in range(500):
    # 随机生成的500个坐标放入到列表中
    Start_X.insert(i, random.randint(0, 800))
    Start_Y.insert(i, random.randint(0, 600))
my_font = pygame.font.SysFont("隶书", 20)
font_surface = my_font.render("*", True,(255, 255, 255))
print(Start_X)
print(Start_Y)
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    screen.fill((0, 0, 0))
    # 将字体显示到窗体中
    for i in range(500):
        screen.blit(font_surface, (Start_X[i], Start_Y[i]))
        # 每个坐标加1
        Start_Y[i] += 1
        # 不同的i控制不同移动距离
        if i % 2 == 0:
            Start_Y[i] += 2
        if i % 3 == 0:
            Start_Y[i] += 3
        if i % 5 == 0:
            Start_Y[i] += 4
        if Start_Y[i] >= 600:
            Start_Y[i] = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()
pygame.quit()