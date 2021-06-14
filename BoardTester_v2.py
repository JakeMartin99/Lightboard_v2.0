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

board.loop(modes.buff2)
