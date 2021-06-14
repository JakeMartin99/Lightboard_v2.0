import pygame
from Utils import *
from Shapes import *
from point2d import Point2D

def CHSV(h,s,v):
    color = pygame.Color(0)
    color.hsva = (h*360//255,s*100//255,v*100//255,100)
    return (color.r, color.g, color.b)

def fadeToBlackBy(colors, fade):
    f = (256-fade)/256
    return [(int(c[0]*f), int(c[1]*f), int(c[2]*f)) for c in colors]

class Modes:
    def __init__(self):
        self.buff = Buffalo()
        self.buff_col = (180, 180, 25)
        self.col_start = 0
        self.ring_rad = 1
        self.offs = 0

    def spiral(self, leds, col_start):
        colors = leds
        for R in range(self.ring_rad):
            point = Point2D(r=R/20, a=R)
            x = round(point.x + 12)
            y = round(point.y + 10)
            pos = pt_finder(x,y,1)
            if pos < 25*20 and pos >= 0:
              colors[pos] = CHSV( (offs + R) % 256, 255, 150)
              self.offs += 1
        self.ring_rad += 1
        if self.ring_rad > 20*12: self.ring_rad = 1
        return fadeToBlackBy(colors, 25)

    def buffonecard(self, leds, col_start):
        colors = leds
        for i in range(70):
            colors[pt_finder(self.buff.outer[i][0], self.buff.outer[i][1], 1)] = self.buff_col
        for i in range(34):
            colors[pt_finder(self.buff.C[i][0], self.buff.C[i][1], 1)] = self.buff_col
        for i in range(32):
            colors[pt_finder(self.buff.U[i][0], self.buff.U[i][1], 1)] = self.buff_col
        for i in range(6):
            colors[pt_finder(self.buff.horn[i][0], self.buff.horn[i][1], 1)] = self.buff_col
        return colors

    def buff2(self, leds, col_start):
        colors = leds
        col = col_start
        for i in range(70):
            colors[pt_finder(self.buff.outer[i][0], self.buff.outer[i][1], 1)] = CHSV( (col + (i*256//70)) % 256, 255, 255)
        for i in range(34):
            colors[pt_finder(self.buff.C[i][0], self.buff.C[i][1], 1)] = CHSV( (col + (i*256//34)) % 256, 255, 255)
        for i in range(32):
            colors[pt_finder(self.buff.U[i][0], self.buff.U[i][1], 1)] = CHSV( (col + (i*256//32)) % 256, 255, 255)
        for i in range(6):
            colors[pt_finder(self.buff.horn[i][0], self.buff.horn[i][1], 1)] = CHSV( (col + (i*256//6)) % 256, 255, 255)
        return colors

    def fun(self, leds, col_start):
        colors = leds
        col = -col_start
        for y in range(20):
            for x in range(25):
                r = round(((x-12)**2 + (y-10)**2)**0.5)
                colors[pt_finder(x, y, 0)] = CHSV((col + 15*r) % 256, 255, 255 - 10*r)
        return colors

    def line(self, leds, col_start, p0, p1):
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
                    colors[pt_finder(x,y,0)] = CHSV(0,0,255*(1-dif))
        return colors
