import os
import datetime
from tkinter import *
from tkinter import ttk
import random

def key_gerador():
    nums = sorted(random.sample(range(1, 51), 5))
    stars = sorted(random.sample(range(1, 13), 2))
    return nums, stars

def menu_admin():
    app = Tk()
    app.geometry("1920x1080") 
    app.title("Painel de Gestão")
    app.config(bg="#1e1e1e")

    if not os.path.exists("Logs"): # -- se nao tiver ele cria 
        os.makedirs("Logs")

    def abrir_historico():
        janela_logs = Toplevel(app)
        janela_logs.title("Histórico de Chaves")
        janela_logs.geometry("500x400")
        janela_logs.config(bg="#2d2d2d")

        Label(janela_logs, text="HISTÓRICO DE CHAVES GERADAS", font=("Arial", 12, "bold"), 
              bg="#2d2d2d", fg="white").pack(pady=10)

        txt_area = Text(janela_logs, bg="#1e1e1e", fg="#2ecc71", font=("Consolas", 10), padx=10, pady=10)
        txt_area.pack(fill=BOTH, expand=True, padx=20, pady=10)

        caminho_arquivo = "Logs/historico_geral.txt"
        
        if os.path.exists(caminho_arquivo):
            with open(caminho_arquivo, "r") as f:
                conteudo = f.read()
                txt_area.insert(END, conteudo)

    def acao_gerar():
        nums, stars = key_gerador()
        
        numeros_label.config(text="  ".join(f"{n:02d}" for n in nums))
        estrelas_label.config(text="  ".join(f"{s:02d}" for s in stars))

        timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        caminho_arquivo = "Logs/historico_geral.txt"
        
        with open(caminho_arquivo, "a") as f:
            f.write(f"[{timestamp}] Nums: {nums} | Estrelas: {stars}\n")
        
        print(f"Chave adicionada ao histórico em: {caminho_arquivo}")

    # --- gui ---
    main_container = Frame(app, bg="#1e1e1e")
    main_container.place(relx=0.5, rely=0.5, anchor="center")

    Label(main_container, text="NÚMEROS SORTEADOS", font=("Segoe UI", 12, "bold"), bg="#1e1e1e", fg="#aaaaaa").pack()
    
    num_display = Frame(main_container, bg="#2d2d2d", padx=20, pady=10)
    num_display.pack(pady=(5, 30))
    
    numeros_label = Label(num_display, text="-- -- -- -- --", font=("Consolas", 28, "bold"), bg="#2d2d2d", fg="#2ecc71")
    numeros_label.pack()

    Label(main_container, text="ESTRELAS", font=("Segoe UI", 12, "bold"), bg="#1e1e1e", fg="#aaaaaa").pack()
    
    star_display = Frame(main_container, bg="#2d2d2d", padx=20, pady=10)
    star_display.pack(pady=(5, 40))
    
    estrelas_label = Label(star_display, text="-- --", font=("Consolas", 28, "bold"), bg="#2d2d2d", fg="#f1c40f")
    estrelas_label.pack()

    btn_gerar = ttk.Button(main_container, text="GERAR NOVA CHAVE", command=acao_gerar)
    btn_gerar.pack(ipadx=20, pady=5)

    btn_key = ttk.Button(main_container, text="VER HISTÓRICO (LOGS)", command=abrir_historico)
    btn_key.pack(ipadx=20, pady=5)

    app.mainloop()
