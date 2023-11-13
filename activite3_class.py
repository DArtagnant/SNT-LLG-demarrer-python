### Programme modifié pour respecter les conventions d'utilisation de Tkinter en programmation orienté objet (préféré aux deux autres)

#Attention créer un répertoire image_resized dans le même répertoire que ce programme et le remplire d'image numérotés de 1 à 6 inclus avant d'executer le programme

import tkinter as tk
from os.path import join
from random import randint

class LanceDe(tk.Tk):
    def __init__(self, *args, **kwrgs) -> None:
        super().__init__(*args, **kwrgs)

        self.wm_title = "Lancé de dés"
        self.geometry = "500x530"
        self["bg"] = "white"

        self.images = LanceDe.load_images("images_resized")

        self.label_de = tk.Label(self)
        self.label_de.pack(side="top")

        self.button = tk.Button(self, text= "Relancer", command= self.change_image_random)
        self.button.pack(side= "bottom")
        
        self.change_image_random()
        self.mainloop()

    @staticmethod
    def tire():
        return randint(1, 6)

    @staticmethod
    def load_images(path):
        return [tk.PhotoImage(file= join(path, f"{i}.gif")) for i in range(0, 7)]

    def change_image_random(self):
        self.change_image(LanceDe.tire())
    
    def change_image(self, num):
        self.label_de["image"] = self.images[num]



if __name__ == "__main__":
    LanceDe()