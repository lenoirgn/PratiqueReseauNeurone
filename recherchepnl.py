from perceptron import calcul_sortie
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from math import exp

# Les fonctions permettant de créer le graphique
import matplotlib.pyplot as plt

def debut_figure (entrées, sorties):
    fig, ax = plt.subplots ()
    couleurs = []
    for i in range (len (sorties)):
        if sorties [i] == 1:
            couleurs.append ("red")
        else:
            couleurs.append ("blue")
    for i in range (len (sorties)):
        ax.scatter (entrées [i, 0], entrées [i, 1], color = couleurs [i], s = 2)
    return fig, ax

def ajoute_droite (ax, a, b, c, xlim = [-2, 7]):
    x1 = xlim
    y1 = [-(xlim[0]*b+a)/c, -(xlim[1]*b+a)/c]
    ax.set_ylim (bottom = -5, top = 5)
    ax.plot (x1, y1, linestyle = ":")

def ajoute_dernière_droite (fig, ax, a, b, c, xlim = [-2, 7]):
    x1 = xlim
    y1 = [-(xlim[0]*b+a)/c, -(xlim[1]*b+a)/c]
    ax.set_ylim (bottom = -5, top = 5)
    ax.plot (x1, y1, color = "red", linestyle = "-", linewidth= 3)
    plt.show ()

# Je charge le jeu de données iris (comme dans le TP précédent).

iris = datasets.load_iris()
entrées_iris = iris.data[:,2:4]

# Il est essentiel de centrer-réduire !!!!!
# On fait comme cela :

scaler = StandardScaler ()
scaler.fit (entrées_iris)
entrées = scaler.transform (entrées_iris)
'''
    entrées est une matrice de 150 lignes (le nombre de données iris) et 4 colonnes (les 4 attributs).
    Les 4 attributs sont maintenant centrés et réduits.
'''

# Je calcule la sortie attendue pour chaque donnée.
sorties_iris = []
for i in range (len (iris.target)):
    if iris.target [i] == 0:
        sorties_iris.append (0)
    else:
        sorties_iris.append (1)
sorties = sorties_iris

def logistique (v) :
    "Retourne la logistique de v"
    return 1/(1+exp(-v))


def calcul_sortie(liste_entree, liste_poids):
    v = liste_poids[0]  # biais
    for i in range(len(liste_entree)):
        v += liste_poids[i+1] * liste_entree[i]
    return logistique(v)

def classe_predite(sortie:int)-> int:
    if sortie <0.5:
        return 0
    else:
        return 1


liste_poids = [1,-3,0]
n=0.01
def descente_gradient_stochastique (liste_entree,liste_sortie,liste_poid,n):
    fig,ax = debut_figure (liste_entree,liste_sortie)
    e= 0.001
    corrections = 1
    while  corrections >e:
        corrections = 0
        for i in range(len(liste_entree)):
            sortie=calcul_sortie(liste_entree[i],liste_poid)
            prediction=classe_predite(sortie)
            d=prediction-liste_sortie[i]
            if d !=0:
                liste_poid[0]=liste_poid[0]-n*d*sortie*(1-sortie)
                corrections=corrections+abs(n*d*sortie*(1-sortie))
                for j in range (len (liste_entree[i])):
                    liste_poid[j+1]=liste_poid[j+1]-n*d*liste_entree[i][j]*sortie*(1-sortie)
                    corrections=corrections+abs(n*d*liste_entree[i][j]*sortie*(1-sortie))
        ajoute_droite (ax,liste_poid[0],liste_poid[1], liste_poid[2])
        print(corrections)
    ajoute_dernière_droite (fig, ax, liste_poid[0],liste_poid[1], liste_poid[2])
                    
descente_gradient_stochastique(entrées,sorties,liste_poids,n)