from Crypto.PublicKey import RSA
from Crypto.Util.asn1 import DerSequence

# Load the DER file
with open('2048b-rsa-example-cert.der', 'rb') as der_file:
    der_data = der_file.read()

# Parse the DER-encoded certificate
certificate = DerSequence().decode(der_data)

# Let's print the structure to inspect it
print(f"Certificate structure (length): {len(certificate)}")

# Check the structure of the tbsCertificate (first part of the certificate)
tbs_certificate = DerSequence().decode(certificate[0])
print(f"tbsCertificate structure (length): {len(tbs_certificate)}")

# Print out the elements to see the structure
for index, element in enumerate(tbs_certificate):
    print(f"Element {index}: {element}")

# Extract the correct element that contains the public key (check indices based on the printout)
# Try adjusting the index based on the output, likely index 5 or 6 contains the public key
subject_public_key_info = tbs_certificate[5]  # Adjust this index as necessary

# Decode the RSA public key
rsa_key = RSA.importKey(subject_public_key_info)

# Get the modulus (n) from the RSA public key
modulus = rsa_key.n

# Print the modulus in decimal form
print(f"Modulus (n): {modulus}")
