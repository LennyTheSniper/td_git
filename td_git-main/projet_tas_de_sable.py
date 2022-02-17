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

############### VARIABLES GLOBALES ###############

CANVAS_SIZE = 500
taille_plateau = int(input("Entrez la taille du plateau: "))
taille_case_SIZE = CANVAS_SIZE // taille_plateau

################### FONCTIONS ####################

root = tk.Tk()
root.title("Tas de Sable")
canvas = tk.Canvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE, bg="black")


def plateau_vide():
    global plateau
    plateau = [[0]*taille_plateau]*taille_plateau


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
    affichage_couleur_quadrillage(taille_plateau)

def affichage_couleur_quadrillage(taille_plateau):
    for x in range (taille_plateau):
        for y in range(taille_plateau):
            if plateau[y][x] == 0:
                canvas.create_rectangle(x*taille_case_SIZE, y*taille_case_SIZE, (x+1)*taille_case_SIZE, (y+1)*taille_case_SIZE, fill="#000000")
            elif plateau[y][x] == 1:
                canvas.create_rectangle(x*taille_case_SIZE, y*taille_case_SIZE, (x+1)*taille_case_SIZE, (y+1)*taille_case_SIZE, fill="#65dd21")
            elif plateau[y][x] == 2:
                canvas.create_rectangle(x*taille_case_SIZE, y*taille_case_SIZE, (x+1)*taille_case_SIZE, (y+1)*taille_case_SIZE, fill="#d9f828")
            elif plateau[y][x] == 3:
                canvas.create_rectangle(x*taille_case_SIZE, y*taille_case_SIZE, (x+1)*taille_case_SIZE, (y+1)*taille_case_SIZE, fill="#f4a118")
            elif plateau[y][x] == 4:
                canvas.create_rectangle(x*taille_case_SIZE, y*taille_case_SIZE, (x+1)*taille_case_SIZE, (y+1)*taille_case_SIZE, fill="#ef490c")
            elif plateau[y][x] == 5:
                canvas.create_rectangle(x*taille_case_SIZE, y*taille_case_SIZE, (x+1)*taille_case_SIZE, (y+1)*taille_case_SIZE, fill="#ff0000")
            elif plateau[y][x] == 6:
                canvas.create_rectangle(x*taille_case_SIZE, y*taille_case_SIZE, (x+1)*taille_case_SIZE, (y+1)*taille_case_SIZE, fill="#ed1b6e")
            elif plateau[y][x] == 7:
                canvas.create_rectangle(x*taille_case_SIZE, y*taille_case_SIZE, (x+1)*taille_case_SIZE, (y+1)*taille_case_SIZE, fill="#e21bed")
            else:
                canvas.create_rectangle(x*taille_case_SIZE, y*taille_case_SIZE, (x+1)*taille_case_SIZE, (y+1)*taille_case_SIZE, fill="#851bed")
    quadrillage(taille_plateau)





############# LISTE DE TOUS LES BOUTONS ############
aleatoire = tk.Button(root, text='Génerer un terrain aleatoire', command=generation_terrain, bg='grey')




############## CREATION DE LA FENETRE #############

canvas.grid(row=0, column=1, columnspan=4)
aleatoire.grid(row=0, column=0)
root.mainloop()