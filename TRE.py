


#import des modules necessaire au bon fonctionnement du programme
from tkinter import *
import tkinter.ttk as ttk
from lib_commun import ouverture_fichier_csv

def tree_etud():
    
    root = Tk()
    root.title("TABLEAU")
    width = 675
    height = 650
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)
    
    TableMargin = Frame(root, width=450)
    TableMargin.pack(side=TOP)
    tree = ttk.Treeview(TableMargin, columns=("ID", "GENRE", "NOM", "PRENOM","EMAIL", "GROUPE"), height=400, selectmode="extended")
    tree.heading('ID', text="ID", anchor=W)
    tree.heading('GENRE', text="GENRE", anchor=W)
    tree.heading('NOM', text="NOM", anchor=W)
    tree.heading('PRENOM', text="PRENOM", anchor=W)
    tree.heading('EMAIL', text="EMAIL", anchor=W)
    tree.heading('GROUPE', text="GROUPE", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=50)
    tree.column('#2', stretch=NO, minwidth=0, width=50)
    tree.column('#3', stretch=NO, minwidth=0, width=150)
    tree.column('#4', stretch=NO, minwidth=0, width=100)
    tree.column('#5', stretch=NO, minwidth=0, width=250)
    
    tree.pack()
    
    data_etudiants = ouverture_fichier_csv("etudiants.csv")
            
    for i in range(1, len(data_etudiants)):
        ID = data_etudiants[i][0]
        GENRE = data_etudiants[i][1]
        NOM = data_etudiants[i][2]
        PRENOM = data_etudiants[i][3]
        EMAIL = data_etudiants[i][4]
        GROUPE = data_etudiants[i][5]
        tree.insert("", END, values=(ID,GENRE,NOM,PRENOM,EMAIL,GROUPE))
                
            
            
    #============================INITIALIZATION==============================
    if __name__ == '__main__':
        root.mainloop()