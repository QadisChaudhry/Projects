import pygame
import random
import time

pygame.init()

wn = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Pong")
pygame.mouse.set_visible(0)

fps = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)

score_font = pygame.font.Font(None, 30)
start_font = pygame.font.Font(None, 48)
start1_font = pygame.font.Font(None, 30)


def timer():
    now = time.localtime(time.time())
    return now[5]


def start():
    while 1:
        start_render = start_font.render('Welcome to Pong!!', 1, white)
        start1_render = start1_font.render('Press Space to Start', 1, white)
        wn.blit(start_render, (250, 275))
        wn.blit(start1_render, (300, 325))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    exit(0)
                if event.key == pygame.K_SPACE:
                    main()
        pygame.display.flip()
        fps.tick(60)


def main():
    score1 = 0
    score2 = 0

    ball_x = 400
    ball_y = 300
    ball_radius = 6
    ball_dx = random.choice([-5, 5])
    ball_dy = random.choice([-5, 5])

    paddle1_x = 10
    paddle1_y = 250
    paddle2_x = 780
    paddle2_y = 250
    paddle_dy = 10
    paddle_width = 10
    paddle_height = 100

    paddle1_up = 0
    paddle1_down = 0
    paddle2_up = 0
    paddle2_down = 0

    while 1:
        ball_x += ball_dx
        ball_y += ball_dy
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    paddle1_up = 1
                    paddle1_down = 0
                elif event.key == pygame.K_s:
                    paddle1_up = 0
                    paddle1_down = 1
                if event.key == pygame.K_UP:
                    paddle2_up = 1
                    paddle2_down = 0
                elif event.key == pygame.K_DOWN:
                    paddle2_up = 0
                    paddle2_down = 1
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    exit(0)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    paddle1_up = 0
                elif event.key == pygame.K_s:
                    paddle1_down = 0
                if event.key == pygame.K_UP:
                    paddle2_up = 0
                elif event.key == pygame.K_DOWN:
                    paddle2_down = 0

        if paddle1_up:
            paddle1_y -= paddle_dy
        elif paddle1_down:
            paddle1_y += paddle_dy
        if paddle2_up:
            paddle2_y -= paddle_dy
        elif paddle2_down:
            paddle2_y += paddle_dy

        if ball_y < 6:
            ball_dy *= -1
        if ball_y > 594:
            ball_dy *= -1

        if ball_x > 790:
            score1 += 1
            ball_dx = -5
            ball_dy = random.choice([-5, 5])
            ball_x = 400
            ball_y = 300
        if ball_x < 0:
            score2 += 1
            ball_dx = 5
            ball_dy = random.choice([-5, 5])
            ball_x = 400
            ball_y = 300

        if paddle1_y < 0:
            paddle1_y = 0
        if paddle1_y > 500:
            paddle1_y = 500
        if paddle2_y < 0:
            paddle2_y = 0
        if paddle2_y > 500:
            paddle2_y = 500

        if 10 < ball_x < 25 and paddle1_y < ball_y < paddle1_y + 100:
            ball_x = 25
            ball_dx = -ball_dx + 1
        if 775 < ball_x < 790 and paddle2_y < ball_y < paddle2_y + 100:
            ball_x = 775
            ball_dx = -ball_dx - 1

        if ball_dx >= 14:
            ball_dx = 14
        elif ball_dx <= -14:
            ball_dx = -14

        wn.fill(black)
        pygame.draw.rect(wn, white, (paddle1_x, paddle1_y, paddle_width, paddle_height))
        pygame.draw.rect(wn, white, (paddle2_x, paddle2_y, paddle_width, paddle_height))
        pygame.draw.rect(wn, white, (400, 0, 1, 600))
        pygame.draw.circle(wn, white, (ball_x, ball_y), ball_radius)
        score1_render = score_font.render(str(score1), 1, white)
        wn.blit(score1_render, (200, 40))
        score2_render = score_font.render(str(score2), 1, white)
        wn.blit(score2_render, (600, 40))
        pygame.display.flip()
        fps.tick(60)


start()
