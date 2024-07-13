from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Key generation
key = get_random_bytes(16)  # AES key must be either 16, 24, or 32 bytes long

# Encryption
cipher = AES.new(key, AES.MODE_EAX)  # EAX mode ensures confidentiality and integrity
nonce = cipher.nonce
plaintext = b'This is a secret message'
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

print(f"Original: {plaintext}")
print(f"Ciphertext: {ciphertext}")

# Decryption
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)  # Recreate the cipher object with the same key and nonce
decrypted_message = cipher.decrypt(ciphertext)

print(f"Decrypted: {decrypted_message}")
