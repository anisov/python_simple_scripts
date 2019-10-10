import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("copy - копирование файла")
    print("remove - удаление файла")
    print("cd - смена директории на")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def copy_file():
    print(os.listdir('.'))
    c = input("Какой файл вы бы хотели копировать:")
    try:
        shutil.copy(c, r'copy_{}'.format(c))
    except FileNotFoundError:
        print("Такого файла не существует")


def remove():
    print(os.listdir('.'))
    dir_name = input("Какую папку удалить?: ")
    decision = input("Вы точно хотите удалить файл Y/N?: ")
    if decision == 'Y' or decision == 'y':
        try:
            os.removedirs(dir_name)
            print("Ваша папка {} успешно удалена".format(c))
        except FileExistsError:
            print("Такой папки не существует")
    elif decision == "N" or decision == 'n':
        print("Вы вышли из программы")


def cd():
    c = input('Введите путь нужной директории: ')
    try:
        os.chdir(c)
        print("Вы перешли")
    except OSError:
        print("Невозможно перейти")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "copy": copy_file,
    "remove": remove,
    "cd": cd
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
