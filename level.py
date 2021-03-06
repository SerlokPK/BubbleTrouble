import random

from level_constants import *
import pygame


class Level:
    def __init__(self):
        self.currentLevel = 1

    def restart_level(self, player1, player2, bubble):
        return self.set_positions(player1, player2, bubble)

    def start_next_level(self, player1, player2, bubble):
        self.currentLevel += 1
        return self.set_positions(player1, player2, bubble)

    # set positions of every object in window
    def set_positions(self, player1, player2, bubble):
        bubble.my_bubbles = []
        player1.projectile.alive = False
        player1.projectile.hitbox = (0, 0, 0, 0)
        player1.projectile.xPosition = -20
        player1.projectile.yPosition = -20
        player1.velocity = 10
        player2.projectile.alive = False
        player2.projectile.hitbox = (0, 0, 0, 0)
        player2.projectile.xPosition = -20
        player2.projectile.yPosition = -20
        player2.velocity = 10

        if player1.lives == 0 and player2.lives == 0:
            self.currentLevel = 1
            player1.lives = 3
            player2.lives = 3

        if self.currentLevel == 1:
            if player1.lives > 0:
                player1.xPosition = L1_P1_xPOSITION
                player1.yPosition = L1_P1_yPOSITION
            if player2.lives > 0:
                player2.xPosition = L1_P2_xPOSITION
                player2.yPosition = L1_P2_yPOSITION
            bubble.positionOfBall = L1_BUBBLE_POSITION
            img = pygame.image.load('Images/transparentBall.png')
            bubble.init_ball(L1_NUMBER_OF_BALLS, 4, 81, 10, img)
            image = L1_IMAGE
        elif self.currentLevel == 2:
            if player1.lives > 0:
                player1.xPosition = L2_P1_xPOSITION
                player1.yPosition = L2_P1_yPOSITION
            if player2.lives > 0:
                player2.xPosition = L2_P2_xPOSITION
                player2.yPosition = L2_P2_yPOSITION
            bubble.positionOfBall = L2_BUBBLE_POSITION
            img = pygame.image.load('Images/yellow_ball.gif')
            bubble.init_ball(L2_NUMBER_OF_BALLS, 3, 61, 8, img)
            image = L2_IMAGE
        elif self.currentLevel == 3:
            if player1.lives > 0:
                player1.xPosition = L3_P1_xPOSITION
                player1.yPosition = L3_P1_yPOSITION
            if player2.lives > 0:
                player2.xPosition = L3_P2_xPOSITION
                player2.yPosition = L3_P2_yPOSITION
            bubble.positionOfBall = L3_BUBBLE_POSITION
            img = pygame.image.load('Images/orange_ball.gif')
            bubble.init_ball(L3_NUMBER_OF_BALLS, 5, 101, 12, img)
            image = L3_IMAGE
        elif self.currentLevel == 4:
            if player1.lives > 0:
                player1.xPosition = L4_P1_xPOSITION
                player1.yPosition = L4_P1_yPOSITION
            if player2.lives > 0:
                player2.xPosition = L4_P2_xPOSITION
                player2.yPosition = L4_P2_yPOSITION
            bubble.positionOfBall = L4_BUBBLE_POSITION
            img = pygame.image.load('Images/green_ball.gif')
            bubble.init_ball(L4_NUMBER_OF_BALLS, 3, 61, 8, img)
            image = L4_IMAGE
        elif self.currentLevel == 5:
            if player1.lives > 0:
                player1.xPosition = L5_P1_xPOSITION
                player1.yPosition = L5_P1_yPOSITION
            if player2.lives > 0:
                player2.xPosition = L5_P2_xPOSITION
                player2.yPosition = L5_P2_yPOSITION
            bubble.positionOfBall = L5_BUBBLE_POSITION
            img = pygame.image.load('Images/orange_ball.gif')
            bubble.init_ball(L5_NUMBER_OF_BALLS, 7, 141, 16, img)
            image = L5_IMAGE
        else:
            if player1.lives > 0:
                player1.xPosition = random.randint(16, 860)
                player1.yPosition = L5_P1_yPOSITION  # Y coordinate is always 663 for players
            if player2.lives > 0:
                player2.xPosition = random.randint(16, 860)
                player2.yPosition = L5_P2_yPOSITION
            bubble.positionOfBall = (random.randint(100, 600), 50)
            img = [pygame.image.load('Images/yellow_ball.gif'),
                   pygame.image.load('Images/orange_ball.gif'),
                   pygame.image.load('Images/green_ball.gif'),
                   pygame.image.load('Images/transparentBall.png')]
            bubble.init_ball(L1_NUMBER_OF_BALLS, 10, 201, 22, img[random.randint(0, 3)])

            if self.currentLevel % 5 == 1:
                image = L1_IMAGE
            elif self.currentLevel % 5 == 2:
                image = L2_IMAGE
            elif self.currentLevel % 5 == 3:
                image = L3_IMAGE
            elif self.currentLevel % 5 == 4:
                image = L4_IMAGE
            else:
                image = L5_IMAGE

        return image
