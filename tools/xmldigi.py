#!/usr/bin/env python3
#Uso: ./decrypt_config.py <SN> config.bin

import sys
import zlib
from Crypto.Cipher import AES
from hashlib import sha256
from struct import unpack

BASE_K = "8cc72b05705d5c46"
BASE_V = "667b02a85c61c786"

ENC_HEAD_LENGTH = 0x63
DEC_HEAD_LENGTH = 0x48

if len(sys.argv) != 3:
    print ("%s <sn> <config.bin>" % sys.argv[0])
    sys.exit(1)

try:
    plain_k = BASE_K + sys.argv[1]
    plain_v = BASE_V + sys.argv[1]

    k = sha256(plain_k.encode('utf-8')).digest()
    v = sha256(plain_v.encode('utf-8')).digest()
    d = AES.new(k, AES.MODE_CBC, v[:16])

    o = d.decrypt(open(sys.argv[2], "rb").read()[ENC_HEAD_LENGTH:])

    #print (zlib.decompress(o[DEC_HEAD_LENGTH:]))

    fs = open(sys.argv[2] + ".dec", "wb")
    fs.write(o)

except (ValueError, IOError) as e:
    print ("ERROR: %s" % e)
    pass
