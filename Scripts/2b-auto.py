#!/usr/bin/python3.6
#Auteur : Maxim Germain
#Date : 03/11/2018
#Script 2b-mol.py
#Description : robot qui répond au script

#Fonction pour Ecrire dans le fichier

import signal
import sys
import time



def writer (nombre) :
 file = open("game.txt", "w")
 file.write(nombre)
 file.close()

 #Pour quitter proprement le programme

def ctrl_c(sig, frame):
 sys.exit(0)


#Défintion des variables limites pour le jeu

name_file= "game.txt"
x= -1
y=101
loop=True
variable=50

while loop == True :

 fichier = open("game.txt", "r")
 test_read = fichier.readline()

 if "petit" in test-read:
    y = variable
    variable = (y - x)/2
    nombre = int(variable)
    writer(nombre)
    time.sleep(5)

 elif "grand" in test-read:
    x = variable
    nombre = (y - x)/2
    nombre = int(variable)
    writer(nombre)
    time.sleep(5)

 else:
    print (variable)
    loop=False
 fichier.close()
