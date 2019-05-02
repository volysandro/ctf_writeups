#!/usr/bin/env python
import sys
from math import sqrt
from pwn import *
import os
import pwnlib

context.log_level = 'critical'
print "...importing pwntools..."

elf = ELF('./be-quick-or-be-dead-2')

def fib(n):
    return pow(2 << n, n + 1, (4 << 2*n) - (2 << n) - 1) % (2 << n)

if (len(sys.argv) == 1):
    print "...importing hardcoded fibonacci number..."
    fibonacci = 59288416551943338727574080408572281287377451615227988184724603969919549034666922046325034891393072356252090591628758887874047734579886068667306295291967872198822088710569576575629665781687543564318377549435421485

elif sys.argv[1] == '-c':
    print "...calculating custom fibonacci number..."
    fibonacci = fib(int(sys.argv[2]))

elif sys.argv[1] == '-f':
    print "...importing custom fibonacci from file..."
    str = open(sys.argv[2], 'r').read()
    fibonacci = int(str)


    
if sys.argv[1] == '-a':
    print "...trying to find fibonacci from binary..."
    
    
    



print "...disabling alarm method..."
elf.asm( elf.symbols['alarm'], 'ret' )


print "...overwriting 'calclate_key' method..."
elf.asm( elf.symbols['calculate_key'], 'mov eax,%s\nret\n' % ( hex(fibonacci & 0xFFFFFFFF ) ) )

print "...key returned! executing patched binary..."
elf.save('./new')

os.system('chmod +x new')

p = process('./new')

p.poll(True)

print "Flag found!"
print p.recvall().split('\n')[-2]


