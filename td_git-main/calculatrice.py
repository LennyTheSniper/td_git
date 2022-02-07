"""
Ok alors je t'explique maintenant comment on va faire fonctionner ça:
Il va falloir en premier déterminer chaque étape à réaliser et bien se les répartir.
Une fois qu'on a bien répartit, on va bosser petit à petit sur le projet chaqun de notre côté.
Si t'es confus et tu sais pas quoi faire, envoie moi un message via Discord: LennyTheSniper#2929

Sinon, à chaque fois que tu termine de faire ton truc et que tu a besoin que je fasse ma partie
pour progresser, tu marque juste en bas de ce commentaire dans le deuxième set de guillemet quelle
est la prochaine étape.
Voilà voilà, bonne chance!
"""


"""

"""
######################
# Import des librairies

import tkinter as tk
from typing import Text
#from unittest import result
import math

###############################
# 1er set des variables de base

CANVAS_WIDTH, CANVAS_HEIGHT = 390, 75

Variable1 = '' ; Variable2 = ''
TextOnScreen = '' ; NegativeTest = 1
Operator = '' ; Result = '' ; Arrondisseur = 10 ** (-10)
EditedVariable = 1



#################################################
# Définition des programmes ajoutant des chiffres

def add1():
    global Variable1, Variable2
    if EditedVariable == 1:
        Variable1 = str(Variable1) + str('1')
        print_on_canvas(Variable1)
    else:
        Variable2 = str(Variable2) + str('1')
        print_on_canvas(Variable2)

def add2():
    global Variable1, Variable2
    if EditedVariable == 1:
        Variable1 = str(Variable1) + str('2')
        print_on_canvas(Variable1)
    else:
        Variable2 = str(Variable2) + str('2')
        print_on_canvas(Variable2)

def add3():
    global Variable1, Variable2
    if EditedVariable == 1:
        Variable1 = str(Variable1) + str('3')
        print_on_canvas(Variable1)
    else:
        Variable2 = str(Variable2) + str('3')
        print_on_canvas(Variable2)

def add4():
    global Variable1, Variable2
    if EditedVariable == 1:
        Variable1 = str(Variable1) + str('4')
        print_on_canvas(Variable1)
    else:
        Variable2 = str(Variable2) + str('4')
        print_on_canvas(Variable2)

def add5():
    global Variable1, Variable2
    if EditedVariable == 1:
        Variable1 = str(Variable1) + str('5')
        print_on_canvas(Variable1)
    else:
        Variable2 = str(Variable2) + str('5')
        print_on_canvas(Variable2)

def add6():
    global Variable1, Variable2
    if EditedVariable == 1:
        Variable1 = str(Variable1) + str('6')
        print_on_canvas(Variable1)
    else:
        Variable2 = str(Variable2) + str('6')
        print_on_canvas(Variable2)

def add7():
    global Variable1, Variable2
    if EditedVariable == 1:
        Variable1 = str(Variable1) + str('7')
        print_on_canvas(Variable1)
    else:
        Variable2 = str(Variable2) + str('7')
        print_on_canvas(Variable2)

def add8():
    global Variable1, Variable2
    if EditedVariable == 1:
        Variable1 = str(Variable1) + str('8')
        print_on_canvas(Variable1)
    else:
        Variable2 = str(Variable2) + str('8')
        print_on_canvas(Variable2)

def add9():
    global Variable1, Variable2
    if EditedVariable == 1:
        Variable1 = str(Variable1) + str('9')
        print_on_canvas(Variable1)
    else:
        Variable2 = str(Variable2) + str('9')
        print_on_canvas(Variable2)

def add0():
    global Variable1, Variable2
    if EditedVariable == 1:
        Variable1 = str(Variable1) + str('0')
        print_on_canvas(Variable1)
    else:
        Variable2 = str(Variable2) + str('0')
        print_on_canvas(Variable2)

def add_pi():
    global Variable1, Variable2
    if EditedVariable == 1:
        Variable1 = math.pi
        print_on_canvas(Variable1)
    else:
        Variable2 = math.pi
        print_on_canvas(Variable2)

def add_e():
    global Variable1, Variable2
    if EditedVariable == 1:
        Variable1 = math.e
        print_on_canvas(Variable1)
    else:
        Variable2 = math.e
        print_on_canvas(Variable2)


###########################################
# Définition du programme ajoutant un point

def addDot():
    global Variable1, Variable2
    if EditedVariable == 1 :
        Variable1 = str(Variable1)
        Variable1 = Variable1.replace('.','')
        Variable1 = str(Variable1) + str('.')
        print_on_canvas(Variable1)
    else:
        Variable2 = str(Variable2)
        Variable2 = Variable2.replace('.','')
        Variable2 = str(Variable2) + str('.')
        print_on_canvas(Variable2)

########################################
# Définition du programme qui reset tout

def clear():
    global Variable1, Variable2, Operator, Result, EditedVariable
    Variable1 = '' ; Variable2 = ''
    Operator = '' ; Result = ''
    if EditedVariable == 1:
        print_on_canvas(Variable1)
        EditedVariable = 1
    else:
        print_on_canvas(Variable2)
        EditedVariable = 1

###############################################
# Définition du programme qui affiche à l'écran

def print_on_canvas(WhatToShow):
    global TextOnScreen
    if TextOnScreen != '':
        canvas.delete(TextOnScreen)
        TextOnScreen = ''
    if (len(str(WhatToShow))*14.5)*2 < CANVAS_WIDTH:
        TextOnScreen = canvas.create_text(CANVAS_WIDTH-len(str(WhatToShow))*14.5, CANVAS_HEIGHT/2,
                                            text=WhatToShow,font=("Arial", "40"), fill="white")
    else:
        TextOnScreen = canvas.create_text(len(str(WhatToShow))*14.5, CANVAS_HEIGHT/2,
                                            text=WhatToShow,font=("Arial", "40"), fill="white")
    


###############################################################
# Définition des programmes qui disent quel opérateur est actif


def SetOperatorAdd():
    global Operator, EditedVariable, Variable2, Variable1
    Operator = 'Add'
    EditedVariable = 2
    Variable2 = ''
    if Variable1 == '' or Variable1 == '.' or Variable1 == '-' or Variable1 == '-.':
        Variable1 = 0

######################################################################################
# Cas spécial du bouton "-", met la variable séléctionnée en négatif, si elle est vide

def SetOperatorSubtract():
    global Operator, EditedVariable, Variable2, Variable1
    if Variable1 == '' and EditedVariable == 1 :
        Variable1 = str('-')
        print_on_canvas(Variable1)
    elif Variable2 == '' and EditedVariable == 2 :
        Variable2 = str('-')
        print_on_canvas(Variable2)
    else:
        Operator = 'Subtract'
        EditedVariable = 2
        Variable2 = ''
        if Variable1 == '' or Variable1 == '.' or Variable1 == '-' or Variable1 == '-.':
            Variable1 = 0

# Fin du cas spécial
####################

def SetOperatorMultiply():
    global Operator, EditedVariable, Variable2, Variable1
    Operator = 'Multiply'
    EditedVariable = 2
    Variable2 = ''
    if Variable1 == '' or Variable1 == '.' or Variable1 == '-' or Variable1 == '-.':
        Variable1 = 0

def SetOperatorDivide():
    global Operator, EditedVariable, Variable2, Variable1
    Operator = 'Divide'
    EditedVariable = 2
    Variable2 = ''
    if Variable1 == '' or Variable1 == '.' or Variable1 == '-' or Variable1 == '-.':
        Variable1 = 0


def SetOperatorPower():
    global Operator, EditedVariable, Variable2, Variable1
    Operator = 'Power'
    EditedVariable = 2
    Variable2 = ''
    if Variable1 == '' or Variable1 == '.' or Variable1 == '-' or Variable1 == '-.':
        Variable1 = 0


###############################################################
# Définition du programme qui fait l'opération finale


def Equals():
    global Operator, EditedVariable, Result, Variable1, Variable2, NegativeTest
    EditedVariable = 1

    if Operator == "Add":
        if float(Variable1) + float(Variable2) <= int(float(Variable1) + float(Variable2)) + Arrondisseur and float(Variable1) + float(Variable2) >= int(float(Variable1) + float(Variable2)) - Arrondisseur:
            Result = int(float(Variable1) + float(Variable2))
        else:
            Result = float(Variable1) + float(Variable2)

    elif Operator == "Subtract":
        if float(Variable1) - float(Variable2) <= int(float(Variable1) - float(Variable2)) + Arrondisseur and float(Variable1) + float(Variable2) >= int(float(Variable1) + float(Variable2)) - Arrondisseur:
            Result = int(float(Variable1) - float(Variable2))
        else:
            Result = float(Variable1) - float(Variable2)

    elif Operator == "Multiply":
        if float(Variable2) < 0:
            NegativeTest = -1
            Variable2 = float(Variable2)
            Variable2 *= -1
        if float(Variable1) * float(Variable2) <= int(float(Variable1) * float(Variable2)) + Arrondisseur and float(Variable1) + float(Variable2) >= int(float(Variable1) + float(Variable2)) - Arrondisseur:
            Result = int(float(Variable1) * float(Variable2)) * NegativeTest
        else:
            Result = float(Variable1) * float(Variable2) * NegativeTest
        if NegativeTest == -1:
            NegativeTest = 1
            Variable2 *= -1
            Variable2 = str(Variable2)

    elif Operator == "Divide":
        if float(Variable2) == 0:
            Result = "Erreur: ÷ par 0"
        elif float(Variable1) / float(Variable2) <= int(float(Variable1) / float(Variable2)) + Arrondisseur and float(Variable1) + float(Variable2) >= int(float(Variable1) + float(Variable2)) - Arrondisseur:
            Result = int(float(Variable1) / float(Variable2))
        else:
            Result = float(Variable1) / float(Variable2)

    elif Operator == "Power":
        if float(Variable1) ** float(Variable2) <= int(float(Variable1) ** float(Variable2)) + Arrondisseur and float(Variable1) + float(Variable2) >= int(float(Variable1) + float(Variable2)) - Arrondisseur:
            Result = int(float(Variable1) ** float(Variable2))
        else:
            Result = float(Variable1) ** float(Variable2)
    print_on_canvas(Result)
    Variable1 = Result
    if Result == 'Erreur: ÷ par 0':
        Variable1 = '' ; Variable2 = '' ; Operator = '' ; Result = ''



##########################
# Ajout des boutons/canvas


root = tk.Tk()
root.title("Calculatrice")

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg= "black")
boutonAdd1 = tk.Button(root, text="1", font=("Arial", "50"), command=add1, bg="white")
boutonAdd2 = tk.Button(root, text="2", font=("Arial", "50"), command=add2, bg="white")
boutonAdd3 = tk.Button(root, text="3", font=("Arial", "50"), command=add3, bg="white")
boutonAdd4 = tk.Button(root, text="4", font=("Arial", "50"), command=add4, bg="white")
boutonAdd5 = tk.Button(root, text="5", font=("Arial", "50"), command=add5, bg="white")
boutonAdd6 = tk.Button(root, text="6", font=("Arial", "50"), command=add6, bg="white")
boutonAdd7 = tk.Button(root, text="7", font=("Arial", "50"), command=add7, bg="white")
boutonAdd8 = tk.Button(root, text="8", font=("Arial", "50"), command=add8, bg="white")
boutonAdd9 = tk.Button(root, text="9", font=("Arial", "50"), command=add9, bg="white")
boutonAdd0 = tk.Button(root, text="0", font=("Arial", "50"), command=add0, bg="white")
boutonAdd_pi = tk.Button(root, text="π", font=("Arial", "50"), command=add_pi, bg="white")
boutonAdd_e = tk.Button(root, text="e", font=("Arial", "50"), command=add_e, bg="white")
boutonAddDot = tk.Button(root, text=".", font=("Arial", "50"), command=addDot, bg="white")
boutonOperatorAdd = tk.Button(root, text="+", font=("Arial", "50"), command=SetOperatorAdd, bg="white")
boutonOperatorSubtract = tk.Button(root, text="-", font=("Arial", "50"), command=SetOperatorSubtract, bg="white")
boutonOperatorMultiply = tk.Button(root, text="×", font=("Arial", "50"), command=SetOperatorMultiply, bg="white")
boutonOperatorDivide = tk.Button(root, text="÷", font=("Arial", "50"), command=SetOperatorDivide, bg="white")
boutonOperatorPower = tk.Button(root, text="^", font=("Arial", "50"), command=SetOperatorPower, bg="white")
boutonEquals = tk.Button(root, text="=", font=("Arial", "50"), command=Equals, bg="white")
boutonClear = tk.Button(root, text="C", font=("Arial", "50"), command=clear, bg="white")

###########################################
# Ajout de l'emplacement des boutons/canvas

boutonAdd1.grid(row=4, column=0)
boutonAdd2.grid(row=4, column=1,ipadx=4)
boutonAdd3.grid(row=4, column=2)
boutonAdd4.grid(row=3, column=0)
boutonAdd5.grid(row=3, column=1,ipadx=4)
boutonAdd6.grid(row=3, column=2)
boutonAdd7.grid(row=2, column=0)
boutonAdd8.grid(row=2, column=1,ipadx=4)
boutonAdd9.grid(row=2, column=2)
boutonAdd0.grid(row=5, column=1,ipadx=4)
boutonAdd_pi.grid(row=1, column=1)
boutonAdd_e.grid(row=1, column=0)
boutonAddDot.grid(row=5, column=2,ipadx=9)
boutonOperatorAdd.grid(row=5, column=3,ipadx=4)
boutonOperatorSubtract.grid(row=4, column=3,ipadx=12)
boutonOperatorMultiply.grid(row=3, column=3,ipadx=4)
boutonOperatorDivide.grid(row=2, column=3,ipadx=5)
boutonOperatorPower.grid(row=1, column=2,ipadx=3)
boutonEquals.grid(row=5, column=0)
boutonClear.grid(row=1, column=3)

########################
# création de la fênetre

canvas.grid(row=0, column=0,columnspan=4)
root.mainloop()