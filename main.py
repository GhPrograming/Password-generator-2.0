import secrets
import customtkinter
import string

X = string.ascii_letters + string.digits + string.punctuation

def buton_callback():
    parola = ""
    for _ in range(10):
        parola = parola + secrets.choice(X)
    label_parola.configure(text=parola) 

app = customtkinter.CTk()
app.geometry("700x400")

customtkinter.set_appearance_mode("dark")
label_parola = customtkinter.CTkLabel(app, text="Aici apare parola")
label_parola.place(x=350, y=150, anchor="center")

buton = customtkinter.CTkButton(app, text="Apasa pentru a creea o parola", command=buton_callback)
buton.place(x=350, y=200, anchor="center")

app.mainloop()
