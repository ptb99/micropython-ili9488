#! /usr/bin/python3

def get_color(i, j):
    return ((i & 0xff) << 8) | ((j & 0xff) | 0xf0)

def main(width, height, step):
    for base in range(0, height, step):
        left = min(step, height-base)
        pixels = (get_color(a,b).to_bytes(2, 'big')
                  for b in range(base, base+left) for a in range(width) )
        print('pixels=', bytes().join(pixels).hex())


if __name__ == '__main__':
    main(8,4,3)
