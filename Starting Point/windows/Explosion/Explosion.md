

```bash
┌─[aexon@parrot]─[~]
└──╼ $sudo nmap -sCV -p- 10.129.1.13 --min-rate 1000 -Pn
[sudo] password for aexon: 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-07 09:28 WIB
Nmap scan report for 10.129.1.13
Host is up (0.38s latency).
Not shown: 65521 closed tcp ports (reset)
PORT      STATE SERVICE       VERSION
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: EXPLOSION
|   NetBIOS_Domain_Name: EXPLOSION
|   NetBIOS_Computer_Name: EXPLOSION
|   DNS_Domain_Name: Explosion
|   DNS_Computer_Name: Explosion
|   Product_Version: 10.0.17763
|_  System_Time: 2024-09-07T02:28:37+00:00
| ssl-cert: Subject: commonName=Explosion
| Not valid before: 2024-09-06T02:25:03
|_Not valid after:  2025-03-08T02:25:03
|_ssl-date: 2024-09-07T02:28:46+00:00; -2m42s from scanner time.
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  msrpc         Microsoft Windows RPC
49671/tcp open  msrpc         Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: -2m42s, deviation: 0s, median: -2m42s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2024-09-07T02:28:40
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 149.79 seconds
```



---

**Questions:**


Task 1

What does the 3-letter acronym RDP stand for?
answer: Remote Desktop Protocol

Task 2

What is a 3-letter acronym that refers to interaction with the host through a command line interface?
answer: CLI

Task 3

What about graphical user interface interactions?
answer: GUI

Task 4

What is the name of an old remote access tool that came without encryption by default and listens on TCP port 23?
answer: telnet

Task 5

What is the name of the service running on port 3389 TCP?
answer: ms-wbt-server

Task 6

What is the switch used to specify the target host's IP address when using xfreerdp?
answer: /v:

  
Task 7

What username successfully returns a desktop projection to us with a blank password?
answer: Administrator

Submit Flag

Submit root flag
answer: 951fa96d7830c451b536be5a6be008a0