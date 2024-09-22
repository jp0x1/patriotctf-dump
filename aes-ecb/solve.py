from pwn import *
from rich.console import Console
import string

#!/usr/bin/env python
# context.log_level = 'debug'

max_blocks = 3
block_size = 16

def main():
    p = remote('chal.competitivecyber.club', 6001)

    max_size_secret = max_blocks * block_size
    secret = b''

    for size in range((max_size_secret - 1), -1, -1):
        # Original
        origin = b"A" * size
        p.recvuntil(b'> ')
        p.sendline(origin)
        original_blocks = p.recvline().strip()

        tmp = b"A" * size + secret
        for character in string.printable[:95]:
            cur_line = tmp + character.encode()
            p.recvuntil(b'> ')
            p.sendline(cur_line)
            candidate_blocks = p.recvline().strip()
            if original_blocks[:max_size_secret * 2] == candidate_blocks[:max_size_secret * 2]:
                secret += character.encode()
                log.info('{}'.format(secret.decode()))
                break

        if len(secret) + size <= max_size_secret - 1:
            log.success('Flag: {}'.format(secret.decode()))
            return


if __name__ == '__main__':
    main()


