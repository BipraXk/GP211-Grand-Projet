'''
Ce programme s'effectue si un des boutons dans TK_GN est pressé. 
Cela créer une fenetre dans laquelle s'affichent des entrées
correspondantes à différentes informations a remplir.
Chaque action definit une action a effectuer si jamais un bouton 
précis est pressé
'''

#import des modules necessaire au bon fonctionnement du programme
import tkinter as tk
import definition as df
import tkinter.ttk as ttk
tree = ttk.Treeview



#ouverture fenetre si ajout notes pressé
def  open_gn_add(fenetre):
    
    #creation fenetre
    fenetre_add_GN = tk.Toplevel(fenetre)
    fenetre_add_GN.geometry("600x800")
    fenetre_add_GN.title("Ajout d'une note")
    
    #ID etudiant entrée
    Idlabel = tk.Label(fenetre_add_GN, text = "ID de l'étudiant",font = ("arial", 10), relief = "groove",bg = '#042a5f',fg='white')
    Idlabel.place(relx = 0.36, rely = 0.28, relwidth = 0.28, relheight = 0.03)
    entry = tk.Entry(fenetre_add_GN, justify = 'center')
    entry.place(relx = 0.36, rely = 0.31, relwidth = 0.28, relheight = 0.03)
    
    #année scolaire entrée
    Idlabel = tk.Label(fenetre_add_GN, text = "Année scolaire", font = ("arial", 10), relief = "groove",bg = '#042a5f',fg='white')
    Idlabel.place(relx = 0.36, rely = 0.34, relwidth = 0.28, relheight = 0.03)
    entry1 = tk.Entry(fenetre_add_GN,justify = 'center')
    entry1.place(relx = 0.36, rely = 0.37, relwidth = 0.28, relheight = 0.03)
    
    #choix menu deroulant matière
    Classelabel = tk.Label(fenetre_add_GN, text = "Matière", font = ("arial", 10), relief = "groove",bg = '#042a5f',fg='white')
    Classelabel.place(relx = 0.36, rely = 0.4, relwidth = 0.28, relheight = 0.03)
    
    ComboClasse = ttk.Combobox(fenetre_add_GN, 
                            values=[
                                    "Mathematique",
                                    "Aeronautique",
                                    "Informatique",
                                    "Anglais",
                                    "Electronique",
                                    "Physique",
                                    "Mecanique",
                                    "Grand Projet"
                                    ],
                            state = "readonly")
    
    ComboClasse.place(relx = 0.36, rely = 0.43, relwidth = 0.28, relheight = 0.03)
    
    Idlabel = tk.Label(fenetre_add_GN, text = "Note",font = ("arial", 10), relief = "groove",bg = '#042a5f',fg='white')
    Idlabel.place(relx = 0.36, rely = 0.46, relwidth = 0.28, relheight = 0.03)
    entry2 = tk.Entry(fenetre_add_GN,justify = 'center')
    entry2.place(relx = 0.36, rely = 0.49, relwidth = 0.28, relheight = 0.03)
    
    
   #confirmation ajout 
    button1 = tk.Button(fenetre_add_GN, text = "Ajout",  fg = 'white', overrelief = "groove", bg = '#00a000',cursor = 'hand2', activebackground ='#006600', activeforeground = 'white',  command = lambda : [df.not_ajt(entry, entry1,ComboClasse, entry2), df.close(fenetre_add_GN)])
    button1.place(relx = 0.475, rely = 0.8, relwidth = 0.2, relheight = 0.05)
    
   
    #retour page pécédente
    button0 = tk.Button(fenetre_add_GN, text = "Retour",  fg = 'white', overrelief = "groove", bg = '#c0001a',cursor = 'X_cursor', activebackground ='#7b0011', activeforeground = 'white', command = lambda : df.close(fenetre_add_GN) )
    button0.place(relx = 0.275, rely = 0.8, relwidth = 0.2, relheight = 0.05)
    

#ouverture fenetre si modif notes pressé    
def open_gn_mod(fenetre):
    
    #creation fenetre
    fenetre_mod_GN = tk.Toplevel(fenetre)
    fenetre_mod_GN.geometry("1000x800")
    fenetre_mod_GN.title("Gestion notes")
    
    #ID entrée
    label1 = tk.Label(fenetre_mod_GN, text = "ID Note", font = ("arial", 10), relief = "groove",bg = '#042a5f',fg='white')
    label1.place(relx = 0.375, rely = 0.100, relwidth = 0.2, relheight = 0.025)
    entry1 = tk.Entry(fenetre_mod_GN, justify = 'center')
    entry1.place(relx = 0.375, rely = 0.125, relwidth = 0.2, relheight = 0.025)
      
    #note entrée
    label4 = tk.Label(fenetre_mod_GN, text = "Notes", font = ("arial", 10), relief = "groove",bg = '#042a5f',fg='white')
    label4.place(relx = 0.375, rely = 0.325, relwidth = 0.2, relheight = 0.025)
    entry4 = tk.Entry(fenetre_mod_GN, justify = 'center')
    entry4.place(relx = 0.375, rely = 0.350, relwidth = 0.2, relheight = 0.025)
   
    
   #confirmation ajout -> action( a definir)
    button1 = tk.Button(fenetre_mod_GN, text = "Modification",  fg = 'white', overrelief = "groove", bg = '#00a000',cursor = 'hand2', activebackground ='#006600', activeforeground = 'white', command = lambda : [df.not_mod(entry1, entry4), df.close(fenetre_mod_GN)])
    button1.place(relx = 0.475, rely = 0.8, relwidth = 0.2, relheight = 0.05)
    
   
    #retour page pécédente
    button0 = tk.Button(fenetre_mod_GN, text = "Retour",  fg = 'white', overrelief = "groove", bg = '#c0001a',cursor = 'X_cursor', activebackground ='#7b0011', activeforeground = 'white', command = lambda : df.close(fenetre_mod_GN) )
    button0.place(relx = 0.275, rely = 0.8, relwidth = 0.2, relheight = 0.05)
    
    
#ouverture fenetre si supp notes pressé        
def open_gn_del(fenetre):
    
    #creation fenetre
    fenetre_del_GN = tk.Toplevel(fenetre)
    fenetre_del_GN.geometry("1000x800")
    fenetre_del_GN.title("Gestion Notes")
    
    #ID entrée
    label1 = tk.Label(fenetre_del_GN, text = "ID de la note", font = ("arial", 10), relief = "groove",bg = '#042a5f',fg='white')
    label1.place(relx = 0.375, rely = 0.100, relwidth = 0.2, relheight = 0.025)
    entry1 = tk.Entry(fenetre_del_GN, justify = 'center')
    entry1.place(relx = 0.375, rely = 0.125, relwidth = 0.2, relheight = 0.025)
    
    #confirmation suppression
    button1 = tk.Button(fenetre_del_GN, text = "Suppression",  fg = 'white', overrelief = "groove", bg = '#00a000',cursor = 'hand2', activebackground ='#006600', activeforeground = 'white', command = lambda : [df.not_sup(entry1), df.close(fenetre_del_GN)])
    button1.place(relx = 0.475, rely = 0.8, relwidth = 0.2, relheight = 0.05)
    
    #retour page pécédente
    button0 = tk.Button(fenetre_del_GN, text = "Retour",  fg = 'white', overrelief = "groove", bg = '#c0001a',cursor = 'X_cursor', activebackground ='#7b0011', activeforeground = 'white', command = lambda : df.close(fenetre_del_GN) )
    button0.place(relx = 0.275, rely = 0.8, relwidth = 0.2, relheight = 0.05)