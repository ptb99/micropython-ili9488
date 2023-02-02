## micropython script

#import framebuf
import sys
import struct
import timeit

def bswap_1(x):
    return (x & 0xff00) >> 8 | (x & 0x00ff) << 8

def bswap_2(x):
    b = x.to_bytes(2, 'big')
    return int.from_bytes(b, 'little')

def bswap_3(x):
    b = struct.pack('>h', x)
    (y,) = struct.unpack('=h', b)
    return y

def alt():
    a = 0x0102
    reps= 1000000
    print('bswap_1= ', timeit.timeit(lambda: bswap_1(a), number=reps))
    print('bswap_2= ', timeit.timeit(lambda: bswap_2(a), number=reps))
    print('bswap_3= ', timeit.timeit(lambda: bswap_3(a), number=reps))
    print('sys.byteorder= ', sys.byteorder)


def main():
    buf = bytearray(16)
    fb = framebuf.FrameBuffer(buf, 4, 1, framebuf.RGB565)

    # colors
    WHITE = 0xffff
    BLACK = 0x0
    RED = 0xf800
    GREEN = 0x07d0
    BLUE = 0x001f

    fb.pixel(0,0, RED)
    fb.pixel(1,0, BLUE)
    fb.pixel(2,0, GREEN)

    print(buf)
    for i in range(4):
        color = fb.pixel(i,0)
        print(i, ': ', hex(color))

    print('sys.byteorder= ', sys.byteorder)


if __name__ == '__main__':
    #main()
    alt()
