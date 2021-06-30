"""
Jake Martin
Updated 2021
"""

# Import my custom libraries
from HardwareEmulator import Lightboard
from Modes import Controller

# Create an object for the lightboard hardware emulator
board = Lightboard()

# Create an object for the mode-selecting "virtual remote control"
mode_remote = Controller()

# Loop for as long as the board is on, and each iteration...
while not board.done:
    # Handle input events from the board and process it with the remote
    mode_remote.process_signals(*board.handle_events())
    # Refresh all of the leds with the remote
    mode_remote.refresh_leds()
    # Retrieve the led list from the remote and display it to the board
    board.display(mode_remote.get_leds())

# Once done, "turn off" the board to properly terminate the emulation
board.turn_off()
