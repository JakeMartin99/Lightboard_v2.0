import random, math
from typing import List, Tuple
import FastLED; from FastLED import *
from Utils import *
from Shapes import *
from Characters import char_pts
from point2d import Point2D

PI = math.pi
TAU = 2*PI
NUM_LEDS = 500
LED_HALF = NUM_LEDS / 2

def split(color: tuple, i: int) -> int:
    return color[i] if 0<=i<=2 else -1

def fade(led_lst: list, damper: float) -> list:
    leds = led_lst
    if (damper >= 1): damper = 0.99
    for i in range(len(leds)):
        col = leds[i]
        if col == (0, 0, 0):continue
        colors = [(0,0,0) for i in range(3)]
        for j in range(3): colors[j] = split(col, j) * damper
        leds[i] = tuple(colors)
    return leds

def Rainbow(i: int) -> tuple:
    if (i > 1529): return Rainbow(i % 1530)
    if (i > 1274): return CRGB(255, 0, 255 - (i % 255))    # violet -> red
    if (i > 1019): return CRGB((i % 255), 0, 255)          # blue -> violet
    if (i > 764): return CRGB(0, 255 - (i % 255), 255)     # aqua -> blue
    if (i > 509): return CRGB(0, 255, (i % 255))           # green -> aqua
    if (i > 255): return CRGB(255 - (i % 255), 255, 0)     # yellow -> green
    return (255, i, 0)                                     # red -> yellow

class Mode:
    """
    A class that represents an abstract lightboard mode.

    ...

    Attributes
    ----------
    leds : list[tuple[int,int,int]]
        1D list of (R, G, B) tuples representing values for each bulb on the light strip.

    Methods
    -------
    open():
        Abstract function to handle opening the mode on the board.
    refresh():
        Abstract function to handle refreshing the frames of the mode.
    """

    def __init__(self, leds:List[Tuple[int,int,int]]):
        """
        Constructs the mode object with necessary parameters

        Parameters
        ----------
        leds : list
            1D list of (R, G, B) tuples representing each bulb on the light strip
        """
        self.leds = leds

    def open(self):
        """
        Abstract function to handle opening the mode on the board.
        Is empty, to be overridden in subclasses for specific mode.
        """
        pass

    def refresh(self):
        """
        Abstract function to handle refreshing the frames of the mode.
        Is empty, to be overridden in subclasses for specific mode.
        """
        pass

class Galaxy(Mode):
    """
    A subclass of Mode that implements the specific "Galaxy" mode.

    ...

    Attributes
    ----------
    leds : list[tuple[int,int,int]]
        1D list of (R, G, B) tuples representing values for each bulb on the light strip.


    Methods
    -------
    open(num_arms=random.randint(2,8)):
        Handles opening the Galaxy mode on the board.
    refresh():
        Refreshes the frames of the Galaxy mode.
    """

    def __init__(self, leds:List[Tuple[int,int,int]]):
        """
        Constructs the Galaxy mode object using the parent Mode constructor

        Parameters
        ----------
        leds : list
            1D list of (R, G, B) tuples representing each bulb on the light strip
        """
        super().__init__(leds)
        self.offset = None
        self.num_arms = None

    def open(self, num_arms:int=random.randint(2,8)) -> None:
        """
        Handles opening the Galaxy mode on the board.
        Sets num_arms based on the parameter and offset to 0.

        Parameters
        ----------
        num_arms : int, optional, default=random.randint(2,8)
            Sets the number of arms the Galaxy shape should have.
            By default is a randomly selected int in range [2,8]

        Returns
        -------
        None
        """
        self.offset = 0
        self.num_arms = num_arms

    def refresh(self) -> None:
        """
        Refreshes the frames of the Galaxy mode.
        Randomly assigns universal hue, assigns the value based on 2D position
        in polar coordinates, and increments the rotational offset.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        hue = random.randint(0,255)
        for y in range(20):
            for x in range(25):
                point = Point2D(x - 12, y - 10)
                r, theta = point.r, point.a
                if theta < 0: theta = TAU + theta
                val = (r-self.num_arms*theta-self.offset)%TAU
                value = abs(round((val-PI)*256/PI))
                self.leds[pt_finder(x,y,0)] = CHSV(hue, 255, value)
        self.offset += 0.2

class Modes:
    def __init__(self, leds):
        self.buff = Buffalo()
        self.buff_col = (180, 180, 25)
        self.ring_rad = 1
        self.offs = 0
        self.bin = False
        self.G = Galaxy(leds)
        self.G.open()

    def off(self, leds):
        return FastLED.fadeToBlackBy(leds, 10)

    def bpm(self, led_lst, v=1):
        leds = led_lst
        bpm = 62
        palette = FastLED.get_p(v)
        beat = FastLED.beatsin8(bpm, 64, 255)
        for i in range(NUM_LEDS):
            leds[i] = palette.get_col(gHue+(i*2), beat-gHue+(i*10))
        return leds

    def juggle(self, led_lst):
        leds = FastLED.fadeToBlackBy(led_lst, 20)
        dothue = 0
        for i in range(8):
            leds[FastLED.beatsin16(i+7, 0, NUM_LEDS-1)] |= CHSV(dothue, 200, 255)
            dothue += 32
        return leds

    def rainbow(self, led_lst):
        return FastLED.fill_rainbow(led_lst, gHue, 7)

    def addGlitter(self, led_lst, glitterProb):
        leds = led_lst
        if random.randint(0, 255) < glitterProb:
            leds[random.randint(0, NUM_LEDS)] = (255, 255, 255)
        return leds

    def rainbowWithGlitter(self, led_lst):
        leds = self.rainbow(led_lst)
        return self.addGlitter(leds, 80)

    def confetti(self, led_lst):
        leds = FastLED.fadeToBlackBy(led_lst, 10)
        pos = random.randint(0, NUM_LEDS)
        leds[pos] += CHSV(gHue + random.randint(0, 63), 200, 255)

    def sinelon(self, led_lst):
        leds = FastLED.fadeToBlackBy(led_lst, 20)
        pos = FastLED.beatsin16(leds, 13, 0, NUM_LEDS-1)
        leds[pos] += CHSV(gHue, 255, 192)
        return leds

    def sinelon2(self, led_lst):
        leds = FastLED.fadeToBlackBy(led_lst, 20)
        pos1 = FastLED.beatsin16(leds, 13, 0, NUM_LEDS-1)
        pos2 = FastLED.beatsin16(leds, 13, 0, NUM_LEDS-1, 5)
        pos3 = FastLED.beatsin16(leds, 13, 0, NUM_LEDS-1, 10)
        pos4 = FastLED.beatsin16(leds, 13, 0, NUM_LEDS-1, 15)
        pos5 = FastLED.beatsin16(leds, 13, 0, NUM_LEDS-1, 20)
        pos6 = FastLED.beatsin16(leds, 13, 0, NUM_LEDS-1, 25)
        for pos in [pos1, pos2, pos3, pos4, pos5, pos6]:
            leds[pos] += CHSV(gHue, 255, 192)
        return leds

    def sound1(led_lst: list) -> list:
        leds = fade(led_lst, 0.75)
        if bump: gradient += 64

        if volume > 0:
            col = Rainbow(gradient)
            start = LED_HALF - (LED_HALF * (volume / maxVol))
            finish = LED_HALF + (LED_HALF * (volume / maxVol)) + NUM_LEDS % 2

            for i in range(start, finish):
                damp = float(((finish - start) / 2.0) - abs((i - start) - ((finish - start) / 2.0))) / float((finish - start) / 2.0)
                leds[i] = (split(col, 0) * math.pow(damp, 2.0), split(col, 1) * math.pow(damp, 2.0), split(col, 2) * math.pow(damp, 2.0))

        return leds

    def sound2(led_lst: list) -> list:
        leds = fade(led_lst, 0.75)
        if bump: gradient += 64

        if volume > 0:
            col = Rainbow(gradient)
            start = LED_HALF - (LED_HALF * (volume / maxVol))
            finish = LED_HALF + (LED_HALF * (volume / maxVol)) + NUM_LEDS % 2

            for i in range(start, finish):
                damp = float(((finish - start) / 2.0) - abs((i - start) - ((finish - start) / 2.0))) / float((finish - start) / 2.0)
                damp *= 2
                leds[i] = (split(col, 0) * math.pow(damp, 2.0), split(col, 1) * math.pow(damp, 2.0), split(col, 2) * math.pow(damp, 2.0))

        return leds

    def spiral(self, leds):
        colors = leds
        for R in range(self.ring_rad):
            point = Point2D(r=R/20, a=R)
            x = round(point.x + 12)
            y = round(point.y + 10)
            pos = pt_finder(x,y,1)
            if pos < NUM_LEDS and pos >= 0:
              colors[pos] = CHSV( (self.offs + R) % 256, 255, 150)
              self.offs += 1
        self.ring_rad += 1
        if self.ring_rad > 20*12: self.ring_rad = 1
        return FastLED.fadeToBlackBy(colors, 25)

    def circles(self, leds):
        colors = [(0,0,0) for c in leds]
        for y in range(20):
            for x in range(25):
                r = round(((x-12)**2 + (y-10)**2)**0.5)
                colors[pt_finder(x, y, 0)] = CHSV((self.offs+ 15*r) % 256, 255, 255 - 10*r)
        self.offs += 10
        return colors

    def galaxy(self):
        '''
        colors = leds
        hue = random.randint(0,255)
        for y in range(20):
            for x in range(25):
                point = Point2D(x - 12, y - 10)
                r, theta = point.r, point.a
                if theta < 0: theta = TAU + theta
                val = (r-num_arms*theta-self.offs)%TAU
                value = abs(round((val-PI)*256/PI))
                colors[pt_finder(x,y,0)] = CHSV(hue, 255, value)
        self.offs += 0.2
        return colors
        '''
        self.G.refresh()
        return self.G.leds


    def buffonecard(self, leds):
        colors = [(10,10,10) for c in leds]
        for i in range(70):
            colors[pt_finder(self.buff.outer[i][0], self.buff.outer[i][1], 1)] = self.buff_col
        for i in range(34):
            colors[pt_finder(self.buff.C[i][0], self.buff.C[i][1], 1)] = self.buff_col
        for i in range(32):
            colors[pt_finder(self.buff.U[i][0], self.buff.U[i][1], 1)] = self.buff_col
        for i in range(6):
            colors[pt_finder(self.buff.horn[i][0], self.buff.horn[i][1], 1)] = self.buff_col
        return colors

    def buff2(self, leds):
        colors = [(10,10,10) for c in leds]
        for i in range(70):
            colors[pt_finder(self.buff.outer[i][0], self.buff.outer[i][1], 1)] = CHSV( (self.offs+ (i*256//70)) % 256, 255, 255)
        for i in range(34):
            colors[pt_finder(self.buff.C[i][0], self.buff.C[i][1], 1)] = CHSV( (self.offs+ (i*256//34)) % 256, 255, 255)
        for i in range(32):
            colors[pt_finder(self.buff.U[i][0], self.buff.U[i][1], 1)] = CHSV( (self.offs+ (i*256//32)) % 256, 255, 255)
        for i in range(6):
            colors[pt_finder(self.buff.horn[i][0], self.buff.horn[i][1], 1)] = CHSV( (self.offs+ (i*256//6)) % 256, 255, 255)
        self.offs += 10
        return colors

    def buff2_muted(self, leds):
        colors = [(10,10,10) for c in leds]
        for i in range(70):
            colors[pt_finder(self.buff.outer[i][0], self.buff.outer[i][1], 1)] = CHSV( (self.offs+ (i*256//70)) % 256, 150, 255)
        for i in range(34):
            colors[pt_finder(self.buff.C[i][0], self.buff.C[i][1], 1)] = CHSV( (self.offs+ (i*256//34)) % 256, 150, 255)
        for i in range(32):
            colors[pt_finder(self.buff.U[i][0], self.buff.U[i][1], 1)] = CHSV( (self.offs+ (i*256//32)) % 256, 150, 255)
        for i in range(6):
            colors[pt_finder(self.buff.horn[i][0], self.buff.horn[i][1], 1)] = CHSV( (self.offs+ (i*256//6)) % 150, 255, 255)
        self.offs += 10
        return colors

    def buff3(self, led_lst):
        leds = self.bpm6(led_lst)

        for i in range(70):
            leds[pt_finder(self.buff.outer[i][0], self.buff.outer[i][1], 1)] = (255, 255, 255)
        for i in range(34):
            leds[pt_finder(self.buff.C[i][0], self.buff.C[i][1], 1)] = (255, 255, 255)
        for i in range(32):
            leds[pt_finder(self.buff.U[i][0], self.buff.U[i][1], 1)] = (255, 255, 255)
        for i in range(6):
            leds[pt_finder(self.buff.horn[i][0], self.buff.horn[i][1], 1)] = (255, 255, 255)
        return leds

    def wow(self, leds):
        return [(random.randint(0,255), random.randint(0,255), random.randint(0,255)) for c in leds]

    def wow_hype(self, leds):
        return [CHSV(random.randint(0,255), 255, 255) for c in leds]

    def wow2(self, leds):
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        return [color for c in leds]

    def wow3(self, leds):
        colors = [(i%255, (i+self.offs)%255, (i*self.offs)%255) for i in range(len(leds))]
        self.offs += 1
        return colors

    def strobe(self, leds):
        color = (255,255,255) if self.bin else (0,0,0)
        self.bin = not self.bin
        return [color for c in leds]

    def line(self, leds, p0, p1):
        colors = leds
        x0, y0 = p0
        x1, y1 = p1
        if x1 - x0 != 0:
            m = (y1 - y0) / (x1 - x0)
            b = y1 - m*x1
            mode = "norm"
        elif y1 - y0 != 0:
            m = (x1 - x0) / (y1 - y0)
            b = x1 - m*y1
            mode = "inv"
        else:
            m = 0
            b = 0
            mode = "pt"

        for y in range(20):
            for x in range(25):
                dif = abs(y - (m*x + b)) if mode == "norm" else (abs(x - (m*y + b)) if mode == "inv" else (1 if (x,y) == (x1,y1) else 0))
                if dif < 1 and (x0 <= x <= x1 or x0 >= x >= x1) and (y0 <= y <= y1 or y0 >= y >= y1):
                    colors[pt_finder(x,y,1)] = CHSV(0,0,255*(1-dif))
        return colors

    def text(self, leds, str, color):
        colors = [(0,0,0) for c in leds]
        size = max(25, len(str)*4)
        for i in range(len(str)):
            chars = [char_pts(str[i], (self.offs + i*4)%(size), 1)]
            for char in chars:
                for pixl in char[1:]:
                    try:
                        if pixl[0] >= size:
                            pixl = (pixl[0] - size, pixl[1])
                        if pixl[0] < 25:
                            colors[pt_finder(pixl[0],pixl[1],0)] = color
                    except:
                        pass
        return colors
