from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists("key.key"):
        generate_key()
    return open("key.key", "rb").read()

def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    with open("encrypted_message.txt", "wb") as file:
        file.write(encrypted_message)

def decrypt_message():
    key = load_key()
    f = Fernet(key)
    with open("encrypted_message.txt", "rb") as file:
        encrypted_message = file.read()
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

def main():
    choice = input("Do you want to (1) encrypt a new message or (2) decrypt the existing message? ")
    if choice == "1":
        message = input("Enter the message to encrypt: ")
        encrypt_message(message)
        print("Message encrypted and saved to encrypted_message.txt")
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
