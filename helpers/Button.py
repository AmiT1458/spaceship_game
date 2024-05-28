import pygame
pygame.init()
main_font = pygame.font.SysFont('Gameplay',50)
screen = pygame.display.set_mode((1200,800))

class Button():
    def __init__(self,image, x_pos,y_pos,text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text_input = text_input
        self.rect = self.image.get_rect(center=(self.x_pos,self.y_pos))
        self.text = main_font.render(self.text_input , True , 'black')
        self.text_rect = self.text.get_rect(center=(self.x_pos,self.y_pos))

    def update(self):
        screen.blit(self.image , self.rect)
        screen.blit(self.text,self.text_rect)

    def checkForInput(self,position):
        if position[0] in range(self.rect.left , self.rect.right) and position[1] in range(self.rect.top , self.rect.bottom):
            return True
        return False

    def changeColor(self,position):
        if position[0] in range(self.rect.left , self.rect.right) and position[1] in range(self.rect.top , self.rect.bottom):
            self.text = main_font.render(self.text_input , True , 'green')

        else:
            self.text = main_font.render(self.text_input , True , 'black')



