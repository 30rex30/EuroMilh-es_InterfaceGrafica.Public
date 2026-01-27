from tkinter import messagebox
from scripts.menu_admin import menu_admin

def login(box_user, box_password, janela_login):
    usuario = box_user.get()
    senha = box_password.get()

    # Exemplo de validação
    if usuario == "admin" and senha == "1234":
        janela_login.destroy()
        menu_admin()
    else:
        messagebox.showerror("Erro", "Credenciais inválidas!")