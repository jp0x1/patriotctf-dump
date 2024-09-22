from pwn import *
key_bytes = '1726595769'.encode('utf-8')

with open("output",'rb') as r:
    data_bytes = r.read()

init_key_len = len(key_bytes)
data_bytes_len = len(data_bytes)
temp1 = data_bytes_len // init_key_len
temp2 = data_bytes_len % init_key_len
key_bytes *= temp1
key_bytes += key_bytes[:temp2]

decrypt_bytes = xor(key_bytes, data_bytes)
with open('input', 'wb') as w:
    w.write(decrypt_bytes)