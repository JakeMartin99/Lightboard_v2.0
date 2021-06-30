"""
Jake Martin
New python code to test board graphics using pygame
Updated 2021
"""

# Import custom libraries
from HardwareEmulator import Lightboard
from ModeSet import Modes

# Create a object for the hardware emulation
board = Lightboard(10)
# Initialize the 500px (R,G,B) color array
leds = [(0,0,0) for c in range(500)]
# Create object holding all of the lightboard modes
modes = Modes(leds)

# Loop for as long as the board is on, and each generation...
while not board.done:
    # Handle input events
    board.handle_events()
    # Assign the pixel array based on the current mode
    if board.mode == 0:
        leds = modes.off(leds)
    elif board.mode == 1:
        leds = modes.spiral(leds)
    elif board.mode == 2:
        leds = modes.circles(leds)
    elif board.mode == 3:
        leds = modes.galaxy()
    elif board.mode == 4:
        leds = modes.buffonecard(leds)
    elif board.mode == 5:
        leds = modes.buff2(leds)
    elif board.mode == 6:
        leds = modes.wow(leds)
    elif board.mode == 7:
        leds = modes.wow_hype(leds)
    elif board.mode == 8:
        leds = modes.wow2(leds)
    elif board.mode == 9:
        leds = modes.wow3(leds)
    elif board.mode == 10:
        leds = modes.strobe(leds)
    # Display the pixel array to the emulated board
    board.display(leds)

# Once done, "turn off" the board to properly terminate the emulation
board.turn_off()
