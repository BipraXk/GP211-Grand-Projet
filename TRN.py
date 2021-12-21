


#import des modules necessaire au bon fonctionnement du programme
from tkinter import *
import tkinter.ttk as ttk
from lib_commun import ouverture_fichier_csv

def tree_note():
    
    root = Tk()
    root.title("TABLEAU")
    width = 400
    height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)
    
    TableMargin = Frame(root, width=450)
    TableMargin.pack(side=TOP)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("ANNEE", "ID_ETUDIANT", "MATIERE", "NOTE"), height=400, selectmode="extended", yscrollcommand=scrollbary.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    tree.heading('ANNEE', text="ANNEE", anchor=W)
    tree.heading('ID_ETUDIANT', text="ID_ETUDIANT", anchor=W)
    tree.heading('MATIERE', text="MATIERE", anchor=W)
    tree.heading('NOTE', text="NOTE", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.column('#4', stretch=NO, minwidth=0, width=100)
    
    tree.pack()
    
    data_notes = ouverture_fichier_csv("notes.csv")
            
    for i in range(1, len(data_notes)):
        ANNEE = data_notes[i][1]
        ID_ETUDIANT = data_notes[i][2]
        MATIERE = data_notes[i][3]
        NOTE = data_notes[i][4]
        tree.insert("", END, values=(ANNEE,ID_ETUDIANT,MATIERE,NOTE))
                
            
            
    #============================INITIALIZATION==============================
    if __name__ == '__main__':
        root.mainloop()