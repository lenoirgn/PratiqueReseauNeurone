
def saisie()->int:
    """ Saisi soit 1 ou 0
    Précondition : 
    Exemple(s) :
    $$$ 
    """
    val=int(input("Entrer la valeur de l'entree soit  1 ou 0: "))
    while val!=1 and val!=0:
        val=int(input("Entrer la valeur de l'entree soit 1 ou 0: "))
    return val
        

def saisie_entree(entier:int)->list[int]:
    """ 
    Précondition : 
    Exemple(s) :
    $$$ 
    """
    liste_entree=[1]
    for i in range(entier-1):
        val=saisie()
        liste_entree.append(val)
    return liste_entree

def saisie_poids(entier:int)->list[float]:
    """ 
    Précondition : 
    Exemple(s) :
    $$$ 
    """
    liste_poids=[]
    for i in range(entier):
        val=float(input("Entrer une valeur du poids: "))
        liste_poids.append(val)
    return liste_poids
    
def calcul_sortie(list_entre:list[int],list_poids:list[float]):
    """ 
    Précondition : 
    Exemple(s) :
    $$$ calcul_sortie([1,0,0,1],[1,-1,1.5,1])
    1
    $$$ calcul_sortie([1,0,0,1],[1,-1,1.5,-1])
    1
    $$$ calcul_sortie([1,1,1,1],[1,-1,-1.5,1])
    0
    $$$ calcul_sortie([1,0,1,1],[1,0,-5,1])
    0
    """
    res=0
    for i in range(len(list_entre)):
        res+=list_entre[i]*list_poids[i]
    
    if res >=0:
        return 1
    return 0
     
def main():
    """ 

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    nb_entree=int(input("Entre le nombre d'entree: "))
    list_entre=saisie_entree(nb_entree)
    list_poid=saisie_poids(nb_entree)
    sortie=calcul_sortie(list_entre,list_poid)
    print(f'La valeur de la sortie est : {sortie}')
if __name__ == '__main__':
   
   main()
       