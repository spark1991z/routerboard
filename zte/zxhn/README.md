# ZTE ZXHN Series Wireless/VoIP Router
<b>Needs tools</b>: decode_zte_config<br>
<b>Supported models</b>: h298a, h118n, ...


### How to decrypt config file
><small>With as web configurator, download configation file.<br>With as <b>decode_zte_config</b>, decrypt it file
>```bash
>$ chmod +x decode_zte_config.py
>$ ./decode_zte_config.py config.bin config.xml --key <KEY>
>```
>__Note__: <i>You can use key from <b>config_v??_key</b> file. Where <b>v??</b> - Firmware version</i>
></small>
  
### How to sign in web configurator via username superadmin
>Get password from decrypted config file

### How to connect via SSH
><small>Connect to router with username <b>admin</b> and password <b>admin</b>
>```bash
>$ ssh admin@192.168.0.1
>```
>```bash
>$ ssh admin@192.168.0.1
>admin@192.168.0.1's password: 
>ZXHN H298A V1.1
>Login:
>```
  
>With username <b>superadmin</b> and password enter to Router CLI (Command Line Interface)
>```bash
>Exec commands:
>enable Turn on privileged commands.
>exit Quit from telnet.
>ping Ping the destination.
>```

>__Note__: <i>You can get password from <b>cli_v??_superadmin</b> file. Where <b>v??</b> - Firmware version</i>
  
>Turn on privileged commands with password <b>zte</b>
>```bash
>CLI> enable
>```
>```bash
>CLI# ?
>Exec commands:
>configure Enter configuration mode.
>disable Exit from privilege mode.
>exit Quit from telnet.
>ping Ping the destination.
>reboot Reboot device.
>restoredefault Reset to factory configuration.
>save Save function.
>```
></small>
----
