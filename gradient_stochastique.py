# Titre : Minimisation de fonctions par descente de gradient stochastique
# Implémentation en Python de la descente de gradient 
# pour trouver les minima locaux de différentes fonctions
# Sow Mamadou Radjaye

def f (x:float) -> float:
    """ calcule l'image x de la fonction f

    Précondition :  avec x ∈ [-10, 10].
    Exemple(s) :
    $$$ f(2)
    approx(2,1.2)
    """
    assert -10 <= x and x <= 10, "x ∈ [-10, 10]"
    return 0.3 * x * x - 2 * x + 4

def derive(x:float) -> float:
    """ calcule derivee x de la fonction f

        Précondition :  avec x ∈ [-10, 10].
        Exemple(s) :
        $$$ derive(2.0)
        approx(-0.80,2)

        """
    assert -10 <= x and x <= 10, "x ∈ [-10, 10]"
    return 0.6 * x  - 2

    

def descente_gradient_stochastique(derive:callable, x:float,n:float) -> tuple[int,float]:
    """ réalise la descente de gradient stochastique.

            Précondition :  avec x ∈ [-10, 10].
            Exemple(s) :
            $$$ descente_gradient_stochastique(derive,-5,0.01)
            (651,approx(3.17,2))

            """
    derivee=derive(x)
    i=0
    while abs(derivee) > 0.1:
        x=x-n*derive(x)
        derivee=derive(x)
        i+=1
    return (i, round(x,2))
def f2(x)->float:
    """ calcule l'image x de la fonction f

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    return round(0.2*x**5-1.1*x**3+0.7*x**2-x+1.2,2)
    
def derive2(x:float)->float:
    """ calcule derivee x de la fonction f

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    return x**4-3.3*x**2+1.4*x-1

def descente_gradient_stochastique2(f2:callable) -> None:
    """réalise la descente de gradient stochastique de ces valeurs.

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    
    for x0 in [-2, -1, 0, 1, 2, 3]:
        print(f"iteration et x min={descente_gradient_stochastique(derive2,x0,n=0.01)}")
        print(f"le minimun est:{f2(descente_gradient_stochastique(derive2,x0,n=0.01)[1])}")
        
def g(x:float)->float:
    return round(x**7/20 + x**6/5 - 0.4375*x**5 - 2.0125*x**4 - 0.4375*x**3 + 2.7125*x**2 + 0.825*x - 0.9,2)

def dg(x:float)->float:
    return 0.35*x**6 + 1.2*x**5 - 2.1875*x**4 - 8.05*x**3 - 1.3125*x**2 + 5.425*x + 0.825

def descente_gradient_stochastique3(f:callable) -> None:
    for x0 in [-3, -2, -1, 0, 1, 2, 2.9]:
        print(f"iteration et x min={descente_gradient_stochastique(dg,x0,n=0.01)}")
        print(f"le minimun est:{f(descente_gradient_stochastique(dg,x0,n=0.01)[1])}")

descente_gradient_stochastique3(g)
# Avec l'appel de la fonction on a ces differentes valeurs:
# (222, 1.67)
# (197, 1.67)
# (150, 1.67)
# (60, 1.67)
# (31, 1.69)
# (36, 1.69)