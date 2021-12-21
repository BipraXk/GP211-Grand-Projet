from lib_commun import ouverture_fichier_csv, ecriture_fichier_csv


    
def ajoutNote(*donneesNote) :
    """
    Cette fonction a pour objectif d'ajouter une note
    IN :note, matiere, id etudiant, année scolaire
    OUT : ecriture dans csv
    """
    nomfichier = "notes.csv"
    L_notes = ouverture_fichier_csv(nomfichier)
    print(L_notes)

    
    existe_id = False  
    existe_matiere = False  

   
  
    new_note = []
    for i in range(0,len(donneesNote)):
        new_note.append(donneesNote[i]) 
        
        
    for j in range(0,len(L_notes)):
        if new_note[0] == L_notes[j][2]:
            existe_id = True
            
    for j in range(0,len(L_notes)):        
        if new_note[2] == L_notes[j][3]:
            existe_matiere = True
            
            
    if (existe_id == True) and   (existe_matiere == True) :
        print("L'élève possède déjà une note dans cette matière")
        return
    
    numlastnote = L_notes[-1][0]
    numlastnoteint = int(numlastnote)
    numlastnoteint += 1
    numlastnoteint = str(numlastnoteint)
    
    ajout = [numlastnoteint]
    for i in range(0, len(donneesNote)):
        ajout.append(donneesNote[i])
    L_notes.append(ajout)
    L_notes.append("\n")
    ecriture_fichier_csv(L_notes, nomfichier)
    
def modificationNote(*donneesNote) :
    """
    Cette fonction a pour objectif de mofifier la note d'un etudiant
    IN : id note, note
    OUT : ecriture dans csv
    """
    
    nomfichier = "notes.csv"
    L_notes = ouverture_fichier_csv(nomfichier)
    
    existe_note = False  
    
    maj_note = []
    for i in range(0,len(donneesNote)):
        maj_note.append(donneesNote[i]) 
    
    for j in range(0,len(L_notes)):
        if maj_note[0] == L_notes[j][0]:
            print("La note existe")
            existe_note = True
            
            
    if (existe_note == True) :
        for i in range (0,len(L_notes)):
            if maj_note[0] == L_notes[i][0]:
                L_notes[i][4] = maj_note[1]
    else :
        return
    
    ecriture_fichier_csv(L_notes, nomfichier)
    
    return

def suppressionNote(*donneesNote) :
    """
    Cette fonction a pour objectif de supprimer une note
    IN :id note
    OUT :suppression de la note dans csv
    """
    nomfichier = "notes.csv"
    existe_note = False
    L_notes = ouverture_fichier_csv(nomfichier)
    rang=0
    
    for j in range(0,len(L_notes)):
        if donneesNote[0] == L_notes[j][0]:
            print("La note existe")
            existe_note = True
            rang=j
            
    if existe_note == True:
        L_notes.pop(rang)
    else:
        return
        
    ecriture_fichier_csv(L_notes, nomfichier)
    print("la suppression est terminée")
        
    
    def affichageNote() :
        """
        Cette procédure a pour objectif d'afficher l'ensemble des informations notes des etudiants.
        Soit : ID, Matiere, Note
        IN : aucun paramètre en entrée
        OUT : aucun retour
        """
        ##################################################
        #ouverture et recuperation du contenu du fichier
        ##################################################
        nomfichier = "notes.csv"
        data = ouverture_fichier_csv(nomfichier)
        



        print("***********************************************************************************************************")
        print("*                                          Gestion Scolaire                                               *")
        print("***********************************************************************************************************")
        print("*   Année Scolaire      *   ID Etudiant           *        Matiere            *         Note              *")
        print("***********************************************************************************************************")

        for i in range(1,len(data)) :
            print("* {:<7}  * {:<4} * {:<15}  *  {:>3}  *" . format(data[i][1],data[i][2], data[i][3], data[i][4]))

        print("***********************************************************************************************************\n")

        
    ##################################################
    #
    ##################################################
    while True:
        menu_choix = int(input("Rentrez votre choix ( valeur entre 1-5): \n 1- Ajout note \n 2- Modification note\n 3- Suppression note\n 4- Affichage notes\n 5- Sortie\n\n Reponse :\n"))

        if menu_choix == 1 :
            id_ = input("Saisissez le ID d'etudiant\n->")
            annee = input("Saisissez l'année scolaire\n->")
            matiere = input("Saisissez le matiere\n->")
            note = input("Saisissez le note\n->")
            ajoutNote(id_,annee,matiere,note)

        if menu_choix == 2 :
            id_note = input("Saisissez l'id de la note\n->")
            note = input("Saisissez la note\n->")
            modificationNote(id_note,note)

        if menu_choix == 3 :
            id_note = input("Saisissez le ID de la note\n->")
            suppressionNote(id_note)

        if menu_choix == 4 :
            affichageNote() 


        if menu_choix == 5 :
            return 