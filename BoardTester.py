"""
Jake Martin
Python code to test board graphics using pygame
Created 2020
"""

# Import libraries
import pygame
import random
from point2d import Point2D
import colorsys
from Stocks import get_data
from Characters import char_pts
import time

# Function to create a randomized color tuple
def rand_color()->(int,int,int):
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

# The spiral animation
ring_rad = 1
offs = 0
def spiral(colors, ring_rad, offs):

    for R in range(ring_rad):
        point = Point2D()
        point.polar(r=R/20, a=R)
        x = point.x - 1 + 12
        y = 19 - (point.y - 1 + 10)
        if y % 2 == 1:
            x = 24 - x
        pos = int(25*x + y)#int(x + (25 * y))
        if pos < 25*20 and pos >= 0:
            colors[pos] = colorsys.hsv_to_rgb( ((offs + R) % 256)/255, 255/255, 150/255)
            colors[pos] = (colors[pos][0]*255, colors[pos][1]*255, colors[pos][2]*255)
            offs += 1
        else:
            ring_rad = 1
            break
    ring_rad += 1
    return ring_rad, offs
    for pix in colors:
        hsv = colorsys.rgb_to_hsv(pix[0], pix[1], pix[2])
        pix = colorsys.hsv_to_rgb(hsv[0], hsv[1], max(hsv[2]-5, 0))

# The wow animation
def wow(colors):
    for i in range(25*20):
        colors[i] = rand_color()

# The wow hype animation
def wow_hype(colors):
    for i in range(25*20):
        colors[i] = colorsys.hsv_to_rgb(random.random(), 1, 1) * 2
        colors[i] = (colors[i][0]*255, colors[i][1]*255, colors[i][2]*255)

# The wow2 animation
def wow2(colors):
    col = rand_color()
    for i in range(25*20):
        colors[i] = col

# The wow3 animation
offset = 0
def wow3(colors, off):
    for i in range(25*20):
        colors[i] = (i % 256, (i+off) % 256, (i*off) % 256)
    return off+1

# The stock scroller animation
tickers = [
            ("SPY", "QQQ", "TLT", "GLD", "SLV", "UUP", "USO"),
            ("AAPL", "AMZN", "MSFT", "GOOG", "FB", "TSLA", "NVDA", "NFLX", "AMD"),
            ("BRK.A", "V", "MA", "PYPL", "JPM", "BAC", "C", "GS", "MS")
            ]
refresh_outer = 0
refresh_inner = 0
strs = []
print("~" * 100)
print("Getting stock data...")
print("-" * 50)
for i in range(len(tickers)):
    strs.append("")
    for j in range(len(tickers[i])):
        try:
            c, pc = get_data(tickers[i][j])
            round(c, 2)
            round(pc, 2)
            if c < pc:
                strs[i] += "<"
            elif c > pc:
                strs[i] += ">"
            else:
                strs[i] += "-"
            c = "%0.2f" % c
            pc = "%0.2f" % pc
            print("$" + str(tickers[i][j]) + ": " + str(pc) + "==>" + str(c))
            time.sleep(0.65)
            print("-" * 50)
            time.sleep(0.65)
            strs[i] += str(tickers[i][j]) + " " + str(c) + "  "
        except:
            pass
    time.sleep(1 + 0.5*i)

count = 0
def stock_scr(colors, strs, count):
    colors[0 + 0*25 : 24 + 0*25] = [WHITE]*25
    colors[0 + 6*25 : 24 + 6*25] = [WHITE]*25
    colors[0 + 12*25 : 24 + 12*25] = [WHITE]*25
    colors[0 + 18*25 : 24 + 19*25] = [WHITE]*50
    color = LGRAY
    for i in range(len(strs)):
        str = strs[i]
        L = len(str)
        size = max(25, L*4)
        chrs = [char_pts(str[x], (count + x*4)%(size), 1 + 6*i) for x in range(L)]
        for chr in chrs:
            if chr[0] == '>':
                color = GREEN
            elif chr[0] == '<':
                color = RED
            elif chr[0] == '-':
                color = LGRAY
            for pixl in chr[1:]:
                try:
                    if pixl[0] >= size:
                        pixl = (pixl[0] - size, pixl[1])
                    if pixl[0] < 25:
                        colors[pixl[0] + 25*pixl[1]] = color
                except:
                    pass
    return (count-1)

# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
GRAY = (20, 20, 20)
LGRAY = (125, 125, 125)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the height and width of the screen to accomodate 25x20 lightboard circles
size = ((30+5)*25+5, (30+5)*20+5)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Board Tester")

# Set the default frame rate
FPS = 120

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# The array to hold the board pixel values
colors = [GRAY for i in range(25*20)]
#[(i % 256, (2*i) % 256, (3*i) % 256) for i in range(25*20)] [rand_color() for i in range(25*20)]

# Set initial board values
ledMode = 0
colorMode = 0
prevButtonState = 0  # 0 is HIGH, 1 is LOW
gHue = 0

# Loop as long as done == False
while not done:

    # Event handler
    for event in pygame.event.get():\
        # If program is quit, end the looping
        if event.type == pygame.QUIT:
            done = True
        # If a key is pressed change the colormode
        elif event.type == pygame.KEYDOWN:
            colorMode = (colorMode + 1) % 7
            colors = [GRAY for i in range(25*20)]

    # Clear the screen and set the screen background
    screen.fill(BLACK)
#===============================================================================
    if colorMode == 0:
        wow(colors)
    elif colorMode == 1:
        wow_hype(colors)
    elif colorMode == 2:
        wow2(colors)
    elif colorMode == 3:
        offset = wow3(colors, offset)
    elif colorMode == 4:
        ring_rad, offs = spiral(colors, ring_rad, offs)
    elif colorMode == 5:
        ring_rad, offs = 0, 0
        count = stock_scr(colors, strs, count)
        FPS = 5
        '''if count % 25 == 24:
            try:
                begin = strs[refresh_outer].index(tickers[refresh_outer][refresh_inner])-1
                end = strs[refresh_outer][begin:].index("  ")
                c, pc = get_data(tickers[refresh_outer][refresh_inner])
                round(c, 2)
                round(pc, 2)
                modif = ''
                if c < pc:
                    modif = "<"
                elif c > pc:
                    modif = ">"
                else:
                    modif = "-"
                c = "%0.2f" % c
                pc = "%0.2f" % pc
                print("$" + str(tickers[refresh_outer][refresh_inner]) + ": " + str(pc) + "==>" + str(c))
                print("-" * 50)
                strs[refresh_outer] = (strs[refresh_outer][0:begin] + modif +
                        str(tickers[refresh_outer][refresh_inner]) + " " + str(c))
                refresh_inner += 1
                if refresh_inner >= len(tickers[refresh_outer]):
                    refresh_inner = 0
                    refresh_outer = (refresh_outer + 1) % 3
            except:
                pass'''

    elif colorMode == 6:
        FPS = 120
        count = 0

    '''# Perform the alternations
    for y in range(21):
        if y % 2 == 1:
            colors = colors[0:25*y] + colors[25*y:25*(y+1)][::-1] + colors[25*(y+1):]'''
    # Iterates over each of the board pixels to display it
    for y in range(20):
        for x in range(25):
            pygame.draw.ellipse(screen, colors[x + 25*y], [(30+5)*x+5,(30+5)*y+5,30,30])

#===============================================================================
    # Put updated pixels on the screen
    pygame.display.flip()
    if colorMode == 5:
        colors = [GRAY for i in range(25*20)]

    # Limit loop to FPS frames per second
    clock.tick(FPS)


# Be IDLE friendly
pygame.quit()
