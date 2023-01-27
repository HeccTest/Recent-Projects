import pygame, time

# https://www.pygame.org/docs/
# snake tutorial: https://www.edureka.co/blog/snake-game-with-pygame/

pygame.init() # initializes all pygame modules

blue = (0,0,255)
red = (255,0,0)
white = (255, 255, 255)
black = (0, 0, 0)

display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
 
pygame.display.set_caption('Snake game')
 
x1 = display_width / 2 # x starting position (half of screen size)
y1 = display_height / 2 # y starting position (half of screen size)
 
x1_change = 0       
y1_change = 0
 
clock = pygame.time.Clock()
frame_rate = 30

font_style = pygame.font.SysFont(None, 50)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [display_width/2 - 50, display_height/2 - 25])

game_over = False
while (game_over != True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True # breaks out of the while loop, ending the game (run the line pygame.quit())
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10
    # pygame.draw.rect(screen,blue,[200,150,10,10]) # draws a rectangle on surface: screen, colour: blue, position: 200,150 (middle of screen), and size: 10,10; a square  
    # pygame.display.update()

    if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
        game_over = True
        message("You lost",red)
        pygame.display.update()
        time.sleep(2)

    x1 += x1_change
    y1 += y1_change
    screen.fill(black)
    pygame.draw.rect(screen, white, [x1, y1, 10, 10])
 
    pygame.display.update()
 
    clock.tick(frame_rate)
pygame.quit()
quit()