import tkinter as tk
from tkinter import filedialog, messagebox

class Okno:
    def __init__(self, master):
        self.master = master
        master.title("Программа")
        master.geometry("400x300")
        # ввод 1
        self.entry1 = tk.Entry(master)
        self.entry1.pack()

        # ввод 2
        self.entry2 = tk.Entry(master)
        self.entry2.pack()

        # кнопка для выбора
        self.file_button = tk.Button(master, text="Выбрать файл", command=self.choose)
        self.file_button.pack()

        #для результата
        self.resultViv = tk.Label(master, text="")
        self.resultViv.pack()

    def choose(self):  #для выбора файла
        file_path = filedialog.askopenfilename()  # открывает диалоговое окно
        if file_path:
            messagebox.showinfo("Выбранный файл", f"Выбран файл: {file_path}")

    def calc(self):
        try:
            num1 = int(self.entry1.get())
            num2 = int(self.entry2.get())
            result = num1 + num2
            self.resultViv.config(text=f"Результат сложения: {result}")
        except ValueError:
            messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректные числа.")

    def subtract(self):
        try:
            num1 = int(self.entry1.get())
            num2 = int(self.entry2.get())
            result = num1 - num2
            self.resultViv.config(text=f"Результат вычитания: {result}")
        except ValueError:
            messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректные числа.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Okno(root)
    root.mainloop()
