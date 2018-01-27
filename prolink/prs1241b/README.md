# ProLink PRS1241B ADSL2+ Wireless Modem/Router
Depends: xortool, normalize_hex, xor_decrypt.py, xor_encrypt

# How to decrypt config file
- Download current configuration from router with web configurator
- Execute <code>$ xortool <MAC>.cfg -l 256 -c 22</code> to try decrypt config file
or
- Execute <code>$ ./normalize_key xortool_out/<?>.txt && mv <MAC>.cfg encrypted.xor && mv xortool_out/<?>.txt.hex keyfile</code>
- Execute <code>$ ./xor_decrypt.py</code>

# How to encrypt config file
- Execute <code>$ cat decrypted.txt | ./xor_encrypt keyfile > new_config.cfg</code>

# How to connect via SSH:
- Open /etc/ssh/ssh_config and enable cipher des-cbc
- Connect to router, execute <code>$ ssh -oKexAlgorithms="+diffie-hellman-group1-sha1" admin@192.168.1.1</code>

# Read more: 
- https://blog.fpmurphy.com/2017/02/decrypt-prolink-adsl2-modem-configuration-file-to-reveal-backdoor.html
- https://www.phcorner.net/threads/280265/
	
