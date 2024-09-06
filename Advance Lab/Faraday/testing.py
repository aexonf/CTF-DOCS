import hashlib

def crack_sha256_hash(known_salt, hash_to_crack, password_list):
    for password in password_list:
        # Generate hash with the given salt and password
        hash_object = hashlib.sha256((known_salt + password).encode())
        if hash_object.hexdigest() == hash_to_crack:
            return password
    return None

# Example hash and salt
salt = 'vb2dtlCwXbyvHvId'
hash_to_crack = '994185cec3cae36fe6de7f579377e0e78b854d76b81ab37423e8a3b009b1af28'

# Example password list (for demo purposes, this should be a larger list or generated dynamically)
password_list = ['password123', '123456', 'password', 'admin', 'aexon']

# Crack the hash
cracked_password = crack_sha256_hash(salt, hash_to_crack, password_list)

if cracked_password:
    print(f'Password found: {cracked_password}')
else:
    print('Password not found')

