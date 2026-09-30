from cryptography.fernet import Fernet


def generate_key():
    """Generate a new encryption key."""
    return Fernet.generate_key()


def encrypt_message(message, key):
    """Encrypt a message using the provided key."""
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message


def decrypt_message(encrypted_message, key):
    """Decrypt a message using the provided key."""
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode()