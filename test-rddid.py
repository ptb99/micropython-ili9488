##
## Try to get read-type commands working
##

import machine
import ili9488
import utime
import ustruct

def timed_function(f, *args, **kwargs):
    def new_func(*args, **kwargs):
        t = utime.ticks_us()
        result = f(*args, **kwargs)
        delta = utime.ticks_diff(utime.ticks_us(), t)
        print('Function {} Time = {:6.3f}ms'.format(f.__name__, delta/1000))
        return result
    return new_func


@timed_function
def setup(baud, color):
    print(f'Setup with baudrate= {baud}')
    spi = machine.SPI(1, baudrate=baud, sck=machine.Pin(10), 
                      mosi=machine.Pin(11), miso=machine.Pin(12))
    print('Init:', spi)
    display = ili9488.Display(spi, dc=machine.Pin(8), 
                              cs=machine.Pin(9), rst=machine.Pin(15),
                              width=480, height=320, rotation=90)
    display.clear(color)
    return display

@timed_function
def main(display, command):
    # buf = bytearray(4)
    # display.block(50, 50, 50, 50, buf)
    # display.write_cmd(display.SET_COLUMN, *ustruct.pack(">HH", 50, 50))
    # display.write_cmd(display.SET_PAGE, *ustruct.pack(">HH", 50, 50))

    display.write_cmd(command)
    display.dc(1)

    # for i in range(4):
    #     try:
    #         display.cs(0)
    #         #b = display.spi.read(1, 0x42)
    #         b = display.spi.read(1, 0xff)
    #         display.cs(1)
    #         print(i, ': read = ', b)
    #     except Exception as e:
    #         print('FAILED with: ', e)
    #     finally:
    #         display.cs(1)

    try:
        display.cs(0)
        b = display.spi.read(6, 0)
        #b = display.spi.read(3, 0x42)
        #b = display.spi.read(6, 0xff)
        display.cs(1)
        strbuf = [hex(x) for x in b]
        print(hex(command), ' read = ', strbuf)
    except Exception as e:
        print('FAILED with: ', e)
    finally:
        display.cs(1)


if __name__ == '__main__':
    # baud = 60000000              # default from examples
    #baud = 20_000_000            # write max from data sheet(?)
    #baud =  6_666_666            # max for reads from data sheet(?)
    baud =  5_000_000            # conservative choice
    disp = setup(baud, ili9488.color565(255, 255, 0))
    #main(disp, disp.RDDID)
    #main(disp, disp.RDDST)
    #main(disp, 0xd8)  # RDIDV
    #main(disp, 0xd3)  # RDID4
    #main(disp, disp.READ_RAM)
    main(disp, 0x0c)  # RD Display COLMOD
