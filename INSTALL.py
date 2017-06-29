import os
import sys
from shutil import copy2
from shutil import rmtree


class PrivilegeException(Exception):
    def __init__(self, value):
        self.paramater = value
    def __str__(self):
        return str(self.paramater)

PIP_STRING = \
"""pip must be installed for this script to function!

debian-based:   apt install python3-pip
arch-based:     pacman -S python-pip
redhat-based:   yum install python-pip

If not listed, check your favorite search engine."""


def main():
    if os.geteuid() != 0:
        raise PrivilegeException("You must have root privileges to run this install script.")
    if sys.version_info[0] < 3:
        raise Exception("Script must be run with python 3")

    print("Checking dependencies...")
    try:
        import colorama
    except ImportError:
        try: 
            import pip
        except ImportError:
            print(PIP_STRING)
            exit(-1)

        def install(package):
            pip.main(['install', package])

        print("Required module [colorama] was not found. Installing via pip.")
        install('colorama')

    print("Copying files...")
    path = '/opt/wr'
    if os.path.exists(path):
        rmtree(path)

    os.mkdir(path)
    file_queue = ['./main.py', './joblib.py', './auxiliary.py']
    for file in file_queue:
        copy2(file, path)

    print("Creating symlink...")
    try: os.remove('/usr/local/bin/wr')
    except:
        pass
    os.symlink('/opt/wr/main.py', '/usr/local/bin/wr')

    print("Successfully installed!")


if __name__ == '__main__':
    main()
