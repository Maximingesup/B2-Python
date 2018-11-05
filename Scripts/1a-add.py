#!/usr/bin/python3.6
import re
#Auteur : Maxim Germain
#Date : 16/10/2018

##Script1.a

#Consignes

#Demander deux nombres à l’utilisateur et afficher le résultat de l’addition des deux nombres.
#Contrôler que l’utilisateur a bien saisi deux nombres et pas autre chose.

#Saisie des deux nombres
while True:
    saisie_1 =  input ('Saisir un nombre : ')
    saisie_2 = input ('Saisir un autre nombre : ')
#je teste les variable pour voir si ce sont des nombres
    try:
                 saisie_1 =int(saisie_1)
                 saisie_2 =int(saisie_2)
    except:
            print ("erreur dans la saisie")
            break
#je convertis les variables
    saisie_r1= int(saisie_1)
    saisie_r2= int(saisie_2)
    result = saisie_r1 + saisie_r2
    print(result)

