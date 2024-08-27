import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1300,72))
pygame.display.set_caption('UDDERWORLD')

# Load the background image
background_image = pygame.image.load('background.png').convert()

# OOP TEXT CLASS
class Text():
    def __init__(self, text, x, y, color, font):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.font = font
        
        self.text_surf = self.font.render(self.text, True, self.color)
        self.rect = self.text_surf.get_rect(mbottom = (self.x, self.y))

     # DISPLAY TEXT METHOD
    def draw(self):
        """
        Draw the text on the given surface.

        :param surface: The surface on which to draw the text.
        """
        screen.blit(self.text_surf, self.rect)

    # Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Draw the text on top of the background
    #text_obj.draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
   
        