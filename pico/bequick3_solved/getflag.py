#!/usr/bin/env python

from pwn import *
import os
import sys

context.log_level = 'critical'

l = 100030
mem = [None]*l


def calc(a1):
  if a1 < l and mem[a1] != None:
    return mem[a1]

  if a1 > 4:
    v1 = calc(a1 - 1)
    v2 = v1 - calc(a1 - 2)
    v3 = calc(a1 - 3)
    v4 = v3 - calc(a1 - 4) + v2
    v6 = v4 + 4660 * calc(a1 - 5)
  else:
    v6 = a1 * a1 + 9029
  
  if v6 >= 4294967296:
    v6 = v6 % 4294967296

  while v6 < 0:
    v6 += 4294967296

  if a1 < l and mem[a1] == None:
    mem[a1] = v6

  return v6


for i in range(l):
  calc(i)


key = calc(0x186B5)

elf = ELF('./be-quick-or-be-dead-3')

elf.asm( elf.symbols['set_timer'], 'ret')
elf.asm( elf.symbols['calculate_key'], 'mov eax,%s\nret\n' % (key))

elf.save('./new')

os.system('sudo chmod +x new')

p = process('./new')
p.poll(True)
print p.recvall().split('\n')[-2]


