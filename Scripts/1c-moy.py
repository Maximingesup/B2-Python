 #!/usr/bin/python3.6 
import re

#Auteur : Maxim Germain
#Date : 16/10/2018

#Consignes

#Demander une saisie utilisateur de plusieurs notes et prénoms :
#l'utilisateur saisit un prénom, et une note pour chacun d'entre eux
#l'utilisateur peut saisir 'q' pour stopper la saisie
#affichez ensuite la moyenne et un top 5 des meilleures notes

#Script 1.c

dico = {}
notes = []
while True:

    try:
        while True:
            try:
                #Filtre du prenom avec lettre majuscule-minuscule, 2 lettres minimums pour le prénom
                #Prénom avec un tiret maximum
                prenom = re.findall(r"(?:[A-Za-z]{2,}(?:-(?:[A-Za-z]{2,}))?)|q", input("Entrez un prenom : "))[0]
                
                #Quitter la boucle avec q
                if prenom == "q":
                    break
                #filtre note pour avoir que des chiffres et éviter intégration de q avec Min 0/20 et Max 20/20    
                else:
                    note = re.findall(r"(-?[0-9]+(?:\.[0-9]+)?)|q", input("Entrez une note : "))[0]
                    
                    if note == "q":
                        break
                    elif float(note) > 20:
                        print("La note est trop élevée. Merci de rentrer une note entre 0 et 20.")
                    elif float(note) < 0:
                        print("La note est trop basse. Merci de rentrer une note entre 0 et 20.")
                    #Rentrée des données dans le dictionaire avec modification du type de la variable
                    else:
                        dico[prenom] = round(float(note), 2)
                     #ajout dans le tableau pour la moyenne   
                        notes.append(round(float(note), 2))

            #Si une erreur est avérée dans la saisie
            except IndexError:
                print("Attention à bien renseigner le prenom ou la note")
            #Moyenne 
        print(round(sum(notes)/len(notes), 2))
        #tri pour les 5 premières notes du dictionaire ordre décroissant
        sorted = sorted(dico.items(), key=lambda eleve: eleve[1], reverse=True)
        del sorted[5:]
        break
    except ZeroDivisionError:
        print("Il n'y a pas de note")