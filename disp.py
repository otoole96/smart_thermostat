import pygame, sys, random
import main_globals

pygame.init()
main_globals.init()

# --------------------------------------------
#   Some definitions
# --------------------------------------------
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320
GRID_X = SCREEN_WIDTH / 4
GRID_Y = SCREEN_HEIGHT / 4
TILES = 16
SPACE = 10
# Color
BLACK = (0, 0, 0)
DARK_GRAY = (145, 145, 145)
GRAY = (175, 175, 175)
BLUE_GRAY = (200, 220, 240)
LIGHT_GRAY = (232, 232, 232)

# ---------------------------------------------------
#    Variables
# ---------------------------------------------------
small_font = pygame.font.SysFont(None, 24)
large_font = pygame.font.SysFont(None, 200)
medium_font = pygame.font.SysFont(None,42)


# --------------------------------------------
#   Screen initialization
# --------------------------------------------
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Thermostat Display")
screen.fill(LIGHT_GRAY)
# Triangles
up_arr = pygame.draw.polygon(screen, BLUE_GRAY, ((360, 80), (420, 150), (300, 150)))
down_arr = pygame.draw.polygon(screen, BLUE_GRAY, ((360, 240), (420, 170), (300, 170)))

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
    screen.fill(LIGHT_GRAY)
    # Buttons
    pygame.draw.polygon(screen, BLUE_GRAY, ((360, 80), (420, 150), (300, 150)))
    pygame.draw.polygon(screen, BLUE_GRAY, ((360, 240), (420, 170), (300, 170)))
    # Outside Temp Label
    disp_text(screen, small_font, 'Outside:', DARK_GRAY, (80, 260))
    # Outside Temp
    disp_text(screen, medium_font, str(main_globals.outside_t), BLACK, (145, 260))
    # Inside Temp Label
    disp_text(screen, small_font, 'Temperature:', DARK_GRAY, (75, 50))
    # Deg Symbol
    disp_text(screen, small_font, 'o', BLACK, (215, 90))
    # Temp Unit
    disp_text(screen, small_font, 'F', BLACK, (215, 185))
    # Inside Temp
    disp_text(screen, large_font, str(main_globals.inside_t), BLACK, (120, 150))
    # Setpoint Label
    disp_text(screen, small_font, 'Set:', DARK_GRAY, (320, 40))
    # Setpoint Display
    disp_text(screen, medium_font, str(main_globals.user_setpoint), DARK_GRAY, (400, 40))
    # AC label
    disp_text(screen, small_font, 'AC:', DARK_GRAY, (270, 280))
    # Furnace label
    disp_text(screen, small_font, 'Furnace:', DARK_GRAY, (390, 280))

    if main_globals.ac == 1:
        disp_text(screen, small_font, 'ON', DARK_GRAY, (300, 280))
    if main_globals.heat == 1:
        disp_text(screen, small_font, 'ON', DARK_GRAY, (440, 280))


def ui_main():
    # --------------------------------------------
    #   Main Loop
    # --------------------------------------------
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

