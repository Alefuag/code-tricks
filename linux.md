
## Linux and WSL2 tricks 

`/etc/wsl.conf` - File to configure WSL2

**Mount drives on root instead of /mnt**
```ini
[automount]
enabled = true
root = /
```

**Add (or not) Windows paths to wsl path**
```ini
[interop]
appendWindowsPath = false
```



