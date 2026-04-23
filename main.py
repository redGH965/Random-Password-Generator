import tkinter as tk
from tkinter import ttk, messagebox
from password_generator import generate_password
from history_manager import add_to_history, load_history

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")
        self.root.geometry("500x400")

        # Длина пароля
        tk.Label(root, text="Длина пароля:").pack(pady=5)
        self.length_scale = tk.Scale(root, from_=4, to=32, orient=tk.HORIZONTAL, length=300)
        self.length_scale.set(12)
        self.length_scale.pack()

        # Чекбоксы
        self.use_digits = tk.BooleanVar(value=True)
        self.use_letters = tk.BooleanVar(value=True)
        self.use_special = tk.BooleanVar(value=True)

        tk.Checkbutton(root, text="Цифры", variable=self.use_digits).pack()
        tk.Checkbutton(root, text="Буквы", variable=self.use_letters).pack()
        tk.Checkbutton(root, text="Спецсимволы", variable=self.use_special).pack()

        # Кнопка генерации
        tk.Button(root, text="Сгенерировать", command=self.generate_and_show).pack(pady=10)

        # Поле для пароля
        self.password_entry = tk.Entry(root, width=40, font=('Arial', 12))
        self.password_entry.pack(pady=5)

        # История
        tk.Label(root, text="История:").pack(pady=5)
        self.history_tree = ttk.Treeview(root, columns=("password",), show="headings")
        self.history_tree.heading("password", text="Пароль")
        self.history_tree.column("password", width=400)
        self.history_tree.pack(fill=tk.BOTH, expand=True)

        self.load_history_to_table()

    def generate_and_show(self):
        try:
            length = self.length_scale.get()
            password = generate_password(
                length,
                self.use_digits.get(),
                self.use_letters.get(),
                self.use_special.get()
            )
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)
            add_to_history(password)
            self.load_history_to_table()
            messagebox.showinfo("Готово", "Пароль сгенерирован!")
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def load_history_to_table(self):
        for i in self.history_tree.get_children():
            self.history_tree.delete(i)
        for pwd in load_history():
            self.history_tree.insert("", tk.END, values=(pwd,))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
