print("Starting")

import board
from kmk.modules.layers import Layers
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

cafe_c87 = KMKKeyboard()

cafe_c87.col_pins = (board.GP15, board.GP14, board.GP13, board.GP12, board.GP11, board.GP10, board.GP9, board.GP8, board.GP7, board.GP6, board.GP5, board.GP4, board.GP3, board.GP2, board.GP1, board.GP0,)
cafe_c87.row_pins = (board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21,)
cafe_c87.diode_orientation = DiodeOrientation.COL2ROW
cafe_c87.debug_enabled = True
cafe_c87.modules.append(Layers())

MOMENTARY = KC.MO(1)

cafe_c87.keymap = [
    [
        # Layer 0 QWERTY
        KC.ESC,   KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,     KC.F6,    KC.F7,     KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.DEL,  KC.INS,  KC.HOME,
        KC.GRAVE, KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,     KC.N6,    KC.N7,     KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC, KC.NO,   KC.END,
        KC.TAB,   KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,      KC.NO,    KC.Y,      KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS, KC.PGUP,
        KC.CAPS,  KC.A,    KC.S,    KC.D,    KC.F,    KC.G,      KC.NO,    KC.H,      KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.ENT,  KC.NO,   KC.PGDN,
        KC.LSFT,  KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,      KC.NO,    KC.B,      KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT, KC.UP,   KC.NO,
        KC.LCTL,  KC.LGUI, KC.LALT, KC.NO,   KC.SPC,  MOMENTARY, KC.NO,    MOMENTARY, KC.SPC,  KC.NO,   KC.RALT, KC.APP,  KC.RCTL, KC.LEFT, KC.DOWN, KC.RGHT,
   ]
]

if __name__ == '__main__':
    cafe_c87.go()
