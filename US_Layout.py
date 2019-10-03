import random


def random_words(length_range, count):
    symbols = minor_keys + major_keys
    lengths = [random.randint(*length_range) for _ in range(count)]
    words = [''.join(random.choices(symbols, k=length)) for length in lengths]
    text = ' '.join(words)
    return text


start_ends = [[0, 25], [3, 28], [4, 25], [5, 24]]
key_coords = []
for row, start_end in enumerate(start_ends):
    for i in range(*start_end, 2):
        key_coords.append([row, i])

major_keys = '~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'
minor_keys = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"

finger_keys = {
    'L_pinky': '`12qaz~!@QAZ',
    'L_ring': '3wsx#WSX',
    'L_middle': '4edc$EDC',
    'L_index': '5rfv6tgb%RFV^TGB',

    'R_index': '7yhn8ujm&YHN*UJM',
    'R_middle': '9ik,(IK<',
    'R_ring': '0ol.)OL>',
    'R_pinky': """-p;/=[']\\_P:?+{"}|""",

    'thumb': ' '
}

key_fingers = {key: finger for finger, keys in finger_keys.items() for key in keys}

finger_colors = {
    'L_pinky': 28,
    'L_ring': 2,
    'L_middle': 42,
    'L_index': 0,

    'R_index': 221,
    'R_middle': 78,
    'R_ring': 164,
    'R_pinky': 34,

    'thumb': 0
}

key_colors = {key: finger_colors[key_fingers[key]] for key in major_keys + minor_keys}
