import pygame
import sys

# 初始化pygame
pygame.init()

# 设置屏幕尺寸
screen = pygame.display.set_mode((800, 600))

# 设置标题
pygame.display.set_caption("Pong")

# 设置颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 设置球的初始位置和速度
ball_x = 400
ball_y = 300
ball_speed_x = 5
ball_speed_y = 5

# 设置球拍的初始位置
paddle_a_y = 250
paddle_b_y = 250

# 主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 更新球的位置
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 碰撞检测
    if ball_y < 0 or ball_y > 600:
        ball_speed_y *= -1
    if ball_x < 0:
        ball_x = 400
        ball_y = 300
        ball_speed_x *= -1
    elif ball_x > 800:
        ball_x = 400
        ball_y = 300
        ball_speed_x *= -1

    # 检测球拍碰撞
    if ball_x < 50 and paddle_a_y - 100 < ball_y < paddle_a_y + 100:
        ball_speed_x *= -1
    elif ball_x > 750 and paddle_b_y - 100 < ball_y < paddle_b_y + 100:
        ball_speed_x *= -1

    # 绘制屏幕
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (30, paddle_a_y - 100, 20, 200))
    pygame.draw.rect(screen, WHITE, (760, paddle_b_y - 100, 20, 200))
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), 10)

    # 更新屏幕
    pygame.display.flip()
    pygame.time.Clock().tick(60)

    # 监听键盘事件
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_a_y -= 5
    if keys[pygame.K_s]:
        paddle_a_y += 5
    if keys[pygame.K_UP]:
        paddle_b_y -= 5
    if keys[pygame.K_DOWN]:
        paddle_b_y += 5
