import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1300, 720))
pygame.display.set_caption('UDDERWORLD')

# Load the background image once outside the loop
background_image = pygame.image.load('background.png').convert()

# Font colors
orange = (255, 69, 0)

# LOOPS

mainMenu_loop = True
login_loop = False
controls_loop = False

# TEXT FONT AND TEXT DEFINITIONS
subtitle_font = pygame.font.Font('pixelFont.ttf', 80)
button_font = pygame.font.Font('pixelFont.ttf', 75)

# OOP TEXT CLASS
class Text:
    def __init__(self, text, x, y, color, font):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.font = font
        
        self.text_surf = self.font.render(self.text, True, self.color)
        self.rect = self.text_surf.get_rect(midtop=(self.x, self.y))

    # DISPLAY TEXT METHOD
    def draw(self):
        # Draw the text on the given surface
        screen.blit(self.text_surf, self.rect)

# OOP BUTTON CLASS - SUBCLASS OF TEXT CLASS (inherits)
class Button(Text):
    # INITIALISING
    def __init__(self, text, x, y, color, font):
        super().__init__(text, x, y, color, font)
        self.clicked = False

    # IF CLICKED METHOD
    def check_if_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.clicked = True
        # if not clicked, returns as false
        return self.clicked

# BUTTON OBJECTS & SUBTITLE
login_button = Button('LOGIN', 650, 300, orange, button_font)
controls_button = Button('CONTROLS', 650, 400, orange, button_font)
exit_button = Button('EXIT', 650, 500, orange, button_font)
login_subtitle = Text('LOGIN', 650, 275, orange, subtitle_font)
create_account_button = Button('create an account', 650, 550, orange, button_font)
create_account_subtitle = Text('CREATE AN ACCOUNT', 650, 275, orange, subtitle_font)
#mainMenu_subtitle = Text('MENU', 650, 275, orange, subtitle_font)

# Game loop
while mainMenu_loop:
    # Fill the background
    screen.blit(background_image, (0, 0))

    # Draw the buttons and subtitle
    login_button.draw()
    controls_button.draw()
    exit_button.draw()
    #mainMenu_subtitle.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainMenu_loop = False
        # Correct key checking
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:  # Check if the ESC key is pressed
            mainMenu_loop = False
        # Check if the exit button was clicked
        if exit_button.check_if_clicked(event):
            mainMenu_loop = False
        if login_button.check_if_clicked(event):
            mainMenu_loop = False
            login_loop = True
    
    pygame.display.update()

while login_loop:
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            login_loop = False
            mainMenu_loop = False

    login_subtitle.draw()
    # (add user and pass box in this screen)
    create_account_button.draw()

    pygame.display.update()
    clock.tick(60)
        #if

# CREATE ACCOUNT LOOP HERE

    # Update the display
    pygame.display.update()

    # Frame rate
    clock.tick(60)

pygame.quit()
