import pygame
import time

class Game:
    gameOver = False
    blue = (0, 0, 255)
    red = (255, 0, 0)
    white = (255, 255, 255)
    dx = 0
    dy = 0
    dis_width = 400
    dis_height = 400
    x = dis_width / 2
    y = dis_height / 2
    snake_block = 10
    snake_speed = 30

    clock = pygame.time.Clock()

    def message(self, msg, color, display, font):
        mesg = font.render(msg, True, color)
        display.blit(mesg, [self.dis_width/3, self.dis_height/2])

    def start_game(self):
        pygame.init()
        dis = pygame.display.set_mode((self.dis_width, self.dis_height))
        pygame.display.set_caption('Cliff\'s snake xenzia')
        pygame.display.update()
        font_style = pygame.font.SysFont(None, 50)

        while not self.gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOver = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.dy = 0
                        self.dx = -10
                    elif event.key == pygame.K_RIGHT:
                        self.dy = 0
                        self.dx = 10
                    elif event.key == pygame.K_UP:
                        self.dx = 0
                        self.dy = -10
                    elif event.key == pygame.K_DOWN:
                        self.dx = 0
                        self.dy = 10
            if self.x >= self.dis_width or self.x < 0 or self.y >= self.dis_height or self.y < 0:
                self.gameOver = True
            self.x += self.dx
            self.y += self.dy
            dis.fill(self.white)
            pygame.draw.rect(dis, self.blue, [self.x, self.y, 10, 10])
            pygame.display.update()
            self.clock.tick(self.snake_speed)

        self.message('You lost', self.red, dis, font_style)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        quit()


my_game = Game()

my_game.start_game()
