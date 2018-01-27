#!/usr/bin/python
def xor(input, key):
    l = len(key)
    j = len(input)
    return bytearray((
        (input[i] ^ key[i % l]) for i in range(0, j)
    ))

input = bytearray(open("encrypted.xor", "rb").read())
key = bytearray(open("keyfile","rb").read())
output = xor(input, key)
open("decrypted.txt", "wb").write(output)
