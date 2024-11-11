p = 857504083339712752489993810777
q = 1029224947942998075080348647219

n = p * q  
phi = (p-1)* (q-1)

e = 65537  
d = pow(e,-1,phi)

m = 12 
 
cipher = pow(m,e,n)
print(f"Cipher text, C = {cipher}")
print(f"Euler's totient, ϕ(N) = {phi}")
print(f"Private key, d = {d}")