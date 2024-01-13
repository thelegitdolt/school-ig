def run():
    print(bytes(5))
    print(bytes([97, 98, 99]))
    print(b'abc')
    print('abc'.encode('utf-8'))
    print(bytes('abc', 'utf-8'))

    print('abc'.encode('utf-16'))
    print('abc'.encode('utf-16-le'))

    print(bytearray(5))
    print(bytearray([1, 2, 3]))
    print(bytearray('abc', 'utf-8'))
    print(bytearray('abc', 'utf-16'))

    b = bytearray('abc', 'utf-8')
    print(b)
    b[1] = 114
    print(b)

    # convert into strings
    a = bytes('abc', 'utf-8')
    print(a)
    print(a.decode('utf-8'))

    b = bytearray('abc', 'utf-16-le')
    print(b)
    bytearray(b'a\x00b\x00c\x00')
    print(b.decode('utf-16-le'))

    # concatenate bytes and bytearray
    print(a + b)  # write the answer for the last print statement