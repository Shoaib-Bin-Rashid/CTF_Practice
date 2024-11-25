from Crypto.Util.number import long_to_bytes
# As e = 1 
# Given value of m
m = 44981230718212183604274785925793145442655465025264554046028251311164494127485

# Try to convert m to bytes
plaintext = long_to_bytes(m)

# Print as bytes and as a string (if possible)
print("Decrypted message (raw bytes):", plaintext)

