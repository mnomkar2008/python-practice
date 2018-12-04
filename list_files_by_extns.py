
"""

List files by extensions
Group files along with their extensions

"""

from os import path

def get_dir_contents(path):
    
    import os
    contents = os.listdir(path)
    return contents 

def show_files(filepath):
    
    files = get_dir_contents(filepath)
    files_only = [item for item in files if path.isfile(item)]
    
    # Print them
    print "="*50
    print "{0} files in {1} are : ".format( len(files_only), path.abspath(filepath))
    print "="*50
    for index, fitem in enumerate(files_only):
        print index + 1, fitem


def show_dirs(dirpath):
    
    dirs= get_dir_contents(dirpath)
    dirs_only = [item for item in dirs if path.isdir(item)]
    
    # Print them
    print "="*50
    print "{0} dirs in {1} are : ".format( len(dirs_only), path.abspath(dirpath))
    print "="*50
    for index, ditem in enumerate(dirs_only):
        print index + 1, ditem


if __name__ == '__main__':
    show_files('/home/omkar/omkar')
    show_dirs('/home/omkar/omkar')

