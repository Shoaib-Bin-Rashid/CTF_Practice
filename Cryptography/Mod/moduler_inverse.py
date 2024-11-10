from math import gcd

def modular_inverse(a, m):
    # Ensure a and m are coprime
    if gcd(a, m) != 1:
        return None  # No modular inverse if gcd(a, m) != 1
    # Using the extended Euclidean algorithm
    t, new_t = 0, 1
    r, new_r = m, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    # Adjust t to be positive
    if t < 0:
        t = t + m
    return t

# Example usage 3 modulo 𝑚=11

a = 22
m = 41
inverse = modular_inverse(a, m)
print(f"The modular inverse of {a} modulo {m} is: {inverse}")