from cryptography.fernet import Fernet
from pathlib import Path

KEY_FILE = Path(".secret")

if KEY_FILE.exists():
    key = KEY_FILE.read_bytes()
else:
    key = Fernet.generate_key()
    KEY_FILE.write_bytes(key)

cipher = Fernet(key)

def encrypt(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt(text):
    return cipher.decrypt(text.encode()).decode()
