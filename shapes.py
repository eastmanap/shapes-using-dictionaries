import pygame

def draw_circle(screen, shape):
    pygame.draw.circle(screen, shape['color'], shape['pos'], shape['radius'])

def draw_rect(screen, shape):
    pygame.draw.rect(screen, shape['color'], (shape['pos'][0], shape['pos'][1], shape['width'], shape['height']))

def draw_line(screen, shape):
    pygame.draw.line(screen, shape['color'], shape['pos1'], shape['pos2'], shape['width'])