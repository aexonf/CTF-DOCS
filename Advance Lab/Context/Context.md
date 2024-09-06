

# PORT Open

```bash
┌─[aexon@parrot]─[~]
└──╼ $nmap -sV -sC 10.13.37.12 -Pn
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-06-21 12:52 WIB
Stats: 0:00:46 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 33.33% done; ETC: 12:53 (0:00:16 remaining)
Nmap scan report for 10.13.37.12
Host is up (0.53s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
443/tcp  open  https?
| ssl-cert: Subject: commonName=WMSvc-SHA2-WEB
| Not valid before: 2020-10-12T18:31:49
|_Not valid after:  2030-10-10T18:31:49
1433/tcp open  ms-sql-s      Microsoft SQL Server 2019 15.00.2070.00; GDR1
| ms-sql-info: 
|   10.13.37.12:1433: 
|     Version: 
|       name: Microsoft SQL Server 2019 GDR1
|       number: 15.00.2070.00
|       Product: Microsoft SQL Server 2019
|       Service pack level: GDR1
|       Post-SP patches applied: false
|_    TCP port: 1433
| ms-sql-ntlm-info: 
|   10.13.37.12:1433: 
|     Target_Name: TEIGNTON
|     NetBIOS_Domain_Name: TEIGNTON
|     NetBIOS_Computer_Name: WEB
|     DNS_Domain_Name: TEIGNTON.HTB
|     DNS_Computer_Name: WEB.TEIGNTON.HTB
|     DNS_Tree_Name: TEIGNTON.HTB
|_    Product_Version: 10.0.17763
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=WEB.TEIGNTON.HTB
| Not valid before: 2024-06-12T13:37:50
|_Not valid after:  2024-12-12T13:37:50
| rdp-ntlm-info: 
|   Target_Name: TEIGNTON
|   NetBIOS_Domain_Name: TEIGNTON
|   NetBIOS_Computer_Name: WEB
|   DNS_Domain_Name: TEIGNTON.HTB
|   DNS_Computer_Name: WEB.TEIGNTON.HTB
|   DNS_Tree_Name: TEIGNTON.HTB
|   Product_Version: 10.0.17763
|_  System_Time: 2024-06-21T05:54:49+00:00
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: -1s, deviation: 0s, median: -1s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 195.42 seconds

```


# FLAG 1

open this url in browser view-source:https://10.13.37.12/Home/Staff
CONTEXT{s3cur1ty_thr0ugh_0bscur1ty}

