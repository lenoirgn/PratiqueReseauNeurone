from perceptron import calcul_sortie
import matplotlib.pyplot as plt

def debut_figure (entrées, sorties):
    fig, ax = plt.subplots ()
    ax. set_ylim (-3, 3)
    couleurs = []
    for i in range (len (sorties)):
        if sorties [i] == 1:
            couleurs.append ("red")
        else:
            couleurs.append ("blue")
    for i in range (len (sorties)):
        ax.scatter (entrées [i] [0], entrées [i] [1], color = couleurs [i], s = 2)
    return fig, ax

def ajoute_droite (ax, a, b, c):
    if c != 0:
        x1 = [0, 7]
        y1 = [-a/c, -(5*b+a)/c]
        ax.plot (x1, y1, linestyle = ":")

def ajoute_dernière_droite (fig, ax, a, b, c):
    if c != 0:
        x1 = [0, 7]
        y1 = [-a/c, -(5*b+a)/c]
        ax.plot (x1, y1, color = "red", linestyle = "-", linewidth= 3)
    fig.show ()
    
def recherche(liste_entree: list[list[int]],liste_sortie:list[int],liste_poid:list[float],n:float):
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    fig,ax = debut_figure (liste_entree,liste_sortie)
    nb_erreurs = 1
    for k in range(len(liste_entree)):
            liste_entree[k].insert(0,1)
    while nb_erreurs > 0:
        nb_erreurs = 0   
        for i in range(len(liste_entree)):
            sorti=calcul_sortie(liste_entree[i],liste_poid)
            d=sorti-liste_sortie[i]
            if d!=0:
                nb_erreurs+=1
                liste_poid[0]=liste_poid[0]-n*d
                for j in range(1,len(liste_poid)):
                    liste_poid[j]=liste_poid[j]-n*d*liste_entree[i][j]
                    
        
        ajoute_droite (ax,liste_poid[0],liste_poid[1], liste_poid[2])
        
        print(nb_erreurs)
    ajoute_dernière_droite (fig, ax, liste_poid[0],liste_poid[1], liste_poid[2])
        
    
entrées = [[1.4, 0.2],
           [4.0, 1.3],
           [1.7, 0.4],
           [1.6, 0.2],
           [3.9, 1.2],
           [5.1, 1.6],
           [1.5, 0.3],
           [4.0, 1.0],
           [1.9, 0.4],
           [4.1, 1.3],
           [1.7, 0.5]]
sorties = [0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0]

from sklearn import datasets
iris = datasets.load_iris()
entrées = iris.data [:,2:4]
sorties = []
for i in range (len (iris.target)):
    if iris.target [i] == 0:
        sorties.append (0)
    else:
        sorties.append (1)
 
recherche(entrées,sorties,[-1, -3, 0],0.01)
