#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Anthony CARRÉ
Révision de tables d’addition
"""
from random import randint
import timeit

class color:
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   RED = '\033[91m'
   END = '\033[0m'

points=0 # initialisation du score
num_question=1 # initialisation du compte du numéro de question

print(color.BLUE)
print("#############  Tables d’addition  #############",color.END)
print("Laisser vide la réponse et valider pour arrêter\n")

start = timeit.default_timer() # initialisation du chrono

while num_question<100:

    x=(randint(1,9))
    y=(randint(1,9))
    z=x+y
    print("---------",color.BLUE,str(num_question),color.END,"---------")
    equation=str(x)+" + "+str(y)+" = "
    input_reponse = input(equation)
    
    # il n’y a pas réponse
    if not input_reponse:
        num_question=num_question-1
        if num_question==0: quit()
        break
   
    # il y a une réponse
    if (z==int(input_reponse)):
        print(color.GREEN,"😋",color.END)
        points=points+1
    else:
        print(color.RED,"😥 ",x,"+",y,"=",z,color.END)

    num_question=num_question+1

stop = timeit.default_timer() # arrêt du chrono
chrono=stop-start
temps_moyen_par_question=chrono/num_question
nb_fautes=num_question-points
score=int( 1000* (points-0.2*nb_fautes)/temps_moyen_par_question )

print("\n#############################")
print(color.BLUE,"Bonnes réponses : ",points,"/",num_question)
print(" Temps :", round(chrono,2)," secondes")
print(" Score :", score," points\n",color.END)
