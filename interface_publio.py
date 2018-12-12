from tkinter import *

# from game_functions import *
fenetre = Tk()

# importation de toutes les photos
# Harmonisation des tailles
#myWidth = 130
#myHeight = 90
# photo_ecoclass =


photo_menu = PhotoImage(file="///Users/publiocrete/Desktop/Python/pics/img_background.png")
photo_ecoclass = PhotoImage(file="///Users/publiocrete/Desktop/Python/pics/A380_Premium_Economy_Class.png")
photo_premiere = PhotoImage(file="///Users/publiocrete/Desktop/Python/pics/380_first_class.png")
photo_cockpit = PhotoImage(file="///Users/publiocrete/Desktop/Python/pics/380_cockpit.png")
photo_siege_joueur = PhotoImage(file="///Users/publiocrete/Desktop/Python/pics/eco2.png")
photo_aile = PhotoImage(file="///Users/publiocrete/Desktop/Python/pics/aile.png")


#photo_premiere.resize((myWidth,myHeight))
#photo_aile.resize((myWidth,myHeight))
#photo_siege_joueur.resize((myWidth,myHeight))
#photo_cockpit.resize((myWidth,myHeight))
# photo_kitchen =
# photo_cc_restarea =
# photo_toilet =
# photo_galley =

f = Frame(fenetre,height=100, width=200,bg='black')
f.pack_propagate(0) # don't shrink
f.pack()

f_texte=Frame(fenetre,height=100, width=200,bg='blue')
f_texte.pack_propagate(0)
f_texte.pack()




main = Canvas(fenetre, width=1000, height=800, background='black')



class Vues:
    def __init__(self):
        global main
        global premiere
        self.nom = "Votre siège"
        self.image = photo_siege_joueur
        #self.btn=Button(fenetre, text=self.nom, command=self._aller_a)
        self.portes = 3
        self.main = Canvas(fenetre, width=1000, height=800, background='black')
        self.boutons={}

    def _aller_a(self):
        global main
        main.delete(ALL)
        #fermer.pack_forget()
        #commencer.pack_forget()
        for i in range(len(AllBtn)):
            AllBtn[i].pack_forget()

        for i in range(len(self.boutons)):
            self.boutons[i].pack(side=self.boutons.get(i), padx=5, pady=5)

        main.create_image(500, 400, image=self.image)
        main.propagate(5)
        main.focus_set()
        return main.pack()


menu=Vues()
menu.nom="menu"
menu.image=photo_menu

siege_joueur = Vues()
siege_joueur.nom = "Votre siège/"


cockpit=Vues()
cockpit.nom="cockpit"
cockpit.image=photo_cockpit



premiere=Vues()
premiere.nom="Première Classe"
premiere.image=photo_premiere

aile=Vues()
aile.nom="Aile"
aile.image=photo_aile

main.create_image(500, 400, image=menu.image)
main.focus_set()
main.pack()

commencer = Button(f, text="Commencer", command=siege_joueur._aller_a)
commencer.pack(side=BOTTOM, padx=5, pady=5)

fermer=Button(f, text="Fermer", command=fenetre.quit)
fermer.pack(side=BOTTOM, padx=5, pady=5)


btn_premiere = Button(f, text="Première Classe", command=premiere._aller_a)
btn_cockpit = Button(f, text="Cockpit", command=cockpit._aller_a)
btn_siege = Button(f, text="Votre siège", command=siege_joueur._aller_a)
btn_aile=Button(f, text="aile", command=aile._aller_a)



siege_joueur.boutons={btn_premiere:BOTTOM}
cockpit.boutons={btn_premiere:BOTTOM}
premiere.boutons={btn_cockpit:BOTTOM,btn_siege:BOTTOM,btn_aile:LEFT}
aile.boutons={btn_premiere:BOTTOM}

AllBtn=[commencer,fermer,btn_cockpit,btn_siege,btn_premiere,btn_aile]

fenetre.mainloop()


#il faut resizer les images
#faire appraitres les bon boutons seulement