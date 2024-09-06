import pygame
import random
pygame.init()


SIDE_PAD = 100
TOP_PAP = 150 


class Drawinformation:
    black = 0, 0, 0,
    white = 255, 255, 255
    green = 0, 255, 0
    red = 255, 0, 0
    grey = 128, 128, 128
    Background_Color = white
    
    def__init__(self,width,height,lst)
        self.height = height
        self.width = width
    
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualization")
        self.set_list(lst)
    
    def set_list(self, lst)
        self.lst = lst
        self.lst = min(lst)
        self.lst = max(lst)
        
        self.block_width = round((self.width - SIDE_PAD) /len(lst))
        self.block_height = round((self.height - TOP_PAD) / (self.max_val - self.min_val)
        self.start_x = self.SIDE_PAD // 2
        
def draw(draw_info):

def generate_starting_list(n, min_val, max_val,):
    lst = []
    
    for _ in range(n):
        val = random.randomint(min_val, max_val)
        lst.append(val)
        
    return lst
    
def main():
    run = True
    clock = pygame,time.Clock
    
    n = 50
    min_val = 0
    max_val = 100
    
    
    lst = generate_starting_list()
    draw_info = DrawInformation(800, 600)
    
    
    pygame.display.update()
    
    while run:
        clock.tick(60)
        for event in pygame.event.get()
            if event == pygame.QUIT:
                run = False
    pygame.quit()
    
if __name__ = "__main__":
main()

    