# ProLink PRS1241B ADSL2+ Wireless Modem/Router
__Needs tools__: xortool, xor_decrypt.py, xor_encrypt, hexedit, meld

### How to decrypt config file
><small>With as web configurator, download configation file. With as __xortool__, decrypt it file
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
>$ ssh -oKexAlgorithms="+diffie-hellman-group1-sha1" admin@192.168.1.1
>```
></small>

### Read more
><small>https://blog.fpmurphy.com/2017/02/decrypt-prolink-adsl2-modem-configuration-file-to-reveal-backdoor.html
>https://www.phcorner.net/threads/280265/</small>
	
