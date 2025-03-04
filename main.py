import pygame
import sys
import colors
import config  # Import the config module
import shapes
import random



def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def main():
    col1 = 0
    col2 = 0
    col3 = 255
    
    col1_ = True
    col2_ = False
    col3_ = False
    
    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock object

    shapes_list = []
    
    running = True
    while running:
        running = handle_events()
        screen.fill(colors.WHITE)  # Use color from config
        
        # Draw on the screen
        shape_type = random.randrange(3)
        

        if shape_type == 0:
            new_shape = {
                'type': 'circle',
                'color': (col1, col2, col3,),
                'pos': (random.randrange(config.WINDOW_WIDTH), random.randrange(config.WINDOW_HEIGHT)),
                'radius': 50
            }
        elif shape_type == 1:
            new_shape = {
                'type': 'rect',
                'color': (col1, col2, col3),
                'pos': (random.randrange(config.WINDOW_WIDTH - 100), random.randrange(config.WINDOW_HEIGHT - 100)),
                'width': 100,
                'height': 100
            }
        elif shape_type == 2:
            
            new_shape = {
                'type': 'line',
                'color': (col1, col2, col3),
                'pos1': (random.randrange(config.WINDOW_WIDTH), random.randrange(config.WINDOW_HEIGHT)),
                'pos2': (random.randrange(config.WINDOW_WIDTH), random.randrange(config.WINDOW_HEIGHT)),
                'width': 10
            }

        
        if col1_:
            col1 += 1
            col3 -= 1
            if col1 == 255:
                col1_ = False
                col2_ = True
        
        elif col2_:
            col2 += 1
            col1 -= 1
            if col2 == 255:
                col2_ = False
                col3_ = True

        elif col3_:
            col3 += 1
            col2 -= 1
            if col3 == 255:
                col3_ = False
                col1_ = True
        
        

        shapes_list.append(new_shape)

        for shape in shapes_list:
            if shape['type'] == 'circle':
                shapes.draw_circle(screen, shape)
            
            elif shape['type'] == 'rect':
                shapes.draw_rect(screen, shape)
           
            elif shape['type'] == 'line':
                shapes.draw_line(screen, shape)
    
        pygame.display.flip()
        # Limit frame rate to certain number of frames per second (FPS)
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
