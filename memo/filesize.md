### using python os module

* `os.stat(file_name).st_size` gives the number of bytes in the file, the same as `os.path.getsize(file_name)`.
* `os.stat(file_name).st_blocks` gives the number of 512-Byte blocks used by the file, i.e. `st_blocks * 512` gives the space used by the file in Byte.

* `os.stat(file_name).st_blksize` gives the "preferred" blocksize for efficient file system I/O.


### using linux command

* `stat file_name` gives the number of bytes in `Size` field, and the number of 512-Byte blocks used by the file in `Blocks` field.





