"""
Mail prof : coline.gianfrotta@ens.uvsq.fr
"""

###################
# MI TD1
# Zachary MARIANI
# Lenny BARBE
# William BRASSART
# https://github.com/LennyTheSniper/td_git/
###########################################

############ IMPORTATION DES MODULES #############

from random import *
import tkinter as tk

############### VARIABLES GLOBALES ###############

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500
taille_plateau = int(input("entrez la taille du plateau"))

################### FONCTIONS ####################

def lignes_et_colones():
    plateau = [[0]*taille_plateau]*taille_plateau
    print(plateau)
lignes_et_colones()


root = tk.Tk()
root.title("Tas de Sable")
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg= "black")




############## CREATION DE LA FENETRE #############

canvas.grid(row=0, column=0, columnspan=4)
root.mainloop()