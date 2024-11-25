from math import gcd
def pollards_rho(n):
    if n % 2 == 0:
        return 2
    x = 2; y = 2; d = 1
    f = lambda x: (x**2 + 1) % n
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
    return d if d != n else None

# Example usage
N = 882564595536224140639625987659416029426239230804614613279163
factor = pollards_rho(N)
print(f"Found factor: {factor}")
