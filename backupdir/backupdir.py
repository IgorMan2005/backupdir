# backupdir
'''
The program copies the source directory (with all files and subdirectories) to the specified LOCAL location and zips it.
Created by IgorMan, 2023
https://igorman2005.github.io/
'''
import os
import shutil
import datetime
import zlib

# You can use this function or https://pypi.org/project/screen-cls/
def cls():
    '''
    Python script for clearing screen for any OS's: Windows, MAC, Linux created by IgorMan
    cls()
    https://pypi.org/project/screen-cls/
    '''
    os.system('cls' if os.name == 'nt' else 'clear')

def lets_begin():
    cls()
    tittle = 'BackupDir'
    print(tittle.upper())
    print('----------')
    print('Let\' Go!\n')
    return True

def folder_exists(folder):
    '''
    Check to folder exists
    '''
    if not os.path.exists(folder):
        return False    
    return True

def __folder_remove(folder):
    '''
    Remove folder if exists
    '''
    if folder_exists(folder):
        try:
            shutil.rmtree(folder)
        except:
            print(f'Can\'t remove {folder}, check your rights and try again...')
            return False
    return True

def __file_remove(file):
    '''
    Remove 1 file
    '''
    if os.path.exists(file):
        try:
            os.remove(file)
        except:
            print(f'Can\'t remove {file}, check your rights and try again...')
            return False
    return True


def folder_archive(archive_name, folder):
    '''
    Add foder to archive
    '''
    try:
        shutil.make_archive(os.path.join(folder, archive_name), 'zip', folder)
        print(f'Archive ready: {folder}.zip')
    except:
        print(f'Can\'t archive {folder}, check your rights and try again...')
        return False
    return True

# --------------

def archive_local(SOURCE_DIR, TARGET_DIR):
    '''
    The program copies the source directory (with all files and subdirectories) to the specified LOCAL location and zips it.
    Created by IgorMan, 2023
    https://igorman2005.github.io/

    archive_local(SOURCE_DIR, TARGET_DIR)
    SOURCE_DIR - source folder
    TARGET_DIR - target folder

    in TARGET_DIR will create zip archive with current date name ;)
    '''

    lets_begin()
    now = datetime.datetime.now()
    subfolder = now.strftime('%d%m%Y') 
    print(now.strftime("%d.%m.%Y %H:%M:%S"), '\n')


    if SOURCE_DIR == '':
        SOURCE_DIR=os.getcwd()

    print(f'SOURCE_DIR = {SOURCE_DIR}')
    print(f'TARGET_DIR = {TARGET_DIR}')
    print('\nWaiting...\n')

    if not folder_exists(SOURCE_DIR):        
        return False

    if not folder_exists(TARGET_DIR):        
        return False
    
    target_foder = os.path.join(TARGET_DIR, subfolder)

    if not __folder_remove(target_foder):
        return False
    
    # copy foder
    shutil.copytree(SOURCE_DIR, target_foder, dirs_exist_ok=False)
    
    # archive folder
    if folder_archive(subfolder, target_foder):
        # check existing same name archive file 
        if __file_remove(os.path.join(TARGET_DIR, (subfolder + '.zip'))):
            # move archive to TARGET_DIR
            shutil.move(os.path.join(target_foder, subfolder + '.zip'), TARGET_DIR)
            # remove target_folder
            __folder_remove(target_foder)
        
    end = datetime.datetime.now()
    print()
    print(end.strftime("%d.%m.%Y %H:%M:%S"), '\n')
    print(f'Time: {str(end - now)}\n')


if __name__ == '__main__':
    print('You can pip install backupdir and use it ;)')
