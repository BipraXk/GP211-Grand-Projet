'''
Le programme principal, celui-ci ouvre la première fenêtre sur laquelle s'affichent plusieurs choses :
- un cadre pour le nom des créateurs.
- un titre.
- des boutons correspondants a différentes actions.
'''


#import des modules necessaire au bon fonctionnement du programme
import tkinter as tk
import definition as df
import TK_GE as te
import TK_GN as tn



#creation fenetre1
fenetre1 = tk.Tk()
fenetre1.geometry("2000x1200")
fenetre1.title('Gestion Scolaire')

#Configuration du cadre affichant le titre et les noms des créateurs
names = tk.Label(fenetre1, text="Made by PUECH Titouan & BOURGEOIS Maxime", fg = '#042a5f',anchor="e")
names.place(relx=-0.02,rely=0.945,relwidth=1, relheight=0.05)

#Titre géneral
label = tk.Label(fenetre1, text = "Gestion scolaire", font = ("arial", 20), relief = "groove",bg = '#042a5f',fg='white')
label.place(relx = -0.08, rely = 0.03, relwidth = 1.2, relheight = 0.2)

#bouton gestion etudiants qui ouvre une autre fenetre, voir TK_GE
but_etu = tk.Button(fenetre1, text = "Gestion des étudiants", fg = 'white', overrelief = "groove",  bg = '#042a5f', activebackground = '#03224c', activeforeground = 'white', cursor = 'pencil', command = lambda : te.open_ge(fenetre1))
but_etu.place(relx = 0.15, rely = 0.45, relwidth = 0.225, relheight = 0.1)

#bouton gestion notes qui ouvre une autre fenetre, voir TK_GN
but_not = tk.Button(fenetre1, text = "Gestion des notes", fg = 'white', overrelief = "groove",  bg = '#042a5f', activebackground = '#03224c', activeforeground = 'white', cursor = 'pencil', command = lambda : tn.open_gn(fenetre1))
but_not.place(relx = 0.675, rely = 0.45, relwidth = 0.15, relheight = 0.1)

#bouton quitter qui enclenche la fermeture de la fenetre
quitte = tk.Button(fenetre1, text = "Quitter", fg = 'white', overrelief = "groove", bg = '#c0001a',cursor = 'X_cursor', activebackground ='#7b0011', activeforeground = 'white', command = lambda : df.close(fenetre1))
quitte.place(relx = 0.425, rely = 0.7, relwidth = 0.15, relheight = 0.1)

fenetre1.mainloop()