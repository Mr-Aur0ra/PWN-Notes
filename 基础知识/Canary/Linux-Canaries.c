//Linux-Canaries.c
//gcc -m32 -fstack-protector -no-pie -z execstack Canaries.c -o Canaries

#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
  char buffer[12];
  gets(buffer);
  puts(buffer);
  return 0;
}
