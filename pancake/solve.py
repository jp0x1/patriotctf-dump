from pwn import *
import base64
r = remote('chal.pctf.competitivecyber.club', 9001)

for i in range(1000):
    payload = r.recvline_startswith(b'Challenge: ').decode('utf-8')
    print(payload)
    base64_str = payload.replace("Challenge: ", "").strip()
    decode_with_num = base64.b64decode(base64_str.encode())
    
    split_data = decode_with_num.split(b'|')
    b64payload = split_data[0]
    num = int(split_data[1])
   
    for j in range(num):
        try:
            b64payload = base64.b64decode(b64payload)
            
        except Exception as e:
            print(f"Error decoding: {e}")
        
    done_payload = b64payload + b'|' + str(i).encode()
    print(done_payload)
    r.sendline(done_payload)
    print(r.recv())
r.interactive()