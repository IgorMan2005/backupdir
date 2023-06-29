# Example using backupdir
'''
The program copies the source directory (with all files and subdirectories) to the specified LOCAL location and zips it.
Created by IgorMan, 2023
https://igorman2005.github.io/
'''
import backupdir

# ARCHIVE LOCAL
SOURCE_DIR = '' # use current dir when SOURCE_DIR = ''
TARGET_DIR = "D:\\TEMP\\backup"

backupdir.archive_local(SOURCE_DIR, TARGET_DIR)

