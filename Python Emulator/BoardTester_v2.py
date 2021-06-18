"""
Jake Martin
New python code to test board graphics using pygame
Updated 2021
"""

# Import libraries
from HardwareEmulator import Lightboard
from ModeSet import Modes

modes = Modes()

board = Lightboard(fps=30)
# Initialize the led strip color list
leds = [(0,0,0) for c in range(500)]

while not board.done:
    board.handle_events()
    leds = modes.text(leds,"BTC 6.9", (255,120,0))
    board.display(leds)

board.turn_off()
