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

taille_plateau = int(input("entrez la taille du plateau"))
plateau = []

################### FONCTIONS ####################

def lignes_et_colones():
    plateau = [[0]*taille_plateau]*taille_plateau
    print(plateau)
lignes_et_colones()


root = tk.Tk()
root.title("Calculatrice")





############## CREATION DE LA FENETRE #############

canvas.grid(row=0, column=0, columnspan=4)
root.mainloop()