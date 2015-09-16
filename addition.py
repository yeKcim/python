#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Ce script à été écrit par Anthony CARRÉ pour aider son fils à réviser ses tables d’addition
"""
from random import randint
import timeit

class color:
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   RED = '\033[91m'
   END = '\033[0m'

points=0 # initialisation du score
num_question=0 # initialisation du compte du numéro de question

input_nb_questions = input("Vous souhaitez faire combien de questions : ")
if input_nb_questions:
    nb_questions=int(input_nb_questions)
else:
    nb_questions=10

start = timeit.default_timer() # initialisation du chrono

while num_question <nb_questions:

    num_question=num_question+1
    x=(randint(1,9))
    y=(randint(1,9))

    # Addition
    z=x+y
    print("-----------------------------")
    print(x,"+",y,"=")
    input_reponse = input("Votre réponse : ")
    
    if not input_reponse:
        break
    
    if (z==int(input_reponse)):
        print (color.GREEN, x,"+",y,"=",z, "😋", color.END)
        points=points+1
    else:
        print(color.RED,x,"+",y,"=",z, " ≠ ",input_reponse, " 😥", color.END)

stop = timeit.default_timer() # arrêt du chrono
chrono=stop-start

temps_moyen_par_question=chrono/num_question
nb_fautes=num_question-points
score=int( 1000000* (points-0.3*nb_fautes)/(temps_moyen_par_question/0.7*nb_questions) )

print("\n#############################")
print(color.BLUE,"Bonnes réponses : ",points,"/",num_question)
print(" Temps :", round(chrono,2)," secondes")
print(" Score :", score," points", color.END)
