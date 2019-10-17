#! /usr/bin/env python3

__author__  = 'Felis-Sapiens'

import argparse
import struct
import zlib
from io import BytesIO
from os import stat
from Crypto.Cipher import AES

def read_aes_data(fd_in, key):
    enc_data = b''
    while True:
        aes_chunk_header = fd_in.read(0xC)
        if len(aes_chunk_header) != 0xC:
            print('ERROR: failed to read AES chunk header')
            return
        aes_chunk_header = struct.unpack('>3I', aes_chunk_header)
        print('AES chunk length:             ', hex(aes_chunk_header[1]))
        chunk = fd_in.read(aes_chunk_header[1])
        if len(chunk) != aes_chunk_header[1]:
            print('ERROR: failed to read AES chunk data')
            return
        enc_data += chunk
        if aes_chunk_header[2] == 0:
            break
    
    aes_cipher = AES.new(key)
    fd_out = BytesIO()
    fd_out.write(aes_cipher.decrypt(enc_data))
    fd_out.seek(0)
    return fd_out

def read_compressed_data(fd_in, enc_header):
    print('encryption header CRC32:       0x{:08X}'.format(enc_header[6]))
    header_crc = zlib.crc32(struct.pack('>6I', *enc_header[:6]))
    if enc_header[6] != header_crc:
        print("ERROR: CRC32 doesn't match")
        return
    
    crc = 0
    fd_out = BytesIO()
    while True:
        compr_chunk_header = fd_in.read(0xC)
        if len(compr_chunk_header) != 0xC:
            print('ERROR: failed to read compression chunk header')
            return
        compr_chunk_header = struct.unpack('>3I', compr_chunk_header)
        print('compressed length:            ', hex(compr_chunk_header[1]))
        print('uncompressed length:          ', hex(compr_chunk_header[0]))
        chunk = fd_in.read(compr_chunk_header[1])
        if len(chunk) != compr_chunk_header[1]:
            print('ERROR: failed to read compression chunk data')
            return
        crc = zlib.crc32(chunk, crc)
        chunk = zlib.decompress(chunk)
        if len(chunk) != compr_chunk_header[0]:
            print('ERROR: wrong length of uncompressed data')
            return
        fd_out.write(chunk)
        if compr_chunk_header[2] == 0:
            break
    
    print('compressed data CRC32:         0x{:08X}'.format(enc_header[5]))
    if enc_header[5] != crc:
        print("ERROR: CRC32 doesn't match")
        return
    fd_out.seek(0)
    return fd_out

def read_config(fd_in, fd_out, key):
    ver_header_1 = fd_in.read(0x14)
    if len(ver_header_1) != 0x14:
        print('ERROR: failed to read the first version header')
        return
    ver_header_1 = struct.unpack('>5I', ver_header_1)
    print('first version header magic:   ',
          ', '.join(map(lambda x: '0x{:08X}'.format(x), ver_header_1[:4])))
    ver_header_2_offset = 0x14 + ver_header_1[4]
    print('second version header offset: ', hex(ver_header_2_offset))
    if ver_header_1[:4] != (0x99999999, 0x44444444, 0x55555555, 0xAAAAAAAA):
        print('ERROR: expected magic is 0x99999999, 0x44444444, 0x55555555, 0xAAAAAAAA')
        return
    
    fd_in.seek(ver_header_2_offset)
    ver_header_2 = fd_in.read(0x2c)
    if len(ver_header_2) != 0x2c:
        print('ERROR: failed to read the second version header')
        return
    ver_header_2 = struct.unpack('>11I', ver_header_2)
    ver_header_3_offset = ver_header_2[10]
    print('third version header offset:  ', hex(ver_header_3_offset))
    
    fd_in.seek(ver_header_3_offset)
    ver_header_3 = fd_in.read(0x18)
    if len(ver_header_3) != 0x18:
        print('ERROR: failed to read the third version header')
        return
    ver_header_3 = struct.unpack('>2H5I', ver_header_3)
    signed_cfg_size = ver_header_3[3]
    print('signed config size:           ', hex(signed_cfg_size))
    file_size = stat(fd_in.name).st_size
    if signed_cfg_size != file_size - 0x80:
        print("ERROR: the config size (0x{:x} + 0x80) doesn't match the real file size (0x{:x})".format(signed_cfg_size, file_size))
    
    fd_in.seek(0x80)
    sign_header = fd_in.read(0xC)
    if len(sign_header) != 0xC:
        print('ERROR: failed to read signature header')
        return
    sign_header = struct.unpack('>3I', sign_header)
    print('signature header magic:        0x{:08X}'.format(sign_header[0]))
    if sign_header[0] != 0x04030201:
        print('ERROR: expected magic is 0x04030201')
        return
    print('signature length:             ', sign_header[2])
    signature = fd_in.read(sign_header[2])
    if len(signature) != sign_header[2]:
        print('ERROR: failed to read the signature')
        return
    print('signature:                    ', signature.decode())
    
    encryption_header = fd_in.read(0x3C)
    if len(encryption_header) != 0x3C:
        print('ERROR: failed to read encryption header')
        return
    encryption_header = struct.unpack('>15I', encryption_header)
    print('encryption header magic:       0x{:08X}'.format(encryption_header[0]))
    if encryption_header[0] != 0x01020304:
        print('ERROR: expected magic is 0x01020304')
        return
    enc_type = encryption_header[1]
    print('encryption type:              ', enc_type)
    
    if enc_type == 2 or enc_type == 1:
        if not key:
            print('ERROR: specify the key, i.e ' + __file__ + " config.bin config.bin.xml --key 'MIK@0STzKpB%qJZe'")
            return
        fd_in = read_aes_data(fd_in,key)
        if fd_in is None:
            return
    
    if enc_type == 2:
        encryption_header = fd_in.read(0x3C)
        if len(encryption_header) != 0x3C:
            print('ERROR: failed to read encryption header')
            return
        encryption_header = struct.unpack('>15I', encryption_header)
        print('encryption header magic:       0x{:08X}'.format(encryption_header[0]))
        if encryption_header[0] != 0x01020304:
            print('ERROR: expected magic is 0x01020304 - probably the AES key is incorrect')
            return
        enc_type = 0
    
    if enc_type == 0:
        fd_in = read_compressed_data(fd_in, encryption_header)
        if fd_in is None:
            return
    
    fd_out.write(fd_in.read())
    return


def main():
    parser = argparse.ArgumentParser(description='Decode configuration file '\
                                     '(config.bin) from ZTE routers',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog="""\
Known AES keys:
  zxhn h118n ert5 - 'MIK@0STzKpB%qJZe'
  zxhn h118n V2.1.3_ROSCNT4 - 'MIK@0STzKpB%qJZf'
  zxhn h168n v3 - '402c38de39bed665'
  zxhn h298n hv17_fv116_mts1t1 - 'Wj%2$CjM'""")
    
    parser.add_argument('infile', type=argparse.FileType('rb'),
                        help='Encoded configuration file (config.bin)')
    parser.add_argument('outfile', type=argparse.FileType('wb'),
                        help='Output file')
    parser.add_argument('--key', type=lambda x:x.encode(), default=b'',
                        help="Key for AES encryption\n\n\n")
    args = parser.parse_args()
    
    read_config(args.infile, args.outfile, args.key)

if __name__ == '__main__':
    main()