'''
Ce programme s'effectue si le bouton 'Gestion des étudiants' est pressé. 
Cela créer la fenetre gestion etudiants dans laquelle s'affichent des boutons 
correspondants a différentes actions.
'''



#import des modules necessaire au bon fonctionnement du programme
import tkinter as tk
import definition as df
import TK_OGE as toe
from TRE import tree_etud



#ouverture fenetre si 'gestion etudiants' pressé dans TK_main
def open_ge(fenetre):
    
    #creation d'une nouvelle,fenetre
    fenetre_GE = tk.Toplevel(fenetre)
    fenetre_GE.geometry("1000x800")
    fenetre_GE.title("Gestion Etudiants")
       
    #bouton ajout etudiants pour ajouter un etudiant, voir TK_OGE
    button0 = tk.Button(fenetre_GE, text = "Ajout Etudiants", fg = 'white', overrelief = "groove", bg = '#042a5f', activebackground = '#03224c', activeforeground = 'white', cursor = 'pencil', command = lambda : toe.open_ge_add(fenetre_GE))
    button0.place(relx=0.350, rely=0, relwidth=0.2, relheight=0.1)
    
    #bouton modification etudiants pour modifier les informations d'un etudiant, voir TK_OGE
    button1 = tk.Button(fenetre_GE, text = "Modification Etudiants", fg = 'white', overrelief = "groove",bg = '#042a5f', activebackground = '#03224c', activeforeground = 'white', cursor = 'pencil', command = lambda : toe.open_ge_mod(fenetre_GE))
    button1.place(relx = 0.350, rely = 0.2, relwidth = 0.2, relheight = 0.1)
    
    #bouton supprimer etudiants pour supprimer un etudiants, ses informations et ses notes, voir TK_OGE
    button2 = tk.Button(fenetre_GE, text = "Suppresion Etudiants", fg = 'white', overrelief = "groove", bg = '#042a5f', activebackground = '#03224c', activeforeground = 'white', cursor = 'pencil', command = lambda : toe.open_ge_del(fenetre_GE))
    button2.place(relx = 0.350, rely = 0.4, relwidth = 0.2, relheight = 0.1)
    
    #bouton affichage etudiants pour afficher un tableau des etudiants avec leur informations, voir tree_etud
    button3 = tk.Button(fenetre_GE, text = "Affichage Etudiants", fg = 'white', overrelief = "groove", bg = '#042a5f', activebackground = '#03224c', activeforeground = 'white', cursor = 'pencil', command = lambda : tree_etud())
    button3.place(relx = 0.350, rely = 0.6, relwidth = 0.2, relheight = 0.1)
    
    #bouton quitter qui enclenche la fermeture de la fenetre
    button4 = tk.Button(fenetre_GE, text = "Retour",  fg = 'white', overrelief = "groove", bg = '#c0001a',cursor = 'X_cursor', activebackground ='#7b0011', activeforeground = 'white', command = lambda : df.close(fenetre_GE) )
    button4.place(relx = 0.350, rely = 0.8, relwidth = 0.2, relheight = 0.1)