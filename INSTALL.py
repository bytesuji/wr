import os
import sys
from shutil import copy2


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
    if os.geteuid() is not 0:
        raise PrivilegeException("You must have root privileges to run this install script.")
    if sys.version_info[0] < 3:
        raise Exception("Script must be run with python 3")
        exit(-1)

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
    os.mkdir(path)
    copy2('./main.py', path)
    copy2('./joblib.py', path)
    copy2('./auxiliary.py', path)

    print("Creating symlink...")
    os.symlink('/opt/wr/main.py', '/usr/local/bin/wr')
    print("Successfully installed!")


if __name__ == '__main__':
    main()
