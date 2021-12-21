'''
Ce programme s'effectue si un des boutons dans TK_GE est pressé. 
Cela créer une fenetre dans laquelle s'affichent des entrées
correspondantes a différentes informations a remplir.
Chaque action definit une action a effectuer si jamais un bouton 
précis est pressé
'''

#import des modules necessaire au bon fonctionnement du programme
import tkinter as tk
import definition as df



#ouverture fenetre si ajout etudiants pressé
def  open_ge_add(fenetre):
    
    #creation fenetre
    fenetre_add_GE = tk.Toplevel(fenetre)
    fenetre_add_GE.geometry("1000x800")
    fenetre_add_GE.title("Gestion Etudiants")
     
    #Prénom entrée
    label1 = tk.Label(fenetre_add_GE, text = "Prénom", font = ("arial", 10), relief = "groove",bg = '#042a5f',fg='white')
    label1.place(relx = 0.375, rely = 0, relwidth = 0.2, relheight = 0.025)
    entry1 = tk.Entry(fenetre_add_GE, justify = 'center')
    entry1.place(relx = 0.375, rely = 0.025, relwidth = 0.2, relheight = 0.025)
    
    #Nom entrée
    label2 = tk.Label(fenetre_add_GE, text = "Nom", font = ("arial", 10), relief = "groove",bg = '#042a5f',fg='white')
    label2.place(relx = 0.375, rely = 0.075, relwidth = 0.2, relheight = 0.025)
    entry2 = tk.Entry(fenetre_add_GE, justify = 'center')
    entry2.place(relx = 0.375, rely = 0.1, relwidth = 0.2, relheight = 0.025)
    
    #Genre choix multiple
    label3 = tk.Label(fenetre_add_GE, text = "Genre", font = ("arial", 10), relief = "groove",bg = '#042a5f',fg='white')
    label3.place(relx = 0.375, rely = 0.15, relwidth = 0.2, relheight = 0.025)
    GenreValue = tk.StringVar() 
    GenreF = tk.Radiobutton(fenetre_add_GE, text = 'Femme',
                             variable=GenreValue, value='F') 
    GenreH = tk.Radiobutton(fenetre_add_GE, text = 'Homme',
                             variable=GenreValue, value='H')
    GenreF.place(relx = 0.368, rely = 0.175, relwidth = 0.075, relheight = 0.025)
    GenreH.place(relx = 0.505, rely = 0.175, relwidth = 0.075, relheight = 0.025)
    
    #mail entrée
    label3 = tk.Label(fenetre_add_GE, text = "Mail", font = ("arial", 10), relief = "groove",bg = '#042a5f',fg='white')
    label3.place(relx = 0.375, rely = 0.225, relwidth = 0.2, relheight = 0.025)
    entry3 = tk.Entry(fenetre_add_GE, justify = 'center')
    entry3.place(relx = 0.375, rely = 0.250, relwidth = 0.2, relheight = 0.025)
    
    
    #classe entrée
    label4 = tk.Label(fenetre_add_GE, text = "Classe", font = ("arial", 10), relief = "groove",bg = '#042a5f',fg='white')
    label4.place(relx = 0.375, rely = 0.300, relwidth = 0.2, relheight = 0.025)
    entry4 = tk.Entry(fenetre_add_GE, justify = 'center')
    entry4.place(relx = 0.375, rely = 0.325, relwidth = 0.2, relheight = 0.025)
   
    #confirmation ajout 
    button1 = tk.Button(fenetre_add_GE, text = "Ajout",  fg = 'white', overrelief = "groove", bg = '#00a000',cursor = 'hand2', activebackground ='#006600', activeforeground = 'white', command = lambda : [df.etu_ajt(GenreValue, entry2, entry1, entry3, entry4),df.close(fenetre_add_GE)])
    button1.place(relx = 0.475, rely = 0.8, relwidth = 0.2, relheight = 0.05)
    
    #retour page pécédente
    button0 = tk.Button(fenetre_add_GE, text = "Retour",  fg = 'white', overrelief = "groove", bg = '#c0001a',cursor = 'X_cursor', activebackground ='#7b0011', activeforeground = 'white', command = lambda : df.close(fenetre_add_GE) )
    button0.place(relx = 0.275, rely = 0.8, relwidth = 0.2, relheight = 0.05)
    

#ouverture fenetre si modification etudiants pressé    
def open_ge_mod(fenetre):
   
    #creation fenetre
    fenetre_mod_GE = tk.Toplevel(fenetre)
    fenetre_mod_GE.geometry("1000x800")
    fenetre_mod_GE.title("Gestion Etudiants")
    
    #ID entrée
    label1 = tk.Label(fenetre_mod_GE, text = "ID", font = ("arial", 10), relief = "groove",bg = '#042a5f',fg='white',)
    label1.place(relx = 0.375, rely = 0, relwidth = 0.2, relheight = 0.025)
    entry1 = tk.Entry(fenetre_mod_GE, justify = 'center')
    entry1.place(relx = 0.375, rely = 0.025, relwidth = 0.2, relheight = 0.025)
    
    #Prénom entrée
    label2 = tk.Label(fenetre_mod_GE, text = "Prénom", font = ("arial", 10), relief = "groove",bg = '#042a5f',fg='white',)
    label2.place(relx = 0.375, rely = 0.075, relwidth = 0.2, relheight = 0.025)
    entry2 = tk.Entry(fenetre_mod_GE, justify = 'center')
    entry2.place(relx = 0.375, rely = 0.1, relwidth = 0.2, relheight = 0.025)
    
    #Nom entrée
    label3 = tk.Label(fenetre_mod_GE, text = "Nom", font = ("arial", 10), relief = "groove",bg = '#042a5f',fg='white',)
    label3.place(relx = 0.375, rely = 0.150, relwidth = 0.2, relheight = 0.025)
    entry3 = tk.Entry(fenetre_mod_GE, justify = 'center')
    entry3.place(relx = 0.375, rely = 0.175, relwidth = 0.2, relheight = 0.025)
    
    #Genre choix multiple
    label3 = tk.Label(fenetre_mod_GE, text = "Genre", font = ("arial", 10), relief = "groove",bg = '#042a5f',fg='white',)
    label3.place(relx = 0.375, rely = 0.225, relwidth = 0.2, relheight = 0.025)
    GenreValue = tk.StringVar() 
    GenreF = tk.Radiobutton(fenetre_mod_GE, text = 'Femme',
                             variable=GenreValue, value='F') 
    GenreH = tk.Radiobutton(fenetre_mod_GE, text = 'Homme',
                             variable=GenreValue, value='H')
    GenreH.deselect()
    GenreF.deselect()
    GenreF.place(relx = 0.368, rely = 0.250, relwidth = 0.075, relheight = 0.025)
    GenreH.place(relx = 0.505, rely = 0.250, relwidth = 0.075, relheight = 0.025)
    
    #Mail entrée
    label4 = tk.Label(fenetre_mod_GE, text = "Mail", font = ("arial", 10), relief = "groove",bg = '#042a5f',fg='white',)
    label4.place(relx = 0.375, rely = 0.300, relwidth = 0.2, relheight = 0.025)
    entry4 = tk.Entry(fenetre_mod_GE, justify = 'center')
    entry4.place(relx = 0.375, rely = 0.325, relwidth = 0.2, relheight = 0.025) 
    
    #Mail entrée
    label5 = tk.Label(fenetre_mod_GE, text = "Classe", font = ("arial", 10), relief = "groove",bg = '#042a5f',fg='white',)
    label5.place(relx = 0.375, rely = 0.375, relwidth = 0.2, relheight = 0.025)
    entry5 = tk.Entry(fenetre_mod_GE, justify = 'center')
    entry5.place(relx = 0.375, rely = 0.400, relwidth = 0.2, relheight = 0.025) 
    
   
    #confirmation ajout 
    button1 = tk.Button(fenetre_mod_GE, text = "Modification",  fg = 'white', overrelief = "groove", bg = '#00a000',cursor = 'hand2', activebackground ='#006600', activeforeground = 'white', command = lambda : [df.etu_mod(entry2, entry3, GenreValue, entry4, entry5, entry1), df.close(fenetre_mod_GE)])
    button1.place(relx = 0.475, rely = 0.8, relwidth = 0.2, relheight = 0.05)
    
    #retour page pécédente
    button0 = tk.Button(fenetre_mod_GE, text = "Retour",  fg = 'white', overrelief = "groove", bg = '#c0001a',cursor = 'X_cursor', activebackground ='#7b0011', activeforeground = 'white', command = lambda : df.close(fenetre_mod_GE) )
    button0.place(relx = 0.275, rely = 0.8, relwidth = 0.2, relheight = 0.05)    

    
#ouverture fenetre si supprimer etudiants pressé        
def open_ge_del(fenetre):
    
    #creation fenetre
    fenetre_del_GE = tk.Toplevel(fenetre)
    fenetre_del_GE.geometry("1000x800")
    fenetre_del_GE.title("Gestion Etudiants")
    
    #ID etudiant entrée
    labeld = tk.Label(fenetre_del_GE, text = "ID de l'étudiant", font = ("arial", 10), relief = "groove",bg = '#042a5f',fg='white',)
    labeld.place(relx = 0.375, rely = 0.250, relwidth = 0.2, relheight = 0.025)
    entry = tk.Entry(fenetre_del_GE, justify = 'center')
    entry.place(relx = 0.375, rely = 0.275, relwidth = 0.2, relheight = 0.025)
    
    #confirmation suppression 
    button1 = tk.Button(fenetre_del_GE, text = "Suppression",  fg = 'white', overrelief = "groove", bg = '#00a000',cursor = 'hand2', activebackground ='#006600', activeforeground = 'white', command = lambda :  [df.etu_sup(entry), df.close(fenetre_del_GE)])
    button1.place(relx = 0.475, rely = 0.8, relwidth = 0.2, relheight = 0.05)
    
    #retour page pécédente
    button0 = tk.Button(fenetre_del_GE, text = "Retour",  fg = 'white', overrelief = "groove", bg = '#c0001a',cursor = 'X_cursor', activebackground ='#7b0011', activeforeground = 'white', command = lambda : df.close(fenetre_del_GE) )
    button0.place(relx = 0.275, rely = 0.8, relwidth = 0.2, relheight = 0.05)