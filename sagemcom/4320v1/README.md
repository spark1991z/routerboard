# Sagemcom F@ST4320V1 Wireless Router
__Needs tools__: xortool, xor_decrypt.py, xor_encrypt, hexedit, meld, binwalk, foremost

### How to decrypt config file
><small>With as web configurator, download configation file.<br>With as __xortool__, decrypt it file
>```bash
>$ xortool <MAC>.cfg -l 256 -c 22
>```
>and from console or file __xortool_out/filename-key.csv__, store key for output file into file with name __keyfile__ 
>```bash
>$ echo -ne "\x81\x8c ... \xa6" > keyfile
>```
></small>

### How to again decrypt config file with exist key
><small>Rename config file to __encrypted.xor__
>```bash
>$ mv <MAC>.cfg encrypted.xor
>```
>With as __xor_decrypt.py__, try again decrypt config file
>```bash
>$ python xor_decrypt.py
>```
>__Note__: <i>You can use __hexedit__ for modify hex data and again try to decrypt config file</i>
>```bash
>$ hexedit keyfile
>```
></small>

### How to encrypt config file
><small>With as __xor_encrypt__, encrypt config file
>```bash
>$ cat decrypted.txt | ./xor_encrypt keyfile > new_config.cfg
>```
>__Warning__: <i>With as __meld__, check hex data for original and encrypted files to will fully equals!</i>
>```bash
>$ meld <MAC>.cfg new_config.cfg
>```
></small>

### How to connect via SSH
><small>With as text editor, open __/etc/ssh/ssh_config__, enable cipher __des-cbc__ and connect to router
>```bash
>$ ssh -oKexAlgorithms="+diffie-hellman-group1-sha1" superadmin@192.168.0.1
>```
>__Note__: <i>You can get password from decrypted config file</i></small>
----
### How to get temporary engineer priority
><small>Open http://192.168.0.1 and skip __Setup Wizard__<br>Switch to manual config after set new password<br>Open browser console with press key __F12__ and write:
>```js
>superprivilege=1; cwmphideflag=0;
>```
>__Warning__: <i>After update page this variables will reset.</i></small>

### How to change admin priority to engineer
><small>With as __hexedit__, replace hex data with __N="PRIORITY" V="0x2"__ to __N="PRIORITY" V="0x1"__<br>Encrypt changed config and upload into router with web configurator</small>

### How to extract web content from firmware file (experimentally)
><small>Sign to folder who firmware file __firmware.bin__ and with as __binwalk__, extract file
>```bash
>$ binwalk -e firmware.bin
>```
>Sign to extracted image folder
>```bash
>$ cd _firmware.bin.extracted
>```
>Now create folder and move into it all 7z files
>```bash
>$ mkdir -p 7z && mv *.7z 7z/
>```
>or just remove them
>```bash
>$ rm *.7z
>```
>With as __foremost__, extract web content (htm, gif, bmp, png) files
>```bash
>$ foremost * -Q -v
>```
>__Note__: You can find content in __output__ folder.</small>


