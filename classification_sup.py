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


N_train = len (Y_train)
permutation_train = gnpa.permutation (np.arange (N_train))


liste_poids = [1,-3,0]
n=0.01

def descente_gradient_stochastique (liste_entree,liste_sortie,liste_poid,n):
    fig,ax = debut_figure (liste_entree,liste_sortie)
    
    E_test_c=0
    E_test_p=1
    while E_test_c<E_test_p :
        
        for i in range(len(liste_entree)):
            sortie=calcul_sortie(liste_entree[i],liste_poid)
            prediction=classe_predite(sortie)
            d=prediction-liste_sortie[i]
            if d !=0:
                delta_b=n*d*sortie*(1-sortie*sortie)
                liste_poid[0]=liste_poid[0]-delta_b
                for j in range (len (liste_entree[i])):
                    delta_p=n*d*liste_entree[i][j]*sortie*(1-sortie*sortie)
                    liste_poid[j+1]=liste_poid[j+1]-delta_p
        ajoute_droite (ax,liste_poid[0],liste_poid[1], liste_poid[2])
        
        
    ajoute_dernière_droite (fig, ax, liste_poid[0],liste_poid[1], liste_poid[2])
                    
descente_gradient_stochastique(entrées,sorties,liste_poids,n)
