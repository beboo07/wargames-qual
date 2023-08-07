from Crypto.Cipher import AES
from Crypto.Util import Counter
import gzip
import os

FLAG = os.getenv("FLAG", "ASCWG{XXXX}").encode("utf-8")

def encrypt(plaintext):
    key = os.urandom(16)
    cipher = AES.new(key=key, counter=Counter.new(128), mode=AES.MODE_CTR)
    return cipher.encrypt(plaintext).hex()

if __name__ == "__main__":
    padding = input("> ").encode("utf-8")
    message = gzip.compress(FLAG + padding)
    enc = encrypt(message)
    print(enc)

