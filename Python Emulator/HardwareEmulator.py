import pygame

def color_adjust(color):
    return tuple([round((235/255)*ch+20) for ch in color])

class Lightboard:
    def __init__(self, fps=30):
        # Initialize the pygame engine
        pygame.init()
        # Set the font with (size, bold, italics)
        self.font = pygame.font.SysFont('Calibri', 12, True, False)
        # Set the height and width of the screen to accomodate 25x20 lightboard circles
        self.size = ((30+5)*25+5, (30+5)*20+5)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Board Tester v2")
        # Set the FPS rate
        self.FPS = fps
        # Set looping variables
        self.done = False
        self.clock = pygame.time.Clock()
        # Set debugging toggle variable
        self.disp_nums = False

    def display(self, leds:list):
        # Clear the screen and set the screen background
        self.screen.fill((0,0,0))
        # Iterates over each of the board pixels to display it
        i=0
        for y in range(20-1,0-1,-1):
            x_path = (0,25,1) if y%2==1 else (25-1,0-1,-1)
            for x in range(*x_path):
                pygame.draw.ellipse(self.screen, color_adjust(leds[i]), [(30+5)*x+5,(30+5)*y+5,30,30])
                if self.disp_nums:
                    text = self.font.render(str(i),True,(255,255,255))
                    self.screen.blit(text, [(30+5)*x+5,(30+5)*y+5])
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

    def turn_off(self):
        pygame.quit()
        del self