"""
Cкрипт отображающий папки текущей директории.
"""

import os


def show_dirs():
    print(os.listdir('.'))


if __name__ == '__main__':
    show_dirs()
