# ZTE ZXHN Series Wireless/VoIP Router
<b>Needs tools</b>: decode_zxhn_h298a_fw_vX.Y<br>
<b>Supported models</b>: h298a_v1.1,h298a_v2.0, h118n, ...


### How to decrypt config file
><small>With as web configurator, download configation file if it possible.<br>With as <b>decode_zxhn_h298a_fw_vX.Y</b>, decrypt it file

><b>Note:</b> You can get manual for current script on tools page
></small>
  
### How to sign in web configurator via any available login
>Get password for him from decrypted config file

### How to connect via SSH
><small>For example, here will used firmware v1.1.
Connect to router with username <b>admin</b> and password <b>admin</b>
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
