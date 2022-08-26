print("Starting")

import board
from kmk.consts import UnicodeMode
from kmk.handlers.sequences import compile_unicode_string_sequences
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.layers import Layers
from kmk.modules.media_keys import MediaKeys
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
keyboard.unicode_mode = UnicodeMode.LINUX
keyboard.tap_time = 150
keyboard.debug_enabled = False

keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP115)
keyboard.row_pins = (board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20,)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.A, ]
]

if __name__ == '__main__':
    keyboard.go()

