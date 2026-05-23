import secrets
import customtkinter
import string

X = string.ascii_letters + string.digits + string.punctuation
#print(string.ascii_letters)
#printeaza caractere de la "a" la "z" si de la "A" la "Z" in ordine alfabetica
#print(string.digits)
#numere de la 0 la 9
#print(string.punctuation)
# punctuatii de la ! la ~ (se iau dupa codul ascii)
# exemplu:  ! are codul 33(minim), iar ~ are codul 126(maxim)

def buton_callback():
    parola = ""
    for _ in range(10):
        parola = parola + secrets.choice(X)
    label_parola.configure(text=parola)  # afiseaza parola in label

app = customtkinter.CTk()
app.geometry("700x400")
#setez dimensiunea aplicatiei
customtkinter.set_appearance_mode("dark")
#culoarea aplicatiei
label_parola = customtkinter.CTkLabel(app, text="Aici apare parola")
label_parola.place(x=350, y=150, anchor="center")

buton = customtkinter.CTkButton(app, text="Apasa pentru a creea o parola", command=buton_callback)
buton.place(x=350, y=200, anchor="center")

app.mainloop()
