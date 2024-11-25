from pwn import *

context.log_level='critical'
p = remote("titan.picoctf.net", 63546)

p.recvuntil(b"decrypt.")

with open("RSA\password.enc") as file:
    encp = int(file.read())

p.sendline(b"E")
p.recvuntil(b"keysize): ")
p.sendline(b"\x03")
p.recvuntil(b"mod n) ")

enc3 = int(p.recvline())

p.sendline(b"D")
p.recvuntil(b"decrypt: ")
p.sendline(str(enc3*encp).encode())
p.recvuntil(b"mod n): ")

password = int(p.recvline(), 16) // 3
password = password.to_bytes(len(str(password))-7, "big").decode("utf-8")

print("Password:", password)