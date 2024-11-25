from Crypto.Cipher import AES
import hashlib


c = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"
ciphertext = bytes.fromhex(c)
with open("pass.txt") as f:
    words = [w.strip() for w in f.readlines()]
for i in words:
    key = hashlib.md5(i.encode()).digest()
    cipher = AES.new(key,AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    if b'crypto' in decrypted:
        print(decrypted)