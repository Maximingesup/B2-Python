#!/usr/bin/python3.6 
#Auteur : Maxim Germain
#Date : 23/10/2018
# Créer jeu du plus ou moins

import random
import sys
import signal




r=random.randint(0, 100)
#Fonction pour le message d'au revoir et la solution 
def leave():
 print("au revoir ! le résultat est de "+str(r))
 sys.exit(0)
def ctrl_c(sig,frame):
 sys.exit(0)
 
print("Jeu du plus ou moins: trouver un nombre entier entre 0 et 100" )
while True:
 signal.signal(signal.SIGINT, ctrl_c)
 reponse=input()
 if reponse == "q":
  leave()

 elif  int(reponse) == r:
  print("Trouvé !")
  break             
 else:
  if int(reponse) > r:
   print("c'est moins")
  else:
   print("c'est plus")
