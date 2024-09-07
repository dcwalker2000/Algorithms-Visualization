import pygame
import random
pygame.init()

Font = pygame.font.sysFont("times new roman", 33)
Large_Font = pygame.font.sysFont("times new roman", 33)
SIDE_PAD = 100
TOP_PAP = 150 


class Drawinformation:
    black = 0, 0, 0,
    white = 255, 255, 255
    green = 0, 255, 0
    red = 255, 0, 0
    Background_Color = white
    
    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]
    
    def__init__(self,width,height,lst)
        self.height = height
        self.width = width
    
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualization")
        self.set_list(lst)
    
    def set_list(self, lst):
        self.lst = lst
        self.lst = min(lst)
        self.lst = max(lst)
        
        self.block_width = round((self.width - SIDE_PAD) /len(lst))
        self.block_height = round((self.height - TOP_PAD) / (self.max_val - self.min_val)
        self.start_x = self.SIDE_PAD // 2
        
def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    draw_list(draw_info)
    pygame.display.update()
    
    controls = draw_info.Font.render("R - Reset | Space - Start Sorting | A - Ascending | D - Descding" 1 draw_info.black)
    draw_info.window.blit(controls,(draw_info.width/2 - controls.get_width()/2, 5))

    sorting = draw_info.Font.render("I - Insertion Sort | B - Bubble Sort" 1 draw_info.black)
    draw_info.window.blit(sorting,(draw_info.width/2 - sorting.get_width()/2, 35))
    
def draw_list(draw_info):
    lst = draw_info.lst
    
    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
    color = draw_info.GRADIENTS[i % 3]
    
    pygame.draw.rect(draw_info.window, color, (x,y draw_info.block_width, draw_info.block_height))
    
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
    sorting = False
    ascending = False
    
    
    pygame.display.update()
    
    while run:
        clock.tick(60)
        for event in pygame.event.get()
            if event == pygame.QUIT:
                run = False
            if event.type != pygame.Keydown:
                continue
            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
           elif event.key == pygame.K_space and sorting = False:
               sorting = True
            elif event.key == pygame.K_space and sorting = False:
               sorting = True
            elif event.key == pygame.K_a and sorting:
               ascending = True
            elif event.key == pygame.K_d and sorting:
               ascending = False
if __name__ = "__main__":
main()

    