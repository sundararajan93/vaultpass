#!/usr/bin/python3.6
import argparse
from cryptography.fernet import Fernet


def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key


def load_key():
    """
    Loads the key named 'secret.key' from current directory
    """
    return open("secret.key", "rb").read()


def encrypt_message(message):
    """
    Encrypts a message
    """
    key = load_key()

    encoded_msg = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_msg)

    with open("encrypted.txt", "wb") as encrypted_file:
        encrypted_file.write(encrypted_message)

    return encrypted_message


def decrypt_message(encrypted_msg):
    """
    Decrypt an encrypted message
    """
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_msg)
    return decrypted_message.decode()


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--en_crypt", help="Pass the text to encrypt as an argument")
    parser.add_argument("-d", "--de_crypt", help="Pass the text to decrypt as an argument", action="store_true")
    parser.add_argument("-k", "--key", help="Generate the 'secret.key' file", action="store_true")
    args = parser.parse_args()

    if args.en_crypt:
        try:
            enc = encrypt_message(args.en_crypt)
            print(enc)
        except FileNotFoundError:
            print("Key file not found!")
            print("Generate key file: ./vaultpass.py -k")

    if args.de_crypt:
        try:
            with open("encrypted.txt", "rb") as file:
                txt = file.read()
            print(decrypt_message(txt))
        except FileNotFoundError:
            print("Encrypted text file not found!")

    if args.key:
        result = generate_key()
        print("Key Generated -> " + str(result))


if __name__ == "__main__":
    Main()

