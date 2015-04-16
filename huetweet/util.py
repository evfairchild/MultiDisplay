import colorsys

MAX_HUE = 65536


def get_rgb_from_hex(hexstr):
    r = int('0x{}'.format(hexstr[1:3]), 16)
    g = int('0x{}'.format(hexstr[3:5]), 16)
    b = int('0x{}'.format(hexstr[5:7]), 16)

    return r, g, b


def get_hue_from_hex(hexstr):
    r, g, b = get_rgb_from_hex(hexstr)
    hsv = colorsys.rgb_to_hsv(r, g, b)

    return int(hsv[0] * MAX_HUE)
