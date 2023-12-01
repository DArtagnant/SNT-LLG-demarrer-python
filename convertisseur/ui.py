import tkinter as tk

fenetre = tk.Tk()

def conv(fun):
    def wrapped():
        nb = int(champ_saisie.get())
        nb_bin = fun(nb)
        label1.config(text= f"Conversion en {fun.__name__} : '{nb_bin}'")
    return wrapped


fenetre.geometry("300x200")
fenetre.title("CONVERTISSEUR")
fenetre.resizable(width=False, height=False)

champ_saisie = tk.Entry(
    bg= "black",
    fg= "white",
    bd= 5,
    font='helevtica',
    justify= 'center',
    )
champ_saisie.place(x= 10, y= 20, width= 180)

label1 = tk.Label(fenetre, text= "test", justify= "left")
label1.place(x= 10, y= 160, width= 180)

label2 = tk.Label(fenetre, text= "Entrez un nombre décimal :")
label2.place(x= 10, y= 0, width= 180)

b1 = tk.Button(text= "Convertir en binaire", command=conv(bin))
b1.place(x= 10, y= 60, width= 180)

b2 = tk.Button(text= "Convertir en hexadecimal", command=conv(hex))
b2.place(x= 10, y= 80, width= 180)

b3 = tk.Button(text= "Caractere ASCII", command=conv(chr))
b3.place(x= 10, y= 100, width= 180)

fenetre.mainloop()