from pwn import *
# we have fourth and the bittysEnc

# we can decrypt bittyes to get the token

# decrement flipflops to get third then reverse xor with bittys
revflipFlops = lambda x: chr(ord(x) - 1)
fourth = 'Ocmu{9gtuf' + 'MmQg8G0eCXWi3MY9QfZ0NjCrXhzJEj50fumttU0ymp'
bittyenc = "Zfo5ibyl6t7WYtr2voUEZ0nSAJeWMcN3Qe3/+MLXoKL/p59K3jgV"
#decode bittyenc back to base64
bittyenc = base64.b64decode(bittyenc)
third = ''
for each in fourth:
    third += revflipFlops(each)
print(third)
second = base64.b64decode(third)
first = xor(bittyenc, second)
print(first)
