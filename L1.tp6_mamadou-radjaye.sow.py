# Titre   : Classification supervisée avec un perceptron
# Objet   : Descente de gradient stochastique (DGS) avec critère d'arrêt
#           basé sur l'erreur de test (E_test), sur le jeu de données iris.
# Auteurs : Mamadou Radjaye SOW
# Date    : 2026

import numpy as np
import matplotlib.pyplot as plt
from math import tanh
from sklearn import datasets
from sklearn.preprocessing import StandardScaler

# ── Taux d'apprentissage ─────────────────────────────────────────────────────
η = 0.01

# ── Fonctions graphiques (fournies, non modifiées) ────────────────────────────
def debut_figure(entrées, sorties):
    fig, ax = plt.subplots()
    couleurs = ["red" if sorties[i] == 1 else "blue" for i in range(len(sorties))]
    for i in range(len(sorties)):
        ax.scatter(entrées[i, 0], entrées[i, 1], color=couleurs[i], s=2)
    return fig, ax

def ajoute_droite(ax, a, b, c, xlim=[-2, 2]):
    x1 = xlim
    y1 = [-(xlim[0]*b + a)/c, -(xlim[1]*b + a)/c]
    ax.set_ylim(bottom=-5, top=5)
    ax.plot(x1, y1, linestyle=":")

def ajoute_dernière_droite(fig, ax, a, b, c, xlim=[-2, 2]):
    x1 = xlim
    y1 = [-(xlim[0]*b + a)/c, -(xlim[1]*b + a)/c]
    ax.set_ylim(bottom=-5, top=5)
    ax.plot(x1, y1, color="red", linestyle="-", linewidth=3)
    plt.show()

# ── Fonction d'activation ─────────────────────────────────────────────────────
def tangente_hyperbolique(v):
    """Calcule la tangente hyperbolique de v.
    
    Paramètre : v (float) — la valeur d'entrée.
    Retourne  : tanh(v) (float), valeur dans [-1, 1].
    Précondition : aucune (définie pour tout réel).
    """
    return tanh(v)

# ── Chargement et préparation des données ─────────────────────────────────────
iris = datasets.load_iris()
entrées_iris = iris.data[:, 2:4]          # longueur et largeur des pétales

# Centrer-réduire (OBLIGATOIRE)
scaler = StandardScaler()
scaler.fit(entrées_iris)
entrées = scaler.transform(entrées_iris)  # données centrées-réduites

# Calcul des étiquettes
N = len(iris.target)
Y_setosa    = np.zeros(N)
Y_virginica = np.zeros(N)
for i in range(N):
    Y_setosa[i]    = 1 if iris.target[i] == 0 else 0
    Y_virginica[i] = 1 if iris.target[i] == 2 else 0

# ── Initialisation du générateur pseudo-aléatoire ────────────────────────────
graine = int("Perceptron", base=36) % 2**31
gnpa   = np.random.default_rng(graine)

# ── Partitionnement train/test (80% / 20%) ────────────────────────────────────
permutation = gnpa.permutation(np.arange(N))
N_train     = int(0.8 * N)

indices_train = permutation[:N_train]
indices_test  = permutation[N_train:]

# CORRECTION clé : construire X_train/X_test à partir de 'entrées' (centrées-réduites)
X_train = entrées[indices_train, :]
X_test  = entrées[indices_test,  :]
Y_train = Y_setosa[indices_train]
Y_test  = Y_setosa[indices_test]
N_train = len(Y_train)

# ── Initialisation des poids [biais, poids_1, poids_2] ───────────────────────
percep = [1.0, -3.0, 2.0]

# ── Figure ────────────────────────────────────────────────────────────────────
fig, ax = debut_figure(entrées, Y_setosa)


# ── Fonction de calcul de E_test ──────────────────────────────────────────────
def calcule_erreur_test():
    """Calcule l'erreur de prédiction sur le jeu de test.
    
    Pour chaque exemple de test, on calcule la sortie du perceptron,
    on en déduit la classe prédite et on compte les erreurs.
    
    Paramètres : aucun (utilise les variables globales X_test, Y_test, percep).
    Retourne   : erreur (float) — proportion d'exemples mal classés dans [0, 1].
    Précondition : X_test et Y_test doivent avoir le même nombre de lignes.
    """
    erreurs = 0
    for i in range(len(Y_test)):
        v = percep[0] + percep[1] * X_test[i][0] + percep[2] * X_test[i][1]
        s = tangente_hyperbolique(v)
        classe_predite = 1 if s >= 0 else 0
        if classe_predite != Y_test[i]:
            erreurs += 1
    return erreurs / len(Y_test)   # proportion d'erreurs


# ── DGS principale ────────────────────────────────────────────────────────────
def DGS():
    """Descente de Gradient Stochastique avec critère d'arrêt sur E_test.
    
    On itère tant que l'erreur de test (E_test) diminue.
    À chaque itération : on mélange les exemples d'entraînement,
    on corrige les poids sur X_train, puis on calcule E_test.
    
    Paramètres : aucun (utilise les variables globales).
    Retourne   : rien. Affiche le graphique des droites de séparation.
    Précondition : percep, X_train, Y_train, X_test, Y_test doivent être
                   initialisés avant l'appel.
    """
    # On initialise E_test_precedent à l'infini pour que la première
    # itération entre toujours dans la boucle
    E_test_precedent = float('inf')
    E_test_actuel    = calcule_erreur_test()

    iteration = 0

    # Boucle tant que E_test diminue
    while E_test_actuel < E_test_precedent:
        iteration += 1
        E_test_precedent = E_test_actuel

        # CORRECTION : mélanger les exemples à CHAQUE itération
        permutation_train = gnpa.permutation(np.arange(N_train))

        # Parcours de tous les exemples d'entraînement dans un ordre aléatoire
        for i in range(N_train):
            idx = permutation_train[i]   # indice de l'exemple dans X_train

            # Calcul de la sortie du perceptron
            v = percep[0] + percep[1] * X_train[idx][0] + percep[2] * X_train[idx][1]
            s = tangente_hyperbolique(v)

            # Classe prédite
            classe_predite = 1 if s >= 0 else 0

            # Erreur
            d = classe_predite - Y_train[idx]

            # Correction des poids si erreur
            if d != 0:
                percep[0] = percep[0] - η * d * (1 - s*s)          # biais
                for j in range(1, len(percep)):
                    percep[j] = percep[j] - η * d * X_train[idx][j-1] * (1 - s*s)

        # CORRECTION : calculer E_test à la fin de chaque itération
        E_test_actuel = calcule_erreur_test()
        print(f"Itération {iteration} — E_test = {E_test_actuel:.4f}")

        # Afficher la droite intermédiaire
        ajoute_droite(ax, percep[0], percep[1], percep[2])

    # Afficher la droite finale en rouge
    ajoute_dernière_droite(fig, ax, percep[0], percep[1], percep[2])
    print(f"\nArrêt après {iteration} itérations.")
    print(f"Poids finaux : biais={percep[0]:.4f}, p1={percep[1]:.4f}, p2={percep[2]:.4f}")


DGS()
