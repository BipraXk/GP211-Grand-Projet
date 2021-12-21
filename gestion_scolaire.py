#--*-- coding:utf-8 --*--
#-------------------------------------------------------------------------------
# Name:       Projet GP211 Gestion Scolaire
#
# Nom :
# Prenom :
#
# Classe :
# Groupe :
#
#-------------------------------------------------------------------------------


from lib_gestionEtudiants import *

from lib_gestionNotes import *



#***************************************************************************
#---------------------------------------------------------------------------
#                  Programme principal
#---------------------------------------------------------------------------
#***************************************************************************

menu_choix = 0


# Lancement du programme
#AffichageMenu()

while True:
    menu_choix = int(input("Rentrez votre choix ( valeur entre 1-3): \n 1- gestion Etudiants \n 2- gestion Notes\n 3- Sortie\n\n Reponse :\n"))
    if menu_choix == 1:
        gestionEtudiants()

    elif menu_choix == 2:
        gestionNotes()

    elif menu_choix == 3:
        break


print("Au revoir")







