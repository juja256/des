from des import *

file1 = open("sonets.txt", "r").read()
key = bitarray(56)
key[20:23] = 1
key[31:34] = 1
key[0:3] = 1 
d = DES(key='helloam', data="abcdefgh").encrypt()
a = DES(key='helloam', data=d).decrypt()
