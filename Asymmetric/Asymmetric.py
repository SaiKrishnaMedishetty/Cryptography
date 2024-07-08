from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import os

def generate_key_pair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open("private_key.pem", "wb") as private_file:
        private_file.write(private_pem)
    
    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open("public_key.pem", "wb") as public_file:
        public_file.write(public_pem)

def load_public_key():
    with open("public_key.pem", "rb") as public_file:
        public_key = serialization.load_pem_public_key(public_file.read())
    return public_key

def load_private_key():
    with open("private_key.pem", "rb") as private_file:
        private_key = serialization.load_pem_private_key(private_file.read(), password=None)
    return private_key

def encrypt_message(message):
    public_key = load_public_key()
    encrypted_message = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("Encrypted message:", encrypted_message.hex())  # Print the encrypted message in hexadecimal format
    with open("encrypted_message.bin", "wb") as file:
        file.write(encrypted_message)

def decrypt_message():
    private_key = load_private_key()
    with open("encrypted_message.bin", "rb") as file:
        encrypted_message = file.read()
    decrypted_message = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_message.decode()

def main():
    if not os.path.exists("private_key.pem") or not os.path.exists("public_key.pem"):
        generate_key_pair()
    
    choice = input("Do you want to (1) encrypt a new message or (2) decrypt the existing message? ")
    if choice == "1":
        message = input("Enter the message to encrypt: ")
        encrypt_message(message)
        print("Message encrypted and saved to encrypted_message.bin")
    elif choice == "2":
        try:
            decrypted_message = decrypt_message()
            print("Decrypted message:", decrypted_message)
        except Exception as e:
            print("An error occurred during decryption:", e)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
