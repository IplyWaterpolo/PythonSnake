import pygame, random, time
s_height = 800
s_width = 800
black = (0,0,0)
red = (255,0,0)
white = (255,255,255)
cx = 0
cy = 0

pygame.display.init()
screen = pygame.display.set_mode([s_height, s_width])
pygame.font.init()
font = pygame.font.SysFont('Comic Sans', 50)
start = True

while start:
    score = 1 #initializes score 
    clock = pygame.time.Clock() #controls the frame rate of the application
    
    class Snake():
        def __init__(self):
            self.x = 400
            self.y = 400

    snake = Snake()
    snakeList = []

    def draw(snakeList):
        for i in snakeList:
            pygame.draw.rect(screen, white, [i[0], i[1], 20, 20])

    def drawFruit():
        drawFruit.x = random.randrange(0,780,20)
        drawFruit.y = random.randrange(0,780,20)
        pygame.draw.rect(screen, red, [drawFruit.x, drawFruit.y, 20, 20])
    
    def eval(): #Evaluates position of snake on screen and controls length of snake
        if snake.x > s_width:
            snake.x = 0
        if snake.x < 0:
            snake.x = 800
        if snake.y > s_height:
            snake.y = 0
        if snake.y < 0:
            snake.y = 800
        if (len(snakeList)) > score:
            del snakeList[0]

    draw(snakeList)
    drawFruit()
    play = True 

    while play:
        pygame.display.update()
        snakeHead = []
        snakeHead.append(snake.x)
        snakeHead.append(snake.y)
        snakeList.append(snakeHead)

        clock.tick(20)
        eval()
        if snake.x == drawFruit.x and snake.y == drawFruit.y:
            drawFruit()
            score += 1
    
        pygame.display.set_caption("Snake Game | Score = "+ str(score-1))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                pygame.display.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    cx = 20
                    cy = 0
                if event.key == pygame.K_LEFT:
                    cx = -20
                    cy = 0
                if event.key == pygame.K_UP:
                    cx = 0
                    cy = -20
                if event.key == pygame.K_DOWN:
                    cx = 0
                    cy = 20
                
        screen.fill(black)
        pygame.draw.rect(screen, red, [drawFruit.x, drawFruit.y, 20, 20])
        snake.x += cx
        snake.y += cy
        draw(snakeList)

        for i in range((len(snakeList)-1)):
            if snakeHead == snakeList[i]:
                text = font.render("Your score was: " + str(score-1), 1, red)
                screen.blit(text, (250,400))
                pygame.display.update()
                time.sleep(3)
                play = False
