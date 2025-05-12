//example.c
//gcc -m32 -fno-stack-protector -no-pie -z execstack example.c -o example
//正常情况下程序始终不会执行success()函数
//我们的目的是通过栈溢出控制程序的执行流程，让程序能够执行succes()函数。

#include <stdio.h>
#include <string.h>

void success() { 
    puts("You Have already controlled it.");
}

void vulnerable() {
  char buffer[12];
  gets(buffer);
  puts(buffer);
  return;
}

int main(int argc, char **argv) {
  vulnerable();
  return 0;
}