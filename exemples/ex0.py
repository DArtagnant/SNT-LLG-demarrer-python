# script bonjour. py
from tkinter import *
# Création de la fenêtre principale (main window)
Mafenetre = Tk()
# Création d'un widget Label (texte 'Bonj our tout le monde
Label1 = Label(Mafenetre, text= 'Bonjour tout le monde')
# Positionnement du widget avec la méthode pack ( )
Label1.pack()
# Création d'un widget Button (bouton Quitter)
Boutonl = Button(Mafenetre, text= 'Quitter' , command=Mafenetre.destroy)
Boutonl.pack()
# Lancement du gestionnaire d' événements
Mafenetre.mainloop()