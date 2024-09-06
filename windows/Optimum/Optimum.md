
```bash
┌─[aexon@parrot]─[~/Desktop/ctf-main/ctf-docs/CTF/hackthebox/windows/Optimum]
└──╼ $sudo nmap -sCV -p- 10.10.10.8 --min-rate 1000 -Pn
[sudo] password for aexon: 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-06 10:32 WIB
Nmap scan report for 10.10.10.8
Host is up (0.40s latency).
Not shown: 65534 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
80/tcp open  http    HttpFileServer httpd 2.3
|_http-server-header: HFS 2.3
|_http-title: HFS /
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 216.94 seconds

```


terdapat kerentanan pada versi httpfileserver
dengan exploit refrensi: https://www.rapid7.com/db/modules/exploit/windows/http/rejetto_hfs_exec/


----
**ROOT**

```powershell
C:\Users\kostas\Desktop>systeminfo
systeminfo

Host Name:                 OPTIMUM
OS Name:                   Microsoft Windows Server 2012 R2 Standard
OS Version:                6.3.9600 N/A Build 9600
OS Manufacturer:           Microsoft Corporation
```

terdapat kerentanan pada os version nya.

saya menggunakan metasploit untuk refrensi nya saya ambil dari sini: https://www.rapid7.com/db/modules/exploit/windows/local/ms16_032_secondary_logon_handle_privesc/

