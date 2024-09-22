from pwn import *

r = remote('chal.pctf.competitivecyber.club', 9001)
#get the base64
#start decoding until we reach a valid hex string or prob when base64 throws an error or sm
def decode_until_error(encoded_string):
    while True:
        try:
            # Try decoding the Base64 string
            encoded_string = base64.b64decode(encoded_string).decode()
        except Exception:
            # Stop when decoding fails (either due to incorrect padding or decoding a non-Base64 string)
            break
    return encoded_string

for i in range(1000):
    pass