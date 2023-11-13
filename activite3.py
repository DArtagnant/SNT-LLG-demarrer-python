### Programme modifié pour respecter les conventions d'utilisation de Tkinter en programmation impérative et fonctionnelle

#Attention créer un répertoire image_resized dans le même répertoire que ce programme et le remplire d'image numérotés de 1 à 6 inclus avant d'executer le programme

import random #récupère les fonctions liés à aléatoire pré-codés
import tkinter #module qui permet de créer des interfaces graphiques
from os.path import join

def lancer_de() -> int:
    """renvoie un entier entre 1 et 6 inclus

    Returns:
        int: -
    """
    return random.randint(1,6)
    
def affichage_lancer() -> None:
    """ remplace dans Tkinter l'image de la face du dé par une tirée au hazard
    """
    global tab_nom_image, label_de, image_de # les variables globales sont à éviter absolument en temps normal

    lancer = lancer_de() #génère un nbr aléatoire entre 1 et 6 inclus
    image_de = tkinter.PhotoImage(file = tab_nom_image[lancer]) #charge l'image en mémoire depuis le chemin d'accés stocké dans la liste tab_nom_image
    label_de.configure(image=image_de) #remplace l'image de la fenêtre en cours d'execution
    
    
#########################################################
# programme principal    
#########################################################
   
fenetre = tkinter.Tk() #création de la fenêtre
fenetre.title("Lancer de dÃ©") #changement du titre de la fenêtre
fenetre.geometry("500x530") #dimensions de la fenetre 300px de large et 120px de haut
fenetre.configure(bg = "white") #configure le fond de la fenêtre en blanc

tab_nom_image = [join("images_resized", f"{i}.gif") for i in range(0, 7)]
#crée par compréhension de liste la liste des chemins d'accés. équivalent au code suivant :
"""
tab_nom_image = []
for i in range(0, 7):
    tab_nom_image.append("images_resized\\" + str(i) + ".gif")
"""
"""
On remarquera que le code précédent permet de créer une liste dont l'index (le numéro d'accés de l'élément) pointe vers le chemins d'accés au numéro correspondant.
On a ainsi par exemple :
Liste :
[0] -> "image_resized\\0.gif"
[1] -> "image_resized\\1.gif"
[2] -> "image_resized\\2.gif"
[3] -> "image_resized\\3.gif"
[4] -> "image_resized\\4.gif"
[5] -> "image_resized\\5.gif"
[6] -> "image_resized\\6.gif"
"""

image_de = tkinter.PhotoImage(file= tab_nom_image[0]) #crée une instance PhotoImage avec par défaut l'image de chiffre 0

label_de = tkinter.Label(fenetre, image= image_de) #crée un widget Label (texte) qui contient uniquement l'image image_de
label_de.configure(bg = "white") #met le fond du widget texte contenant l'image en blanc
label_de.pack(side="top") #place le widget en haut de la fenetre

#on fait un premier tirage
affichage_lancer()

# création d'un bouton button contenant le texte 'relancer' et appelant la fonction affichage_lancer lorsqu'il est cliqué 
# notez l'absence de parenthèses 
button = tkinter.Button(fenetre, text= "Relancer", command= affichage_lancer)

button.pack(side= "bottom") #place l'image en bas de la fenetre

fenetre.mainloop() # démarre la boucle principale de Tkinter