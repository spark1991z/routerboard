# ProLink PRS1241B ADSL2+ Wireless Modem/Router
<pre>**Needs tools**
<small>- xortool
- xor_decrypt.py
- xor_encrypt
- hexedit
- meld</small></pre>

<pre>**How to decrypt config file**
<small>- Download config file from router with web configurator
- With as **xortool**, decrypt config file```bash
$ xortool <MAC>.cfg -l 256 -c 22
```and from console or file **xortool_out/filename-key.csv**, store key for output file into file with name **keyfile**```bash
$ echo -ne "\x81\x8c ... \xa6" > keyfile
```</small></pre>

<pre>**How to again decrypt config file with exist key**
<small>- Rename config file to **encrypted.xor**```bash
$ mv <MAC>.cfg encrypted.xor
```- With as **xor_decrypt.py**, try again decrypt config file```bash
$ python xor_decrypt.py```**Note**: <i>You can use **hexedit** for modify hex data and again try to decrypt config file</i>```bash
$ hexedit keyfile```</small></pre>

<pre>**How to encrypt config file**
<small>- With as **xor_encrypt**, encrypt config file```bash
$ cat decrypted.txt | ./xor_encrypt keyfile > new_config.cfg
```**Warning**: <i>With as **meld**, check hex data for original and encrypted files to will fully equals!</i>```bash
$ meld <MAC>.cfg new_config.cfg```</small></pre>

<pre>**How to connect via SSH**
<small>- With text editor, open **/etc/ssh/ssh_config** and enable cipher **des-cbc**
- Connect to router```bash
$ ssh -oKexAlgorithms="+diffie-hellman-group1-sha1" admin@192.168.1.1```</small></pre>

<pre>**Read more**
<small>- https://blog.fpmurphy.com/2017/02/decrypt-prolink-adsl2-modem-configuration-file-to-reveal-backdoor.html
- https://www.phcorner.net/threads/280265/</small></pre>
	
