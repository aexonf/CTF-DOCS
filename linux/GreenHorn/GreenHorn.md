# Nmap Scan Report

**Host:** 10.10.11.25

**Scan Date:** 2024-07-22 17:33 WIB

**Nmap Version:** 7.94SVN (https://nmap.org)

**Host Status:** Up (0.81s latency)

## Open Ports:

### 22/tcp
- **State:** open
- **Service:** ssh
- **Version:** OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
- **SSH Host Key:**
  - 256 57:d6:92:8a:72:44:84:17:29:eb:5c:c9:63:6a:fe:fd (ECDSA)
  - 256 40:ea:17:b1:b6:c5:3f:42:56:67:4a:3c:ee:75:23:2f (ED25519)

### 80/tcp
- **State:** open
- **Service:** http
- **Version:** nginx 1.18.0 (Ubuntu)
- **HTTP Title:** Did not follow redirect to [http://greenhorn.htb/](http://greenhorn.htb/)
- **HTTP Server Header:** nginx/1.18.0 (Ubuntu)

### 3000/tcp
- **State:** open
- **Service:** unknown (possibly Gitea)
- **Fingerprint Strings:**
  - **GenericLines, Help, RTSPRequest:**
    ```
    HTTP/1.1 400 Bad Request
    Content-Type: text/plain; charset=utf-8
    Connection: close
    Request
    400 Bad Request
    ```
  - **GetRequest:**
    ```
    HTTP/1.0 200 OK
    Cache-Control: max-age=0, private, must-revalidate, no-transform
    Content-Type: text/html; charset=utf-8
    Set-Cookie: i_like_gitea=e573dc086ea82f55; Path=/; HttpOnly; SameSite=Lax
    Set-Cookie: _csrf=n3Z58w0NLf9tFwBMM38pqhOHcvI6MTcyMTY0NDQ1MDUxMjgzMzI1NA; Path=/; Max-Age=86400; HttpOnly; SameSite=Lax
    X-Frame-Options: SAMEORIGIN
    Date: Mon, 22 Jul 2024 10:34:10 GMT
    <!DOCTYPE html>
    <html lang="en-US" class="theme-auto">
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>GreenHorn</title>
    <link rel="manifest" href="data:application/json;base64,eyJuYW1lIjoiR3JlZW5Ib3JuIiwic2hvcnRfbmFtZSI6IkdyZWVuSG9ybiIsInN0YXJ0X3VybCI6Imh0dHA6Ly9ncmVlbmhvcm4uaHRiOjMwMDAvIiwiaWNvbnMiOlt7InNyYyI6Imh0dHA6Ly9ncmVlbmhvcm4uaHRiOjMwMDAvYXNzZXRzL2ltZy9sb2dvLnBuZyIsInR5cGUiOiJpbWFnZS9wbmciLCJzaXplcyI6IjUxMng1MTIifSx7InNyYyI6Imh0dHA6Ly9ncmVlbmhvcm4uaHRiOjMwMDAvYXNzZXRzL2ltZy9sb2dvLnBuZyIsInR5cGUiOiJpbWFnZS9wbmciLCJzaXplcyI6IjUxMng1MTIifV19
    ```
  - **HTTPOptions:**
    ```
    HTTP/1.0 405 Method Not Allowed
    Allow: HEAD, GET
    Cache-Control: max-age=0, private, must-revalidate, no-transform
    Set-Cookie: i_like_gitea=e95abb8a10f9e03c; Path=/; HttpOnly; SameSite=Lax
    Set-Cookie: _csrf=BC3X-6hdUE9xETB0xbmlyKutP046MTcyMTY0NDQ1OTcyMzI2MTc4NQ; Path=/; Max-Age=86400; HttpOnly; SameSite=Lax
    X-Frame-Options: SAMEORIGIN
    Date: Mon, 22 Jul 2024 10:34:19 GMT
    Content-Length: 0
    ```

**Service Info:** OS: Linux; CPE: cpe:/o:linux:linux_kernel

**Service Detection Performed:** Please report any incorrect results at [https://nmap.org/submit/](https://nmap.org/submit/)

**Scan Duration:** 236.30 seconds


# USER FLAG

1. pertama bukak ke port :3000 itu nanti ada repository gitea untuk website utama nya
2. masuk ke data -> settings -> pass.php
3. `d5443aef1b64544f3685bf112f6c405218c573c7279a831b1fe9612e3a4d770486743c5580556c0d838b51749de15530f87fb793afdcc689b6b39024d7790163`: iloveyou1
4. login password nya ke halaman /login.php

ada cme dengan nama **Pluck v4.7.18**

link exploit: https://github.com/1mirabbas/Pluck_Cms_4.7.18_RCE_Exploit

setelah di exploit masuk ke user junior

```bash
(remote) www-data@greenhorn:/home/junior$ su junior
Password: iloveyou1
junior@greenhorn:~$ cat user.txt
c9f844418470110a3291a11d8f99faa3
junior@greenhorn:~$ 
```


# ROOT FLAG

enum menggunakan linpeas.sh tidak ada hasil

curiga dengan file pdf di home nya mari kita coba download

1. pakai server php 
```php
php -S 0.0.0.0:4445
```
2. http://10.10.11.25:4445/Using%20OpenVAS.pdf
3. setelah download pakai pdfimage buat convert
4. pakai defix tool

```bash
(remote) www-data@greenhorn:/$ su root
Password: 
root@greenhorn:/# cd /root
root@greenhorn:~# ls -al
total 44
drwx------  5 root root 4096 Jul 22 15:05 .
drwxr-xr-x 20 root root 4096 Jun 20 07:06 ..
lrwxrwxrwx  1 root root    9 Jun 11 14:42 .bash_history -> /dev/null
-rw-r--r--  1 root root 3106 Oct 15  2021 .bashrc
drwx------  2 root root 4096 Jun 20 06:36 .cache
-rwxr-xr-x  1 root root  250 Jun 19 17:06 cleanup.sh
drwxr-xr-x  3 root root 4096 Jun 20 06:36 .local
lrwxrwxrwx  1 root root    9 Jun 20 05:44 .mysql_history -> /dev/null
-rw-r--r--  1 root root  161 Jul  9  2019 .profile
-rwxr-xr-x  1 root root  962 Jul 18 13:01 restart.sh
-rw-r-----  1 root root   33 Jul 22 15:05 root.txt
-rw-r--r--  1 root root   66 Jul 18 12:59 .selected_editor
drwx------  2 root root 4096 Jun 20 06:36 .ssh
root@greenhorn:~# cat root.txt
d40a28c54c400640620ab4675b8fc2e6
```

password: sidefromsidetheothersidesidefromsidetheotherside