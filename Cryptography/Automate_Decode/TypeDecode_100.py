from pwn import *  # pip install pwntools
import json
import base64
import codecs
from Crypto.Util.number import long_to_bytes
import time

# Connect to the server
r = remote('socket.cryptohack.org', 13377, level='debug')

# Helper functions to send/receive JSON data
def json_recv():
    try:
        line = r.recvline()
        if not line:
            return None
        data = json.loads(line.decode())
        print(f"Received JSON: {data}")  # Debug print
        return data
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e} on line {line}")
        return None

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)
    print(f"Sent JSON: {hsh}")  # Debug print

# Decoding functions for each type of encoding
def decode_base64(encoded):
    return base64.b64decode(encoded).decode()

def decode_hex(encoded):
    return bytes.fromhex(encoded).decode()

def decode_rot13(encoded):
    return codecs.decode(encoded, 'rot_13')

def decode_bigint(encoded):
    return long_to_bytes(int(encoded, 16)).decode()

def decode_utf8(encoded):
    return ''.join(chr(i) for i in encoded)

# Main loop to handle all challenge levels
while True:
    # Receive the encoded message
    received = json_recv()
    if not received:
        print("No data received, exiting.")
        break

    # Check for a flag in the response
    if "flag" in received:
        print(f"Flag: {received['flag']}")
        break

    # Get the encoding type and value, and decode accordingly
    encoding_type = received.get("type")
    encoded_value = received.get("encoded")

    if encoding_type not in ["base64", "hex", "rot13", "bigint", "utf-8"]:
        print(f"Unknown encoding type: {encoding_type}")
        break

    try:
        # Decode based on encoding type
        if encoding_type == "base64":
            decoded_value = decode_base64(encoded_value)
        elif encoding_type == "hex":
            decoded_value = decode_hex(encoded_value)
        elif encoding_type == "rot13":
            decoded_value = decode_rot13(encoded_value)
        elif encoding_type == "bigint":
            decoded_value = decode_bigint(encoded_value)
        elif encoding_type == "utf-8":
            decoded_value = decode_utf8(encoded_value)

        print(f"Decoded value: {decoded_value}")

        # Send the decoded value back to the server
        to_send = {"decoded": decoded_value}
        json_send(to_send)

        # Pause briefly to avoid rate-limiting issues
        time.sleep(0.1)

    except Exception as e:
        print(f"Error while decoding: {e}")
        break
