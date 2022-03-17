"""
Mail prof : coline.gianfrotta@ens.uvsq.fr
"""

###################s
# MI TD1
# Zachary MARIANI
# Lenny BARBE
# William BRASSART
# https://github.com/LennyTheSniper/td_git/
###########################################

############ IMPORTATION DES MODULES #############

import random
import tkinter as tk
from turtle import color
import time

############### VARIABLES GLOBALES ###############

CANVAS_SIZE = 500
taille_plateau = int(input("Entrez la taille du plateau: "))
taille_case_SIZE = CANVAS_SIZE / taille_plateau
#                    0         1         2         3         4         5         6         7         8
liste_couleur = ["#000000","#65dd21","#d9f828","#f4a118","#ef490c","#ff0000","#ed1b6e","#e21bed","#851bed"]

################### FONCTIONS ####################

root = tk.Tk()
root.title("Tas de Sable")
canvas = tk.Canvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE, bg="black")


def plateau_vide():
    global plateau
    plateau = [[0]*taille_plateau]*taille_plateau
plateau_vide()

def quadrillage(nombre_case):
    x = 0
    y = 0
    for i in range(nombre_case):
        canvas.create_line(x, 0, x, y+CANVAS_SIZE, fill="white")
        canvas.create_line(0, y, x+CANVAS_SIZE, y, fill="white")
        x += taille_case_SIZE
        y += taille_case_SIZE
quadrillage(taille_plateau)


def generation_terrain():
    global plateau
    plateau = [[random.randint(0,5) for i in range(taille_plateau)] for j in range(taille_plateau)]
    print(plateau)
    affichage_couleur_quadrillage(plateau)

def affichage_couleur_quadrillage(plateau_val):
    canvas.delete("all")
    for x in range(taille_plateau):
        for y in range(taille_plateau):
            canvas.create_rectangle(x*taille_case_SIZE, y*taille_case_SIZE, (x+1)*taille_case_SIZE, (y+1)*taille_case_SIZE, fill=liste_couleur[plateau_val[y][x]])
    quadrillage(taille_plateau)

def equilibre_terrain():
    global plateau, taille_plateau
    plateau_mem = plateau.copy()
    for x in range(taille_plateau):
        for y in range(taille_plateau):
            if plateau[y][x] >= 4:
                plateau_mem[y][x] -= 4
                if y-1 >= 0:
                    plateau_mem[y-1][x] += 1
                if y+1 < taille_plateau:
                    plateau_mem[y+1][x] += 1
                if x-1 >= 0:
                    plateau_mem[y][x-1] += 1
                if x+1 < taille_plateau:
                    plateau_mem[y][x+1] += 1
    plateau = plateau_mem.copy()
    affichage_couleur_quadrillage(plateau)
    


def terrain_identite():
    global plateau
    plateau = [[4 for i in range(taille_plateau)] for j in range(taille_plateau)]
    print(plateau)
    affichage_couleur_quadrillage(plateau)


def sauvegarde () : 
    fic = open ("sauvegarde", "w")
    fic.write(str(taille_plateau)+"\n")
    for i in range (taille_plateau):
        for j in range (taille_plateau):
            fic.write(str(plateau[i][j])+" ")
    fic.close()


def charge () :
    global taille_plateau, plateau
    fic = open ("sauvegarde", "r")
    while True:
        ligne = fic.readline()
        if ligne == "":
            affichage_couleur_quadrillage(plateau)
            break
        else:
            if " " not in ligne:
                taille_plateau = int(ligne)
            else:
                split = ligne.split()
                for i in range (taille_plateau):
                    for j in range (taille_plateau):
                        plateau[i][j] = int(split[i*taille_plateau+j])




        









############# LISTE DE TOUS LES BOUTONS ############
aleatoire = tk.Button(root, text='Génerer un terrain aleatoire', command=generation_terrain, bg='grey')
equilibre_terrain = tk.Button(root, text='Équilibrer le terrain', command=equilibre_terrain, bg='grey')
sauvegarder = tk.Button(root, text = "Sauvegarder le terrain", command = sauvegarde, bg = 'grey')
charger = tk.Button(root, text = "Charger une sauvegarde", command = charge, bg = 'grey')
identite = tk.Button(root, text = "Charger le terrain identité", command = terrain_identite, bg = 'grey')

############## CREATION DE LA FENETRE #############

canvas.grid(row=0, column=1, rowspan=5)
aleatoire.grid(row=0, column=0)
equilibre_terrain.grid(row=1, column=0, ipadx=22)
sauvegarder.grid(row=2, column=0)
charger.grid(row=3, column=0)
identite.grid(row=4, column=0)
root.mainloop()