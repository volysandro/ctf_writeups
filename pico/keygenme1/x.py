#!/usr/bin/env python

from pwn import *




elf = ELF('./activate')



elf.asm(elf.symbols['check_valid_key'], 'mov eax,1\nret\n')
elf.asm(elf.symbols['validate_key'], 'mov eax,1\nret\n' )

elf.save('./new')

