import os
from shutil import copy2


class PrivilegeException(Exception):
    def __init__(self, value):
        self.paramater = value
    def __str__(self):
        return str(self.paramater)


def install(package):
    pip.main(['install', package])


def main():
    if os.geteuid() is not 0:
        raise PrivilegeException("You must have root privileges to run this install script.")

    print("Checking dependencies...")
    try:
        import colorama
    except ImportError:
        try: 
            import pip
        except ImportError:
            print("pip must be installed for this script to function.")
            exit(-1)
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
