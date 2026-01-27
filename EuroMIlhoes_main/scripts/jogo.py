from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage,messagebox
import random
from scripts.menu_admin import key_gerador 


numeros_sorteados, estrelas_sorteadas = key_gerador()

print("Números sorteados:", numeros_sorteados)
print("Estrelas sorteadas:", estrelas_sorteadas)

def verificar_chave(entry_numeros, entry_estrelas):
    # Pegamos o texto das caixas
    numeros_user_txt = entry_numeros.get()
    estrelas_user_txt = entry_estrelas.get()

    try:
        if not numeros_user_txt or not estrelas_user_txt:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return

        u_nums = sorted([int(n) for n in numeros_user_txt.replace(',', ' ').split()])
        u_ests = sorted([int(e) for e in estrelas_user_txt.replace(',', ' ').split()])

        if u_nums == numeros_sorteados and u_ests == estrelas_sorteadas:
            messagebox.showinfo("Parabéns!", "Você acertou a chave!")
        else:
            messagebox.showinfo("Tente novamente", f"Chave incorreta!\nSorteio: {numeros_sorteados} Estrelas: {estrelas_sorteadas}")
            
    except ValueError:
        messagebox.showerror("Erro", "Formato inválido. Use números separados por espaços (ex: 1 10 25...)")


def menu_jogo():
    app = Tk()
    app.geometry("1920x1080")
    app.title("EuroMilhões - Jogo")
    app.config(bg="#242323")


    Label(app, text="JOGO EURO MILHÕES", fg="white", bg="#242323", font=("Arial", 20, "bold")).pack(pady=10)

    Label(app, text="Insira os Numeros", fg="white", bg="#242323", font=("Arial", 16)).pack(pady=5)
    entry_numeros = Entry(app, bg="white", fg="black", width=30, bd=0, relief="flat", font=("Arial", 12))
    entry_numeros.pack(pady=5)

    Label(app, text="Insira as Estrelas", fg="white", bg="#242323", font=("Arial", 16)).pack(pady=5)
    entry_estrelas = Entry(app, bg="white", fg="black", width=30, bd=0, relief="flat", font=("Arial", 12))
    entry_estrelas.pack(pady=5)

    Button(app, text="Vereficar", bg="#e70130", fg="white", width=20, height=1, command=lambda:verificar_chave(entry_numeros, entry_estrelas)).pack(pady=15)
    Label(app, text="© 2025 By: Renato Gonçalves Bento 11ºG", fg="white", bg="#242323", font=("Arial", 8)).pack(side="bottom", pady=10)


    app.mainloop() 