from tkinter import * 
from tkinter import PhotoImage,messagebox
from scripts.login import login
from scripts.jogo import menu_jogo

app = Tk()
app.geometry("1920x1080")
app.title("EuroMilhões")
app.config(bg="#242323")

img_original = PhotoImage(file="/home/renatobento30/Desktop/EuroMIlhoes_main/img/LogoTIpo.png")
logo_pequeno = img_original.subsample(2, 2) 
label_logo = Label(app, image=logo_pequeno, bg="#242323")
label_logo.image = logo_pequeno 
label_logo.pack(pady=0.5)



Label(app, text="User", fg="white", bg="#242323", font=("Arial", 12)).pack(pady=(10, 0))
box_user = Entry(app, bg="white", fg="black", width=30, bd=0, relief="flat", font=("Arial", 10))
box_user.pack(pady=5, padx=50)

#  Password
Label(app, text="PassWord", fg="white", bg="#242323",font=("Arial", 12)).pack(pady=(10, 0))
box_password = Entry(app, show="*", bg="white", fg="black", width=30, bd=0, relief="flat", font=("Arial", 10))
box_password.pack(pady=5,padx=50)


Button(app, text="Login", bg="#e70130", fg="white", width=20, height=1,
       command=lambda: login(box_user, box_password, app)).pack(pady=15)

Button(app, text="Sem Login", bg="#00b120", fg="white", width=20, height=1,
       command=lambda: [app.destroy(), menu_jogo()]).pack(pady=5)

Label(app, text="© 2025 By: Renato Gonçalves Bento 11º", fg="white", bg="#242323", font=("Arial", 8)).pack(side="bottom", pady=10)

app.mainloop()   