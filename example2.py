# Example using backupdir
'''
The program copies the source directory (with all files and subdirectories) to the specified LOCAL location and zips it.
Created by IgorMan, 2023
https://igorman2005.github.io/
'''
import backupdir

# ARCHIVE NETWORK
SOURCE_DIR = '\\\\192.168.100.1\\source' 
TARGET_DIR = '\\\\192.168.100.2\\target'

backupdir.archive_local(SOURCE_DIR, TARGET_DIR)

