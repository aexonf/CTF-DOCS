import hashlib
import binascii

def pbkdf2_hash(password, salt, iterations=50000, dklen=50):
    hash_value = hashlib.pbkdf2_hmac(
        'sha256',  # hashing algorithm
        password.encode('utf-8'),  # password
        salt,  # salt
        iterations,  # number of iterations
        dklen=dklen  # key length
    )
    return hash_value

def find_matching_password(dictionary_file, target_hash, salt, iterations=50000, dklen=50):
   
    target_hash_bytes = binascii.unhexlify(target_hash)
   
   
    with open(dictionary_file, 'r', encoding='utf-8') as file:
        for line in file:
           
            password = line.strip()
           
            # generating hash
            hash_value = pbkdf2_hash(password, salt, iterations, dklen)
           
            # Check if hash is correct
            if hash_value == target_hash_bytes:
                print(f"Found password: {password}")
                return password
   
    print("Password not found.")
    return None

# Parameters
salt = binascii.unhexlify('227d873cca89103cd83a976bdac52486')  # Salt from gitea.db
target_hash = '97907280dc24fe517c43475bd218bfad56c25d4d11037d8b6da440efd4d691adfead40330b2aa6aaf1f33621d0d73228fc16' # hash from gitea.db

# Patch to dictionary
dictionary_file = '/home/aexon/tools/wordlist/rockyou.txt'

find_matching_password(dictionary_file, target_hash, salt)
