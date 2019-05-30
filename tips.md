# Remote debugging with GDB

On remote:
```
gdbserver :31337 ./stack0
```

Then run gdb on local system and enter:
```
target remote <remote_ip>:31337
```
# Injecting payloads

See [this](https://reverseengineering.stackexchange.com/questions/13928/managing-inputs-for-payload-injection) StackExchange post
