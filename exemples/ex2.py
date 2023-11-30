from tkinter import *
# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title('Frame widget')
Mafenetre['bg'] = 'bisque' # couleur de fond
# création d'un widget Frame dans la fenêtre principale
Frame1 = Frame(Mafenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=10, pady=10)
# création d'un second widget Frame dans la fenêtre principale
Frame2 = Frame(Mafenetre, borderwidth=2, relief=GROOVE)
Frame2.pack(side=LEFT, padx=10, pady=10)
# création d'un widget Frame... dans un widget Frame
# le widget Framel est le parent du widget Frame3
# le parent du widget Framel est le widget Mafenetre (fenêtre principale)
Frame3 = Frame (Frame1, bg="white" , borderwidth=2 , relief=GROOVE)
Frame3.pack(side=LEFT , padx=10 , pady=10 )
# création d'un widget Label et d'un widget Button dans un widget Frame
Label(Frame1, text= "RDV dentiste samedi à 15h").pack(padx= 10, pady= 10)
Button(Frame1, text="Effacer", fg= 'navy', command=Frame1.destroy).pack(padx=10, pady=10)
Label(Frame2, text="Réviser le contrôle d' info").pack(padx= 10, pady= 10)
Button(Frame2, text="Effacer", fg= 'navy' , command= Frame2.destroy).pack(padx=10, pady=10)
Label(Frame3, text="RDV dentiste à 10h").pack(padx=10, pady=10)
Button(Frame3, text="Effacer" , fg= 'navy', command= Frame3.destroy).pack(padx= 10, pady= 10)
Mafenetre.mainloop()