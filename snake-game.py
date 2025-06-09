import pygame
import random

pygame.init()

square_width = 750
pixel_width = 50
screen = pygame.display.set_mode([square_width, square_width])
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
running = True

def generate_starting_position():
    position_range = range(pixel_width // 2, square_width, pixel_width)
    return [random.choice(position_range), random.choice(position_range)]

snake_pixel = pygame.Rect(0, 0, pixel_width - 2, pixel_width - 2)
snake_pixel.center = generate_starting_position()
snake = [snake_pixel.copy()]
snake_direction = (0, 0)
snake_length = 1

target = pygame.Rect(0, 0, pixel_width - 2, pixel_width - 2)
target.center = generate_starting_position()

def is_out_of_bounds():
    return (
        snake_pixel.left < 0 or
        snake_pixel.right > square_width or
        snake_pixel.top < 0 or
        snake_pixel.bottom > square_width
    )

while running:
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and snake_direction != (0, pixel_width):
                snake_direction = (0, -pixel_width)
            elif event.key == pygame.K_s and snake_direction != (0, -pixel_width):
                snake_direction = (0, pixel_width)
            elif event.key == pygame.K_a and snake_direction != (pixel_width, 0):
                snake_direction = (-pixel_width, 0)
            elif event.key == pygame.K_d and snake_direction != (-pixel_width, 0):
                snake_direction = (pixel_width, 0)

    if snake_direction != (0, 0):
        snake_pixel.move_ip(snake_direction)
        snake.append(snake_pixel.copy())
        snake = snake[-snake_length:]

    if snake_pixel.colliderect(target):
        target.center = generate_starting_position()
        snake_length += 1

    if is_out_of_bounds():
        snake_length = 1
        snake_pixel.center = generate_starting_position()
        snake = [snake_pixel.copy()]
        snake_direction = (0, 0)
        target.center = generate_starting_position()

    for part in snake:
        pygame.draw.rect(screen, "green", part)
    pygame.draw.rect(screen, "red", target)

    pygame.display.flip()
    clock.tick(10)

pygame.quit()