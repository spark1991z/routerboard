# Sagemcom F@ST4320V1 Wireless Router
Depends: xortool, normalize_hex, xor_decrypt, hexedit, xor_encrypt

# How to get temporary (engineer) superadmin priority
- Open http://192.168.0.1 and skip Setup Wizard
- Set Up new password for 'admin' and switch to manual config with new password
- Open Browser console with press key F12, and write <code>superprivilege=1; cwmphideflag=0;</code>

Warning: After update page this variables will reset.

# How to decrypt config file
- Download current configuration from router with web configurator
- Execute <code>$ xortool <MAC>.cfg -l 256 -c 22</code> to try decrypt config file
or
- Execute <code>$ ./normalize_key xortool_out/<?>.txt && mv <MAC>.cfg encrypted.xor && mv xortool_out/<?>.txt.hex keyfile</code>
- Execute <code>$ ./xor_decrypt</code>

# How to encrypt config file
- Execute <code>$ cat decrypted.txt | ./xor_encrypt keyfile > new_config.cfg</code>

# How to change 'admin' to (engineer) superadmin priority
- Decrypt config
- With hexedit and searching replace <code>N="PRIORITY" V="0x2"</code> to <code>N="PRIORITY" V="0x1"</code> for 'admin'
- Encrypt config
- Upload into router with web configurator

# How to connect via SSH:
- Open /etc/ssh/ssh_config and enable cipher des-cbc
- Connect to router, execute <code>$ ssh -oKexAlgorithms="+diffie-hellman-group1-sha1" superadmin@192.168.0.1</code>

Reference: Try use password for superadmin from decrypted config file  


