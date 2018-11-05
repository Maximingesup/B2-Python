#!/usr/bin/python3.6
import re

#Auteur : Maxim Germain
#Date : 16/10/2018

#Script 1.b

#Consignes

#Demander une saisie utilisateur de plusieurs prénoms.
#L’utilisateur peut choisir d’arrêter la saisie en appuyant sur la touche ‘q’.
#Les stocker dans une liste. Afficher le résultat en ordonnant les prénoms par ordre alphabétique.

list = []

while True:
        try:
           #tri des prénoms AZ az et saisie
           list.append(re.findall(r"[A-Za-z]+", input("Entrez un prenom : "))[0])
           #implémentation du q (on l'enlève de la liste à la fin)
           if list[-1] == "q":
              list.pop()
              break
              #erreur en cas de mauvaise saisie dans l'input
        except IndexError :
            print("Attention à bien renseigner le prenom")
           #Affichage par ordre alphabétique
print(sorted(list))