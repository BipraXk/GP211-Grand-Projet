'''
Ce programme contient les definitions de fonctions qui seront utilis�es dans les autres programmes.
'''


#import des modules necessaire au bon fonctionnement du programme
import tkinter as tk
import tkinter.ttk as ttk
import lib_gestionEtudiants as lge
import lib_gestionNotes as lgn
import lib_commun as lc
tree = ttk.Treeview



#pour fermer une fenetre
def close(x):
    x.destroy()
    return
    

#verification et ajout, si validation, d'un etudiant    
def etu_ajt(prenom, nom, genre, email, classe):
    
    data = lc.ouverture_fichier_csv("etudiants.csv")
    
    #verification de la non-existence de l'etudiant
    for i in range(1, len(data)):
        if (str(data[i][4]) == str(email.get())) or \
                ((str(data[i][2]) == str(nom.get())) and (str(data[i][3]) == str(prenom.get()))):
            tk.messagebox.showerror("Erreur", "L'etudiant existe deja")
            return
    
    #verification du bon nombre de données entrées
    if (prenom.get() == "") or (nom.get() == "") or (email.get() == "") or (classe.get() == ""):
        tk.messagebox.showerror("Erreur", "Informations manquantes")
        return
    
    #utilisation fonction pour ajouter l'etudiant
    else:
        lge.ajoutEtudiant(prenom.get(), nom.get(), genre.get(), email.get(), classe.get())
        return


#verification et modification, si validation, d'un etudiant   
def etu_mod(prenom, nom, genre, email, classe, id):
    
    #verification du bon nombre de données entrées
    if (prenom.get() == "") or (nom.get() == "") or (email.get() == "") or (classe.get() == ""):
        tk.messagebox.showerror("Erreur", "Informations manquantes")
        return
    
    #verification de l'existence de l'etudiant et de son ID, puis modification
    else:
        data = lc.ouverture_fichier_csv("etudiants.csv")
        id_ = id.get()
        for i in range(1, len(data)):
            #utilisation fonction pour modifier l'etudiant
            if data[i][0] == id_:
                lge.modificationEtudiant(id_, prenom.get(), nom.get(), genre.get(), email.get(), classe.get())
                return
        tk.messagebox.showerror("Erreur", "ID erronné")
        return


#verification et suppression, si validation, d'un etudiant  
def etu_sup(id):
    
    data = lc.ouverture_fichier_csv("etudiants.csv")
    id_ = int(id.get())
    
    #utilisationd fonction pour supprimer l'etudiant et ses notes
    for i in range(1, len(data)):
        
        #verification existence ID
        if int(data[i][0]) == id_:
            lge.suppressionEtudiant(id_)
            lgn.suppressionNote(str(id), str("2021/2022"), str("Informatique"))
            lgn.suppressionNote(str(id), str("2021/2022"), str("Aeronotique"))
            lgn.suppressionNote(str(id), str("2021/2022"), str("Electronique"))
            lgn.suppressionNote(str(id), str("2021/2022"), str("Grand Projet")) 
            return
    tk.messagebox.showerror("Erreur", "ID erronné")
    return


#verification et ajout, si validation, d'une note
def not_ajt(id, annee, matiere, note):
    
    data = lc.ouverture_fichier_csv("notes.csv")
    data1 = lc.ouverture_fichier_csv("etudiants.csv")
    
    for j in range(1, len(data1)):
       
        #verification de l'existence de l'etudiant et de son ID
        if data1[j][0] == id.get():
            
            #verification de la non-existence de la note
            for i in range(1, len(data)):
                if str(data[i][2]) == str(id.get()) and str(data[i][3]) == str(matiere.get()):
                    tk.messagebox.showerror("Erreur", "L'etudiant a deja ete evalue sur cette matiere")
                    return
                
            #verification du bon nombre de données entrées    
            if (id.get() == "") or (annee.get() == "") or (matiere.get() == "") or (note.get() == ""):
                tk.messagebox.showerror("Erreur", "Informations manquantes")
                return
            
            #utilisation fonction pour ajouter la note 
            else:
                lgn.ajoutNote(id.get(), annee.get(), matiere.get(), note.get())
                return
    
    tk.messagebox.showerror("Erreur", "L'etudiant n'existe pas")
    return
 
  
#verification et modification, si validation, d'une note  
def not_mod(id, note):
    
    data = lc.ouverture_fichier_csv("notes.csv")
    
    #verification du bon nombre de données entrées
    if (id.get() == "") or (note.get() == ""):
        tk.messagebox.showerror("Erreur","Informations manquantes")
        
    #verification de l'existence de la note
    else:
        for j in range(1, len(data)):
            
            #utilisation fonction pour modifier la note 
            if (data[j][0] == id.get()):
                lgn.modificationNote(id.get(), note.get())
                return
            
        tk.messagebox.showerror("Erreur", "La note n'existe pas")
        return
   

#verification et suppression, si validation, d'une note    
def not_sup(id):
    
    data = lc.ouverture_fichier_csv("notes.csv")
    
    #verification du bon nombre de données entrées
    if (id.get() == ""):
                tk.messagebox.showerror("Erreur", "Informations manquantes")
    
    else:
        
        #verification existence note par son ID
        for j in range(1, len(data)):
            
            #utilisation fonction pour supprimer une note
            if (data[j][0] == id.get()):
                lgn.suppressionNote(id.get())
                return
    return


#creation d'un tableau et d'une scrollbar si besoin selon taille tableau
def tableau(dcsv):
    
    tab = ttk.Treeview(dcsv)
    tab.place(relx= 0.35,rely=0.05,relheight=0.85,relwidth= 0.55)
    
    data_tab = lc.ouverture_fichier_csv("etudiants.csv")
    tab['column'] = data_tab[0]

    for i in data_tab[0]:
        tab.column(str(i), width = 20)
        tab.heading(str(i),text=str(i))
    tab['show'] = 'headings'

    for i in range(len(data_tab)-1):
        tab.insert('',tk.END, values =data_tab[i+1])

    scbr = ttk.Scrollbar(dcsv, orient="vertical", command=tab.yview)
    scbr.place(relx=0.9,rely=0.05,relwidth=0.1,relheight=0.85)
    tab.configure(yscrollcommand=scbr.set)