from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_ssh_public_key
from cryptography.hazmat.backends import default_backend

try:
    # Load SSH public key from a file
    with open("bruce_rsa.pub", "r") as key_file:  # Replace with your actual public key file path
        ssh_public_key_data = key_file.read().strip()

    # Load the SSH public key
    public_key = load_ssh_public_key(ssh_public_key_data.encode(), backend=default_backend())

    # Ensure the public key is RSA, then extract the modulus
    if isinstance(public_key, rsa.RSAPublicKey):
        modulus = public_key.public_numbers().n
        print("Modulus as a decimal integer:", modulus)
    else:
        print("The key is not an RSA public key.")

except FileNotFoundError:
    print("The specified public key file was not found.")
except ValueError as e:
    print(f"ValueError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
