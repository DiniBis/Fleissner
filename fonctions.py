from random import *

cle = ((1,2,3,1,0,1),
    (0,0,0,0,1,0),
    (0,0,1,0,0,0),
    (0,1,0,0,1,0),
    (0,0,0,0,0,1),
    (0,0,0,1,0,0))

message="jaimelespommes"
resultat=[[0]*len(cle[0]) for i in range(len(cle[0]))] #création d'une grille vide pour le résultat

def nettoyer_message(message):
    """
        IN: message brut
        OUT: message sans espaces
    """
    message = message.replace(' ', '')
    return message

def rotation_droite(cle):
    """
        IN: une clé
        OUT: clé après rotation sur la droite
    """
    taille=len(cle[0])
    nouv_cle=[[0]*taille for i in range(taille)] #création d'une nouvelle clé vide aux mêmes dimensions
    for ligne in range(taille):
        for colonne in range(taille):
            nouv_cle[colonne][taille-1-ligne]=cle[ligne][colonne] #Lors d'une rotation vers la droite, ma première ligne devient ma dernière colonne
    return nouv_cle
nouvelle_cle=rotation_droite(cle)

def rotation_gauche(cle):
    """
        IN: une clé
        OUT: clé après rotation sur la gauche
    """
    taille=len(cle[0])
    nouv_cle=[[0]*taille for i in range(taille)] #création d'une nouvelle clé vide aux mêmes dimensions
    for ligne in range(taille):
        for colonne in range(taille):
            nouv_cle[taille-1-colonne][ligne]=cle[ligne][colonne] #Lors d'une rotation vers la gauche, ma première ligne devient ma première colonne (inversée)
    return nouv_cle
nouvelle_cle=rotation_gauche(cle)

def test_cle_valide(cle):
    """
        IN: une clé
        OUT: booléen, True si valide, False sinon.
    """
    #Pour vérifier qu'une clé soit valide, ses cases ne doivent pas se superposer
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
    """
        IN: une clé, le message, le resultat(tableau du résultat final, comprend les caractères du message)
        OUT: les lettres restantes du message (remplir_resultat[0]), le tableau du résultat après remplissage sur cette rotation(remplir_resultat[1])

        Exemple d'appel:
        resultat, message = remplir_resultat(cle,message,resultat)[0], remplir_resultat(cle,message,resultat)[1]
    """
    taille=len(cle[0])
    alphabet="abcdefghijklmnopkrstuvwxyz"
    for ligne in range(taille): #On parcours la clé
        for colonne in range(taille):
            if message=="": #Si le message n'a plus de caractère, ajouter un caractère aléatoire
                resultat[ligne][colonne]=random.choice(alphabet)
            elif cle[ligne][colonne]==1: #à chaques fois que l'on tombe sur une case valide
                resultat[ligne][colonne]=message[0] #on transpose dans le résultat la première lettre du message
                message=message[1:] #on retire le premier caractère
    return (resultat,message) #on renvoie le résultat pour ce sens de la clé, et le message modifié
resultat, message = remplir_resultat(cle,message,resultat)[0], remplir_resultat(cle,message,resultat)[1]

def resultat_vers_texte(resultat):
    """
        IN: le tableau resultat remplis (après la fonction remplir_resultat)
        OUT: string comprenant le message correspondant au Cipher
    """
    taille=len(cle[0])
    texte=""
    for ligne in range(taille): 
        for colonne in range(taille):
            if str(resultat[ligne][colonne]).isalpha(): #Si c'est une lettre, l'ajouter au message
                texte+=resultat[ligne][colonne]
    return texte
    
def cipher(cle, message):
    """
        IN: message, cle
        OUT: message (string) après Cipher / une erreur si la cle n'est pas valide
    """
    if test_cle_valide(cle)==False:
        return "erreur: cle non valide"
    message=nettoyer_message(message)
    resultat=[[0]*len(cle[0]) for i in range(len(cle[0]))] #création d'une grille vide pour le résultat
    #1er sens
    resultat, message = remplir_resultat(cle,message,resultat)[0], remplir_resultat(cle,message,resultat)[1]
    #2ème sens
    cle=rotation_droite(cle)
    resultat, message = remplir_resultat(cle,message,resultat)[0], remplir_resultat(cle,message,resultat)[1]
    #3ème sens
    cle=rotation_droite(cle)
    resultat, message = remplir_resultat(cle,message,resultat)[0], remplir_resultat(cle,message,resultat)[1]
    #4ème sens
    cle=rotation_droite(cle)
    resultat, message = remplir_resultat(cle,message,resultat)[0], remplir_resultat(cle,message,resultat)[1]
    #Renvoyer un résultat lisible
    texte=resultat_vers_texte(resultat)
    return texte
