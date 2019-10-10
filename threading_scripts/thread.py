from tkinter import *
import threading

root = Tk()
root.title("Многопоточная программа")

e = Entry(root, width=17)
e.grid(row=1, column=1, padx=(1, 1))


def writer(filename, n):
    with open(filename, "w") as file:
        for i in range(n):
            file.write(str(e.get()) + "\n")


def run_tread():
    t1 = threading.Thread(target=writer, args=('text1.txt', 1,))
    t2 = threading.Thread(target=writer, args=('text2.txt', 1,))
    t1.start()
    t2.start()


b = Button(root, text="Записать символы в файл", bg="white", fg="black", font="Arial", width=22, height=1,
           command=run_tread)
b.grid(row=2, column=1, padx=(1, 1))

root.mainloop()
