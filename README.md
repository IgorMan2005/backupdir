# backupdir

<img src="https://igorman2005.github.io/images/backupdir.jpg" alt="backupdir">

BackupDir (backup directory). 
The program copies the source directory (with all subdirectories) to the specified location and zips it.

## Setup
https://pypi.org/project/backupdir/

**pip install backupdir**

## Example1:
```
import backupdir

# ARCHIVE LOCAL
SOURCE_DIR = 'D:\\Documents'    # use current dir when SOURCE_DIR = ''
TARGET_DIR = "E:\\Archive\\Documents"

backupdir.archive_local(SOURCE_DIR, TARGET_DIR)

```

## Example2:
```
import backupdir

# ARCHIVE NETWORK
SOURCE_DIR = '\\\\192.168.100.1\\source' 
TARGET_DIR = "\\\\192.168.100.2\\target"

backupdir.archive_local(SOURCE_DIR, TARGET_DIR)

```


### Documentation

https://best-itpro.ru/news/backupdir/


