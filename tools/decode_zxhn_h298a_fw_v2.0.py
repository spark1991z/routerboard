#!/usr/bin/env python3
#Use: ./zte_decrypt_config.py config.bin

import sys
import zlib
HEADER_MAGIC = b'\x04\x03\x02\x01\x00\x00\x00\x00\x00\x00\x00\x05' 
MODEL = "H298A"
ZLIB_HEADER_POS = 89
ZLIB_HEADER_MAGIC = b'\x78\xda'

if len(sys.argv) != 2:
    print ("%s <config.bin>" % sys.argv[0])
    sys.exit(1)

try: 
    print("Try to open file "+sys.argv[1]+"...")
    f = open(sys.argv[1],"rb")
    print("Checking header and router model...")
    hlen = len(HEADER_MAGIC)
    mlen = len(MODEL)
    rlen = hlen+mlen
    data = f.read()[:rlen]
    if len(data) != rlen:
        print("File corrupt")
        sys.exit(1)
    if data[:hlen] != HEADER_MAGIC:
        print("Invalid header")
        sys.exit(1)
    if  data[hlen:] != MODEL:
        print("This file is not for "+MODEL+"! Model in config is :")
        print(data[hlen:])
        sys.exit(1)     
    f.seek(ZLIB_HEADER_POS)
    print("Decompressing...")
    out = open(sys.argv[1]+".xml","wb")
    out.write(zlib.decompress(f.read()))
    print("Done.")

except (ValueError, IOError) as e:
    print ("ERROR: %s" % e)
    pass
