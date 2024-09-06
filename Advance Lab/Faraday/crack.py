#!/usr/bin/python3
from werkzeug.security import check_password_hash


hashes = open("hashes", "r")

for hash in hashes:
    hash = hash.strip()
    user = hash.split(":")[0]
    hash = hash.split(":")[1]

    with open("/root/rockyou.txt", "r", errors="ignore") as file:  
        for line in file:
            password = line.strip()
            if check_password_hash(hash, password):
                print(f"Password found: {password}")
                break
else:
    print("Password not found in the given wordlist.")
