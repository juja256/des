from bitarray import *

__author__ = 'juja'


class BitUtils:
    @staticmethod
    def bitarray_to_int(b):
        size = b.length()
        c = 0
        for i in range(0, size):
            c += b[size - i - 1] * 2 ** i
        return c

    @staticmethod
    def bitarray_to_hex(b):
        return ' '.join(format(x, '02x') for x in bytearray(b.tobytes()))

    @staticmethod
    def bitarray_fancy_view(b):
        return ' '.join([b[i:i + 8].to01() for i in range(0, len(b), 8)])

    @staticmethod
    def int_to_bitarray(number, size):
        a = bitarray()

        n = number
        while n / 2 > 0:
            a.insert(0, n % 2)
            n = n / 2

        a.insert(0, 1)

        if a.length() > size:
            return a[a.length() - size:]
        else:
            return bitarray([0] * (size - a.length())) + a

    @staticmethod
    def lshift(a, count):
        return a[count:] + a[0:count]

    @staticmethod
    def rshift(a, count):
        return a[len(a) - count:] + a[:-count]

    @staticmethod
    def swap_block64(block):
        return BitUtils.rshift(block, 32)
