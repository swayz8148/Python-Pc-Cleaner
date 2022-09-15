import os
import subprocess
import winshell
from random import randint
from time import sleep


def main():
    file_size = os.path.getsize('C:\Windows\Temp')
    print("{} kb of data will be removed".format(file_size))
    del_dir = r'c:\windows\temp'

    # Could this just be os.rmdir(del_dir)???
    process = subprocess.Popen('rmdir /S /Q {}'.format(del_dir), shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _ = process.communicate()
    return_code = process.returncode
    if return_code == 0:
        print('Success: Cleaned Windows Temp Folder')
    else:
        print('Fail: Unable to Clean Windows Temp Folder')

    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
    sleep(randint(4, 6))
    input("Press any key to continue")


if __name__ == '__main__':
    main()
