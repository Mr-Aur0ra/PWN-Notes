//Function.c
//gcc -m32 -fno-stack-protector -no-pie -z execstack Function.c -o Function
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
  char buffer[12];
  gets(buffer);
  puts(buffer);
  return 0;
}