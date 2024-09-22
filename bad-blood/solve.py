from pwn import *

r = remote('chal.competitivecyber.club', 10001)

r1 = b'Invoke-P0wnedshell.ps1'
r2 = b'Invoke-UrbanBishop.ps1'
r3 = b'WinRM'
r4 = b'Covenant'
r.sendline(r1)
print(r.recv())
r.sendline(r2)
print(r.recv())
r.sendline(r3)
print(r.recv())
r.sendline(r4)
r.interactive()