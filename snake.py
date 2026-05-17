import pygame, sys, random
pygame.init()

cell_size = 20
cell_number = 20
screen_width = cell_number * cell_size
screen_height = cell_number * cell_size
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
snake_body = [(10, 10), (9, 10), (8, 10)]
direction = (1, 0)  # Start moving to the right
food_position = (random.randint(0, cell_number - 1), random.randint(0, cell_number - 1))
color_bg = (175, 215, 70)
color_snake = (0, 100, 0)
color_food = (200, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    # Move the snake
    new_head = (snake_body[0][0] + direction[0], snake_body[0][1] + direction[1])
    snake_body.insert(0, new_head)

    # Check for food collision
    if new_head == food_position:
        food_position = (random.randint(0, cell_number - 1), random.randint(0, cell_number - 1))
    else:
        snake_body.pop()  # Remove the tail

    # Check for collisions with walls or self
    if (new_head[0] < 0 or new_head[0] >= cell_number or
        new_head[1] < 0 or new_head[1] >= cell_number or
        new_head in snake_body[1:]):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(color_bg)
    for segment in snake_body:
        pygame.draw.rect(screen, color_snake, (segment[0] * cell_size, segment[1] * cell_size, cell_size, cell_size))
    pygame.draw.rect(screen, color_food, (food_position[0] * cell_size, food_position[1] * cell_size, cell_size, cell_size))

    pygame.display.flip()
    clock.tick(5)  # Control the speed of the game