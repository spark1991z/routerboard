# Sagemcom F@ST4320V1 Wireless Router
<pre>**Needs tools**
<small>- xortool
- xor_decrypt.py
- xor_encrypt
- hexedit
- binwalk
- foremost
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
$ ssh -oKexAlgorithms="+diffie-hellman-group1-sha1" superadmin@192.168.0.1```**Note**: <i>You can try use password for superadmin from decrypted config file</i></small></pre>

<pre>**How to get temporary engineer priority**
<small>- Open http://192.168.0.1 and skip **Setup Wizard**
- Switch to manual config after set new password
- Open browser console with press key **F12** and write:```js
superprivilege=1; cwmphideflag=0;```**Warning**: <i>After update page this variables will reset.</i></small></pre>

<pre>**How to change admin to engineer priority**
<small>- With as **hexedit**, replace hex data with **N="PRIORITY" V="0x2"** to **N="PRIORITY" V="0x1"**
- Encrypt chenged config and upload into router with web configurator</small></pre>

<pre>**How to extract web content from firmware file (experimentally)**
<small>- Install **binwalk** and **foremost**```bash
$ sudo apt-get install binwalk foremost -y
```- Sign to folder who firmware file **firmware.bin** and with as **binwalk**, extract file```bash
$ binwalk -e firmware.bin
```- Sign to extracted image folder```bash
$ cd _firmware.bin.extracted
```- Now create folder and move into it all 7z files ```bash
$ mkdir -p 7z && mv *.7z 7z/
```or just remove them```bash
$ rm *.7z
```- With as **foremost**, extract web content (htm, gif, bmp, png) files```bash
$ foremost * -Q -v
```</pre>



