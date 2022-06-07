BUTTON_NAMES = {
    1: 'select',
    2: 'start',
    3: 'cross',
    4: 'up',
    5: 'circle',
    6: 'left',
    7: 'right',
    8: 'triangle',
    9: 'down',
    10: 'square'
}

HID_KEY_CODES = {
    '1': 0x1E,
    '2': 0x1F,
    '3': 0x20,
    '4': 0x21,
    '5': 0x22,
    '6': 0x23,
    '7': 0x24,
    '8': 0x25,
    '9': 0x26,
    '0': 0x27,
    'a': 0x04,
    'b': 0x05,
    'c': 0x06,
    'd': 0x07,
    'e': 0x08,
    'f': 0x09,
    'g': 0x0A,
    'h': 0x0B,
    'i': 0x0C,
    'j': 0x0D,
    'k': 0x0E,
    'l': 0x0F,
    'm': 0x10,
    'n': 0x11,
    'ñ': 0x33,
    'o': 0x12,
    'p': 0x13,
    'q': 0x14,
    'r': 0x15,
    's': 0x16,
    't': 0x17,
    'u': 0x18,
    'v': 0x19,
    'w': 0x1A,
    'x': 0x1B,
    'y': 0x1C,
    'z': 0x1D,
    'f1': 0x3A,
    'f2': 0x3B,
    'f3': 0x3C,
    'f4': 0x3D,
    'f5': 0x3E,
    'f6': 0x3F,
    'f7': 0x40,
    'f8': 0x41,
    'f9': 0x42,
    'f10': 0x43,
    'f11': 0x44,
    'f12': 0x45,
    '{': 0x34,
    '}': 0x31,
    '<': 0x64,
    ',': 0x36,
    '.': 0x37,
    '-': 0x38,
    '+': 0x30,
    '|': 0x35,
    "'": 0x2D,
    '¿': 0x2E,
    'backspace': 0x2A,
    'insert': 0x49,
    'home': 0x4A,
    'page_up': 0x4B,
    'tab': 0x2B,
    'esc': 0x29,
    'print_screen': 0x46,
    'scroll_lock': 0x47,
    'pause': 0x48,
    'enter': 0x28,
    'delete': 0x4C,
    'end': 0x4D,
    'page_down': 0x4E,
    'caps_lock': 0x39,
    'shift': 0xE1,
    'ctrl': 0xE0,
    'cmd': 0xE3,
    'alt': 0xE2,
    'alt_gr': 0xE6,
    'space': 0x2C,
    'menu': 0x65,
    'left': 0x50,
    'down': 0x51,
    'right': 0x4F,
    'up': 0x52,
    'none': None,
    None: None,
}

HID_KEY_CODES.update({
    'shift_l': HID_KEY_CODES['shift'],
    'shift_left': HID_KEY_CODES['shift'],
    'shift_r': HID_KEY_CODES['shift'],
    'shift_right': HID_KEY_CODES['shift'],

    'ctrl_l': HID_KEY_CODES['ctrl'],
    'ctrl_left': HID_KEY_CODES['ctrl'],
    'ctrl_r': HID_KEY_CODES['ctrl'],
    'ctrl_right': HID_KEY_CODES['ctrl'],

    'alt_l': HID_KEY_CODES['alt'],
    'alt_left': HID_KEY_CODES['alt']
})
