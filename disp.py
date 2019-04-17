import pygame, sys, random
import main_globals

pygame.init()

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
#Display Text
IN_LABEL = 'Temperature:'
OUT_LABEL = 'Outside:'
SET_LABEL = 'Set:'

# ---------------------------------------------------
#    Variables
# ---------------------------------------------------
in_temp = 70
out_temp = 75
setpoint = 69
ac_on = False
furn_on = True
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


# --------------------------------------------
#   Text Display Function
# --------------------------------------------
def disp_text(surface, font, text, color, center):
    text_rend = font.render(text, True, color)
    text_rect = text_rend.get_rect()
    text_rect.center = center
    surface.blit(text_rend, text_rect)


# --------------------------------------------
#   Text Display Function
# --------------------------------------------
def update_disp():
    # Outside Temp
    disp_text(screen, medium_font, str(out_temp), BLACK, (145, 260))
    # Inside Temp
    disp_text(screen, large_font, str(in_temp), BLACK, (120, 150))
    # Setpoint Display
    disp_text(screen, medium_font, str(setpoint), DARK_GRAY, (400, 40))
    if ac_on:
        disp_text(screen, small_font, 'ON', DARK_GRAY, (300, 280))
    if furn_on:
        disp_text(screen, small_font, 'ON', DARK_GRAY, (440, 280))

# --------------------------------------------
#   Draw Initial UI
# --------------------------------------------
# Triangle Buttons
pygame.draw.polygon(screen, BLUE_GRAY, ((360, 80), (420, 150), (300, 150)))
pygame.draw.polygon(screen, BLUE_GRAY, ((360, 240), (420, 170), (300, 170)))
# Outside Temp Label
disp_text(screen, small_font, OUT_LABEL, DARK_GRAY, (80, 260))
# Outside Temp
# disp_text(screen, medium_font, str(out_temp), BLACK, (145, 260))
# Inside Temp Label
disp_text(screen, small_font, IN_LABEL, DARK_GRAY, (75, 50))
# Inside Temp
# disp_text(screen, large_font, str(in_temp), BLACK, (120, 150))
# Deg Symbol
disp_text(screen, small_font, 'o', BLACK, (215, 90))
# Temp Unit
disp_text(screen, small_font, 'F', BLACK, (215, 185))
# AC label
disp_text(screen, small_font, 'AC:', DARK_GRAY, (270, 280))
# Furnace label
disp_text(screen, small_font, 'Furnace:', DARK_GRAY, (390, 280))
# Setpoint Label
disp_text(screen, small_font, 'Set:', DARK_GRAY, (320, 40))
# Setpoint Display
# disp_text(screen, medium_font, str(setpoint), DARK_GRAY, (400, 40))


# --------------------------------------------
#   Main Loop
# --------------------------------------------
while 1:
    # Run until someone closes the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Update Display
    update_disp()
    pygame.display.flip()
