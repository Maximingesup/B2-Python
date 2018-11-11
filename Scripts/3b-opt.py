# !/usr/bin/python3.6
# Auteur : Maxim Germain
# Date : 03/11/2018
# Script 3b-opt.py
# Description : 3a avec des options de lancement

# Fonction pour Ecrire dans le fichier


import shutil
import gzip
import os
import sys
import signal


def leave(sig, frame):
    sys.stdout.write("Au revoir ! \n")
    sys.exit(0)


sys.stdout.write("saisissez q pour quitter ou Ctr c \n")

while True:
    sys.stdout.write("Chemin du fichier à sauvegarder: \n")
    src = input()
    sys.stdout.write("Répertoire où stocker le fichier: \n")
    dst = input()
    signal.signal(signal.SIGINT, leave)
    if src == q or dst == q:
        leave()
    isHere = False
    shutil.make_archive('folder_test', 'gztar', 'folder_test')

    if not os.path.exists(dst):
        os.makedirs(dst)  # On vérifie la présence d 'un fichier
    try:
        if isHere == False:
            sys.stdout.write("Vérification du fichier data \n")
            for file in os.listdir(dst):
                if file == "folder_test.tar.gz":
                    ishere = True
                    sys.stdout.write("Comparaison des deux sauvegardes\n")
                    with gzip.open(dst) as file:
                        old_save = f.read()
                    with gzip.open(src + ".tar.gz") as file:
                        new_save = f.read()
                    if new_save != old_save:
                        os.remove("data/folder_test.tar.gz")
                        shutil.make_archive(src, "gztar")
                        os.remove("folder_test.tar.gz")
                        shutil.move(src + ".tar.gz", dst)
                        sys.stdout.write("Suppression et déplacement de l'archive dans le fichier data")
                else:
                    sys.stdout.write("Fichiers identiques!\n")

        else:
            shutil.make_archive(src, "gztar")
            shutil.move(src, dst)
    except FileNotFoundError:
        sys.stdout.write("Fichier non trouvé ! Vérifiez le chemin d'accès !")
