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

from random import *
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
aleatoire = tk.Button(root, text='Génerer un terrain aleatoire', bg='grey')


def lignes_et_colones():
    global plateau
    plateau = [[0]*taille_plateau]*taille_plateau
lignes_et_colones()

def quadrillage(nombre_case):
    x = 0
    y = 0
    for i in range(nombre_case):
        canvas.create_line(x, 0, x, y+CANVAS_SIZE, fill="white")
        canvas.create_line(0, y, x+CANVAS_SIZE, y, fill="white")
        x += taille_case_SIZE
        y += taille_case_SIZE
quadrillage(taille_plateau)

'''
def generation_terrain () :
    for i in range taille_plateau :
        a = random.randint(0,5)
        plateau.append(a)
        return plateau
'''








############## CREATION DE LA FENETRE #############

canvas.grid(row=0, column=1, columnspan=4)
aleatoire.grid(row=0, column=0)
root.mainloop()