### Programme modifié pour respecter les conventions d'utilisation de Tkinter en programmation orienté objet (préféré aux deux autres)

#Attention créer un répertoire image_resized dans le même répertoire que ce programme et le remplire d'image numérotés de 1 à 6 inclus avant d'executer le programme

import tkinter as tk
from PIL import Image, ImageTk
from os.path import join
from random import randint

class DeFrame(tk.Frame):
    def __init__(self, parent, images, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.images = images
        self.label_de = tk.Label(self, image= self.images[0])
        self.label_de.pack(side="bottom")
        self.choose_random()
    
    def choose_random(self):
        self.label_de["image"] = self.images[randint(0, 6)]

class LanceDe(tk.Tk):
    def __init__(self, *args, **kwrgs) -> None:
        tk.Tk.__init__(self, *args, **kwrgs)
        self.images = self.load_images()
        self._des = []
        nbr_de = 3
        for i in range(nbr_de):
            self._des.append(DeFrame(self, self.images))
            self._des[-1].grid(row= 0, column= i)

        self.button = tk.Button(self, text= "Relancer", command= self.choose_random)
        self.button.grid(row= 1, column= 0, columnspan= nbr_de)
        self.mainloop()
    
    def load_images(self):
        l = []
        for n in range(0, 7):
            image = Image.open(join("images_resized", f"{n}.gif"))
            image.resize((100, 100))
            l.append(ImageTk.PhotoImage(image))
        return l
    
    def choose_random(self):
        for de in self._des:
            de.choose_random()

if __name__ == "__main__":
    LanceDe()