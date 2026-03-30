from recherchepnl import *
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from math import exp,tanh


iris = datasets.load_iris()
entrées_iris = iris.data[:,2:4]

graine = int ("Perceptron", base=36)%2**31
gnpa = np.random.default_rng (graine)

N = len (iris.target) # le nombre d'exemples
Y_setosa = np.zeros ((N))      # Y_setosa est un tableau contenant N 0
Y_virginica = np.zeros ((N))   # idem pour Y_virginica
for i in range (len (iris.target)):
    if iris.target [i] == 0:
        Y_setosa [i] = 1
    else:
        Y_setosa [i] = 0
    if iris.target [i] == 2:
        Y_virginica [i] = 1
    else:
        Y_virginica [i] = 0

permutation = gnpa.permutation (np.arange (N))
N_train = int (0.8 * N)
indices_des_exemples_entrainement = permutation [:N_train]
indices_des_exemples_test = permutation [N_train:]
X_train = entrées_iris [indices_des_exemples_entrainement,:]
X_test = entrées_iris [indices_des_exemples_test,:]
Y_train = Y_setosa [indices_des_exemples_entrainement]
Y_test = Y_setosa [indices_des_exemples_test]


def calcul_Etest(X_test,Y_test,list_poid):
    """ 

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    nb_erreur=0
    for i in range(len(X_test)):
        s=calcul_sortie(X_test,list_poid)
        s_predite=classe_predite(s)
        if s_predite!=Y_test[i]:
            nb_erreur+=1
            
    return nb_erreur/len(X_test)
    

liste_poid = [2,-3,1]
n=0.01


def descente_gradient_stochastique (X_train,Y_train,X_test,Y_test,liste_poid,n):
    fig, ax = debut_figure(X_train, Y_train)
    E_test_c=0
    E_test_p=1
    while E_test_c < E_test_p :
        E_test_p=E_test_c
        N_train = len (Y_train)
        permutation_train = gnpa.permutation (np.arange (N_train))
        
        for i in range(len(liste_poid)):
            s=classe_predite(calcul_sortie(X_test[i],liste_poid))
            d=s- Y_train[i]
            print(d)
            if d !=0:
                liste_poid[0]=liste_poid[0]-n*d*s*(1-s)
                for j in range(len(liste_poid)):
                    liste_poid[j]=liste_poid[j]-n*d*X_train[i][j-1]*s*(1-s)
                    
        E_test_c=calcul_Etest(X_test[i],Y_test,liste_poid)
        print(E_test_c,E_test_p)
        
    ajoute_dernière_droite (fig, ax, liste_poid[0],liste_poid[1], liste_poid[2])

descente_gradient_stochastique(X_train,Y_train,X_test,Y_test,liste_poid,n)
