from Crypto.Random import get_random_bytes
import os

# 1. Generate Random Bytes
random_bytes = get_random_bytes(16)  # Generate 16 random bytes
print(f"Random Bytes: {random_bytes.hex()}")

# 2. Generate Random Integers
random_int = int.from_bytes(get_random_bytes(4), byteorder='big')  # Convert 4 random bytes to an integer
print(f"Random Integer: {random_int}")

# 3. Generate Random Data for Cryptographic Keys
# AES keys can be 16, 24, or 32 bytes long
aes_key = get_random_bytes(32)  # Generate a 256-bit AES key
print(f"AES Key: {aes_key.hex()}")

# RSA keys typically use larger sizes
# Generate a random 2048-bit (256 bytes) value for RSA key material (not a complete key, just an example of key material size)
rsa_key_material = get_random_bytes(256)
print(f"RSA Key Material: {rsa_key_material.hex()}")

# 4. Generate Random Nonces and Salts
nonce = get_random_bytes(12)  # Generate a 12-byte nonce, suitable for many encryption schemes
salt = get_random_bytes(16)   # Generate a 16-byte salt for hashing or key derivation
print(f"Nonce: {nonce.hex()}")
print(f"Salt: {salt.hex()}")
