"""ILI9488 demo (w/ fonts) on RPi Pico with Waveshare Pico-ResTouch-LCD-3.5."""
from ili9488 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont
import time

def test():
    """Test code."""
    # Baud rate of 60000000 seems about the max
    spi = SPI(1, baudrate=60000000, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
    display = Display(spi, dc=Pin(8), cs=Pin(9), rst=Pin(15),
                      width=480, height=320, rotation=90)

    display.clear(color565(255,0,0))
    print('wrote clear RED')
    time.sleep(1)
    display.draw_rectangle(100, 100, 100, 100, 0xffff)
    print('wrote outline WHITE')
    display.fill_hrect(200, 150, 100, 100, color565(0,255,0))
    print('wrote hrect GREEN')
    time.sleep(1)

    print('Loading fonts...')
    print('Loading arcadepix')
    arcadepix = XglcdFont('fonts/ArcadePix9x11.c', 9, 11)
    print('Loading bally')
    bally = XglcdFont('fonts/Bally7x9.c', 7, 9)
    time.sleep(1)

    display.draw_text(0, 10, "This's a small test!", arcadepix, 
                      color565(255, 255, 255))
    display.draw_text(0, 100, 'Bally 7x9', bally, color565(0, 255, 0))
    display.draw_text8x8(0, 150, 'Built-in 8x8', color565(0, 255, 255))

    display.draw_line(160, 0, 160, 319, color565(0, 0, 255))
    # for i in range(320):
    #     display.draw_pixel(160, i, color565(0, 0, 255))


test()
