# Hand-Python-ized functions from FastLED code available at http://fastled.io/docs/3.1/
# The only purpose of this is to provision functions used in the FastLED library
# That are necessary to emulate some of the lightboard modes
#
# The creators of FastLED deserve full credit for the majority of the logic here

import math, time, pygame

def CHSV(h,s,v):
    color = pygame.Color(0)
    try:
        color.hsva = (h*360//255,s*100//255,v*100//255,100)
    except:
        print((h*360//255,s*100//255,v*100//255,100))
        exit()
    return (color.r, color.g, color.b)

# Returns a fade of all pixels by the given fadeBy parameter
def fadeToBlackBy(leds_lst, fadeBy):
    leds = leds_lst
    f = (255 - fadeBy)/255
    return [(int(c[0]*f), int(c[1]*f), int(c[2]*f)) for c in leds]

class Palette():
    def __init__(self, color_lst):
        if type(color_lst[0]) == int:
            self.colors = []
            for c in color_lst:
                h = "{0:0{1}x}".format(c,6)
                val = (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))
                self.colors.append(val)
        else:
            self.colors = color_lst
        if len(self.colors) != 16:
            print("Error: Incorrent number of colors for a palette!")
            exit()

    def get_col(self, index, brightness):
        real_ind = 15.0/255 * index
        floor, ceil = math.floor(real_ind), math.ceil(real_ind)
        if floor == ceil: return self.colors[floor]
        f = real_ind - floor
        c = 1 - f
        return tuple([round((f*self.colors[floor][ch] + c*self.colors[ceil][ch])*brightness)/255 for ch in range(3)])


AliceBlue=0xF0F8FF,
Amethyst=0x9966CC,
AntiqueWhite=0xFAEBD7,
Aqua=0x00FFFF,
Aquamarine=0x7FFFD4,
Azure=0xF0FFFF,
Beige=0xF5F5DC,
Bisque=0xFFE4C4,
Black=0x000000,
BlanchedAlmond=0xFFEBCD,
Blue=0x0000FF,
BlueViolet=0x8A2BE2,
Brown=0xA52A2A,
BurlyWood=0xDEB887,
CadetBlue=0x5F9EA0,
Chartreuse=0x7FFF00,
Chocolate=0xD2691E,
Coral=0xFF7F50,
CornflowerBlue=0x6495ED,
Cornsilk=0xFFF8DC,
Crimson=0xDC143C,
Cyan=0x00FFFF,
DarkBlue=0x00008B,
DarkCyan=0x008B8B,
DarkGoldenrod=0xB8860B,
DarkGray=0xA9A9A9,
DarkGrey=0xA9A9A9,
DarkGreen=0x006400,
DarkKhaki=0xBDB76B,
DarkMagenta=0x8B008B,
DarkOliveGreen=0x556B2F,
DarkOrange=0xFF8C00,
DarkOrchid=0x9932CC,
DarkRed=0x8B0000,
DarkSalmon=0xE9967A,
DarkSeaGreen=0x8FBC8F,
DarkSlateBlue=0x483D8B,
DarkSlateGray=0x2F4F4F,
DarkSlateGrey=0x2F4F4F,
DarkTurquoise=0x00CED1,
DarkViolet=0x9400D3,
DeepPink=0xFF1493,
DeepSkyBlue=0x00BFFF,
DimGray=0x696969,
DimGrey=0x696969,
DodgerBlue=0x1E90FF,
FireBrick=0xB22222,
FloralWhite=0xFFFAF0,
ForestGreen=0x228B22,
Fuchsia=0xFF00FF,
Gainsboro=0xDCDCDC,
GhostWhite=0xF8F8FF,
Gold=0xFFD700,
Goldenrod=0xDAA520,
Gray=0x808080,
Grey=0x808080,
Green=0x008000,
GreenYellow=0xADFF2F,
Honeydew=0xF0FFF0,
HotPink=0xFF69B4,
IndianRed=0xCD5C5C,
Indigo=0x4B0082,
Ivory=0xFFFFF0,
Khaki=0xF0E68C,
Lavender=0xE6E6FA,
LavenderBlush=0xFFF0F5,
LawnGreen=0x7CFC00,
LemonChiffon=0xFFFACD,
LightBlue=0xADD8E6,
LightCoral=0xF08080,
LightCyan=0xE0FFFF,
LightGoldenrodYellow=0xFAFAD2,
LightGreen=0x90EE90,
LightGrey=0xD3D3D3,
LightPink=0xFFB6C1,
LightSalmon=0xFFA07A,
LightSeaGreen=0x20B2AA,
LightSkyBlue=0x87CEFA,
LightSlateGray=0x778899,
LightSlateGrey=0x778899,
LightSteelBlue=0xB0C4DE,
LightYellow=0xFFFFE0,
Lime=0x00FF00,
LimeGreen=0x32CD32,
Linen=0xFAF0E6,
Magenta=0xFF00FF,
Maroon=0x800000,
MediumAquamarine=0x66CDAA,
MediumBlue=0x0000CD,
MediumOrchid=0xBA55D3,
MediumPurple=0x9370DB,
MediumSeaGreen=0x3CB371,
MediumSlateBlue=0x7B68EE,
MediumSpringGreen=0x00FA9A,
MediumTurquoise=0x48D1CC,
MediumVioletRed=0xC71585,
MidnightBlue=0x191970,
MintCream=0xF5FFFA,
MistyRose=0xFFE4E1,
Moccasin=0xFFE4B5,
NavajoWhite=0xFFDEAD,
Navy=0x000080,
OldLace=0xFDF5E6,
Olive=0x808000,
OliveDrab=0x6B8E23,
Orange=0xFFA500,
OrangeRed=0xFF4500,
Orchid=0xDA70D6,
PaleGoldenrod=0xEEE8AA,
PaleGreen=0x98FB98,
PaleTurquoise=0xAFEEEE,
PaleVioletRed=0xDB7093,
PapayaWhip=0xFFEFD5,
PeachPuff=0xFFDAB9,
Peru=0xCD853F,
Pink=0xFFC0CB,
Plaid=0xCC5533,
Plum=0xDDA0DD,
PowderBlue=0xB0E0E6,
Purple=0x800080,
Red=0xFF0000,
RosyBrown=0xBC8F8F,
RoyalBlue=0x4169E1,
SaddleBrown=0x8B4513,
Salmon=0xFA8072,
SandyBrown=0xF4A460,
SeaGreen=0x2E8B57,
Seashell=0xFFF5EE,
Sienna=0xA0522D,
Silver=0xC0C0C0,
SkyBlue=0x87CEEB,
SlateBlue=0x6A5ACD,
SlateGray=0x708090,
SlateGrey=0x708090,
Snow=0xFFFAFA,
SpringGreen=0x00FF7F,
SteelBlue=0x4682B4,
Tan=0xD2B48C,
Teal=0x008080,
Thistle=0xD8BFD8,
Tomato=0xFF6347,
Turquoise=0x40E0D0,
Violet=0xEE82EE,
Wheat=0xF5DEB3,
White=0xFFFFFF,
WhiteSmoke=0xF5F5F5,
Yellow=0xFFFF00,
YellowGreen=0x9ACD32,
def get_palette(v:int):
    # CloudColors
    if v == 1:
        return Palette([Blue, DarkBlue, DarkBlue, DarkBlue,
                        DarkBlue, DarkBlue, DarkBlue, DarkBlue,
                        Blue, DarkBlue, SkyBlue, SkyBlue,
                        LightBlue, White, LightBlue, SkyBlue])
    # LavaColors
    elif v == 2:
        return Palette([Black, Maroon, Black, Maroon,
                        DarkRed, Maroon, DarkRed, DarkRed,
                        Maroon, DarkRed, Red, Orange,
                        White, Orange, Red, DarkRed])
    # OceanColors
    elif v == 3:
        return Palette([MidnightBlue, DarkBlue, MidnightBlue, Navy,
                        DarkBlue, MediumBlue, SeaGreen, Teal,
                        CadetBlue, Blue, DarkCyan, CornflowerBlue,
                        Aquamarine, SeaGreen, Aqua, LightSkyBlue])
    # ForestColors
    elif v == 4:
        return Palette([DarkGreen, DarkGreen, DarkOliveGreen, DarkGreen,
                        Green, ForestGreen, OliveDrab, Green,
                        SeaGreen, MediumAquamarine, LimeGreen, YellowGreen,
                        LightGreen, LawnGreen, MediumAquamarine, ForestGreen])
    # RainbowColors
    elif v == 5:
        return Palette([0xFF0000, 0xD52A00, 0xAB5500, 0xAB7F00,
                        0xABAB00, 0x56D500, 0x00FF00, 0x00D52A,
                        0x00AB55, 0x0056AA, 0x0000FF, 0x2A00D5,
                        0x5500AB, 0x7F0081, 0xAB0055, 0xD5002B])
    # RainbowStripeColors
    elif v == 6:
        return Palette([0xFF0000, 0x000000, 0xAB5500, 0x000000,
                        0xABAB00, 0x000000, 0x00FF00, 0x000000,
                        0x00AB55, 0x000000, 0x0000FF, 0x000000,
                        0x5500AB, 0x000000, 0xAB0055, 0x000000])
    # PartyColors
    elif v == 7:
        return Palette([0x5500AB, 0x84007C, 0xB5004B, 0xE5001B,
                        0xE81700, 0xB84700, 0xAB7700, 0xABAB00,
                        0xAB5500, 0xDD2200, 0xF2000E, 0xC2003E,
                        0x8F0071, 0x5F00A1, 0x2F00D0, 0x0007F9])
    # HeatColors
    elif v == 8:
        return Palette([0x000000, 0x330000, 0x660000, 0x990000,
                        0xCC0000, 0xFF0000, 0xFF3300, 0xFF6600,
                        0xFF9900, 0xFFCC00, 0xFFFF00, 0xFFFF33,
                        0xFFFF66, 0xFFFF99, 0xFFFFCC, 0xFFFFFF])

def fill_rainbow(leds_lst, init_hue, delta_hue):
    leds = leds_lst
    hue, val, sat = init_hue, 255, 240
    for i in range(len(leds)):
        leds[i] = CHSV(hue, val, sat)
        hue += delta_hue
    return leds

def GET_MILLIS():
    return round(time.time() * 1000)

def beat88(bpm, timebase=0):
    return ((GET_MILLIS() - timebase) * bpm * 280) >> 16

def beat16(bpm, timebase=0):
    BPM = bpm
    if BPM<256: BPM <<= 8
    return beat88(BPM, timebase)

def sin16(x): return math.sin((x/32768.0) * math.pi * 32767)

def scale16(i, scale): return i * (scale / 65536)

def beatsin16(bpm, lowest=0, highest=65535, timebase=0, phase_offset=0):
    beat = beat16(bpm, timebase)
    beatsin = sin16(beat + phase_offset) + 32768
    rangewidth = highest - lowest
    scaledbeat = scale16(beatsin, rangewidth)
    return int(lowest + scaledbeat)

def beat8(bpm, timebase=0):
    return beat16(bpm, timebase) >> 8

def sin8(x): return math.sin((x/128.0) * math.pi * 128) + 128

def scale8(i, scale): return i * (scale / 256)

def beatsin8(bpm, lowest=0, highest=255, timebase=0, phase_offset=0):
    beat = beat8(bpm, timebase)
    beatsin = sin8(beat + phase_offset)
    rangewidth = highest - lowest
    scaledbeat = scale8(beatsin, rangewidth)
    return int(lowest + scaledbeat)
