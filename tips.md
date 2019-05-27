# Remote debugging with GDB

On remote:
```
gdbserver :31337 ./stack0
```

Then run gdb on local system and enter:
```
target remote <remote_ip>:31337
```
