#! /usr/bin/python3

import time
for n in (100000, 200000, 300000, 400000):
    #data = 'x'*n
    data = bytearray(n)
    start = time.time()
    b = data
    while b:
        b = b[1:]
    print('bytearray', n, time.time()-start)

for n in (100000, 200000, 300000, 400000):
    #data = 'x'*n
    data = bytes(n)
    start = time.time()
    b = memoryview(data)
    while b:
        b = b[1:]
    print('memoryview', n, time.time()-start)
