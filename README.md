Fernet is a symmetric encryption method provided by the `cryptography` library in Python. It ensures that the data is encrypted in such a way that it can be safely stored and transmitted. Here are some key points about Fernet:

- Symmetric Encryption: Fernet uses the same key for both encryption and decryption.
- AES-128: Under the hood, Fernet uses the Advanced Encryption Standard (AES) with a 128-bit key for encryption.
- Base64 Encoding: The encrypted data is base64 encoded, making it safe for storage and transmission in text-based formats.

In the context of the provided script:
- `Fernet.generate_key()`: Generates a new symmetric encryption key.
- `Fernet(key)`: Creates a Fernet instance with the given key.
- `f.encrypt(message.encode())`: Encrypts the given message.
- `f.decrypt(encrypted_message)`: Decrypts the given encrypted message.
