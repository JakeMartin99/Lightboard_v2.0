# Import the graphical library pygame
import pygame

# Python-only color adjustment function to make "off" circles still appear on the black background
def color_adjust(color):
    return tuple([round((235/255)*ch+20) for ch in color])

# A class that implements an emulation of the hardware 25x20 lightboard
class Lightboard:
    # Lightboard constructor, with num_modes parameter
    def __init__(self, num_modes):
        # Initialize the pygame engine
        pygame.init()
        # Set the font with (size, bold, italics)
        self.font = pygame.font.SysFont('Calibri', 12, True, False)
        # Set the height and width of the screen to accomodate 25x20=500 lightboard pixels of
        # diameter 30px with 5px margin on all sides, and 80x70 for the wood frame
        self.size = ((30+5)*25+5+80, (30+5)*20+5+70)
        self.screen = pygame.display.set_mode(self.size)
        self.background = pygame.image.load("wood.jpg")
        pygame.display.set_caption("Lightboard Emulator")
        # Set the FPS rate
        self.FPS = 30
        # Set looping variables
        self.done = False
        self.clock = pygame.time.Clock()
        # Set mode control variables
        self.mode = 0
        self.num_modes = num_modes
        # Set debugging toggle variable
        self.disp_nums = False

    def display(self, leds:list):
        # Clear the screen and set the screen background
        self.screen.fill((0,0,0))
        self.screen.blit(self.background, (0,0))
        # Iterates over each of the board pixels to display it
        i=0
        for y in range(20-1,0-1,-1):
            x_path = (0,25,1) if y%2==1 else (25-1,0-1,-1)
            for x in range(*x_path):
                pygame.draw.ellipse(self.screen, color_adjust(leds[i]), [(30+5)*x+5+40,(30+5)*y+5+35,30,30])
                if self.disp_nums:
                    text = self.font.render(str(i),True,(255,255,255))
                    self.screen.blit(text, [(30+5)*x+5+40,(30+5)*y+5+35])
                i+=1
        # Put updated pixels on the screen
        pygame.display.flip()
        # Limit loop to FPS frames per second
        self.clock.tick(self.FPS)

    def handle_events(self):
        for event in pygame.event.get():
            # If program is quit, end the looping
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.disp_nums = not self.disp_nums
                elif event.key == pygame.K_LEFT:
                    self.mode = abs((self.mode-1) % self.num_modes)
                elif event.key == pygame.K_RIGHT:
                    self.mode = (self.mode+1) % self.num_modes

    def turn_off(self):
        pygame.quit()
        del self
