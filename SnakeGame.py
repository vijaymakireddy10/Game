import pygame , random

pygame.init()

WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
snake = [(100, 100)]
snake_direction = (1, 0)
score = 0
food = (random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE,random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE) 
font = pygame.font.Font(None, 36) 
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    snake_head = (snake[0][0] + snake_direction[0] * GRID_SIZE, snake[0][1] + snake_direction[1] * GRID_SIZE)
    snake.insert(0, snake_head)
    
    if snake_head == food:
        score= score+1
        food = (random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE, random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE)
    else:
        snake.pop()

    if (snake_head[0] < 0 or snake_head[0] >= WIDTH or snake_head[1] < 0 or snake_head[1] >= HEIGHT) or snake_head in snake[1:]:
        running = False
    
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))
    
    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))
    
    score_text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(score_text, (10, 10)) 
    
    pygame.display.flip()
    clock.tick(5)
pygame.quit()
