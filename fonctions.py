cle = ((0,1,0,1,0,1),
        (0,0,0,0,1,0),
        (0,0,1,0,0,0),
        (0,1,0,0,1,0),
        (0,0,0,0,0,1),
        (0,0,0,1,0,0))

message="jaimelespommes"
resultat=[[0]*len(cle[0]) for i in range(len(cle[0]))] #création d'une grille vide pour le résultat

def rotation_droite(cle):
    taille=len(cle[0])
    nouv_cle=[[0]*taille for i in range(taille)] #création d'une nouvelle clé vide aux mêmes dimensions
    for ligne in range(taille):
        for colonne in range(taille):
            nouv_cle[colonne][taille-1-ligne]=cle[ligne][colonne] #Lors d'une rotation vers la droite, ma première ligne devient ma dernière colonne
    return nouv_cle
nouvelle_cle=rotation_droite(cle)

def test_cle_valide(cle):
    #Pour vérifier si une clé est valide, ses cases ne doivent pas se superposer
    copie_cle = [list(row) for row in cle] #Vraie copie de liste, sans modification de l'original
    rotation1=rotation_droite(copie_cle)
    rotation2=rotation_droite(rotation1)
    rotation3=rotation_droite(rotation2) #Pour obtenir tous les sens possibles, on fait une rotation de la rotation précédente
    taille=len(cle[0])
    for ligne in range(taille):
        for colonne in range(taille):
            copie_cle[ligne][colonne]+=rotation1[ligne][colonne]
            copie_cle[ligne][colonne]+=rotation2[ligne][colonne]
            copie_cle[ligne][colonne]+=rotation3[ligne][colonne]
    #Si après avoir supperposé tous les sens on obtient une case plus grande que 1, la clé n'est pas valide
    for ligne in range(taille):
        for colonne in range(taille):
            if copie_cle[ligne][colonne]>1:
                return False
    return True

def remplir_resultat(cle,message,resultat):
    taille=len(cle[0])
    for ligne in range(taille): #On parcours la clé
        for colonne in range(taille):
            if cle[ligne][colonne]==1: #à chaques fois que l'on tombe sur une case valide
                resultat[ligne][colonne]=message[0] #on transpose dans le résultat la première lettre du message
                message=message[1:] #on retirer le premier caractère
    return (resultat,message) #on renvoie le résultat pour ce sens de la clé, et le message modifié
resultat, message = remplir_resultat(cle,message,resultat)[0], remplir_resultat(cle,message,resultat)[1]

def resultat_vers_texte(resultat):
    taille=len(cle[0])
    texte=""
    for ligne in range(taille): 
        for colonne in range(taille):
            if str(resultat[ligne][colonne]).isalpha(): #Si c'est une lettre, l'ajouter au message
                texte+=resultat[ligne][colonne]
    return texte


for i in range(6):
    print(resultat[i])


print(resultat_vers_texte(resultat))
