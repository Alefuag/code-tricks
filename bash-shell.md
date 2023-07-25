

### TODO
History Expansion
--> echo !!
--> echo !-2
...

### Basic Commands
Basics: `cd, ls, rm`, etc

`sw_vers` : show system info

`where / which / type` look for path locations (executable files)

`uname -a` system info (minimal) 

`neofetch` system info

`landscape-sysinfo` drive and memory usage

### Drives
`mount [-t type] //server/path/to/folder /path/to/local/folder`

`du -h --max-depth=1` : show all files and folder size in the current directory


### Git
- `git reset --hard origin/master` : discard local changes and sync with head of repo
- `git rev-parse --abbrev-ref HEAD` : get current branch name


### Utilities
`watch [options] [command]` : check a command output at intervals

`Ctrl + r`: reverse-i-search

`grep` : `another command | grep 'word to search'

`ln [options] origin linkname` create a link (`-s` creates a symlink)

`tree -L 2` : show a tree-like structure of current. Set depth level with `-L`

`alias cdl=" cd '$@' ; ls "`
or
`alias cdl='f(){ cd "$@"; ls ;  unset -f f; }; f'`

`cdl / cls / cdls` choose whatever you want

### Docker

`docker run [OPTIONS] IMAGE[:TAG] [COMMAND]`
-d to start in detached mode | -it to attach terminal | --name name

`docker exec [OPTIONS] CONTAINER COMMAND`
-it to attach to terminal

docker start

### mpv
`winget install mpv`


