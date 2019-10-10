"""
Cкрипт создающий директории dir_1 - dir_9 в папке из которой запущен данный скрипт.
И второй скрипт удаляющий эти папки.
"""

import os
import sys

print('sys.argv = ', sys.argv)


def print_help():
    print("mkdir - создает папки dir_1 - dir_9")
    print("help - получение справки")
    print("remove - что бы удалить папки(dir_1 - dir_9)")


def make_dir():
    dir_name = ["dir_1", "dir_2", "dir_3", "dir_4", "dir_5", "dir_6", "dir_7", "dir_8", "dir_9"]
    for i in dir_name:
        dir_path = os.path.join(os.getcwd(), i)
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print("Такая директория {} уже создана".format(i))


def remove():
    dir_name = ["dir_1", "dir_2", "dir_3", "dir_4", "dir_5", "dir_6", "dir_7", "dir_8", "dir_9"]
    for i in dir_name:
        os.removedirs(i)
    print("Все папки dir_1-dir_9 были удалены")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "remove": remove
}

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан не верный ключ")
        print("Используйте help")
