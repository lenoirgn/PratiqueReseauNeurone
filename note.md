# 🧠 RÉSEAUX DE NEURONES — FICHE DE COURS COMPLÈTE (L1)

---

# 1. Introduction

Les réseaux de neurones artificiels s'inspirent du fonctionnement du cerveau humain.  
Un neurone biologique reçoit des signaux, les accumule, et déclenche un potentiel d'action si un seuil est dépassé.  
Les neurones artificiels simplifient ce mécanisme.

Applications historiques :
- reconnaissance de chiffres manuscrits (années 1990)
- lecture automatique de chèques
- jeux (Backgammon, Go)
- vision, langage, modèles génératifs
- dangers : surveillance, manipulation, consommation énergétique

---

# 2. Perceptron binaire (entrées binaires, sortie binaire)

## 2.1 Définition

- Entrées : $e_j \in \{0,1\}$
- Poids : $p_j \in \mathbb{R}$
- Biais : $p_0$
- Potentiel : $v = p_0 + \sum_{j=1}^P p_j e_j$

- Sortie (Heaviside) : $s = \begin{cases} 1 & v \ge 0 \\ 0 & v < 0 \end{cases}$

---

## 2.2 Interprétation géométrique

Pour 2 entrées : $p_0 + p_1 e_1 + p_2 e_2 = 0$

Droite : $e_2 = -\frac{p_1}{p_2} e_1 - \frac{p_0}{p_2}$

→ Le perceptron sépare le plan en deux demi-espaces.

Fonctions réalisables :
- AND, OR, NAND, NOR

Non réalisable :
- XOR (pas de séparation linéaire possible)

---

## 2.3 Trouver les poids

Méthode :
- écrire les contraintes (inégalités)
- résoudre si possible
- sinon → fonction non linéairement séparable

Exemple AND :
- contraintes sur $p_0, p_1, p_2$
- plusieurs solutions possibles

---

# 3. Perceptron à entrées réelles, sortie binaire

On dispose d'un ensemble d'exemples $(x_i, y_i)$.

Objectif : trouver les poids qui minimisent le nombre d'erreurs.

---

## 3.1 Descente de gradient (idée générale)

Pour minimiser une fonction $f(x)$ :

$$x_{k+1} = x_k - \eta f'(x_k)$$

- $\eta$ : taux d'apprentissage
- on s'arrête quand la pente devient petite

---

## 3.2 Descente de gradient pour le perceptron

Erreur : $d = s - y$

Mise à jour : $p_0 \leftarrow p_0 - \eta d$

$p_j \leftarrow p_j - \eta d x_{i,j}$

On répète jusqu'à ce que les corrections deviennent très petites.

---

## 3.3 Fonction réellement minimisée

Erreur quadratique : $\zeta = \sum_i (s_i - y_i)^2$

La fonction Heaviside n'étant pas dérivable, on remplace $s_i$ par le potentiel brut dans la dérivation.

---

# 4. Perceptron réel (sortie réelle)

On remplace Heaviside par une fonction **dérivable**.

## 4.1 Fonctions d'activation

### Sigmoïde (logistique)

$$\phi(v) = \frac{1}{1 + e^{-v}}$$

$$\phi'(v) = \phi(v)(1 - \phi(v))$$

### Tangente hyperbolique

$$\phi(v) = \tanh(v)$$

$$\phi'(v) = 1 - \tanh^2(v)$$

→ tanh est centrée, souvent plus efficace.

---

# 5. Perceptron multi-couches (PMC)

Un PMC = plusieurs perceptrons organisés en couches :

- couche d'entrée
- couches cachées
- couche de sortie

Chaque neurone applique : $s = \phi(p_0 + \sum_j p_j e_j)$

---

# 6. Rétropropagation du gradient (Backprop)

Principe :
1. propagation avant
2. calcul de l'erreur
3. propagation arrière des gradients
4. mise à jour des poids

Erreur locale : $\delta = (s - y)\phi'(v)$

Mise à jour : $p_{ij} \leftarrow p_{ij} - \eta \delta_j e_i$

---

# 7. Théorème d'approximation universelle

Un PMC à **une seule couche cachée** peut approximer **toute fonction continue et bornée** avec une précision arbitraire.

---

# 8. Calcul matriciel

Pour toutes les données : $v = Xp$

→ Justifie l'usage des GPU.

---

# 9. Apprentissage supervisé

Objectif : généraliser à des données jamais vues.

Sur-apprentissage :
- erreur entraînement ↓
- erreur test ↑

---

# 10. Résumé des formules essentielles

### Perceptron binaire :

$$v = p_0 + \sum p_j e_j$$

$$s = 1_{v \ge 0}$$

$$d = s - y$$

$$p_j \leftarrow p_j - \eta d e_j$$

### Sigmoïde :

$$\sigma(v) = \frac{1}{1 + e^{-v}}$$

$$\sigma'(v) = \sigma(v)(1 - \sigma(v))$$

### tanh :

$$\tanh'(v) = 1 - \tanh^2(v)$$

### Descente de gradient :

$$p_j \leftarrow p_j - \eta \frac{\partial E}{\partial p_j}$$

---

# 11. Idée générale

Les réseaux de neurones apprennent en ajustant leurs poids pour minimiser une erreur, grâce à la descente de gradient et à la rétropropagation.
