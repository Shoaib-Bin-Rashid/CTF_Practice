import base64

def multi_decode(base64_string):
    decoded_string = base64_string
    iteration = 0
    
    while True:
        try:
            # Decode the Base64 string
            decoded_string = base64.b64decode(decoded_string).decode('utf-8')
            iteration += 1
            print(f"Decoding iteration {iteration}: {decoded_string}")
        except Exception as e:
            # Stop if the string is not valid Base64 or not decodable
            print("Final Decoded Result:", decoded_string)
            break

# Example usage
encoded_string = """
VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVh
RmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNk
MlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVW
VkpEVGxaYVdFMVhSbFZhTTBKUFdXdGtlbVF4V2tkWGJYUllDbUY2UWpSWmEyaFRWakpHZEdWRlZs
aGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg==
"""
multi_decode(encoded_string)
