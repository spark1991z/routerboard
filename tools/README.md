# How to encrypt file:
- Build, execute <code>$ cc -o xor_encrypt xor_encrypt.c</code>
- Usage, execute <code>$ cat source.txt | ./xor_encrypt <keyfile> > <new_encrypted_file></code>

# XORTool
- Build, execute <code>$ sudo python setup.py install</code>
- Usage, execute <code>$ xortool -h</code> <code>$ xortool <encrypted_file> -l <key_length> -c <char_hex></code>

Read more: https://github.com/hellman/xortool

