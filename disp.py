import pygame, sys, random, os
import main_globals

#os.environ['SDL_VIDEODRIVER'] = 'fbcon'
#os.environ['SDL_FBDEV'] = '/dev/fb1'
#os.environ['SDL_MOUSEDRV'] = 'TSLIB'
#os.environ['SDL_MOUSEDEV'] = '/dev/input/event0'

os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV'      , '/dev/fb1')
os.putenv('SDL_MOUSEDRV'   , 'TSLIB')
os.putenv('SDL_MOUSEDEV'   , '/dev/input/touchscreen')

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
screen = pygame.display.set_mode((480,320))
pygame.display.set_caption('Thermostat')
screen.fill(BLACK)
# Triangles
up_arr = pygame.draw.polygon(screen, GREEN, ((360, 80), (420, 140), (300, 140)))
down_arr = pygame.draw.polygon(screen, GREEN, ((360, 240), (420, 180), (300, 180)))

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
    pygame.draw.polygon(screen, GREEN, ((360, 80), (420, 140), (300, 140)))
    pygame.draw.polygon(screen, GREEN, ((360, 240), (420, 180), (300, 180)))
    # Outside Temp Label
    disp_text(screen, small_font, 'Outside:', DARK_GRAY, (60, 280))
    # Outside Temp
    disp_text(screen, medium_font, str(main_globals.outside_t), DARK_GRAY, (180, 280))
    # Inside Temp Label
    disp_text(screen, small_font, 'Temperature:', DARK_GRAY, (60, 40))
    # Deg Symbol
    disp_text(screen, small_font, 'o', WHITE, (210, 80))
    # Temp Unit
    disp_text(screen, small_font, 'F', WHITE, (210, 240))
    # Inside Temp
    disp_text(screen, large_font, str(main_globals.inside_t), WHITE, (120, 160))
    # Setpoint Label
    disp_text(screen, small_font, 'Set:', DARK_GRAY, (300, 40))
    # Setpoint Display
    disp_text(screen, medium_font, str(main_globals.user_setpoint), DARK_GRAY, (420, 40)
    # AC label
    disp_text(screen, small_font, 'AC:', DARK_GRAY, (270, 280))
    # Furnace label
    disp_text(screen, small_font, 'Heat:', DARK_GRAY, (390, 280))
    # AC and Furnace Indicators
    if main_globals.ac == 1 :
        disp_text(screen, small_font, 'ON', DARK_GRAY, (315, 280))
    if main_globals.heat == 1 :
        disp_text(screen, small_font, 'ON', DARK_GRAY, (435, 280))


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

