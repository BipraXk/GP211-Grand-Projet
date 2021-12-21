'''
Ce programme s'effectue si le bouton 'Gestion des notes' est pressé. 
Cela créer la fenetre gestion notes dans laquelle s'affichent des boutons 
correspondants a différentes actions.
'''



#import des modules necessaire au bon fonctionnement du programme
import tkinter as tk
import definition as df
import TK_OGN as ton
from TRN import tree_note



#ouverture fenetre si 'gestion notes' pressé dans main
def open_gn (fenetre):
    
    #creation d'une nouvelle fenetre
    fenetre_GN = tk.Toplevel(fenetre)
    fenetre_GN.geometry("1000x600")
    fenetre_GN.title("Gestion Notes")
    
    #bouton ajout notes pour ajouter une note a un etudiant, voir TK_OGN
    button0 = tk.Button(fenetre_GN, text = "Ajout Notes", fg = 'white', overrelief = "groove", bg = '#042a5f', activebackground = '#03224c', activeforeground = 'white', cursor = 'pencil', command = lambda : ton.open_gn_add(fenetre_GN))
    button0.place(relx = 0.375, rely = 0, relwidth = 0.2, relheight = 0.1)
    
    #bouton modification notes pour modifier une note d'un etudiant, voir TK_OGN
    button1 = tk.Button(fenetre_GN, text = "Modification Notes", fg = 'white', overrelief = "groove",bg = '#042a5f', activebackground = '#03224c', activeforeground = 'white', cursor = 'pencil', command = lambda : ton.open_gn_mod(fenetre_GN))
    button1.place(relx = 0.375, rely = 0.2, relwidth = 0.2, relheight = 0.1)
    
    #bouton supprimer notes pour supprimer une note d'un etudiant, voir TK_OGN
    button2 = tk.Button(fenetre_GN, text = "Suppresion Notes", fg = 'white', overrelief = "groove", bg = '#042a5f', activebackground = '#03224c', activeforeground = 'white', cursor = 'pencil', command = lambda : ton.open_gn_del(fenetre_GN))
    button2.place(relx = 0.375, rely = 0.4, relwidth = 0.2, relheight = 0.1)
    
    #bouton affichage notes pour afficher un tableau avec les notes des etudiants, voir tree_note
    button3 = tk.Button(fenetre_GN, text = "Affichage Notes", fg = 'white', overrelief = "groove", bg = '#042a5f', activebackground = '#03224c', activeforeground = 'white', cursor = 'pencil', command = lambda : tree_note())
    button3.place(relx = 0.375, rely = 0.6, relwidth = 0.2, relheight = 0.1)
    
    #bouton fermeture fenetre
    button4 = tk.Button(fenetre_GN, text = "Retour",  fg = 'white', overrelief = "groove", bg = '#c0001a',cursor = 'X_cursor', activebackground ='#7b0011', activeforeground = 'white', command = lambda : df.close(fenetre_GN))
    button4.place(relx = 0.375, rely = 0.8, relwidth = 0.2, relheight = 0.1)