from lib_commun import ouverture_fichier_csv, ecriture_fichier_csv


def ajoutEtudiant(*donneesEtudiant) :
    """
    Cette fonction a pour objectif d'ajouter un etudiant
    IN : Prénom, nom, genre, mail, classe
    OUT : ecriture dans csv
    """
    nomfichier = "etudiants.csv"
    L_etudiants = ouverture_fichier_csv(nomfichier)
    for i in range(0, len(L_etudiants)):
        if donneesEtudiant[3] == L_etudiants[i][4] :  
            print("L'étudiant existe déjà")
            return
     
    ajout = [len(L_etudiants)]
    
    for i in range(0, len(donneesEtudiant)):
        ajout.append(donneesEtudiant[i])
    L_etudiants.append(ajout)

    ecriture_fichier_csv(L_etudiants, nomfichier)
    return

def modificationEtudiant(*donneesEtudiant) :
    """
    Cette fonction a pour objectif
    IN :ID, prénom, nom, genre, mail, classe
    OUT : ecriture dans csv
    """
    nomfichier = "etudiants.csv"
    L_etudiants = ouverture_fichier_csv(nomfichier)
    for i in range(0, len(L_etudiants)):
        if donneesEtudiant[0] == L_etudiants[i][0] :  
            print("L'étudiant existe")
            L_etudiants[i][1] = donneesEtudiant[3]
            L_etudiants[i][2] = donneesEtudiant[2]
            L_etudiants[i][3] = donneesEtudiant[1]
            L_etudiants[i][4] = donneesEtudiant[4]
            L_etudiants[i][5] = donneesEtudiant[5]
            print("Modification Etudiant")
            ecriture_fichier_csv(L_etudiants, nomfichier)
    return

def suppressionEtudiant(id) :
    """
    Cette fonction a pour objectif de supprimer l'etudiant (de la liste)
    IN : ID de l'étudiant
    OUT : supprime l'étudiant et ses informations du csv'
    """
    data = ouverture_fichier_csv("etudiants.csv")
    for i in range(1, len(data)):
        if int(data[i][0]) == id:
            del data[i]
            ecriture_fichier_csv(data, "etudiants.csv")
            return
    return

        
    
    def affichageEtudiant() :
        """
        Cette procédure a pour objectif d'afficher l'ensemble des informations administratives des etudiants.
        Soit : ID, prenom, nom, genre, email, groupe
        IN : aucun paramètre en entrée
        OUT : aucun retour
        """
        ##################################################
        #ouverture et recuperation du contenu du fichier
        ##################################################
        nomfichier = "etudiants.csv"
        data = ouverture_fichier_csv(nomfichier)



        print("***********************************************************************************************************")
        print("*                                          Gestion Scolaire                                               *")
        print("***********************************************************************************************************")
        print("*  ID   *   Genre      *     Prenom          *   Nom              * Email adresse          *   Groupe      ")
        print("***********************************************************************************************************")

        for i in range(1,len(data)) :
            print("* {:<8}  * {:<8}  * {:<15}  *  {:<15}  *  {:<25} * {:>5} *" . format(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))

        print("***********************************************************************************************************\n")

        
    ##################################################
    #
    ##################################################
    while True:
        menu_choix = int(input("Rentrez votre choix ( valeur entre 1-5): \n 1- Ajout etudiant \n 2- Modification etudiant\n 3- Suppression etudiant\n 4- Affichage etudiant\n 5- Sortie\n\n Reponse :\n"))

        if menu_choix == 1 :
            genre = input("Saisissez le genre d'etudiant\n->")
            nom = input("Saisissez le nom d'etudiant\n->")
            prenom = input("Saisissez le prenom d'etudiant\n->")
            email = input("Saisissez le email d'etudiant\n->")
            classe = input("Saisissez la classe de l'etudiant\n->")
            ajoutEtudiant(genre,nom,prenom,email,classe)

        if menu_choix == 2 :
            id_ = input("Saisissez ID d'etudiant\n->")
            prenom = input("Saisissez le prenom d'etudiant\n->")
            nom = input("Saisissez le nom d'etudiant\n->")
            genre = input("Saisissez le genre d'etudiant\n->")
            email = input("Saisissez le email d'etudiant\n->")
            classe = input("Saisissez la classe de l'etudiant\n->")
            modificationEtudiant(id_,prenom,nom,genre,email,classe)

        if menu_choix == 3 :
            id_ = input("Saisissez ID d'etudiant\n->")
            suppressionEtudiant(id_)

        if menu_choix == 4 :
            affichageEtudiant() 


        if menu_choix == 5 :
            return 