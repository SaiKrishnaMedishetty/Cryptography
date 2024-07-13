from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Key generation
key = RSA.generate(2048)  # Generate a 2048-bit RSA key pair
private_key = key.export_key()
public_key = key.publickey().export_key()

print(f"Private Key: {private_key.decode()}")
print(f"Public Key: {public_key.decode()}")

# Signing
message = b'This is a message'
hash_obj = SHA256.new(message)  # Create a SHA-256 hash object
signature = pkcs1_15.new(key).sign(hash_obj)  # Sign the hash with the private key

print(f"Signature: {signature.hex()}")

# Verification
pub_key = RSA.import_key(public_key)  # Import the public key

try:
    pkcs1_15.new(pub_key).verify(hash_obj, signature)  # Verify the signature
    print("The signature is valid.")
except (ValueError, TypeError):
    print("The signature is not valid.")
