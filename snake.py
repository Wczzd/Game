import pygame
import random

# 初始化pygame
pygame.init()

# 设置游戏窗口的大小
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("贪吃蛇")

# 定义颜色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 定义蛇的初始位置和大小
snake_block_size = 20
snake_speed = 10
snake_list = []
snake_length = 1

# 定义蛇的初始位置和移动方向
snake_x = window_width // 2
snake_y = window_height // 2
snake_x_change = 0
snake_y_change = 0

# 定义食物的初始位置
food_x = round(random.randrange(0, window_width - snake_block_size) / snake_block_size) * snake_block_size
food_y = round(random.randrange(0, window_height - snake_block_size) / snake_block_size) * snake_block_size

# 定义分数
score = 0

# 游戏结束标志
game_over = False

# 游戏循环
while not game_over:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_block_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_block_size
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_block_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_block_size
                snake_x_change = 0

    # 更新蛇的位置
    snake_x += snake_x_change
    snake_y += snake_y_change

    # 判断蛇是否吃到食物
    if snake_x == food_x and snake_y == food_y:
        score += 1
        food_x = round(random.randrange(0, window_width - snake_block_size) / snake_block_size) * snake_block_size
        food_y = round(random.randrange(0, window_height - snake_block_size) / snake_block_size) * snake_block_size
        snake_length += 1

    # 游戏结束条件
    if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
        game_over = True

    # 更新游戏窗口
    window.fill(black)
    pygame.draw.rect(window, red, [food_x, food_y, snake_block_size, snake_block_size])
    snake_head = [snake_x, snake_y]
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_head:
            game_over = True

    for x in snake_list:
        pygame.draw.rect(window, white, [x[0], x[1], snake_block_size, snake_block_size])

    pygame.display.update()

    # 设置游戏速度
    pygame.time.Clock().tick(snake_speed)

# 退出pygame
pygame.quit()