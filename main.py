import pygame


class Game:
    gameOver = False
    def start_game(self):
        pygame.init()
        dis = pygame.display.set_mode((400, 300))
        pygame.display.set_caption('Cliff snake xenzia')
        pygame.display.update()

        while not self.gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOver = True
        pygame.quit()
        quit()


my_game = Game()

my_game.start_game()
