from bitarray import *

__author__ = 'juja'


class Permutation:

    def __init__(self, l):
        # if sorted(l) != range(1, len(l)+1):
        #	raise ValueError("List is not valid!")
        self.__bare = [i - 1 for i in l]

    def Get(self):
        return self.__bare

    def Reverse(self):
        rev = [0] * len(self.__bare)
        for i in range(0, len(self.__bare)):
            rev[self.__bare[i]] = i + 1

        return Permutation(rev)

    def Substitude(self, msg):
        """
            Substitudes all bits in input message
        """

        bits = bitarray()
        if type(msg) == str:
            bits.frombytes(msg)
        elif type(msg) == bitarray:
            bits = msg
        else:
            raise ValueError("Not valid type of input data")

        res = bitarray(bits.length() * [0])
        for i in range(0, bits.length()):
            res[i] = bits[(i / len(self.__bare)) * len(self.__bare) + self.__bare[i % len(self.__bare)]]
        return res

    def Reduce(self, block, size):
        """
        Shrinks or extends block to specified size with permutation
        """

        bits = bitarray()
        if type(block) == str:
            bits.frombytes(block)
        elif type(block) == bitarray:
            bits = block
        else:
            raise ValueError("Not valid type of input data")

        res = bitarray(size * [0])

        for i in range(0, size):
            res[i] = bits[self.__bare[i]]
        return res