import numpy as np
# Les fonctions permettant de créer le graphique
η=0.01
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

def ajoute_droite (ax, a, b, c, xlim = [-2, 2]):
    x1 = xlim
    y1 = [-(xlim[0]*b+a)/c, -(xlim[1]*b+a)/c]
    ax.set_ylim (bottom = -5, top = 5)
    ax.plot (x1, y1, linestyle = ":")

def ajoute_dernière_droite (fig, ax, a, b, c, xlim = [-2, 2]):
    x1 = xlim
    y1 = [-(xlim[0]*b+a)/c, -(xlim[1]*b+a)/c]
    ax.set_ylim (bottom = -5, top = 5)
    ax.plot (x1, y1, color = "red", linestyle = "-", linewidth= 3)
    plt.show()

# Je charge le jeu de données iris (comme dans le TP précédent).
from sklearn import datasets
iris = datasets.load_iris()
entrées_iris = iris.data[:,2:4]

# Il est essentiel de centrer-réduire !!!!!
# On fait comme cela :
from sklearn.preprocessing import StandardScaler  
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
    if iris.target [i] != 2:
        sorties_iris.append (0)
    else:
        sorties_iris.append (1)
sorties = sorties_iris

# J'ai besoin d'utiliser la fonction exp(), donc j'écris :
from math import tanh 

# On définit la fonction logistique (je vous laisse le faire) :
def tangeante_hyperbolique(v):
    return tanh(v)

# On va maintenant réaliser la DGS
    
'''
    On commence par initialiser les poids. Vous initialisez avec les valeurs
    que vous voulez mais si vous voulez obtenir exactement le même résultat
    que moi, il faut les initialiser comme cela :
'''

'''
    Tout est en place.
    Maintenant, vous écrivez la DGS.
    
'''
percep=[1,-3,0]
fig, ax = debut_figure(entrées, sorties)
def DGS():
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    
    somme_correction=1
    correction_precedente=0
    while abs(correction_precedente-somme_correction)>10**-5:
        correction_precedente=somme_correction
        somme_correction=0
        for i in range(len(entrées)):  
            v=percep[0]+percep[1]*entrées[i][0] +percep[2]*entrées[i][1]
            s=tangeante_hyperbolique(v)
            if s>=0:
                classe_predite=1
            else:
                classe_predite=0
            
            d=classe_predite-sorties[i]
            if d!=0:
                percep[0]=percep[0]-η*d*(1-s*s)
                somme_correction+=abs(η*d*(1-s*s))
                for j in range(1,len(percep)):
                    percep[j]=percep[j]-(η*d*entrées[i][j-1])*(1-s*s)
                    somme_correction+= abs((η*d*entrées[i][j-1])*(1-s*s))
        ajoute_droite (ax, percep[0], percep[1],percep[2])
    ajoute_dernière_droite(fig, ax, percep[0], percep[1],percep[2])
DGS()            
                    
    

