#!/usr/bin/python3.6
#Auteur : Maxim Germain
#Date : 03/11/2018
#Script 2a-mol.py
#Description : jeu du plus ou moins en daemon

import random
import sys
import signal
import re


#Fonction pour Ecrire dans le fichier
def writer (saisie) :
 file = open("game.txt", "w")
 file.write(saisie)
 file.close()
#Fonction pour lire le fichier
def reader():
 file=open("game.txt", "r")
 saisie= file.readline().strip()
 file.close()
 return saisie

#Génération du nombre aléatoire
r=random.randint(0, 100)


jump= 0
#Fonction pour le message d'au revoir et la solution
def leave():
 writer("au revoir ! le résultat est de "+str(r))
 sys.exit(0)
#Pour quitter proprement le programme
def ctrl_c(sig,frame):
 sys.exit(0)

writer("Jeu du plus ou moins: trouver un nombre entier entre 0 et 100" )
while True:
 signal.signal(signal.SIGINT, ctrl_c)

 answer=reader()
 if answer == "q":
  leave()
 if re.match("^[0-9]+$", answer):
        answer = int(answer)
 elif  int(answer) == r:
  print("Trouvé !")
  leave()
 else:
  if int(answer) > r:
   file= open("game.txt","a")
   file.write ("c'est moins")
  else:
   file= open("game.txt","a")
   print("c'est plus")


