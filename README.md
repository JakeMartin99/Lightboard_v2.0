# Lightboard_v2.0

Code by Jake Martin, hardware by Eric Heising

# Arduino folder
Contains present version of Arduino C++ to operate the physical lightboard. Still in-progress is implementing some of the successfully Python-emulated modes, fixing minor hardware bugs, and making codebase more readable by structuring it similar to the emulator. Intended to be run off of an ESP32 board with a connected button, audio volume sensor, and a linearly-connected grid arrangement of FastLED compatible light strips.

# Python Emulator
Contains in-progress implementation of a Pygame-based emulator of the lightboard. The goal with this is to enable faster testing of new modes, and to develop a better code structure that can later be mirrored for the hardware Arduino code. At present, can best be run with command line cmd: "python BoardTester_v2.py"
