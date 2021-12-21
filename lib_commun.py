import csv

def ouverture_fichier_csv(nomfichier):
    """
    Cette fonction a pour objectif l'ouverture d'un fichier au format csv(sep=',')
    IN : le nom du fichier à traiter
    OUT : une liste de listes de chaines de caractères: [["1","Monsieur","AUSCHITZKY","Quentin","quentin.auschitzky@ipsa.fr"],..]
          ex pour le fichier matieres.csv : ["Mathematique","Aeronautique",...]
    """
    import os
    ##################################################
    #ouverture et recuperation du contenu du fichier
    ##################################################
    data = []
    print("Je suis dans le repertoire : ", os.path.basename(os.path.abspath(os.curdir)))
    try :
        
        print("ouverture de fichier :",nomfichier)

        # Boucle permettant de transformer la liste de chaines de caractères en
        # liste de listes de chaines de caractères
        with open(f'./data/{nomfichier}',encoding = 'utf-8') as csvfile:
            rows = csv.reader(csvfile)
            for i in rows:
                data.append(i)
                
        if nomfichier == "matieres.csv":
            return data[0]
        return data
    
    except :
        print("1-Problème d'ouverture de fichier en lecture")
        return


    return  data


def ecriture_fichier_csv(contenu_fichier, nomFichier):
    """
    Cette fonction a pour objectif l'ecriture dans un fichier au format csv(sep=',')
    IN : le contunu à écrire dans le fichier, le nom du fichier
    OUT : 
    """


    #try :
    with open(f'./data/{nomFichier}', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
    
        # Ecrire les données dans le fichier
        for row in contenu_fichier:

            writer.writerow(row)
    #except :
        #print("2-Problème d'ouverture de fichier en ecriture")
        #return
