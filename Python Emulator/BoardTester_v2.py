"""
Jake Martin
New python code to test board graphics using pygame
Updated 2021
"""

# Import custom libraries
from HardwareEmulator import Lightboard
from ModeSet import Modes

# Create object holding all of the lightboard modes
modes = Modes()

# Create a object for the hardware emulation
board = Lightboard()
# Initialize the 500px (R,G,B) color array
leds = [(0,0,0) for c in range(500)]

# Loop for as long as the board is on, and each generation...
while not board.done:
    # Handle input events
    board.handle_events()
    # Assign the pixel array based on a mode
    leds = modes.buff2(leds)
    # Display the pixel array to the emulated board
    board.display(leds)

# Once done, "turn off" the board to properly terminate the emulation
board.turn_off()
