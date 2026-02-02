from perceptron import calcul_sortie

ENTREE = [[0, 0], [0, 1], [1, 0], [1, 1]]
SORTIE= [0, 0, 0, 1]
def est_valide(liste_entree: list[list[int]],liste_sortie:list[int],liste_poids:list[int])->bool:
    """Renvoie True si la sortie est correct

    Précondition : 
    Exemple(s) :
    $$$ est_valide([[0, 0], [0, 1], [1, 0], [1, 1]],[0, 0, 0, 1],[-5, 3, 3])
    True
    """
    for i in range(len(liste_entree)):
        liste_entree[i].insert(0,1)
        if calcul_sortie(liste_entree[i],liste_poids) != liste_sortie[i]:
            return False
    return True
def ont_egalement(liste_entree:list[list[int]],liste_sortie:list[int])->bool:
    """ Renvoie True si la liste des entrées contient autant d'également
        que la liste des sorties. 

    Précondition : 
    Exemple(s) :
    $$$ ont_egalement(ENTREE,SORTIE)
    True
    """
    return len(liste_entree)==len(liste_sortie) 

def contient_que_deux(liste_entree:list[list[int]]):
    """ Renvoie True si chaque sous-liste de entrées contient bien 2 éléments
    Précondition : 
    Exemple(s) :
    $$$ contient_que_deux([[0, 0], [0, 1], [1, 0], [1, 1]])
    True
    """
    for liste in liste_entree:
        if len(liste)!=2:
            return False
    return True
        
    
def main(liste_entree: list[list[int]],liste_sortie:list[int],liste_poids:list[int]):
    """ la fontion principale

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    if est_valide(liste_entree,liste_sortie,liste_poids):
        print(" Aucune erreur détectée")
    else:
        print(" erreur détectée !!")
    if ont_egalement(liste_entree,liste_sortie):
        print("ils ont meme nombre d'elements")
    else:
        print("ils n'ont pas meme nombre d'element")
    if contient_que_deux(liste_entree):
        print("ils contient que deux")
    else:
        print("ils n'ont contient que deux")

        