from Crypto.Hash import SHA256

# Message to be hashed
message = b'I love you'

# Hashing
# Create a SHA-256 hash object
hash_obj = SHA256.new(data=message)

# Get the hexadecimal representation of the hash
message_hash = hash_obj.hexdigest()

# Verification
# Create a new hash object for verification
verification_hash = SHA256.new(data=message).hexdigest()

# Print results
print(f"Message: {message}")
print(f"Hash: {message_hash}")
print(f"Verification Hash: {verification_hash}")
print(f"Hashes match: {message_hash == verification_hash}")  # Ensure both hashes are the same
