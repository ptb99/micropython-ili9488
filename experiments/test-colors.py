## micropython script

def color565(r, g, b):
    return (r & 0xf8) << 8 | (g & 0xfc) << 3 | b >> 3

def parse_color(color):
    r = (color & 0xf800) >> 8
    g = (color & 0x07e0) >> 3
    b = (color & 0x001f) << 3
    return (r, g, b)

def bswap16(x):
    """Convert between little-endian and big-endian colors."""
    return (x & 0xff00) >> 8 | (x & 0x00ff) << 8

def test_1():
    disp_color = 0x001F
    for i in range(0,12):
        print(f'i={i} - color= {disp_color:#x} - {parse_color(bswap16(disp_color))}')
        disp_color = disp_color << 1

if __name__ == '__main__':
    test_1()
