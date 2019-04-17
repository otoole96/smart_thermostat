import pygame, sys, random
import main_globals

pygame.init()
main_globals.init()

# --------------------------------------------
#   Some definitions
# --------------------------------------------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Color
BLACK = (0, 0, 0)
DARK_GRAY = (145, 145, 145)
GREEN = (50, 255, 25)
WHITE = (255, 255, 255)

# ---------------------------------------------------
#    Variables
# ---------------------------------------------------
small_font = pygame.font.SysFont(None, 24)
large_font = pygame.font.SysFont(None, 400)
medium_font = pygame.font.SysFont(None,42)


# --------------------------------------------
#   Screen initialization
# --------------------------------------------
#SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode((0,0))
pygame.display.set_caption('Thermostat')
screen.fill(BLACK)
# Triangles
up_arr = pygame.draw.polygon(screen, GREEN, ((600, 150), (700, 290), (500, 290)))
down_arr = pygame.draw.polygon(screen, GREEN, ((600, 450), (700, 310), (500, 310)))

# --------------------------------------------
#   Text Display Function
# --------------------------------------------
def disp_text(surface, font, text, color, center):
    text_rend = font.render(text, True, color)
    text_rect = text_rend.get_rect()
    text_rect.center = center
    surface.blit(text_rend, text_rect)


# --------------------------------------------
#   Redraw the Display
# --------------------------------------------
def update_disp():
    # Clear screen
    screen.fill(BLACK)
    # Buttons
    pygame.draw.polygon(screen, GREEN, ((600, 150), (700, 290), (500, 290)))
    pygame.draw.polygon(screen, GREEN, ((600, 450), (700, 310), (500, 310)))
    # Outside Temp Label
    disp_text(screen, small_font, 'Outside:', DARK_GRAY, (100, 525))
    # Outside Temp
    disp_text(screen, medium_font, str(main_globals.outside_t), DARK_GRAY, (300, 525))
    # Inside Temp Label
    disp_text(screen, small_font, 'Temperature:', DARK_GRAY, (100, 75))
    # Deg Symbol
    disp_text(screen, small_font, 'o', WHITE, (365, 165))
    # Temp Unit
    disp_text(screen, small_font, 'F', WHITE, (365, 375))
    # Inside Temp
    disp_text(screen, large_font, str(main_globals.inside_t), WHITE, (200, 300))
    # Setpoint Label
    disp_text(screen, small_font, 'Set:', DARK_GRAY, (500, 75))
    # Setpoint Display
    disp_text(screen, medium_font, str(main_globals.user_setpoint), DARK_GRAY, (700, 75))
    # AC label
    disp_text(screen, small_font, 'AC:', DARK_GRAY, (450, 525))
    # Furnace label
    disp_text(screen, small_font, 'Heat:', DARK_GRAY, (600, 525))
    # AC and Furnace Indicators
    if main_globals.ac == 1 :
        disp_text(screen, small_font, 'ON', DARK_GRAY, (525, 525))
    if main_globals.heat == 1 :
        disp_text(screen, small_font, 'ON', DARK_GRAY, (700, 525))


def ui_main():
    # --------------------------------------------
    #   Main Loop
    # --------------------------------------------
    print("Entering display main loop.")
    while 1:
        # Run until someone closes the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if up_arr.collidepoint(pos):
                    main_globals.user_setpoint += 1
                elif down_arr.collidepoint(pos):
                    main_globals.user_setpoint -= 1

        # Update Display
        update_disp()
        pygame.display.flip()

