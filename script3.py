"""
Cкрипт создающий копию файла, из которого запущен данный скрипт
"""

import shutil


def copy_file():
    shutil.copy(r'script1.py', r'script1_copy.py')


if __name__ == '__main__':
    copy_file()
