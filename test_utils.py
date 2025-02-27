import pytest
import utils

def test_fact():
    # test la fonction fact, test les cas particulier et 1 cas générale (le happy path) 
    with pytest.raises(ArithmeticError): # capture l'erreur généré par la fonction appelé, on peut manipuler cette erreur avec un as "variable pour stocké l'erreur"
        utils.fact(-1)
    assert utils.fact(0) ==1
    assert utils.fact(3) ==6


def test_roots():
    assert utils.roots(3,-1,2) == (0)
    assert utils.roots(1/3,-2,3) == (3)
    assert utils.roots(3,-4,1) == (1/3,1)

def test_integrate():
    # Utiliser eval =() !! possibilité de se faire hacker avec Eval 
    #function_test = str("5x**3-3x+7") 
    function_test = "5*x**3-3*x+7" #!!! à la multiplication entre les x et les valeur, 5x = faux, 5*x = bonne syntaxte
    assert utils.integrate(function_test,0,1) == pytest.approx(27/4) #!!! lower d'abord 0 => borne du bas, puis upper value 1 => borne du haut